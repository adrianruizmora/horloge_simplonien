from flask import Flask


def create_app():
    app = Flask(__name__, template_folder="templates")

    from .web import web as index_horloge_simplonien
    app.register_blueprint(index_horloge_simplonien)

    from .api import api as clock
    app.register_blueprint(clock, url_prefix="/api")
    
    return app
