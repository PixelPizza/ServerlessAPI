from fastapi import FastAPI

from app.root.root import router as root_router
from app.api.v1 import app as api_v1

app = FastAPI()

app.include_router(root_router)
app.mount("/v1/", api_v1)
