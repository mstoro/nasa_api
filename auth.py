import datetime

import jwt
from flask import request, jsonify, Blueprint, current_app
from werkzeug.security import generate_password_hash, check_password_hash


from db import User
from db import db

auth = Blueprint('auth', __name__)


@auth.route('/sign-up', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(name=data['name'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})


@auth.route('/login', methods=['POST'])
def login():
    auth_data = request.authorization

    if not auth_data.username:
        return jsonify({'message': 'Name required!'})

    user = User.query.filter_by(name=auth_data.username).first()

    if not user:
        return jsonify({'message': 'User not found!'})

    if check_password_hash(user.password, auth_data.password):
        token = jwt.encode(
            {
                'id': user.id,
                'exp': datetime.datetime.utcnow() +
                datetime.timedelta(minutes=30)
            },
            current_app.config['SECRET_KEY'])

        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Incorrect password!'})
