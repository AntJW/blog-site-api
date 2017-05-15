from flask import request
from bson.json_util import loads
from utilities.token import authenticate_jwt


def get_authorized_headers():
    auth_jwt_result = authenticate_jwt(request.headers['Authorization'].replace('Bearer ', ''))
    acct_id = request.headers['Account']
    if acct_id != auth_jwt_result:
        raise Exception("Unable to Authenticate")

    headers_date = loads(request.headers['Datetime'])
    client_utc = headers_date['DatetimeUTC']
    client_utc_offset = headers_date['TimeOffset']

    return acct_id, client_utc, client_utc_offset
