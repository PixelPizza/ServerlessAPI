from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .error import PixelPizzaError


def add_exception_handler(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
        errors = {}
        for error in exc.errors():
            location = error["loc"][-1]
            message = error["msg"]
            errors[location] = message
        return JSONResponse(
            status_code=422,
            content=PixelPizzaError.INVALID_FORM_BODY.dict() | {
                "errors": errors
            }
        )
