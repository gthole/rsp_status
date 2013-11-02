from sensors import FloodSensor, MotionSensor, TemperatureSensor

import time
import sys


SENSOR_REGISTY = {
    'flood': FloodSensor,
    'motion': MotionSensor,
    'temp': TemperatureSensor
}

WAIT_TIME = 60 * int(sys.argv[1])
SENSORS = [SENSOR_REGISTY[name] for name in sys.argv[2:]
           if name in SENSOR_REGISTY]
print "Checking %s every %d seconds" % (SENSORS, WAIT_TIME)

while True:
    for sensor in SENSORS:
        sensor().run()
        time.sleep(WAIT_TIME)
