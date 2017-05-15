import jwt
from app import config


def generate_jwt(user_id):
    token = jwt.encode({'user_id': str(user_id)}, config['DEFAULT']['SECRET_KEY'], algorithm='HS256')
    return bytes.decode(token)


def authenticate_jwt(token):
    payload = jwt.decode(str(token), config['DEFAULT']['SECRET_KEY'])
    return payload['user_id']
