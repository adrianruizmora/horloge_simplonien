from flask import Blueprint

# creation instance blueprint pour module web
web = Blueprint("web", __name__)

from . import views
