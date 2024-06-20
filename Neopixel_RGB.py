import board
from digitalio import DigitalInOut, Direction, Pull
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.1

switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    if (switch.value==True):
        led[0] = (255,50,155)
    else:
        led[0] = (100,0,245)
