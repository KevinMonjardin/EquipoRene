from machine import Pin
from time import sleep

buzzer = Pin(17, Pin.OUT)

while True:
    print(buzzer.value())
    buzzer.value(not buzzer.value())
    sleep(0.5)
