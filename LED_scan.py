import board
from digitalio import DigitalInOut, Direction, Pull
import time

#define LEDs that are connected to CPX connectors
red = DigitalInOut(board.A0) 
blue = DigitalInOut(board.A1) 
green = DigitalInOut(board.A2) 

#configure LEDs as output
red.direction = Direction.OUTPUT
blue.direction = Direction.OUTPUT
green.direction = Direction.OUTPUT

while True:
    #ALL ON
    red.value = True
    time.sleep(0.3)
    red.value = False
    
    blue.value = True
    time.sleep(0.3)
    blue.value = False
    
    green.value = True
    time.sleep(0.3)
    green.value = False
    
    red.value = False
    blue.value = False
    green.value = False
    
    time.sleep(0.3)
    
    blue.value = True
    time.sleep(0.3)
    blue.value = False
    
    red.value = True
    time.sleep(0.3)
    red.value = False
