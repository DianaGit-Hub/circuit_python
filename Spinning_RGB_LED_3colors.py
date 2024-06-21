import board
from digitalio import DigitalInOut, Direction, Pull
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 10)

led.brightness = 0.1


while True:
    for i in range(10) : 
        led[i] = (225,0,250)
        time.sleep(0.05)
        led[i] = (0,0,0)
        
    for i in range(10) :
        led[i] = (210,55,0)
        time.sleep(0.05)
        led[i] = (0,0,0)
        
    for i in range(10) :
        led[i] = (0,180,200)
        time.sleep(0.05)
        led[i] = (0,0,0)
