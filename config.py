API_KEY = 'XyC4z59YK8gk9RqJVSgSHouFnXnZIdsPxgOwisWk2p2A1OzGkFEnQxqnPRTSmzm9'
API_SECRET = '4kpALMPoITLtRJymSwvpDtaPdXJAPPe8xWUsWPZB3VC2BK5sQIDdG4Y5DtCRu4kf'
WEBHOOK_PASSWORD = 'abc123'
"""
import os
from dotenv import load_dotenv

load_dotenv()
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
WEBHOOK_PASSWORD = os.getenv("WEBHOOK_PASSWORD")

#print(WEBHOOK_PASSWORD)

import boto3
import json
import os
boto_client = boto3.client('secretsmanager',
                            region_name='us-east-1',
                            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)
response = boto_client.get_secret_value(SecretId='API')
database_secrets = json.loads(response['SecretString'])
print(database_secrets)

# Store secrets in AWS
API_KEY = database_secrets['API_KEY']
API_SECRET = database_secrets['API_SECRET']
WEBHOOK_PASSWORD = database_secrets['WEBHOOK_PASSWORD']
"""