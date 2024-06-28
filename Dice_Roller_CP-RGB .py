from adafruit_circuitplayground import cp
import time
import random

cp.pixels.brightness = 0.1

while True :
    if cp.button_b == True :
        while(cp.button_b==True):
            pass
        
        roll = random.randint(1,10)
        print("You rolled:",roll)
                
        for i in range(10):
            cp.pixels[i] =(0,0,0)
            time.sleep(0.1)
            
        for i in range(roll):
            cp.pixels[i] =(25,0,50)
            time.sleep(0.1)
