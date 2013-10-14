import RPi.GPIO as GPIO
from base import BaseSensor


class MotionSensor(BaseSensor):
    collection = 'motion'

    def read(self):
        GPIO.setmode(GPIO.BCM)

        pir_pin = 18

        GPIO.setup(pir_pin, GPIO.IN)  # activate input

        if GPIO.input(pir_pin):
            return 1
        return 0
