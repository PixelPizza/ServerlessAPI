from fastapi import FastAPI

from .request_validation import add_exception_handler as add_rv_handler


def add_exception_handlers(app: FastAPI):
    add_rv_handler(app)
