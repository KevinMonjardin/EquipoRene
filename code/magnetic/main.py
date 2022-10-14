from machine import Pin
import time

pin = Pin(14, Pin.IN)

while True:
    if pin.value() == 1:
        print("No magnet")
    else:
        print("Magnet detected")
    time.sleep(0.5)
    



        
 

