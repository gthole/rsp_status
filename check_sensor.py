from sensors import FloodSensor, MotionSensor, TemperatureSensor

import time
import sys
import logging


SENSOR_REGISTY = {
    'flood': FloodSensor,
    'motion': MotionSensor,
    'temp': TemperatureSensor
}

WAIT_TIME = 60 * int(sys.argv[1])
SENSOR = SENSOR_REGISTY[sys.argv[2]]

logging.warning("Checking %s every %d seconds" % (SENSOR, WAIT_TIME))

while True:
    start = time.time()
    SENSOR().run()
    end = time.time()
    time.sleep(max(WAIT_TIME - (end - start), 1))
