from adafruit_circuitplayground import cp
import time
import random

cp.pixels.brightness = 0.1

while True :
        i = random.randint(0,9)
     	cp.pixels[i] =(25,0,50)
        time.sleep(0.4)
  
     	cp.pixels[i] =(0,0,0)
        time.sleep(0.4)
