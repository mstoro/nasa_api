from datetime import date

from marshmallow import Schema, fields, ValidationError, validates_schema


def validate_date(given_date):
    if given_date > date.today():
        raise ValidationError('Enter existing date')


class PayloadSchema(Schema):
    date = fields.Date(required=True, validate=validate_date)
    hd = fields.Boolean(required=True)
    thumbs = fields.Boolean(missing=True)


class CMEPayloadSchema(Schema):
    startDate = fields.Date(format='%Y-%m-%d',
                            required=True)
    endDate = fields.Date(format='%Y-%m-%d',
                          required=True)

    @validates_schema()
    def validate_cme_period(self, data, **kwargs):
        if not (data['startDate'] <= data['endDate']):
            raise ValidationError(
                'statDate must be earlier of equal to endDate'
            )
