import cv2
import numpy as np

image1 = cv2.imread('imag.jpg')

img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
cv2.imshow('1',img)

img2 = cv2.blur(img, (3, 3),)
cv2.imshow('2',img2)

ret, thresh1 = cv2.threshold(img2, 120, 255, cv2.THRESH_TOZERO)
cv2.imshow('thresh1',thresh1)

ret, thresh11 = cv2.threshold(thresh1, 190, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh11',thresh11)

img3 = cv2.blur(thresh11, (3, 3),)
cv2.imshow('2',img3)

ret, thresh111 = cv2.threshold(img3, 190, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh111',thresh111)


sobel=cv2.Sobel(thresh111,cv2.CV_64F,1,0,ksize=3)
sobel2=cv2.Sobel(thresh111,cv2.CV_64F,0,1,ksize=3)
cv2.imshow('Sobel Image',sobel)
cv2.imshow('Sobel Image2',sobel2)


if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()

"""Conclusions:
while working on grayscale image to extract a singular object (line) from photo best aproach is to thres_tozero and then thresh_binary
blurring both the grayscale image before threshholding and the image after threshholding creats a desired effect of mode unified body i.e clearer object detection
Sobel operator for edge detection is not a proper aproach due"""