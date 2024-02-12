from ..ddb.user import UserDDBDAO
from ..entity.user import UserEntity


class UserDAO:
    def __init__(self, user_ddb_dao: UserDDBDAO = UserDDBDAO()):
        self.user_ddb_dao = user_ddb_dao

    def has_user(self, user_id: int) -> bool:
        return self.user_ddb_dao.has_user(user_id)

    def create_user(self, user: UserEntity) -> None:
        self.user_ddb_dao.create_user(user)

    def get_user(self, user_id: int) -> UserEntity:
        return self.user_ddb_dao.get_user(user_id)
