# Python program to illustrate
# simple thresholding type on an image
	
# organizing imports
import cv2
import numpy as np
import time


cap = cv2.VideoCapture("/dev/v4l/by-id/usb-OmniVision_Technologies__Inc._USB_Camera-B4.09.24.1-video-index0") # video capture source camera (Here webcam of laptop) 

cap.set(3, 160)
cap.set(4, 120)

while True:
	ret,frame = cap.read() # return a single frame in variable `frame`
	img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#	img=1-img
	img = cv2.blur(img, (3, 3),)
	ret, img = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
	ret, img = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)
	img = cv2.blur(img, (3, 3),)
	ret, img = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY)

	contours, hierarchy = cv2.findContours(img,1,cv2.CHAIN_APPROX_NONE)

	if len(contours)>0:
		c=max(contours,key=cv2.contourArea)
		M = cv2.moments(c)
		R = cv2.minAreaRect(c)

		if M["m00"] != 0:
			cx = int(M['m10']/M['m00'])
			cy = int(M['m01']/M['m00'])

			angle = R[-1]

			print("CX : "+str(cx)+"  CY : "+str(cy)+" Angle : "+str(angle))
		else :
			print("I don't see the line")

	cv2.circle(frame,(cx,cy),5,(255,255,255),-1)

	box = cv2.boxPoints(R)
	box = np.intp(box)

	cv2.drawContours(frame,c,-1,(0,255,0),1)
	cv2.drawContours(frame,[box],-1,(0,0,255),1)



	cv2.imshow('Final', frame)
	cv2.imshow('Fl', img)

#	time.sleep(1)
	if cv2.waitKey(1) & 0xff == ord('q'):		
		break