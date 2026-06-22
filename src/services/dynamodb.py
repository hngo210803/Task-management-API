import boto3
dynamodb = boto3.resource(
    "dynamodb",
    region_name="eu-west-3"
)
tasks_table = dynamodb.Table("Tasks")