from adafruit_circuitplayground.express import cpx
import time

while True:
    if cpx.touch_A1:
        cpx.pixels.fill((15,0,0))
        cpx.start_tone(262)
        
    elif cpx.touch_A2:
        cpx.pixels.fill((0,15,0))
        cpx.start_tone(294)
        
    elif cpx.touch_A3:
        cpx.pixels.fill((0,0,15))
        cpx.start_tone(330)
        
    elif cpx.touch_A4:
        cpx.pixels.fill((15,15,0))
        cpx.start_tone(349)
        
    elif cpx.touch_A5:
        cpx.pixels.fill((0,15,15))
        cpx.start_tone(392)
        
    elif cpx.touch_A6:
        cpx.pixels.fill((15,0,15))
        cpx.start_tone(440)
        
    elif cpx.touch_A7:
        cpx.pixels.fill((15,15,15))
        cpx.start_tone(494)
        
    else:
        cpx.pixels.fill((0,0,0))
        cpx.stop_tone()

    time.sleep(0.4)
