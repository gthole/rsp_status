from pymongo import MongoClient
from config import settings

CLIENT = MongoClient(settings.DB_URI)
DB = CLIENT.get_default_database()


def put(collection_name, data):
    collection = DB[collection_name]
    collection.save(data)


def get_since(collection_name, since_date):
    collection = DB[collection_name]
    return collection.find({"timestamp": {"$gte": since_date}})


def get_last(collection_name):
    collection = DB[collection_name]
    return collection.find_one()
