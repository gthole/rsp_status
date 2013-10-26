from pymongo import MongoClient
from config import settings
from datetime import datetime, timedelta
import glob
import json
import os

CLIENT = MongoClient(settings.DB_URI)
DB = CLIENT.get_default_database()


def put(collection_name, data):
    collection = DB[collection_name]
    collection.save(data)


def get_since(collection_name, since_date):
    collection = DB[collection_name]
    cursor = collection.find({"time": {"$gte": since_date}})
    return [
        {
            'time': r['time'].isoformat(),
            'val': r['val']
        } for r in cursor
    ]


def get_last(collection_name):
    collection = DB[collection_name]
    return collection.find_one()


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
            put(name, point)
        print 'Loaded %d data points into %s' % (len(data), name)
