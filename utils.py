from flask_jwt_extended import (create_access_token,
create_refresh_token,
get_jwt_identity,get_jwt,
verify_jwt_in_request)
from functools import wraps
from jwt import ExpiredSignatureError
from flask_restful import abort
from config import jwt,blacklist

# This function is for setting role
def role(refresh,role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request(refresh=refresh)
            except ExpiredSignatureError:
                abort(http_status_code=403,message="Token has expired")
            claims = get_jwt()
            if claims["role"]==role:
                return fn(*args, **kwargs)
            else:
                abort(http_status_code=403,message=role+" only Tokens!")
        return decorator

    return wrapper

def jwt_required(refresh):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):     
            try:
                verify_jwt_in_request(refresh=refresh)
                return fn(*args, **kwargs)
            except ExpiredSignatureError:
                abort(http_status_code=403,message="Token has expired")
        return decorator
    return wrapper


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklist