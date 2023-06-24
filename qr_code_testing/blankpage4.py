import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

# Initialize the camera
cap = cv2.VideoCapture("/dev/v4l/by-id/usb-OmniVision_Technologies__Inc._USB_Camera-B4.09.24.1-video-index0") # video capture source camera (Here webcam of laptop) 



while True:
    # Capture a frame from the camera
    ret, frame = cap.read()



    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find the QR codes in the frame
    decoded_objects = pyzbar.decode(gray)


    # Display the frame
    qr = cv2.QRCodeDetector()
    ret_qr, points = qr.detect(gray)
    if points is None:
        print('qr not detected')
        
    else:     
        count=0
        for i in range(3):
            xpos=int(points[0,count,0])
            ypos=int(points[0,count,1])
            cv2.circle(frame, [xpos,ypos], 5, (0, 0, 255), -1)
            count=count+1

        point1x=int(points[0,0,0])
        point1y=int(points[0,0,1])
        point2x=int(points[0,3,0])
        point2y=int(points[0,3,1])
        if point1x-point2x != 0:
            angle=np.arctan((point1y-point2y)/(point1x-point2x))
            #angle=np.rad2deg(angle)
            angle=angle*180/np.pi
            print('angle ',angle)
        print([point1x,point1y],'..', [point2x,point2y])
            
   
    cv2.imshow('QR Code Scanner', frame)



    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
