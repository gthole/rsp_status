#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from config import settings
from base import BaseSensor


class FloodSensor(BaseSensor):
    collection = 'flood'

    def read():
        reading = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(settings.FLOOD_PIN, GPIO.OUT)
        GPIO.output(settings.FLOOD_PIN, GPIO.LOW)
        time.sleep(0.1)
        GPIO.setup(settings.FLOOD_PIN, GPIO.IN)

        # This takes about 1 millisecond per loop cycle
        while True:
            if (GPIO.input(settings.FLOOD_PIN) == GPIO.LOW):
                reading += 1
            if reading >= 1000:
                return 0
            if (GPIO.input(settings.FLOOD_PIN) != GPIO.LOW):
                return 1
