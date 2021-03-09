from unittest import TestCase
from unittest.mock import Mock

from authlib.jose import jwt

from app import app


class BaseTest(TestCase):
    jwt_token = None
    secret_key = 'dev'
    headers = {'alg': 'HS256'}
    payload = {'key': 'DEMO_KEY'}

    @classmethod
    def setUpClass(cls):
        cls.jwt_token = jwt.encode(cls.headers,
                                   cls.payload,
                                   cls.secret_key).decode('utf-8')

    def setUp(self):
        app.secret_key = self.secret_key
        self.client = app.test_client()
        self.jwt_token = self.jwt_token

    @staticmethod
    def get_mock_requests(json=None, status=None, content=None):
        mock_data = Mock()
        if json:
            mock_data.json.return_value = json
        if status:
            mock_data.status_code = status
        if content:
            mock_data.content = content

        return mock_data

    def get_headers(self, jwt_token='', content_type=None):
        headers = {'Authorization': f'bearer {jwt_token}'}
        if content_type:
            headers['Content-Type'] = content_type
        return headers
