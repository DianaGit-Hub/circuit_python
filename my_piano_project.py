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

#note = [262,294,330,349,392,440,494]
#duration = [1,1,1,1,1,1,1]
direction = Direction.INPUT



while True:
    
    if cp.touch_a1:
        cp.pixels.fill((15,0,0))
 #       cp.play_tone(262)
        print ("A1 has been touched")
        
        
    elif cp.touch_a2:
        cp.pixels.fill((0,15,0))
 #       cp.play_tone(294)
        print ("A2 has been touched")
        
    elif cp.touch_a3:
        cp.pixels.fill((0,0,15))
 #       cp.play_tone(330)
        print ("A3 has been touched")
        
    elif cp.touch_a4:
        cp.pixels.fill((15,15,0))
 #       cp.play_tone(349)
        print ("A4 has been touched")
        
    elif cp.touch_a5:
        cp.pixels.fill((0,15,15))
 #       cp.play_tone(392)
        print ("A5 has been touched")
        
    elif cp.touch_a6:
        cp.pixels.fill((15,0,15))
 #       cp.play_tone(440)
        print ("A6 has been touched")
        
    elif cp.touch_a7:
        cp.pixels.fill((15,15,15))
 #       cp.play_tone(494)
        print ("A7 has been touched")
        
    else:
        cp.pixels.fill((0,0,0))
        cp.stop_tone()
    
    time.sleep(1)




__________________________________________________________________________________________________________________________






import board
from digitalio import DigitalInOut, Direction, Pull
import time
from adafruit_circuitplayground import cp


#define ir as a digital device connected
ir = DigitalInOut(board.A1) 
ir2 = DigitalInOut(board.A2)
ir3 = DigitalInOut(board.A3) 
ir4 = DigitalInOut(board.A4)
ir5 = DigitalInOut(board.A5) 
ir6 = DigitalInOut(board.A6)
ir7 = DigitalInOut(board.A7)

#key notes = [262,294,330,349,392,440,494]

#configure ir as INPUT
ir.direction = Direction.INPUT

while True:
    #read ir value (True or False)
 #   print(ir.value,ir2.value,ir3.value,ir4.value,ir5.value,ir6.value,ir7.value)
 #   time.sleep(1)
    
#all the keys down below
    if ir == True:
        cp.pixels.fill((15,0,0))
#        cp.play_tone(262)
        
    elif ir2 == True:
        cp.pixels.fill((0,15,0))
#        cp.play_tone(294)
    
    elif ir3 == True:
        cp.pixels.fill((0,0,15))
#        cp.play_tone(330)
        
    elif ir4 == True:
        cp.pixels.fill((15,15,0))
#        cp.play_tone(349)
        
    elif ir5 == True:
        cp.pixels.fill((0,15,15))
#        cp.play_tone(392)
        
    elif ir6 == True:
        cp.pixels.fill((15,0,15))
#        cp.play_tone(440)
        
    elif ir7 == True:
        cp.pixels.fill((15,15,15))
#        cp.play_tone(494)

    else:
        cp.pixels.fill((0,0,0))
        cp.stop_tone()

