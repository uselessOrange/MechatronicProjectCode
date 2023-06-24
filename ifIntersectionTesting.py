import time
from whileOnLineMod import whileOnLine
from ControlRobotMock import ControlRobot
from HowToGetThereMod import HowToGetThere

WhereIsRobot='H1'
WhereRobotGoing='T1'
path=HowToGetThere(WhereIsRobot,WhereRobotGoing)
inter=[]
dir=[]
for intersection, direction in path :
    inter.append(intersection)
    dir.append(direction)
    print(f'INTER: {intersection}')
    print(f'DIR: {direction}')
counterIntersection=0
run=True
while run==True:

    cx=160
    cy=160
    if cx & cy != 0:
 
        #Controls robot during line following
        speed = 100
        whileOnLine(cx,speed)


        qr_data=(1)
        
        if counterIntersection==len(inter):
            run=False
            pass
        elif qr_data == 1 or qr_data == 2:
            ControlRobot(dir[qr_data-1],speed)
            print("on intersection")
            counterIntersection=counterIntersection+1
            print(counterIntersection)
            time.sleep(2)


        



