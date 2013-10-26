import RPi.GPIO as GPIO
import time
from config import settings
from base import BaseSensor


class FloodSensor(BaseSensor):
    collection = 'flood'

    def read():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(settings.FLOOD_PIN, GPIO.OUT)
        GPIO.output(settings.FLOOD_PIN, GPIO.LOW)
        time.sleep(0.1)
        GPIO.setup(settings.FLOOD_PIN, GPIO.IN)

        reading = 0
        for i in range(10000):
            if (GPIO.input(settings.FLOOD_PIN) == GPIO.LOW):
                reading += 1

        if reading > 9990:
            return 1
