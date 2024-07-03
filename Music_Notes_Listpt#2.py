from adafruit_circuitplayground import cp

#twinkle twinkle little star below
note = [262,262,392,392,440,440,392]

# c,d,e,f,g,a,b,c

#note = [262,294,330,349,392,440,494,523]
duration = [2,1,1,1,1,1,2,1]

for i in range(8):
    cp.pixels[i] = (25,0,60)
    cp.play_tone(note[i], duration[i])
    cp.pixels[i] = (0,0,0)
