from http import HTTPStatus


class ApiKeyError(Exception):
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


class AuthorizationError(ApiKeyError):
    def __init__(self):
        super().__init__('Invalid api key', HTTPStatus.BAD_REQUEST)


class RequestError(ApiKeyError):
    def __init__(self, message):
        super().__init__(message, status=HTTPStatus.BAD_REQUEST)


# class MissingApiKeyError(ApiKeyError):
#     def __i
