from PIL import Image
input_path =  'input_image.jpg' # specify path to input image

# Store path of the output image in the variable output_path
output_path = 'output_image.jpg'

# Processing the image
input = Image.open(input_path)

# Removing the background from the given Image
output = remove(input)
#convert image to RGB, because jpeg format uses RGB
output = output.convert('RGB')
#Saving the image in the given path
output.save(output_path)
