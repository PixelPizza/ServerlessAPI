from dataclasses import dataclass


@dataclass
class UserEntity:
    user_id: int
    roles: int
    balance: int
    created_at: int
    delivery_message: str | None = None
