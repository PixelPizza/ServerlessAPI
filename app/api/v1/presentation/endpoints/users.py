from typing import Annotated

from fastapi import APIRouter, Depends
from mangum import Mangum

from ...app import PixelPizzaAPI
from ..model.user import Registration, User
from ..mapper.user import map_registration_to_user_domain, map_user_domain_to_user
from ...application.service.user import UserService

router = APIRouter(prefix="/users")

type UserServiceDep = Annotated[UserService, Depends()]


@router.post("/", status_code=201)
async def create_user(
    registration: Registration,
    user_service: Annotated[UserService, Depends()]
) -> User:
    user_domain = map_registration_to_user_domain(registration)
    user_service.create_user(user_domain)
    user_response = user_service.get_user(registration.user_id)
    return map_user_domain_to_user(user_response)

app = PixelPizzaAPI()
app.include_router(router)
handler = Mangum(app)
