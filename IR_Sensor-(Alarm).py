import board
from adafruit_circuitplayground import cp
from digitalio import DigitalInOut, Direction, Pull
import time

#define ir as a digital device connected to A1
ir = DigitalInOut(board.A1) 


#configure ir as INPUT
#remember, you're going to READ the sensor output in CPX)
ir.direction = Direction.INPUT

while True:
    if ir.value == True :
        print("sound on")
        cp.play_file('mixkit-fast-small-sweep-transition-166.wav')
    time.sleep(.5)
