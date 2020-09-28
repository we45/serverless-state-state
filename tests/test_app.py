import pytest
from app.get_user_id import get_user_data
from app.password_gen import gen_pass
import json


def test_get_user_data():
    response = get_user_data({}, None)
    print(response)


def test_gen_pass():
    response = gen_pass({"body": json.dumps({"password": "password"})}, None)
    print(response)