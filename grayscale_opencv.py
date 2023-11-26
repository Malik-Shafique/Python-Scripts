#convert to grayscale using OpenCV

import cv2

#read image file any 'my_image.jpg' (name of file) in same folder as grayscale_opencv.py
img_cv2 = cv2.imread('my_image.jpg',0)    # 2nd argument 0 means to read image as grayscale

cv2.imshow('My Image',img_cv2)
 
cv2.waitKey(0) # to waits until a key is pressed
cv2.destroyAllWindows() # it destroys the window displaying image


