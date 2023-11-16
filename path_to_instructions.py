import math
import time
from utils.brick import Motor, wait_ready_sensors, EV3ColorSensor

CM = Motor("B")
KM = Motor("C")
# CM.reset_encoder()
# KM.reset_encoder()

#thisfilewaswrittenbykALE

d = 0

def turn_right():
    pass

def turn_left():
    pass

def forward():
    pass

input = [[0,0], [0,1], [0,2], [1,2], [1,3], [1,2], [0,2], [0,1], [0,0]]

def path_to_instruction(input):
    for i in range(len(input - 1)):
        if input[i][0] < input[i+1][0] and input[i][1] == input[i+1][1] and d == 0: #travel in +x direction, already facing +x direction
            forward()
        elif input[i][0] < input[i+1][0] and input[i][1] == input[i+1][1] and d != 0: #travel in +x direction, not already facing +x direction
            if d == 1:
                turn_right()
                forward()
            elif d == 2:
                turn_right()
                turn_right()
                forward()
            elif d == 3:
                turn_left()
                forward()
        elif input[i][0] == input[i+1][0] and input[i][1] < input[i+1][1] and d == 1: #travel in +y direction, already facing +y direction
            forward()
        elif input[i][0] == input[i+1][0] and input[i][1] < input[i+1][1] and d != 1: #travel in +y direction, not already facing +y direction
            if d == 0:
                turn_left()
                forward()
            elif d == 2:
                turn_right()
                forward()
            elif d == 3:
                turn_right()
                turn_right()
                forward()
        elif input[i][0] > input[i+1][0] and input[i][1] == input[i+1][1] and d == 2: #travel in -x direction, already facing -x direction
            forward()
        elif input[i][0] > input[i+1][0] and input[i][1] == input[i+1][1] and d != 2: #travel in -x direction, not already facing -x direction
            if d == 0:
                turn_right()
                turn_right()
                forward()
            if d == 1:
                turn_left()
                forward()
            if d == 3:
                turn_right()
                forward()
        elif input[i][0] == input[i+1][0] and input[i][1] > input[i+1][1] and d == 3: #travel in -y direciton, already facing -y direction
            forward()
        elif input[i][0] == input[i+1][0] and input[i][1] > input[i+1][1] and d != 3: #travel in -y direciton, not already facing -y direction
            if d == 0:
                turn_right()
                forward()
            elif d == 1: 
                turn_right()
                turn_right()
                forward()
            elif d== 2:
                turn_left()
                forward()