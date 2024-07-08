import time
from adafruit_circuitplayground import cp

# set tapped to true if tapped once
cp.detect_taps = 1

while True:
    
    if cp.tapped:
        position = 0
        sleep = 0.01
        
        for i in range(30):
            cp.pixels[position] = (25,0,55)
            time.sleep (sleep)
            cp.pixels[position] = (0,0,0)
            time.sleep (sleep)
            
            position = position + 1
            if position == 10:
               position = 0
           
            sleep = sleep + 0.01
