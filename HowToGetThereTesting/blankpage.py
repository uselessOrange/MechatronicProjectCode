WhereIsRobot='H1'
WhereRobotGoing='T1'

my_tuple=[[(1,180),(2,80)],[(1,90)],[(1,0)]]
for path in my_tuple:
    print('PATH')
    print(path)
    print()
    for intersection, direction in path:
        print(f'INTER: {intersection}')
        print(f'DIR: {direction}')