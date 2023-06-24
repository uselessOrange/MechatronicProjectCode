import cv2
import numpy as np
from pyzbar.pyzbar import decode
import math
import time
from QR_read import QR_Read
# Initialize the camera
cap = cv2.VideoCapture("/dev/v4l/by-id/usb-OmniVision_Technologies__Inc._USB_Camera-B4.09.24.1-video-index0") # video capture source camera (Here webcam of laptop) 

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()


    qr_data,angle = QR_Read(frame)

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
