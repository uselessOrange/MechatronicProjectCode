from lineDetec import LineDetec
import cv2
import numpy as np
import time


# video capture source camera (Here webcam of laptop)
cap = cv2.VideoCapture(
    "/dev/v4l/by-id/usb-OmniVision_Technologies__Inc._USB_Camera-B4.09.24.1-video-index0")

cap.set(3, 160)
cap.set(4, 120)


while True:

    ret, frame = cap.read()
    
    cx,cy,c,R,angle = LineDetec(frame)

    if cx & cy != 0:
        cv2.circle(frame,(cx,cy),5,(255,255,255),-1)

        box = cv2.boxPoints(R)
        box = np.intp(box)

        cv2.drawContours(frame,c,-1,(0,255,0),1)
        cv2.drawContours(frame,[box],-1,(0,0,255),1)



        print("CX : "+str(cx)+" Angle : "+str(angle))
        cv2.imshow('Final', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):		
        break
