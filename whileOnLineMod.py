from ControlRobotMock import ControlRobot

def whileOnLine(cx,speed):
    #If line in frame is to the right: turn right
    if cx <= 135:
        angleTurn=100
        ControlRobot(angleTurn,speed)
    if cx < 175 and cx > 135 :
        angleTurn=90
        ControlRobot(angleTurn,speed)
    #If line in frame is to the left: turn left
    if cx >=175:
        angleTurn=80
        ControlRobot(angleTurn,speed)
