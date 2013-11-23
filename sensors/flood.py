try:
    import RPi.GPIO as GPIO
except ImportError:
    pass
from config import settings
from base import BaseSensor


class FloodSensor(BaseSensor):
    slug = 'flood'

    def read(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(settings.FLOOD_PIN, GPIO.IN)

        for i in range(10000):
            if not GPIO.input(settings.FLOOD_PIN):
                return

        return 1
