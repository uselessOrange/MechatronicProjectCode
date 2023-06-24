
"""Module returns a list: path of type: 
[(int IntersectionID,int angleToTurn),(int 2ndIntersectionID,int 2ndAngleToTurn),...]"""

def HowToGetThere(WhereIsRobot,WhereRobotGoing):
    # Open the Map in read mode
    with open("PathMap.txt", "r") as file:
        # Read the contents of the Map
        content = file.read()

        # Convert the string representation of the tuple to an actual tuple
        # This variable stores all paths for all cases
        my_tuple = eval(content)

# Cases for all paths
    if WhereIsRobot=='H1' and WhereRobotGoing == 'T1':
        path=my_tuple[0]

    elif WhereIsRobot=='H1' and WhereRobotGoing == 'T2':
        path=my_tuple[1]

    elif WhereIsRobot=='H1' and WhereRobotGoing == 'T3':
        path=my_tuple[2]

    elif WhereIsRobot=='T1' and WhereRobotGoing == 'H1':
        path=my_tuple[2]

    elif WhereIsRobot=='T2' and WhereRobotGoing == 'H1':
        path=my_tuple[2]

    elif WhereIsRobot=='T3' and WhereRobotGoing == 'H1':
        path=my_tuple[2]


    else:
        print('path error')

    return path