from machine import Pin
from time import sleep

# Set up the pins
pin = Pin(17, Pin.IN)

while True:
    try:
        print(pin)
        temperature_c = pin.temperature
        print("Temperature: %3.1f C" % temperature_c)
        sleep(1)
    except OSError as e:
        print("Failed to read temperature")
        sleep(1)
