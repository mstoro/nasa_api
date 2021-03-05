from http import HTTPStatus
from unittest.mock import patch

from tests.mocks_for_tests import (
    APOD_RESPONSE_OK,
    RESPONSE_APOD_WITHOUT_JWT,
    RESPONSE_APOD_WITH_WRONG_PAYLOAD
)
from tests.test_class import BaseTest


class APODTest(BaseTest):
    dayimage_endpoint = '/apod'
    request_params = {"date": "2021-03-01", "hd": True}
    request_content_type = 'application/json'
    wrong_jwt = 'wrong_jwt'
    wrong_request_params = {'date': '2021', 'hd': 'Tru'}

    @patch('builtins.open')
    @patch('os.getcwd')
    @patch('requests.get')
    def test_dayimage_all_is_valid(self, mock_requests, mock_os_getcwd,
                                   expected_success_response):
        mock_os_getcwd.return_value = '/Users/mstoro/PycharmProjects/NASA_APIs'
        mock_requests.side_effect = [
            self.get_mock_requests(
                json=expected_success_response,
                status=HTTPStatus.OK
            ),
            self.get_mock_requests(content=b'returned image')
        ]

        response = self.client.post(
            path=self.dayimage_endpoint,
            headers=self.get_headers(
                self.jwt_token,
                content_type=self.request_content_type
            ),
            json=self.request_params
        )
        expected_result = APOD_RESPONSE_OK

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)

    def test_apod_without_jwt(self):
        response = self.client.post(
            path=self.dayimage_endpoint,
            headers=self.get_headers(
                content_type=self.request_content_type
            ),
            json=self.request_params,
        )
        expected_result = RESPONSE_APOD_WITHOUT_JWT

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)

    def test_dayimage_invalid_apod_data(self):
        response = self.client.post(
            path=self.dayimage_endpoint,
            headers=self.get_headers(
                self.jwt_token,
                content_type=self.request_content_type
            ),
            json=self.wrong_request_params
        )
        expected_result = RESPONSE_APOD_WITH_WRONG_PAYLOAD

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)
