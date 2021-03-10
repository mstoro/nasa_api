import os


class Config(object):
    DEBUG = True
    SECRET_KEY = str(os.environ.get('SECRET_KEY'))
    APOD_URL = 'https://api.nasa.gov/planetary/apod'
    CME_URL = 'https://api.nasa.gov/DONKI/CME'
    MEDIA_FOLDER = 'media'
