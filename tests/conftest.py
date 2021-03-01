from datetime import datetime

from authlib.jose import jwt
from pytest import fixture

from app import app


@fixture(scope='session')
def secret_key():
    return datetime.utcnow().isoformat()


@fixture(scope='session')
def client(secret_key):
    app.secret_key = secret_key

    app.testing = True

    with app.test_client() as client:
        yield client


@fixture(scope='session')
def valid_jwt(client):
    header = {'alg': 'HS256'}

    payload = {'key': 'DEMO_KEY'}

    secret_key = client.application.secret_key

    return jwt.encode(header, payload, secret_key).decode('ascii')


@fixture(scope='session')
def invalid_jwt_expected_payload():
    return {
        'message': {
            '_schema': ['Invalid input type.']
        },
        'status': 400
    }


@fixture(scope='session')
def expected_success_response():
    return {
        'path': '/Users/mstoro/PycharmProjects/NASA_APIs/media/2021-03-01.jpg',
        'status': 'Success! Image saved.'
    }


@fixture(scope='session')
def expected_response_with_invalid_date():
    return {
        'message': {
            "date": ["Enter existing date"]
        },
        "status": 400
    }


@fixture(scope='session')
def invalid_jwt(client):
    header = {'alg': 'HS256'}

    payload = {'key': ''}

    secret_key = client.application.secret_key

    return jwt.encode(header, payload, secret_key, check=False).decode('ascii')
