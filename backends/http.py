import requests
from requests import ConnectionError
from config import settings


def post_to_api(slug, payload):
    """
    Simple abstraction for posting sensor data to the API
    """
    tries = 0
    status = None

    while status is None and tries < 3:
        tries += 1
        try:
            response = requests.post(
                '%s/api/v1/%s/' % (settings.HOST_NAME, slug),
                data=payload,
                headers={'AUTHENTICATION': settings.API_TOKEN}
            )
            status = response.status_code
            assert status == 202
        except (AssertionError, ConnectionError):
            pass
