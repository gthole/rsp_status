from flood import FloodSensor
from motion import MotionSensor
from temp import TemperatureSensor

from celery.task.schedules import crontab
from celery.task import periodic_task

from datetime import datetime, timedelta


@periodic_task(run_every=crontab(hour="*"))
def check_hourly_sensors():
    sensors = [TemperatureSensor, FloodSensor]

    for sensor in sensors:
        sensor().run()


@periodic_task(run_every=crontab(minute="*"))
def check_frequent_sensors():
    sensors = [MotionSensor]

    for sensor in sensors:
        s = sensor()
        last = s.last()
        now = datetime.utcnow()
        if last and last['val'] <= now - timedelta(hour=1):
            s.run()
