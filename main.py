from SimpleGUIMod import buttonEventMod
from HowToGetThereMod import HowToGetThere
from RobotJourneyMod import RobotJourney

run=True
while run==True:
    print("Whould you like to start a journey?\n1.Star a new journey\n2.Turn Robot Off")
    choice = input()
    if int(choice) == 1:
        #Getting robot position and destination from GUI
        WhereIsRobot,WhereRobotGoing=buttonEventMod()

        path=HowToGetThere(WhereIsRobot,WhereRobotGoing)

        RobotJourney(path)
    else:
        run=False