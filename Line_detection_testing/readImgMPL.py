#import cv2, numpy and matplotlib libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("imag.jpg")

# Converting BGR color to RGB color format
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Displaying image using plt.imshow() method
plt.imshow(img)

plt.waitforbuttonpress()

plt.imshow(RGB_img)

plt.waitforbuttonpress()

cv2.imshow('',img2)

plt.waitforbuttonpress()

plt.imshow(img2)


#hold the window
plt.waitforbuttonpress()
plt.close('all')
