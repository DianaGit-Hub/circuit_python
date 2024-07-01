from adafruit_circuitplayground import cp
import time
import random

#Player A in this section
while True :
    if cp.button_a == True :
        while(cp.button_a==True):
            pass
        
        playerA_roll = random.randint(1,5)
        print("PlayerA rolled:",playerA_roll)
        
      #  for i in range(5):
      #      cp.pixels[i] =(0,0,0)
       #     time.sleep(0.1)
            
        for i in range(playerA_roll):
            cp.pixels[i] =(25,0,60)
            time.sleep(0.1)
            
# Player B down here
    if cp.button_b == True :
        while(cp.button_b==True):
            pass
        playerB_roll = random.randint(1,5)
        print("PlayerB rolled:",playerB_roll)
        
      #  for i in range(5,10):
      #      cp.pixels[i] =(0,0,0)
      #      time.sleep(0.1)
        
        for i in range(5,5+playerB_roll):
            cp.pixels[i] =(60,25,0)
            time.sleep(0.1)
#Winner
        if  playerA_roll > playerB_roll:
            for x in range(3):
                for i in range(playerA_roll):
                    cp.pixels[i] =(0,60,0)
                time.sleep(0.1)
                    
                cp.pixels.fill((0,0,0))
                time.sleep(0.1)
                
        elif playerB_roll > playerA_roll:
            for x in range(3):
                for i in range (5,5+playerB_roll):
                    cp.pixels[i] = (0,60,0)
                time.sleep(0.1)
                
                cp.pixels.fill((0,0,0))
                time.sleep(0.1)
                
        else:
            for x in range (3):
                for i in range(playerA_roll):
                    cp.pixels[i]=(0,60,0)
                time.sleep(0.1)
                
                for i in range(5,5+playerB_roll):
                    cp.pixels[i] = (0,60,0)
                time.sleep(0.1)
                    
                cp.pixels.fill((0,0,0))
                time.sleep(0.1)
