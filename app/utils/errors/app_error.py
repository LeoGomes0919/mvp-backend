class AppError(Exception):
    def __init__(self, message: str, code=500) -> None:
        super().__init__(message)
        self.code = code


class ValidationError(AppError):
    def __init__(self, message: str, code=400) -> None:
        super().__init__(message, code)
