LightCup

Un LightCup es un dispositivo el cual tiene un led, esté cuenta con un switch con contenido de mercurio,
de manera que el modulo del LightCup opera en 5 volts junto con una placa de arduino.

```
from machine import Pin
import time

led = Pin(14, Pin.OUT)
sensor = Pin(27, Pin.IN)

while True:
    if sensor.value() == 1:
        led.off()
        print("NO INCLINADO")
    else:
        led.on()
        print("INCLINADO")
    time.sleep(0.5)
```
