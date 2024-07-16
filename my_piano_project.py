import time 
import board 
from adafruit_circuitplayground import cp
import neopixel
from digitalio import DigitalInOut, Direction, Pull
 
# This gon' be all the notes
# c, d, e, f, g, a, b
cp.touch_a1 = DigitalInOut(board.A1) 
cp.touch_a2 = DigitalInOut(board.A2)
cp.touch_a3 = DigitalInOut(board.A3)
cp.touch_a4 = DigitalInOut(board.A4)
cp.touch_a5 = DigitalInOut(board.A5)
cp.touch_a6 = DigitalInOut(board.A6)
cp.touch_a7 = DigitalInOut(board.A7)

note = [262,294,330,349,392,440,494]
duration = [1,1,1,1,1,1,1]
direction = Direction.INPUT



while True:
    if cp.button_a:
        while (cp.button_a):  
		pass
        print("pressed a")
        cp.play_tone(note[i],duration[i])
        
    
    elif cp.touch_a1:
        cp.pixels.fill((15,0,0))
 #       cp.play_tone(note[1])
        print ("A1 has been touched")
        
    elif cp.touch_a2:
        cp.pixels.fill((0,15,0))
 #       cp.play_tone(note[2])
        print ("A2 has been touched")
        
    elif cp.touch_a3:
        cp.pixels.fill((0,0,15))
 #       cp.play_tone(note[3])
        print ("A3 has been touched")
        
    elif cp.touch_a4:
        cp.pixels.fill((15,15,0))
 #       cp.play_tone(note[4])
        print ("A4 has been touched")
        
    elif cp.touch_a5:
        cp.pixels.fill((0,15,15))
 #       cp.play_tone(note[5])
        print ("A5 has been touched")
        
    elif cp.touch_a6:
        cp.pixels.fill((15,0,15))
 #       cp.play_tone(note[6])
        print ("A6 has been touched")
        
    elif cp.touch_a7:
        cp.pixels.fill((15,15,15))
 #       cp.play_tone(note[7])
        print ("A7 has been touched")
        
    else:
        cp.pixels.fill((0,0,0))
        cp.stop_tone()
    
    time.sleep(1)
