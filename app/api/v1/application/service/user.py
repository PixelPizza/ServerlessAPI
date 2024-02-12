from ...datasource.dao.user import UserDAODep
from ..domain.user import UserDomain
from ..mapper.user import map_user_domain_to_user_entity, map_user_entity_to_user_domain


class UserService:
    def __init__(self, user_dao: UserDAODep):
        self.user_dao = user_dao

    def create_user(self, user: UserDomain) -> None:
        has_user: bool = self.user_dao.has_user(int(user.user_id))
        if has_user:
            return
        user_entity = map_user_domain_to_user_entity(user)
        self.user_dao.create_user(user_entity)

    def get_user(self, user_id: str) -> UserDomain:
        user_entity = self.user_dao.get_user(int(user_id))
        return map_user_entity_to_user_domain(user_entity)
