def HowToGetThere(WhereIsRobot,WhereRobotGoing):
    # Open the Map in read mode
    with open("PathMap.txt", "r") as file:
        # Read the contents of the Map
        content = file.read()

        # Convert the string representation of the tuple to an actual tuple
        my_tuple = eval(content)

    if WhereIsRobot=='H1' and WhereRobotGoing == 'T1':
        print('Going from H1 to T1')
        path=my_tuple[0]
        for intersection, direction in path:
            print(f'INTER: {intersection}')
            print(f'DIR: {direction}')
    elif WhereIsRobot=='H1' and WhereRobotGoing == 'T2':
        print('Going from H1 to T2')
        path=my_tuple[1]
        for intersection, direction in path:
            print(f'INTER: {intersection}')
            print(f'DIR: {direction}')
    elif WhereIsRobot=='H1' and WhereRobotGoing == 'T3':
        print('Going from H1 to T3')
        path=my_tuple[2]
        for intersection, direction in path:
            print(f'INTER: {intersection}')
            print(f'DIR: {direction}')
    else:
        print('path error')


WhereIsRobot='H1'
WhereRobotGoing='T1'

HowToGetThere(WhereIsRobot,WhereRobotGoing)