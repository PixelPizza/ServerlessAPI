from pydantic import BaseModel
from .utils import SNOWFLAKE_FIELD


class Registration(BaseModel):
    user_id: str = SNOWFLAKE_FIELD


class User(BaseModel):
    user_id: str = SNOWFLAKE_FIELD
    roles: int
    balance: int
    created_at: int
    delivery_message: str | None
