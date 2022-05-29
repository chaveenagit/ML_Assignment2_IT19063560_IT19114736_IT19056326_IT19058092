from PIL import Image
import csv
import numpy as np

temp_list = []

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

img = np.array(Image.open("19194965.png"))

for i in img:
    temp_list.append(float(int(rgb2hex(i[0][0],i[0][1],i[0][2])[1:],16))/100000000)
    for j in i[1:]:
        temp_list.append(float(int(rgb2hex(j[0],j[1],j[2])[1:],16))/100000000)

img = np.array(temp_list)

#print(img)
def csvWriter(fil_name, nparray):
    nparray = np.insert(nparray, 0, 1, axis=0)
    example = nparray.tolist()
    with open(fil_name+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(example)

csvWriter("myfilenamse1112", img)



