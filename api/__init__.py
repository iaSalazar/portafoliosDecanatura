import time
from flask import Flask
from .extensions import db,ma,api
from .controllers.articulo_controller import *
from .controllers.profesor_controller import *
import os

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    with app.app_context():
        db.create_all()
    return app

#app = create_app()
# ma = Marshmallow(app)
# api = Api(app)
