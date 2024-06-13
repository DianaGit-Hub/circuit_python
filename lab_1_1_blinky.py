import board
from digitalio import DigitalInOut, Direction
import time

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value  = False
    time.sleep(0.5)
