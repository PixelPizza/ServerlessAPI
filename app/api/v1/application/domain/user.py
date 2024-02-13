from datetime import datetime
from dataclasses import dataclass
from ..bitfield.roles import Role


@dataclass
class UserDomain:
    user_id: str
    roles: int = Role.CUSTOMER
    balance: int = 0
    created_at: int = int(round(datetime.now().timestamp() * 1000))
    delivery_message: str | None = None
