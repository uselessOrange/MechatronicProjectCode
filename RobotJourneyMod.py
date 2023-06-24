import cv2
import time
from lineDetec import LineDetec
from QR_read import QR_Read
from whileOnLineMod import whileOnLine
from frameVisM import frameVis
from ControlRobotMock import ControlRobot
from findLineMod import FindLine
from sensorsMock import CheckForCollision
def RobotJourney(path):    
    

    codeFrequency=1/30 #[1/s] or [Hz]
    TimeToWaitIfLost=1 #[s]
    
    #Video capture source camera 
    cap = cv2.VideoCapture(
        "/dev/v4l/by-id/usb-OmniVision_Technologies__Inc._USB_Camera-B4.09.24.1-video-index0")
    #horisontal pixels for 0-320
    cap.set(3, 160)
    cap.set(4, 120)    
    
    inter=[]
    dir=[]

    #Unboxing the path object into two arrays
    for intersection, direction in path :
        inter.append(intersection)
        dir.append(direction)

    counterIntersection=0
    run=True
    pastQR=[0]
    while run==True:


        #takes a image
        ret, frame = cap.read()
        
        #detects line and returns needed data
        cx,cy,c,R,angle = LineDetec(frame)

        collision=CheckForCollision()
        if collision==True:

            #Stop robot
            ControlRobot(0,0)
            time.sleep(0.5) #[s]

            #Overwriting the LineDetec parameters
            #This makes the robot activate the FindLine() after an amout of time while stuck 
            cx=0
            cy=0


        if cx & cy != 0:
            LineLostIter=[]

            #Draws contours on detected line
            frameVis(frame,cx,cy,c,R)
    #        print('cx>>',cx)

            #Controls robot during line following
            speed = 100
            whileOnLine(cx,speed)


            qr_data,angle = QR_Read(frame)

        #QR detection logic:
            #if recognised QR is detected:
            if qr_data == 1 or qr_data == 2 or qr_data == 3 or qr_data == 4: #here add all recognised QR codes you might expect
                
                #Save the last detected QR
                pastQR.append(qr_data)


                #If last value of list pastQR is on qr_data: skip the intersection logic.
                #This error occurs due to frame buffering and makes the same QR being recognised multiple times
                if pastQR[len(pastQR)-2]==qr_data:
                    
                    #In case of buffering error qr_data is overwritten so that the 
                    # QR logic is skipped and counter unchaned
                    qr_data=None
                
                #In number of intersections passed by robot (counterIntersection) 
                #is greater than supposed number of intersections needed to compleate the path 
                #it means that the robot is at its destination
                elif counterIntersection==len(inter):
                    run=False
                    break

                #If the qr_data is proper and is not a repetition due to buffering then qr_data 
                # will be used to control the direction og the robot
                elif qr_data == 1 or qr_data == 2 or qr_data == 3 or qr_data == 4: #here add all recognised QR codes you might expect
                    ControlRobot(dir[qr_data-1],speed)
                    print("on intersection")
                    counterIntersection=counterIntersection+1
                    time.sleep(2)



            cv2.imshow('Final', frame)
            #cap frequency of while loop
            time.sleep(codeFrequency)
        else:
            LineLostIter=LineLostIter+1
            #If the robot has lost the line for the amount of time specified beforehand,
            #the robot preceeds to find the line
            if LineLostIter*codeFrequency==TimeToWaitIfLost:
                FindLine()

        if cv2.waitKey(1) & 0xff == ord('q'):		
            break
        if cx & cy == 0:
            pass
