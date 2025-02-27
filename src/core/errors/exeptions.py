class BaseAPIException(Exception):
    def __init__(self, detail: str, status_code: int):
        self.detail = detail
        self.status_code = status_code


class NotFoundException(BaseAPIException):
    def __init__(self, detail: str = 'Resource not found'):
        super().__init__(detail, status_code=404)


class ValidationException(BaseAPIException):
    def __init__(self, detail: str = 'Validation Error'):
        super().__init__(detail, status_code=400)


class DatabaseException(BaseAPIException):
    def __init__(self, detail: str = 'Database Error'):
        super().__init__(detail, status_code=500)
