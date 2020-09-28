import secrets
import json

user_id = secrets.token_urlsafe(16)

def get_user_data(event, context):
    body_dict = {"user_id": user_id}
    return {
        "statusCode": 200,
        "body": json.dumps(body_dict)
    }