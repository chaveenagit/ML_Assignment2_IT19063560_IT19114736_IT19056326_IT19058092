import os
from PIL import Image
  
temp_list = []

arr = os.listdir()

for i in arr:
	try:
		image_path = i
		image_file = Image.open(image_path).convert('RGB')
		image_file = image_file.convert('RGB')
		image_file = image_file.resize((64, 64), Image.ANTIALIAS)
		image_file = image_file.convert('RGB')
		image_file.save(str(i)+"low.png")
	except Exception as e:
	 	print("Unknown file")
