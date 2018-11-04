from flask import request
from ..helpers.auth_helpers import decode_token

def token_required(decorated_function):
    
    def wrapper(*args, **kwargs):
        user_token = request.headers.get('Authorization')
        if user_token:
            decoded_data = decode_token(user_token.split(' ')[1], **kwargs)
            return decorated_function(*args, decoded = decoded_data)
        

        return {
            'errors':{
                'message': 'Authorization token is required in the header'
            }
        }, 401
    return wrapper
