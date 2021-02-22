from flask import Flask

from api.apod import apod_api
from auth import auth

from db import db
app = Flask(__name__)

app.config.from_object('app.config.Config')

app.register_blueprint(auth)
app.register_blueprint(apod_api)

db.init_app(app)
