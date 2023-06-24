import cv2
import numpy as np
from pyzbar.pyzbar import decode
import math

#Here we first use cv2 to get the three orientational points of the QR code 
# and use them to determine the angle of the QR code

def QR_Read(frame):
    
    
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get points od orientation of the QR code using cv2
    qr = cv2.QRCodeDetector()
    ret_qr, points = qr.detect(gray)
    qr_data=None
    angle=None

    if points is None:
       pass
        
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

        #Calculation of the angle between two points on the QR code
        if point1x-point2x != 0:
            angle=math.atan2((point1y-point2y),(point1x-point2x))
            angle=(angle*180/np.pi)+180
            
         

            

   



    # Find the QR codes in the frame
    decoded_objects = decode(gray)

    # Loop through each QR code found
    for obj in decoded_objects:
        # Draw a bounding box around the QR code
        cv2.polylines(frame, [np.int32(obj.polygon)], True, (0, 255, 0), 2)

        # Get the QR code data, type and orientation
        qr_data = obj.data.decode("utf-8")
        if qr_data=='1' or qr_data == '2':
            qr_data=int(qr_data)
        else:
            qr_data=None
    return qr_data,angle