from PIL import Image
  


# Open the image by specifying the image path.
image_path = "21858127.png"
image_file = Image.open(image_path)
image_file = image_file.resize((28, 28), Image.ANTIALIAS)
  
# the default
image_file.save("image_name.png")
  
# Changing the image resolution using quality parameter
# Example-1
image_file.save("image_name2.png")
  
# Example-2
image_file.save("image_name3.png")
