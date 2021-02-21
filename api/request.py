import requests


class Request:
    def __init__(self, url, payload=None, params=None):
        self.url = url
        self.payload = payload
        self.params = params

    def get(self):
        response = requests.get(self.url, params=self.params)
        return response

    def post(self):
        response = requests.post(self.url, data=self.payload)
        return response
