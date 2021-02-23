MISSING_TOKEN = 'Token is missing!'
EXPIRED_TOKEN = 'Your token expired! Please refresh it!'
INVALID_TOKEN = 'Token is invalid!'


class TokenError(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    @property
    def json(self):
        return {'message': self.message}
