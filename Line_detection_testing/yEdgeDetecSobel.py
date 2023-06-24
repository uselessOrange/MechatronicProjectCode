import cv2
import numpy as np

image1 = cv2.imread('imag.jpg')

img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

sobel=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
cv2.imshow('Sobel Image',sobel)

if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
