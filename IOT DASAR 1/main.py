from machine import Pin 
from utime import sleep

WAKTU_TUNGGU = 0.25

print("Hello, ESP32!")
led1 = Pin (2, Pin.OUT)
led2 = Pin (0, Pin.OUT)
led3 = Pin (4, Pin.OUT)
led4 = Pin (16, Pin.OUT)
led5 = Pin (17, Pin.OUT)
led6 = Pin (5, Pin.OUT)
led7 = Pin (18, Pin.OUT)
led8 = Pin (19, Pin.OUT)

while True:
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    led5.value(1)
    led6.value(1)
    led7.value(1)
    led8.value(1)

    sleep(WAKTU_TUNGGU)

    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    led6.value(0)
    led7.value(0)
    led8.value(0)

    sleep(WAKTU_TUNGGU)