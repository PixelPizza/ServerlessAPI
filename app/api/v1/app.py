from fastapi import FastAPI
from .exception.mapper import add_exception_handlers


class PixelPizzaAPI(FastAPI):
    def __init__(self, *args, **kwargs):
        super(PixelPizzaAPI, self).__init__(*args, **kwargs)
        add_exception_handlers(self)
