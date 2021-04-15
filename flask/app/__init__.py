from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__, template_folder="templates")
    CORS(app, resources={r'/*': {'origins': '*'}})

    from .web import web as index_horloge_simplonien
    app.register_blueprint(index_horloge_simplonien)

    from .api import api as clock
    app.register_blueprint(clock, url_prefix="/api")
    
    return app
