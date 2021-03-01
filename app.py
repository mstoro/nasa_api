from flask import Flask, jsonify

from api.apod import apod_api
from api.errors import ApiKeyError

app = Flask(__name__)

app.config.from_object('config.Config')

app.register_blueprint(apod_api)


@app.errorhandler(ApiKeyError)
def handle_token_errors(error):
    app.logger.error(error.json)
    return jsonify(error.json)


if __name__ == '__main__':
    app.run()
