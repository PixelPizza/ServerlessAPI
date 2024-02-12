from typing import Dict
from mypy_boto3_dynamodb.type_defs import TableAttributeValueTypeDef
from ..entity.user import UserEntity


def map_user_item_to_user_entity(item: Dict[str, TableAttributeValueTypeDef]) -> UserEntity:
    return UserEntity(
        user_id=item["UserId"],
        roles=item["Roles"],
        balance=item["Balance"],
        created_at=item["CreatedAt"],
        delivery_message=item["DeliveryMessage"]
    )
