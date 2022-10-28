from machine import Pin
import time

RUNNING = True

green = Pin(27,Pin.OUT)
red = Pin(17,Pin.OUT)
blue = Pin(22,Pin.OUT)

time_to_sleep = 250

while True:
    red.on()
    time.sleep_ms(time_to_sleep)
    green.on()
    time.sleep_ms(time_to_sleep)
    red.off()
    time.sleep_ms(time_to_sleep)
    blue.on()
    time.sleep_ms(time_to_sleep)
    green.off()
    time.sleep_ms(time_to_sleep)
    red.on()
    time.sleep_ms(time_to_sleep)
    blue.off()
    time.sleep_ms(time_to_sleep)
    red.off()
    time.sleep_ms(time_to_sleep)
# ky-016
