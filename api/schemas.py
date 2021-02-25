import os
from datetime import date

from marshmallow import Schema, fields, ValidationError


def validate_date(given_date):
    if given_date > date.today():
        raise ValidationError('Enter existing date')


class PayloadSchema(Schema):
    api_key = fields.String(missing=os.environ.get('API_KEY'))
    date = fields.Date(required=True, validate=validate_date)
    hd = fields.Boolean(required=True)
    thumbs = fields.Boolean(missing=True)
