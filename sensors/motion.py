import RPi.GPIO as GPIO
from base import BaseSensor
from config import settings


class MotionSensor(BaseSensor):
    collection = 'motion'

    def read(self):
        GPIO.setmode(GPIO.BCM)

        pir_pin = settings.MOTION_PIN

        GPIO.setup(pir_pin, GPIO.IN)  # activate input

        if GPIO.input(pir_pin):
            return 1
