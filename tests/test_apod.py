from http import HTTPStatus

from pytest import fixture

from tests.utils import headers


def routes():
    yield '/apod'


@fixture(scope='module', params=routes(), ids=lambda route: f'POST {route}')
def route(request):
    return request.param


def test_post_without_jwt(
         route, client, invalid_jwt, invalid_jwt_expected_payload
):
    response = client.post(route, headers=headers(invalid_jwt))
    print(response.json)
    assert response.status_code == HTTPStatus.OK
    assert response.json == invalid_jwt_expected_payload


def test_correct_post(route, client, valid_jwt, expected_success_response):
    payload = {
        'date': '2021-03-01',
        'hd': True
    }

    response = client.post(route,
                           headers=headers(valid_jwt),
                           json=payload)

    assert response.status_code == HTTPStatus.OK
    assert response.json == expected_success_response


def test_with_invalid_date(
        route, client, valid_jwt, expected_response_with_invalid_date
):
    payload = {
        'date': '2121-03-01',
        'hd': False
    }

    response = client.post(route,
                           headers=headers(valid_jwt),
                           json=payload)

    assert response.status_code == HTTPStatus.OK
    assert response.json == expected_response_with_invalid_date
