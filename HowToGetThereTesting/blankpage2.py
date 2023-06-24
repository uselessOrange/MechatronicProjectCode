WhereIsRobot='H1'
WhereRobotGoing='T1'


# Open the file in read mode
with open("PathMap.txt", "r") as file:
    # Read the contents of the file
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
    print('Going from H1 to T1')
    path=my_tuple[1]
    for intersection, direction in path:
        print(f'INTER: {intersection}')
        print(f'DIR: {direction}')
else:
    print('path error')


"""
for path in my_tuple:
    print('PATH')
    print(path)
    print()
    for intersection, direction in path:
        print(f'INTER: {intersection}')
        print(f'DIR: {direction}')
"""