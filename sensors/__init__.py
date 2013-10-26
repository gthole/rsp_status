from flood import FloodSensor
from motion import MotionSensor
from temp import TemperatureSensor

from config import settings

from celery import Celery
from celery.task.schedules import crontab
from celery.task import periodic_task

celery = Celery(broker=settings.DB_URI)


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
        s.run()
