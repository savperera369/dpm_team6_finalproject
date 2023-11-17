import math
import time
from utils.brick import Motor, wait_ready_sensors, EV3ColorSensor

CM = Motor("B")
KM = Motor("C")

def spin_carousel(fire_type):
    SPIN_POWER = 25
    T_A = 0.85
    
    if fire_type == "A": #blue
        CM.set_power((-1) * SPIN_POWER)
        time.sleep(T_A)
        CM.set_power(0)
        knock()
        CM.set_power(SPIN_POWER)
        time.sleep(T_A + 0.25)
        CM.set_power(0)
    elif fire_type == "B": #yellow
        pass
    elif fire_type == "C":#purple
        pass
    elif fire_type == "D":#red
        pass
    elif fire_type == "E":#orange
        pass
    elif fire_type == "F":#green
        pass
    
def knock():
    KM.set_dps(-180)
    time.sleep(2)
    KM.set_dps(180)
    time.sleep(2)
    KM.set_power(0)
    
spin_carousel("A")
