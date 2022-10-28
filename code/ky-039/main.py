from machine import Pin
import time

led = Pin(14, Pin.IN)
buzzer = Pin(27, Pin.OUT)

while True:
    if led.value() == 1:
        print("TRUE")
        buzzer.on()
    else:
        print("FALSE")
        buzzer.off()
    time.sleep(0.5)