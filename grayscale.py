from PIL import Image

im_path = 'color.jpg'  #change path to your image file
pil_image = Image.open(im_path).convert('L')   # open image file and convert to grayscale
pil_image.save('grayscale.jpg')  # save file at desired location

pil_image.show()    # display image
