import math
import time
from utils.brick import Motor, wait_ready_sensors, EV3ColorSensor

CM = Motor("B")
KM = Motor("C")
# CM.reset_encoder()
# KM.reset_encoder()

def spin_carousel(fire_type):
    
    if fire_type == "A": #blue
        print(CM.get_position())
        CM.set_dps(-90)
        time.sleep(3)
        knock()
        CM.set_dps(90)
        time.sleep(3)
        CM.set_dps(90)
        time.sleep(1)
        CM.set_power(0) 
    elif fire_type == "B": #yellow
        CM.set_dps(-90)
        time.sleep(1.65)
        knock()
        CM.set_dps(90)
        time.sleep(1.65)
        CM.set_dps(90)
        time.sleep(1)
        CM.set_power(0)
    elif fire_type == "C":#purple
        CM.set_dps(-90)
        time.sleep(1)
        knock()
        CM.set_dps(90)
        time.sleep(1)
        CM.set_dps(90)
        time.sleep(1)
        CM.set_power(0)
    elif fire_type == "D":#red
        CM.set_dps(-90)
        time.sleep(3.65)
        knock()
        CM.set_dps(90)
        time.sleep(3.65)
        CM.set_dps(90)
        time.sleep(1)
        CM.set_power(0)
    elif fire_type == "E":#orange
        CM.set_dps(-90)
        time.sleep(.35)
        knock()
        CM.set_dps(90)
        time.sleep(.35)
        CM.set_dps(90)
        time.sleep(1)
        CM.set_power(0)
    elif fire_type == "F":#green
        CM.set_dps(-90)
        time.sleep(2.4)
        knock()
        CM.set_dps(90)
        time.sleep(2.4)
        CM.set_dps(90)
        time.sleep(1)
        CM.set_power(0)

        
def knock():
    CM.set_dps(0)
    KM.set_dps(-180)
    time.sleep(2)
    KM.set_dps(180)
    time.sleep(2)
    KM.set_power(0)
    

spin_carousel("F")
#spin_carousel("B")
# spin_carousel("C")
# spin_carousel("D")
# spin_carousel("E")
# spin_carousel("F")