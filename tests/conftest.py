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
