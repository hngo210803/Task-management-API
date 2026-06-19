import boto3
dynamodb = boto3.resource("dynamodb")
tasks_table = dynamodb.Table("Tasks")