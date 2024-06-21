import board
from digitalio import DigitalInOut, Direction, Pull
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 10)

led.brightness = 0.1


while True:
    for i in range(5) : 
        led[i] = (30,0,50)
        led[9-i] = (30,0,50)
        time.sleep(0.1)
        led[i] = (0,0,0)
        led[9-i] = (0,0,0)
        
    for i in range(3,0,-1) :
        led[i] = (30,0,50)
        led[9-i] = (30,0,50)
        time.sleep(0.1)
        led[i] = (0,0,0)
        led[9-i] = (0,0,0)
