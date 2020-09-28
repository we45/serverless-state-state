import json
import bcrypt

uppu = bcrypt.gensalt()

def gen_pass(event, context):
    data = json.loads(event.get('body'))
    bpass = bcrypt.hashpw(password = str(data.get('password')).encode(), salt = uppu).decode()
    body_dict = {"password": bpass}
    return {
        "statusCode": 200,
        "body": json.dumps(body_dict)
    }