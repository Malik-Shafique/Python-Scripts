from PIL import Image
input_path =  '/content/drive/MyDrive/pics/pic-sep-2023.jpg'

# Store path of the output image in the variable output_path
output_path = '/content/drive/MyDrive/pics/pic-sep-2023-rembg.jpg'

# Processing the image
input = Image.open(input_path)

# Removing the background from the given Image
output = remove(input)

output = output.convert('RGB')
#Saving the image in the given path
output.save(output_path)
