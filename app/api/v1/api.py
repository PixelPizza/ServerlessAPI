from .app import PixelPizzaAPI
from .presentation.endpoints import users

app = PixelPizzaAPI()
app.include_router(users.router, tags=["Users"])
