import base64
import unittest

from faker import Faker
from flask import current_app

from app import app
from db import delete_test_user

fake = Faker()


class AuthenticationTest(unittest.TestCase):
    def test_not_allowed_method(self):
        with app.app_context():
            client = current_app.test_client(self)
            response = client.get('/sign-up')

            self.assertEqual(response.status_code, 405)

    def test_correct_registration(self):
        with app.app_context():
            client = current_app.test_client(self)
            payload = {'name': fake.name(),
                       'password': fake.word()
                       }

            response = client.post('/sign-up', json=payload)
            json_data = response.get_json()

            self.assertEqual(response.status_code, 200)
            self.assertEqual(json_data, {'message': 'New user created!'})

            payload['name'] = 'test'
            payload['password'] = 'test'
            client.post('/sign-up', json=payload)

    def test_login(self):
        with app.app_context():
            client = current_app.test_client(self)
            credentials = base64.b64encode(b'test:test').decode('utf-8')

            response = client.post(
                '/login',
                headers={'Authorization': f'Basic {credentials}'}
            )
            json_data = response.get_json()

            self.assertEqual(response.status_code, 200)

            # test getting token
            self.assertTrue('token' in json_data)
            global token
            token = json_data.get('token')

    def test_request(self):
        with app.app_context():
            client = current_app.test_client(self)
            payload = {
                'date': '2021-02-20',
                'hd': True
            }

            # request without jwt token
            response = client.post('/apod', json=payload)
            json_data = response.get_json()

            self.assertEqual(json_data[0], {'message': 'Token is missing!'})

            # request with jwt token
            response = client.post(
                '/apod',
                json=payload,
                headers={'token': token}
            )
            json_data = response.get_json()
            delete_test_user()

            self.assertEqual(response.status_code, 200)
            self.assertTrue('status' in json_data)
            self.assertTrue('bytes' in json_data)


if __name__ == '__main__':
    unittest.main()
