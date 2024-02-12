import os
from typing import Dict

from mypy_boto3_dynamodb.service_resource import Table
from mypy_boto3_dynamodb.type_defs import TableAttributeValueTypeDef

from .utils import dynamodb
from ..entity.user import UserEntity
from ..mapper.user import map_user_item_to_user_entity


class UserDDBDAO:
    __TABLE_NAME: str = os.getenv("USER_TABLE_NAME")
    dynamodb_table: Table

    def __init__(self):
        self.set_dynamodb_client(dynamodb.Table(self.__TABLE_NAME))

    def set_dynamodb_client(self, dynamodb_table: Table):
        self.dynamodb_table = dynamodb_table

    def has_user(self, user_id: int) -> bool:
        user = self.__get_raw_user(user_id)
        if user is None:
            return False
        return True

    def create_user(self, user: UserEntity) -> None:
        self.dynamodb_table.put_item(
            Item={
                "UserId": user.user_id,
                "Roles": user.roles,
                "Balance": user.balance,
                "DeliveryMessage": user.delivery_message,
                "CreatedAt": user.created_at
            }
        )

    def get_user(self, user_id: int) -> UserEntity | None:
        user = self.__get_raw_user(user_id)
        if user is None:
            return None
        return map_user_item_to_user_entity(user)

    def __get_raw_user(self, user_id: int) -> Dict[str, TableAttributeValueTypeDef] | None:
        response = self.dynamodb_table.get_item(
            Key={
                "UserId": user_id
            }
        )
        if "Item" not in response:
            return None
        return response["Item"]
