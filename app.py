from jinja2 import Environment, FileSystemLoader
import os

TEMPLATE_ENV = Environment(loader=FileSystemLoader('templates/'))
TEMPLATE = TEMPLATE_ENV.get_template('index.html')


def application(environ, start_response):
    data = TEMPLATE.render(message="Hello World!")

    start_response(
        "200 OK",
        [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ]
    )
    return [data]


if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer
    port = int(os.getenv('PORT', 8000))
    WSGIServer(('0.0.0.0', port), application).serve_forever()
