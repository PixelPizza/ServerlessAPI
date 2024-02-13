from fastapi import APIRouter
from mangum import Mangum

from ...app import PixelPizzaAPI
from ..model.user import Registration, User
from ..mapper.user import map_registration_to_user_domain, map_user_domain_to_user
from ...application.service.user import UserServiceDep

router = APIRouter(prefix="/users")


@router.post("/", status_code=201)
async def create_user(
    registration: Registration,
    user_service: UserServiceDep
) -> User:
    user_domain = map_registration_to_user_domain(registration)
    user_service.create_user(user_domain)
    user_response = user_service.get_user(registration.user_id)
    return map_user_domain_to_user(user_response)

app = PixelPizzaAPI()
app.include_router(router)
handler = Mangum(app)
