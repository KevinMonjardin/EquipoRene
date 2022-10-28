# KY-018 Photoresistor

![image](./photoresistor.gif)

```
from machine import Pin,ADC,PWM
from time import sleep

adc_pin = Pin(26,Pin.IN)
adc = ADC(adc_pin)

while True:
  print(adc.read_u16())
  sleep(1)
```
