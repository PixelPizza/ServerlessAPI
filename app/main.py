from fastapi import FastAPI
from mangum import Mangum

from app.api.root import router as root_router
from app.api.api_v1.api import router as api_router

app = FastAPI()

app.include_router(root_router)
app.include_router(api_router, prefix="/api/v1")

api_handler = Mangum(api_router)
