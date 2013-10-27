from backends import mongo
import os
import json
from urlparse import parse_qs
from datetime import datetime, timedelta
import logging
import iso8601

ENDPOINTS = ['/temp/', '/motion/', '/flood/']


def application(environ, start_response):
    if environ['REQUEST_METHOD'] != 'GET':
        status = '405 Method Not Allowed'
        data = {'message': 'Only GET requests supported'}
    elif environ['PATH_INFO'] in ENDPOINTS:
        try:
            status = '200 OK'
            data = make_response(environ)
        except iso8601.ParseError:
            status = '400 Not Found'
            data = {'message': 'Malformed parameter'}
        except:
            logging.exception("Caught exception:\n\n%s" % environ)
            status = '500 Server Error'
            data = {'message': 'Server error'}
    else:
        status = '404 Not Found'
        data = {'message': 'Resource not found'}

    content = json.dumps(data)
    headers = [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(content)))
    ]
    start_response(
        status,
        headers
    )
    return [content]


def make_response(environ):
    collection = environ['PATH_INFO'].strip('/')
    params = parse_qs(environ['QUERY_STRING'])
    if params.get('since'):
        since = iso8601.parse_date(params['since'][0])
    else:
        since = datetime.now() - timedelta(days=7)

    return mongo.get_since(collection, since)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    port = int(os.getenv('PORT', 8888))
    make_server('', port, application).serve_forever()
