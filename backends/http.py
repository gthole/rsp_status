import requests
from requests import ConnectionError
from config import settings
import logging
import traceback
import json


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
                data=json.dumps(payload),
                headers={
                    'content-type': 'application/json',
                    'AUTHENTICATION': settings.API_TOKEN
                }
            )
            status = response.status_code
            assert status == 200
        except ConnectionError:
            logging.error(traceback.format_exc())
        except AssertionError:
            logging.error("\n\n".join([status, traceback.format_exc(),
                                       response.content]))
            pass
