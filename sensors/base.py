from backends import http
from datetime import datetime
from config import settings


class BaseSensor(object):
    def read(self):
        raise NotImplementedError

    def notify(self):
        pass

    def run(self):
        value = self.read()
        if value:
            self._store(value)

    def _store(self, value):
        now = datetime.now()
        payload = {
            'val': value,
            'time': now.isoformat(),
            'station': settings.STATION
        }
        http.post_to_api(self.slug, payload)
