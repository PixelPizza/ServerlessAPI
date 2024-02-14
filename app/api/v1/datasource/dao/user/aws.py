from typing import Annotated

from fastapi import Depends

from .base import UserDAO
from ...ddb.user import UserDDBDAO
from ...entity.user import UserEntity


class AWSUserDAO(UserDAO):
    def __init__(self, user_ddb_dao: Annotated[UserDDBDAO, Depends()]):
        self.user_ddb_dao = user_ddb_dao

    def has_user(self, user_id: int) -> bool:
        return self.user_ddb_dao.has_user(user_id)

    def create_user(self, user: UserEntity) -> None:
        self.user_ddb_dao.create_user(user)

    def get_user(self, user_id: int) -> UserEntity:
        return self.user_ddb_dao.get_user(user_id)
