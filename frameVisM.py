import cv2
import numpy as np

def frameVis(frame,cx,cy,c,R):
    cv2.circle(frame,(cx,cy),5,(255,255,255),-1)

    box = cv2.boxPoints(R)
    box = np.intp(box)

    cv2.drawContours(frame,c,-1,(0,255,0),1)
    cv2.drawContours(frame,[box],-1,(0,0,255),1)