from adafruit_circuitplayground import cp

light_ON = False

while True:
    if cp.button_a:
        while(cp.button_a):
            pass
        
        light_ON = not light_ON
        
        if light_ON:
            cp.pixels.fill((25,0,50))
        else:
	        cp.pixels.fill((0,0,0))
