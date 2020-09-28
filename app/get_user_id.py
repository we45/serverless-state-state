from nanoid import generate
import json

user_id = generate(size=21)

def get_user_data(event, context):
    body_dict = {"user_id": user_id}
    return {
        "statusCode": 200,
        "body": json.dumps(body_dict)
    }