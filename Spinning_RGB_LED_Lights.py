import board
from digitalio import DigitalInOut, Direction, Pull
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 10)

led.brightness = 0.1


while True:
    for i in range(10) : 
        led[i] = (100,0,245)
        time.sleep(0.02)
        led[i] = (0,0,0)
