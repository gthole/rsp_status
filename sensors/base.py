from backends import http, notifier
from datetime import datetime
from config import settings


class BaseSensor(object):
    def read(self):
        raise NotImplementedError

    def run(self):
        value = self.read()
        if value:
            self._store(value)

    def _store(self, value):
        now = datetime.now()

        # Post to API
        payload = {
            'val': value,
            'time': now.isoformat(),
            'station': settings.STATION
        }
        http.post_to_api(self.slug, payload)

        # Email notifications
        self._notify(value, now)

    def _notify(self, value, time):
        if self._should_notify(value):
            subject = "%s Alert at %s" % (
                self.slug.capitalize(), settings.STATION)
            message = "Recorded %s at %s" (self._format_value(value), time)
            notifier.notify(subject, message)

    def _should_notify(self, value):
        return False

    def _format_value(self, value):
        return str(value)
