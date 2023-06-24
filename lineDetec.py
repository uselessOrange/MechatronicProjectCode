import cv2
import numpy as np

def LineDetec(frame):

    cx=0
    cy=0
    angle=0
    c=0
    R=0

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Blurring and thresholding for object detection
    img = cv2.blur(img, (3, 3),)
    ret, img = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
    ret, img = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)
    img = cv2.blur(img, (3, 3),)
    ret, img = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)
    #Finding objects
    contours, hierarchy = cv2.findContours(img, 1, cv2.CHAIN_APPROX_NONE)


    if len(contours) > 0:
        #Taknig the biggest object
        c = max(contours, key=cv2.contourArea)
        #Getting the moment (center) of object
        M = cv2.moments(c)
        #Getting the smallest emcompassing rectangle of object
        R = cv2.minAreaRect(c)

        if M["m00"] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            angle = R[-1]

           
        else:
            print("I don't see the line")
    return cx,cy,c,R,angle