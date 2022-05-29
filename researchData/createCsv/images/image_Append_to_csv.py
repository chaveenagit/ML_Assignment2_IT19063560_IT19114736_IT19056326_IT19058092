from PIL import Image
import csv
import numpy as np
import os
import io
from numpy import asarray


temp_list = []

arr = os.listdir()


def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def csvWriter(fil_name, nparray, name):
    nparray = np.insert(nparray, 0, float(name), axis=0)
    example = nparray.tolist()
    with open(fil_name + '.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        # writer.writerow([example])
        writer.writerow(example)


for i in arr:
    name = i[i.find("_")+1:i.find(".")]
    try:
        img = Image.open(i)
        data = list(img.getdata())
        for i in range(len(data)):
            temp_list.append(
                float(int(str(rgb2hex(data[i][0], data[i][1], data[i][2]))[1:], 16))/100000000)

        img = np.array(temp_list)

        csvWriter('data', img, name)
        temp_list = []
    except Exception as e:
        print(e)
