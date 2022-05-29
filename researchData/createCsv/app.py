from PIL import Image
  


# Open the image by specifying the image path.
image_path = "19194965.png"
image_file = Image.open(image_path)
image_file = image_file.resize((64, 64), Image.ANTIALIAS)
  
# the default
image_file.save("image_name.png", quality=95)
  
# Changing the image resolution using quality parameter
# Example-1
image_file.save("image_name2.png", quality=95)
  
# Example-2
image_file.save("image_name3.png", quality=95)
