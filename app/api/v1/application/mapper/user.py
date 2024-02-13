import time
from ..domain.user import UserDomain
from ...datasource.entity.user import UserEntity


def map_user_domain_to_user_entity(user_domain: UserDomain) -> UserEntity:
    return UserEntity(
        user_id=int(user_domain.user_id),
        roles=user_domain.roles,
        balance=user_domain.balance,
        delivery_message=user_domain.delivery_message,
        created_at=user_domain.created_at
    )


def map_user_entity_to_user_domain(user_entity: UserEntity) -> UserDomain:
    return UserDomain(
        user_id=str(user_entity.user_id),
        roles=user_entity.roles,
        balance=user_entity.balance,
        delivery_message=user_entity.delivery_message,
        created_at=user_entity.created_at
    )
