from marshmallow import Schema, fields, ValidationError
from datetime import date


def validate_str(string):
    if not string:
        raise ValidationError("The field can't be blank")


def validate_date(given_date):
    if given_date > date.today():
        raise ValidationError('Enter existing date')


class PayloadSchema(Schema):
    api_key = fields.String(validate=validate_str)
    date = fields.Date(required=True, validate=validate_date)
    hd = fields.Boolean(required=True)
    thumbs = fields.Boolean()
