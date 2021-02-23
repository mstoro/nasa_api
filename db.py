from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


def delete_test_user():
    test_user = User.query.filter_by(name='test').first()
    db.session.delete(test_user)
    db.session.commit()
