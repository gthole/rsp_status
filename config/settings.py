MONGODB_HOST = 'localhost'
MONGODB_PORT = '27017'
MONGODB_DB = 'rsp_status'

FLOOD_PIN = 18
MOTION_PIN = 23

HOST_NAME = 'http://localhost:8000'
STATION = 'Default'
API_TOKEN = None

EMAIL_USER = None
EMAIL_PASS = None
EMAIL_ADDY = None
EMAIL_PORT = '587'
EMAIL_STLS = False

HIGH_TEMP = 90
LOW_TEMP = 28

NOTIFY = []
ADMINS = []

try:
    from settings_local import *
except ImportError:
    pass
