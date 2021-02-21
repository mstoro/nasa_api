import jwt
from flask import request, jsonify, current_app
from functools import wraps


from db import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'token' in request.headers:
            token = request.headers['token']

        if not token:
            return jsonify({'message': 'Token is missing!'})

        try:
            data = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256']
            )
            current_user = User.query.filter_by(id=data['id']).first()
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Your token expired! Please refresh it!'})
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'})

        return f(current_user, *args, **kwargs)
    return decorated
