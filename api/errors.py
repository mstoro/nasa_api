from http import HTTPStatus


class BaseError(Exception):
    def __init__(self, message, status):
        super().__init__()
        self.message = message
        self.status = status

    @property
    def json(self):
        return {
            'status': self.status,
            'message': self.message,
        }


class AuthorizationError(BaseError):
    def __init__(self):
        super().__init__('Invalid api key', HTTPStatus.BAD_REQUEST)


class RequestError(BaseError):
    def __init__(self, message):
        super().__init__(message, status=HTTPStatus.BAD_REQUEST)
