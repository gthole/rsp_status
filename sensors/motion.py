try:
    import RPi.GPIO as GPIO
except ImportError:
    pass
from base import BaseSensor
from config import settings
import time


class MotionSensor(BaseSensor):
    slug = 'motion'

    def read(self):
        GPIO.setmode(GPIO.BCM)

        pir_pin = settings.MOTION_PIN

        GPIO.setup(pir_pin, GPIO.IN)  # activate input

        for i in range(100):
            if GPIO.input(pir_pin):
                return 1
            time.sleep(.5)
