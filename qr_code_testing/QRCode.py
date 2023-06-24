import cv2
import numpy as np
from pyzbar.pyzbar import decode
import math
import time
# Initialize the camera
#cap = cv2.VideoCapture("/dev/v4l/by-id/usb-OmniVision_Technologies__Inc._USB_Camera-B4.09.24.1-video-index0") # video capture source camera (Here webcam of laptop) 
cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of >

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get angle using cv2
    qr = cv2.QRCodeDetector()
    ret_qr, points = qr.detect(gray)

    if points is None:
        print('')
        
    else:     
        # Draw QR code boundary
        count=0
        for i in range(4):
            xpos=int(points[0,count,0])
            ypos=int(points[0,count,1])
            cv2.circle(frame, [xpos,ypos], 5, (0, 0, 255), -1)
            count=count+1

        point1x=int(points[0,0,0])
        point1y=int(points[0,0,1])
        point2x=int(points[0,3,0])
        point2y=int(points[0,3,1])

        if point1x-point2x != 0:
            angle=math.atan2((point1y-point2y),(point1x-point2x))
            angle=(angle*180/np.pi)+180
            
         

            print('angle ',angle)

   



    # Find the QR codes in the frame
    decoded_objects = decode(gray)

    # Loop through each QR code found
    for obj in decoded_objects:
        # Draw a bounding box around the QR code
        cv2.polylines(frame, [np.int32(obj.polygon)], True, (0, 255, 0), 2)

        # Get the QR code data, type and orientation
        qr_data = obj.data.decode("utf-8")

        # Print the QR code data
        print("QR Code Data: ", qr_data,' Angle: ',angle)

    # Display the frame
    cv2.imshow('QR Code Scanner', frame)
    #time.sleep(1/30)
    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
