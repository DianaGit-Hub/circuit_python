from adafruit_circuitplayground import cp
import random

odd = ("mixkit-fast-small-sweep-transition-166.wav","mixkit-dog-barking-twice-1.wav", "mixkit-single-criket-screech-1780.wav" )

pick = random.choice(odd)
#cp.play_file(pick)
#print ('Random chosen sound is..', (pick))

while True:
    if cp.tapped == True:
        print ('Random chosen sound is..', (odd))
        cp.play_file(odd)
