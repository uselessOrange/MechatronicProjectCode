# Python program to illustrate
# simple thresholding type on an image
	
# organizing imports
import cv2
import numpy as np

# path to input image is specified and
# image is loaded with imread command
image1 = cv2.imread('imag.jpg')

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# applying different thresholding
# techniques on the input image
# all pixels value above 120 will
# be set to 255

#ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
#ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
#ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
#ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# the window showing output images
# with the corresponding thresholding
# techniques applied to the input images
#cv2.imshow('Binary Threshold', thresh1)
#cv2.imshow('Binary Threshold Inverted', thresh2)
#cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
#cv2.imshow('Set to 0 Inverted', thresh5)
	


ret, thresh11 = cv2.threshold(thresh4, 190, 255, cv2.THRESH_BINARY)
#ret, thresh21 = cv2.threshold(thresh4, 120, 255, cv2.THRESH_BINARY_INV)
#ret, thresh31 = cv2.threshold(thresh4, 120, 255, cv2.THRESH_TRUNC)
#ret, thresh41 = cv2.threshold(thresh4, 120, 255, cv2.THRESH_TOZERO)
#ret, thresh51 = cv2.threshold(thresh4, 120, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('Binary Threshold1', thresh11)
#cv2.imshow('Binary Threshold Inverted1', thresh21)
#cv2.imshow('Truncated Threshold1', thresh31)
#cv2.imshow('Set to 01', thresh41)
#cv2.imshow('Set to 0 Inverted1', thresh51)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
