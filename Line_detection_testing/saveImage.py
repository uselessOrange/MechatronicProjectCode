import cv2

import cv2

cap = cv2.VideoCapture("/dev/v4l/by-id/usb-OmniVision_Technologies__Inc._USB_Camera-B4.09.24.1-video-index0") # video capture source camera (Here webcam of laptop) 
ret,frame = cap.read() # return a single frame in variable `frame`



while(True):
    cv2.imshow('img1',frame) #display the captured image
    cv2.imwrite('/home/miko/Desktop/proj/imag.jpg',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

