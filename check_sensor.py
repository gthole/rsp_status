from sensors import FloodSensor, MotionSensor, TemperatureSensor
from backends import notifier

import time
import datetime
import sys
import logging
import traceback


SENSOR_REGISTY = {
    'flood': FloodSensor,
    'motion': MotionSensor,
    'temp': TemperatureSensor
}

WAIT_TIME = 60 * int(sys.argv[1])
SENSOR = SENSOR_REGISTY[sys.argv[2]]

logging.warning("Checking %s every %d seconds" % (SENSOR, WAIT_TIME))

try:
    while True:
        start = time.time()
        SENSOR().run()
        end = time.time()
        time.sleep(max(WAIT_TIME - (end - start), 1))
except:
    notifier.alert(
        "Sensor loop %s has crashed" % sys.argv[1],
        "%s\n\n%s" % (datetime.datetime.now(), traceback.format_exc())
    )
