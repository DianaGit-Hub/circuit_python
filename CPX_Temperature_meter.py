import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.1

print("startplot:", "Temperature Sensor")

while True:
    print(cp.temperature * 1.8 + 32)
    
    temp = cp.temperature * 1.8 + 32
    
    if temp < 70:
        cp.pixels.fill((0, 0, 255))
    elif temp < 73:
        cp.pixels.fill((0,128,255))
    elif temp < 76:
        cp.pixels.fill((0,255,0))
    elif temp < 79:
        cp.pixels.fill((28,255,0))
    elif temp < 82:
        cp.pixels.fill((255,0,0))
    else:
        cp.pixels.fill((128,0,128))
    
    time.sleep(0.5)
