from .base import UserDAO
from ...entity.user import UserEntity


class HardcodedUserDAO(UserDAO):
    def has_user(self, user_id: int) -> bool:
        return True

    def create_user(self, user: UserEntity) -> None:
        pass

    def get_user(self, user_id: int) -> UserEntity:
        return UserEntity(
            user_id,
            1,
            0,
            0
        )

