from ..model.user import Registration, User
from ...application.domain.user import UserDomain


def map_registration_to_user_domain(registration: Registration) -> UserDomain:
    return UserDomain(user_id=registration.user_id)


def map_user_domain_to_user(user_domain: UserDomain) -> User:
    return User(
        user_id=user_domain.user_id,
        roles=user_domain.roles,
        balance=user_domain.balance,
        created_at=user_domain.created_at,
        delivery_message=user_domain.delivery_message
    )
