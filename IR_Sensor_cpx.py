import board
from digitalio import DigitalInOut, Direction, Pull
import time

#define ir as a digital device connected to A1
ir = DigitalInOut(board.A1) 


#configure ir as INPUT
#remember, you're going to READ the sensor output in CPX)
ir.direction = Direction.INPUT

while True:
    
    #read ir value (True or False)
    print(ir.value)
    time.sleep(1)
