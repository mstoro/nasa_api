from flask import Flask, jsonify

from api.apod import apod_api
from api.errors import TokenError
from auth import auth
from db import db

app = Flask(__name__)

app.config.from_object('config.Config')

app.register_blueprint(auth)
app.register_blueprint(apod_api)

db.init_app(app)


@app.errorhandler(TokenError)
def handle_token_errors(error):
    app.logger.error(error.json)
    return jsonify(error.json)


if __name__ == '__main__':
    app.run()
