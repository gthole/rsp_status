from backends import mongo
from datetime import datetime


class BaseSensor:
    def read(self):
        raise NotImplementedError

    def notify(self):
        pass

    def run(self):
        value = self.run()
        if value:
            self._store(value)

    def _store(self, value):
        now = datetime.now()
        mongo.put({'time': now, 'val': value})

    def last(self):
        last = mongo.get_last(self.collection)
        if last:
            return last.get('val')
