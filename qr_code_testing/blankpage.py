import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Initialize the camera
cap = cv2.VideoCapture("/dev/v4l/by-id/usb-OmniVision_Technologies__Inc._USB_Camera-B4.09.24.1-video-index0") # video capture source camera (Here webcam of laptop) 

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find the QR codes in the frame
    decoded_objects = decode(gray)

    # Loop through each QR code found
    for obj in decoded_objects:
        # Draw a bounding box around the QR code
        cv2.polylines(frame, [np.int32(obj.polygon)], True, (0, 255, 0), 2)
        # Get the QR code data, type and orientation
        qr_data = obj.data.decode("utf-8")
        qr_type = obj.type
        orientation = obj.rect[-1]

        # Print the QR code data, type and orientation to the console
        print("QR Code Type:", qr_type)
        print("QR Code Data:", qr_data)
        print("QR Code Orientation:", orientation)

    # Display the frame
    cv2.imshow('QR Code Scanner', frame)

    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
