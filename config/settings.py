MONGODB_HOST = 'localhost'
MONGODB_PORT = '27017'
MONGODB_DB = 'rsp_status'

FLOOD_PIN = 18
MOTION_PIN = 23

HOST_NAME = 'http://localhost:8000'
STATION = 'Default'
API_TOKEN = None

try:
    from settings_local import *
except ImportError:
    pass
