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


@fixture(scope='session')
def expected_cme_success_response():
    return {
        'info': [
            {
                'enlilList': [
                    {
                        'au': 2.0,
                        'cmeIDs': ['2021-03-01T15:36:00-CME-001'],
                        'estimatedDuration': None,
                        'estimatedShockArrivalTime': None,
                        'impactList': None,
                        'isEarthGB': False,
                        'kp_135': None,
                        'kp_18': None,
                        'kp_180': None,
                        'kp_90': None,
                        'link': 'https://kauai.ccmc.gsfc.nasa.gov/DONKI/view/W'
                                'SA-ENLIL/16561/-1',
                        'modelCompletionTime': '2021-03-02T15:45Z',
                        'rmin_re': None
                    }
                ],
                'halfAngle': 24.0,
                'isMostAccurate': True,
                'latitude': -3.0,
                'levelOfData': 0,
                'link': 'https://kauai.ccmc.gsfc.nasa.gov/DONKI/view/CMEAnalys'
                        'is/16557/-1',
                'longitude': 68.0,
                'note': 'Preliminary analysis based on data available during r'
                        'eal-time.',
                'speed': 350.0,
                'time21_5': '2021-03-02T00:55Z',
                'type': 'S'
            }
        ],
        'note': 'Associated with rising material and field lines due to erupti'
                'on from vicinity of AR 2805 visible in SDO/AIA 171/193/304 be'
                'ginning 2021-03-01T12:45Z.',
        'startDate': '2021-03-01T15:36Z'
    }
