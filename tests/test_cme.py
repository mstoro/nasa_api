from http import HTTPStatus

from pytest import fixture

from tests.utils import headers


def routes():
    yield '/cme'


@fixture(scope='module', params=routes(), ids=lambda route: f'GET {route}')
def route(request):
    return request.param


def test_cme_get_without_jwt(
        route, client, invalid_jwt, invalid_jwt_expected_payload
):
    response = client.get(route, headers=headers(invalid_jwt))

    assert response.status_code == HTTPStatus.OK
    assert response.json == invalid_jwt_expected_payload


def test_correct_params(
        route, client, valid_jwt, expected_cme_success_response
):
    params = {
        'startDate': '2021-02-26',
        'endDate': '2021-03-01'
    }

    response = client.get(route, headers=headers(valid_jwt), json=params)

    assert response.status_code == HTTPStatus.OK
    assert response.json == expected_cme_success_response
