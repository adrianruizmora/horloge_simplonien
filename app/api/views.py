# from flask_cors import CORS
from . import api
from . import fonctions as f
from flask_restplus import Api, Resource

# swagger api doc sera localisé en localhost:5000/api/docs
api = Api(api, doc="/docs")
name_space = api.namespace("clock", description="API Project")


@name_space.route("/time")
class time(Resource):
    def get(self):
        return {
            "time" : f.clock()
        }
