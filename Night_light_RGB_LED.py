import board
import analogio
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL,10)

light = analogio.AnalogIn(board.LIGHT)

#print("startplot:","Light Sensor")

while True :
    if light.value < 7500 :
        for i in range(9) : 
            led[i] = (15,0,40)

        print("An if block" , light.value)
        time.sleep(2)
    
    else: 
        for i in range(9):
            led[i] = (0,0,0)

        print("An else block" , light.value)
        time.sleep(2)
