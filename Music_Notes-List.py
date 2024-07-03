from adafruit_circuitplayground import cp

note = [262,294,330,349,392,440,494,523]
duration = [1,1,1,1,1,1,1,1]

for i in range(8):
    cp.play_tone(note[1], duration[1]) 
    cp.play_tone(note[1], duration[1])

    cp.play_tone(note[5], duration[1]) 
    cp.play_tone(note[5], duration[1])
    
    cp.play_tone(note[6], duration[1]) 
    cp.play_tone(note[6], duration[1])
   
    cp.play_tone(note[5], duration[1])
