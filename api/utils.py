import os

import jwt
from flask import request, current_app

from api.errors import AuthorizationError, RequestError


def save_image(byte_array, path, name):
    with open(os.path.join(path, name), 'wb') as file:
        file.write(byte_array)


def get_media_path():
    return os.path.join(
        os.getcwd(),
        current_app.config['MEDIA_FOLDER'],
    )


def get_file_name(name, extension='.jpg'):
    return ''.join([name, extension])


def get_jwt():
    try:
        scheme, token = request.headers['Authorization'].split()
        assert scheme.lower() == 'bearer'
    except (KeyError, ValueError):
        raise AuthorizationError

    return jwt.decode(
        token,
        current_app.config['SECRET_KEY'],
        algorithms=['HS256']
    )['key']


def get_json(scheme):
    data = request.get_json()
    errors = scheme.validate(data)
    if errors:
        raise RequestError(errors)

    return data


def form_cme_data(data):
    if isinstance(data, list):
        res = []
        for element in data:
            res.append(
                {
                    'note': element['note'],
                    'startDate': element['startTime'],
                    'info': element['cmeAnalyses']
                }
            )

        return res

    return data


def get_params(scheme):
    data = dict(request.args)
    errors = scheme.validate(data)

    if errors:
        raise RequestError(errors)

    return data
