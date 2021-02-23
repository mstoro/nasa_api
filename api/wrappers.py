from functools import wraps

import jwt
from flask import request, current_app

from api.errors import TokenError, EXPIRED_TOKEN, INVALID_TOKEN, MISSING_TOKEN


def token_required(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        token = None

        if 'token' in request.headers:
            token = request.headers['token']

        if not token:
            raise TokenError(MISSING_TOKEN)

        try:
            jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256']
            )
        except jwt.ExpiredSignatureError:
            raise TokenError(EXPIRED_TOKEN)
        except jwt.InvalidTokenError:
            raise TokenError(INVALID_TOKEN)

        return function(*args, **kwargs)
    return decorated
