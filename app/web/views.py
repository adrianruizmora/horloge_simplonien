# import web from app/web/__init__.py
from . import web
from flask import render_template


# localhost:5000 acceder cette entrée et
# renvoyer render template d'index.html
@web.route("/")
def index():
    return render_template("index.html")
