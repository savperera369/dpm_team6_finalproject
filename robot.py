print("Beginning startup...")

import time
import math
from utils.brick import Motor, wait_ready_sensors, EV3ColorSensor

# GLOBAL VARIABLES

enabled = True
job_list = {(0,0,"A"),(0,0,"A"),(0,0,"A")}
RED = (44, 9, 8)
GREEN = (5, 20, 10)
BLUE = (15, 12, 15)
BROWN = (46, 30, 21)
MAX_ERROR = 100

# INITIALIZE SENSORS AND MOTORS
print("Initializing sensors and motors...")
CS1 = EV3ColorSensor(1)
CS2 = EV3ColorSensor(2)

wait_ready_sensors()
print("Sensors and motors initialized.")

# NAVIGATION FUNCTIONS

def color_distance(raw_value1, raw_value2):
    dR = raw_value1[0] - raw_value2[0]
    dG = raw_value1[1] - raw_value2[1]
    dB = raw_value1[2] - raw_value2[2]
    return math.sqrt((dR**2)+(dG**2)+(dB**2))

def color(sensor_name):
    raw_value = sensor_name.get_raw_value()
    d_red = color_distance(raw_value, RED)
    d_green = color_distance(raw_value, GREEN)
    d_blue = color_distance(raw_value, BLUE)
    d_brown = color_distance(raw_value,BROWN)
    if (d_brown <= d_red) and (d_brown <= d_green) and (d_brown <= d_blue)and (d_brown <= MAX_ERROR):
        return "BROWN"
    elif (d_blue <= d_red) and (d_blue <= d_green) and (d_brown <= d_brown)and (d_blue <= MAX_ERROR):
        return "BLUE"
    elif (d_green <= d_red) and (d_green <= d_blue) and (d_green <= d_brown)and (d_green <= MAX_ERROR):
        return "GREEN"
    elif (d_red <= d_green) and (d_red <= d_blue) and (d_red <= d_brown)and (d_red <= MAX_ERROR):
        return "RED"
    else:
        return "NONE"
    
def forward(d):
    print("Forward", end="")
    print(d)
    
def reverse(d):
    print("Reverse", end="")
    
def left():
    print("left")
    
def right():
    print("right")

# MAIN PROGRAM
print (CS1.get_raw_value, end="")
print(color(CS1))
print (CS2.get_raw_value, end="")
print(color(CS2))
while enabled:
    pass
BP.resetall()