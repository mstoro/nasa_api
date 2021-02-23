import os


class Config(object):
    DEBUG = True
    SECRET_KEY = str(os.environ.get('SECRET_KEY'))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    APOD_URL = 'https://api.nasa.gov/planetary/apod'
