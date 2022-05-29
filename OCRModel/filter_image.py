import numpy as np
from PIL import Image

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def filter():
    temp_list = []
    try:
        img = Image.open("image.png")
        img = img.resize((64, 64), Image.ANTIALIAS)
  

        img.save("image.png")
        img = Image.open("image.png")
        data = list(img.getdata())
        for i in range(len(data)):
            temp_list.append(
                float(int(str(rgb2hex(data[i][0], data[i][1], data[i][2]))[1:], 16))/100000000)

        img = np.array(temp_list)
        return img;

    except Exception as e:
        print(e)