from adafruit_circuitplayground import cp

while True:
    if cp.button_a == True:
        cp.play_file('mixkit-fast-small-sweep-transition-166.wav')
    
    elif cp.button_b == True:
        cp.play_file('mixkit-dog-barking-twice-1.wav')
