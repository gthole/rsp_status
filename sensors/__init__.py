from flood import FloodSensor
from motion import MotionSensor
from temp import TemperatureSensor

import sys


SENSOR_REGISTY = {
    'flood': FloodSensor,
    'motion': MotionSensor,
    'temp': TemperatureSensor
}

def check_sensors_by_name(sensor_names):
    sensors = [SENSOR_REGISTY[name] for name in sensor_names
               if name in SENSOR_REGISTY]

    for sensor in sensors:
        sensor().run()


if __name__ == '__main__':
    check_sensors_by_name(sys.argv[1:])
