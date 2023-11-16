#thisfilewaswrittenbykALE

d = 0

def turn_right():
    pass

def turn_left():
    pass

def forward():
    pass

inputVar = [[0,0], [0,1], [0,2], [1,2], [1,3], [1,2], [0,2], [0,1], [0,0]]

def path_to_instruction(inputVar,d):
    for i in range(len(inputVar)-1):
        if inputVar[i][0] < inputVar[i+1][0] and inputVar[i][1] == inputVar[i+1][1] and d == 0: #travel in +x direction, already facing +x direction
            forward()
            d = 0
            print("+x from +x")
        elif inputVar[i][0] < inputVar[i+1][0] and inputVar[i][1] == inputVar[i+1][1] and d != 0: #travel in +x direction, not already facing +x direction
            if d == 1:
                turn_right()
                forward()
                d = 0
                print("+x from +y")
            elif d == 2:
                turn_right()
                turn_right()
                forward() 
                d = 0
                print("+x from -x")
            elif d == 3:
                turn_left()
                forward()
                d = 0
                print("+x from -y")
        elif inputVar[i][0] == inputVar[i+1][0] and inputVar[i][1] < inputVar[i+1][1] and d == 1: #travel in +y direction, already facing +y direction
            forward()
            d = 1
            print("+y from +y")
        elif inputVar[i][0] == inputVar[i+1][0] and inputVar[i][1] < inputVar[i+1][1] and d != 1: #travel in +y direction, not already facing +y direction
            if d == 0:
                turn_left()
                forward()
                d = 1
                print("+y from +x")
            elif d == 2:
                turn_right()
                forward()
                d = 1
                print("+y from -x")
            elif d == 3:
                turn_right()
                turn_right()
                forward()
                d = 1
                print("+y from -y")
        elif inputVar[i][0] > inputVar[i+1][0] and inputVar[i][1] == inputVar[i+1][1] and d == 2: #travel in -x direction, already facing -x direction
            forward()
            d = 2
            print("-x from -x")
        elif inputVar[i][0] > inputVar[i+1][0] and inputVar[i][1] == inputVar[i+1][1] and d != 2: #travel in -x direction, not already facing -x direction
            if d == 0:
                turn_right()
                turn_right()
                forward() 
                d = 2
                print("-x from +x")
            if d == 1:
                turn_left()
                forward()
                d = 2
                print("-x from +y")
            if d == 3:
                turn_right()
                forward()
                d = 2
                print("-x from -y")
        elif inputVar[i][0] == inputVar[i+1][0] and inputVar[i][1] > inputVar[i+1][1] and d == 3: #travel in -y direciton, already facing -y direction
            forward()
            d = 3
            print("-y from -y")
        elif inputVar[i][0] == inputVar[i+1][0] and inputVar[i][1] > inputVar[i+1][1] and d != 3: #travel in -y direciton, not already facing -y direction
            if d == 0:
                turn_right()
                forward()
                d = 3
                print("-y from +x")
            elif d == 1: 
                turn_right()
                turn_right()
                forward()
                d = 3
                print("-y from +y")
            elif d== 2:
                turn_left()
                forward()
                d =3
                print("-y from -x")

#path_to_instruction(inputVar,d)