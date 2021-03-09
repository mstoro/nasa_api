APOD_RESPONSE_OK = {
        'path': '/Users/mstoro/PycharmProjects/NASA_APIs/media/2021-03-01.jpg',
        'status': 'Success! Image saved.'
}

RESPONSE_APOD_WITHOUT_JWT = {
    'message': 'Invalid api key',
    'status': 400
}

RESPONSE_APOD_WITH_WRONG_PAYLOAD = {
    'message': {
        'date': [
            'Not a valid date.'
        ],
        'hd': [
            'Not a valid boolean.'
        ]
    },
    'status': 400
}
