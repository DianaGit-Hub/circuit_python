import time 
import board 
import adafruit_hcsr04
from adafruit_circuitplayground import cp
import neopixel

#set pixels brightness to 10%
cp.pixels.brightness=0.1

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A2, echo_pin=board.A1)

while True:
    try:
    #get distance
        dis = sonar.distance
        print("dis in cm", dis)
    # convert cm to in
        dis = dis / 2.54
        print("dis in in", dis)
    #round up
        dis = round(dis)
        print("Dis round up to...", dis)
        
    # if the distance is ten: light up leds
        if dis < 10:
            for i in range(dis):
                cp.pixels[i] = (25,0,60)
                time.sleep(0.2)
    #if the distanc eis more than ten: turn on red light
        else:
            for i in range(10):
                cp.pixels[i] = (255,0,0)
                time.sleep(0.2)
    #turn off all leds after they light up
        cp.pixels.fill((0,0,0))
    except RuntimeError:
        print("Retrying!")
        
    time.sleep(1)
