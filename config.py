import boto3
import json

boto_client = boto3.client('secretsmanager')
response = boto_client.get_secret_value(SecretId='API')
database_secrets = json.loads(response['SecretString'])

# Store secrets in AWS
API_KEY = database_secrets['API_KEY']
API_SECRET = database_secrets['API_SECRET']
WEBHOOK_PASSWORD = database_secrets['WEBHOOK_PASSWORD']
