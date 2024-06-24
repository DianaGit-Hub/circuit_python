import board
from digitalio import DigitalInOut, Direction, Pull
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 10)

led.brightness = 0.1

switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

print(switch.value)

while True:
    if (switch.value==True):
        for i in range(9,-1,-1) : 
            led[i] = (225,0,250)
            led[9-i] = (0,150,70)
            time.sleep(0.2)
            led[i] = (0,0,20)
            led[9-i] = (0,0,0)
         
          #for i in range(10) : 
            led[i] = (225,0,250)
            time.sleep(0.05)
            led[i] = (0,0,20)
        
#        for i in range(10) :
            led[i] = (210,55,0)
            time.sleep(0.05)
            led[i] = (20,0,0)
        
 #       for i in range(10) :
            led[i] = (0,180,200)
            time.sleep(0.05)
            led[i] = (0,20,0)

    else:
        for i in range(5) : 
            led[i] = (30,0,50)
            led[9-i] = (30,0,50)
            time.sleep(0.08)
            led[i] = (0,0,15)
            led[9-i] = (0,0,15)
        
        for i in range(3,0,-1) :
            led[i] = (30,0,50)
            led[9-i] = (30,0,50)
            time.sleep(0.08)
            led[i] = (0,20,0)
            led[9-i] = (0,20,0)
