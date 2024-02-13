from enum import Enum


class PixelPizzaError(Enum):
    INVALID_FORM_BODY = (10001, "Invalid Form Body")

    def __new__(cls, code: int, message: str):
        obj = object.__new__(cls)
        obj._value_ = code
        obj.code = code
        obj.message = message
        return obj

    def dict(self):
        return {"code": self.code, "message": self.message}
