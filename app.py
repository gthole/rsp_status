from flask import Flask, request
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongorest import MongoRest
from flask.ext.mongorest.views import ResourceView
from flask.ext.mongorest.resources import Resource
from flask.ext.mongorest import operators as ops
from flask.ext.mongorest import methods
from flask.ext.mongorest.authentication import AuthenticationBase
from config import settings
import os


app = Flask(__name__)

app.config.update(
    MONGODB_HOST=getattr(settings, 'MONGODB_HOST'),
    MONGODB_PORT=getattr(settings, 'MONGODB_PORT'),
    MONGODB_DB=getattr(settings, 'MONGODB_DB')
)

db = MongoEngine(app)
api = MongoRest(app, url_prefix='/api/v1')


#######################
# Base configurations #
#######################

class ApiKeyAuthentication(AuthenticationBase):
    def authorized(self):
        return request.headers.get('AUTHENTICATION') == settings.API_TOKEN


class BaseDocument(db.Document):
    meta = {'allow_inheritance': True}
    val = db.IntField()
    time = db.DateTimeField()
    station = db.StringField()


class BaseResource(Resource):
    filters = {
        'time': [ops.Gt, ops.Lt],
        'station': [ops.Exact],
    }


class BaseView(ResourceView):
    authentication_methods = [ApiKeyAuthentication]
    methods = [methods.Create, methods.Fetch, methods.List]


#######################
#      Documents      #
#######################

class Motion(BaseDocument):
    pass


class Temp(BaseDocument):
    val = db.FloatField()


class Flood(BaseDocument):
    pass


#######################
#      Resources      #
#######################

class MotionResource(BaseResource):
    document = Motion


class TempResource(BaseResource):
    document = Temp


class FloodResource(BaseResource):
    document = Flood


#######################
#        Views        #
#######################

@api.register(name='motion', url='/motion/')
class MotionView(BaseView):
    resource = MotionResource


@api.register(name='temp', url='/temp/')
class TempView(BaseView):
    resource = TempResource


@api.register(name='flood', url='/flood/')
class FloodView(BaseView):
    resource = FloodResource


if __name__ == "__main__":
    print app.url_map._rules
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
