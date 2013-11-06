import glob
import json
import os
from datetime import datetime, timedelta
from backends import mongo


def load_fixtures():
    """
    Loads some fake data points into mongo for local development
    """
    fixtures = glob.glob(os.path.join('tests', 'fixtures', '*.json'))
    now = datetime.utcnow()
    for fixture in fixtures:
        name = os.path.basename(fixture)[:-5]
        with open(fixture, 'r') as file_:
            data = json.loads(file_.read())
        for index, point in enumerate(data):
            point['time'] = now - timedelta(hours=index)
            mongo.put(name, point)
        print 'Loaded %d data points into %s' % (len(data), name)