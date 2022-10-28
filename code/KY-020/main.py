from machine import Pin

import time
 
sensor = Pin(17,Pin.IN)
#create ds18x20 object
while True:
   
   if sensor.value == 0:
       print("No se detecta movimiento")
   else:
       print("hay movimiento")
   
   time.sleep(1)
