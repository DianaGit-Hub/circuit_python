import time
from adafruit_circuitplayground import cp

print(cp.button_a)
print(cp.button_b)

while True:
    if cp.button_a:
        while (cp.button_a):  
		pass
        print("pressed a")
    if cp.button_b:
        while (cp.button_b):  
		pass
        print("pressed b")
