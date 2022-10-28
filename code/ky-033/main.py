from machine import Pin
import time


receiver = Pin(24,Pin.IN)
# Break between the results will be defined here (in seconds)
# main loop

while True:
    if receiver.value == False:
        print( "Line detected")
    else:
        print("No line detected")

            # Reset + Delay
        time.sleep(0.5)

