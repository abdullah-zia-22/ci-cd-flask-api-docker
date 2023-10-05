"""Modules required for utilities"""
from functools import wraps
from flask_jwt_extended import (get_jwt,
verify_jwt_in_request)
from jwt import ExpiredSignatureError
from flask_restful import abort
from config import jwt,blacklist

# This function is for setting role
def role(refresh,role_args):
    """role function for defining JWT roles"""
    def wrapper(fn):
        """wrapper function for role"""
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request(refresh=refresh)
            except ExpiredSignatureError:
                abort(http_status_code=403,message="Token has expired")
            claims = get_jwt()
            if claims["role"]==role_args:
                return fn(*args, **kwargs)
            return abort(http_status_code=403,message=role+" only Tokens!")
        return decorator
    return wrapper

def jwt_required(refresh):
    """jwt function for checking jwt in request"""
    def wrapper(fn):
        """wrapper function for jwt"""
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request(refresh=refresh)
                return fn(*args, **kwargs)
            except ExpiredSignatureError:
                return abort(http_status_code=403,message="Token has expired")
        return decorator
    return wrapper


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_payload):
    """jwt function for blacklisting the token"""
    jti = jwt_payload['jti']
    return jti in blacklist
