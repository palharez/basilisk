import json
import os
from basilisk.__init__ import __directory__


def encode_password(name, hashed_password):
    return json.dumps({"name": name, "password": hashed_password})


def decode_password(content):
    data = json.loads(content)

    return data.get("name"), data.get("password")


def get_password_directory():
    return os.getcwd() + __directory__
