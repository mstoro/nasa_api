from http import HTTPStatus
from unittest.mock import patch

from tests.mocks_for_tests import (
    RESPONSE_CME_OK,
    RESPONSE_APOD_WITHOUT_JWT,
    EXPECTED_RESPONSE_FROM_CME
)
from tests.test_class import BaseTest


class CMETest(BaseTest):
    cme_endpoint = '/cme'
    request_params = {'startDate': '2020-09-01', 'endDate': '2020-10-03'}
    wrong_jwt = 'wrong_jwt'

    @patch('requests.get')
    def test_cme_all_is_valid(self, mock_requests):
        mock_requests.side_effect = [self.get_mock_requests(
            json=EXPECTED_RESPONSE_FROM_CME,
            status=HTTPStatus.OK
        )]
        response = self.client.get(
            path=self.cme_endpoint,
            query_string=self.request_params,
            headers=self.get_headers(self.jwt_token)
        )
        expected_result = RESPONSE_CME_OK

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)

    def test_cme_without_jwt(self):
        response = self.client.get(
            path=self.cme_endpoint,
            headers=self.get_headers(),
            query_string=self.request_params,
        )
        expected_result = RESPONSE_APOD_WITHOUT_JWT

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)
