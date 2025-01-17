import board
from digitalio import DigitalInOut, Direction, Pull
import time

red = DigitalInOut(board.A0) 
blue = DigitalInOut(board.A1) 
green = DigitalInOut(board.A2) 

#configure LEDs as output
red.direction = Direction.OUTPUT
blue.direction = Direction.OUTPUT
green.direction = Direction.OUTPUT


switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

print(switch.value)

while True:
    if (switch.value==True):
        
        red.value = True
        blue.value = True
        green.value = True

        time.sleep(1)
        
        
    else:
        red.value = False
        blue.value = False
        green.value = False

        time.sleep(1)
