from pytest import fixture


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
def cme_expected_success_response():
    return {
        'info': [
            {
                'enlilList': None,
                'halfAngle': 20.0,
                'isMostAccurate': True,
                'latitude': -14.0,
                'levelOfData': 0,
                'link':
                    'https://kauai.ccmc.gsfc.nasa.gov/DONKI/view/'
                    'CMEAnalysis/16576/-1',
                'longitude': None,
                'note':
                    'The source location is unknown and only approximate based'
                    ' off of field line movement seen on the southwestern limb'
                    ' of SDO/AIA 171 beginning around 2021-03-03T20:40Z. Based'
                    ' off of measurements, longitude could range between 90'
                    ' and 125 degrees. Depending on feature tracked, velocity'
                    ' could range from 230km/s (black/white boundary) to '
                    '330km/s (bright leading edge).',
                'speed': 280.0,
                'time21_5': '2021-03-04T11:03Z',
                'type': 'S'
            }
        ],
        'note':
            'The CME is visible in C2 in the SW quadrant. It has a bright '
            'front that becomes more diffuse as it propagates to the edge of'
            ' the field of view. The source location is uncertain with '
            'potential longitudes ranging from 90 to 125 degrees based off of'
            ' visible field line movement seen in SDO/AIA 171 off of the SW '
            'limb beginning around 20:40Z.',
        'startDate': '2021-03-03T21:48Z'
    }
