import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.1


left_light = False
right_light = False

#This top section is the left side.

while True:
    if cp.button_a:
        while(cp.button_a):
            pass
        
        left_light = not left_light
        print("left_light:" , left_light)
        
        
   #     while cp.button_a == False:
        while left_light == True:
            for i in range(5):
                cp.pixels[i] = (15,0,30)
                time.sleep(0.1)
        
            for i in range(5):
                cp.pixels[i] = (0,0,0)
                
            if cp.button_a:
                while (cp.button_a):
                    pass
                left_light = False
            
# This bottom section is the right side.

    if cp.button_b:
        while(cp.button_b):
            pass
        
        right_light = not right_light
        print("right_light:" , right_light)
        
        while right_light == True:
            for i in range(9,4,-1):
                cp.pixels[i] = (15,0,30)
                time.sleep(0.1)
        
            for i in range(9,4,-1):
                cp.pixels[i] = (0,0,0)
                
            if cp.button_b:
                while (cp.button_b):
                    pass
                right_light = False
