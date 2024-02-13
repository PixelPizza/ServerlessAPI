import boto3
from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource

dynamodb: DynamoDBServiceResource = boto3.resource("dynamodb")
