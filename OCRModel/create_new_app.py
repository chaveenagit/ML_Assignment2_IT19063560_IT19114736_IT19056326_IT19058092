import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv', header=None, sep='\t')

data_new = data[0].str.split(',', expand=True)
data_new.to_csv('new_data.csv', index=False, header=None)

df_ = pd.read_csv('new_data.csv')
print(df_.shape)
