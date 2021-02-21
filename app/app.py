from flask import Flask

from api.apod import apod_api
from auth import auth

from db import db
app = Flask(__name__)

app.config['SECRET_KEY'] = 'asd[jdsvcx3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.register_blueprint(auth)
app.register_blueprint(apod_api)

db.init_app(app)


