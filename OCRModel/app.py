from operator import mod
from flask import Flask, make_response
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from flask import request
import urllib.request 
from filter_image import filter


app = Flask(__name__)

data = pd.read_csv('new_data.csv', header=None, sep=",")

x = np.array(data.drop(data.columns[0], axis=1))
y = np.array(data.iloc[:,0])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y, test_size=0.3)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)

predicted = model.predict(x_test)

chars = {
    1.0: 'අ',
    21.0: 'ක',
    54.0: 'ව'
}

for x in range(len(predicted)):
    print("predicted : ", chars[predicted[x]], " Actual : ", chars[y_test[x]])

predicted = model.predict(x_test[[0]])
print((x_test[[0]]), type((x_test[[0]])))

@app.route("/ocr", methods=["POST"])
def index():
    data = request.get_json()
    urllib.request.urlretrieve(str(data['url']), "image.png")
    result = filter()
    result = result.reshape(1,-1)
    print(result.shape)
    predicted = model.predict(result)
    print("Predicted character is : ", chars[predicted[0]])
    return make_response({
        "predicted": str(chars[predicted[0]])
    })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')