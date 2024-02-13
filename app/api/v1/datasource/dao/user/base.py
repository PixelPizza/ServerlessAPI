from abc import ABC, abstractmethod
from ...entity.user import UserEntity


class UserDAO(ABC):
    @abstractmethod
    def has_user(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def create_user(self, user: UserEntity) -> None:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> UserEntity:
        pass
