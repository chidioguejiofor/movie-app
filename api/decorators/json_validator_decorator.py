from flask import request
from marshmallow.exceptions import ValidationError

def check_json_decorator(error_message):
    
    def wrapper(f):

        def inner_wrapper(*args, **kwargs):
            if request.data and request.get_json():
                return f(*args, **kwargs)
            else:

                return {
                    'errors': {
                        'message': error_message
                    }
                }, 400
                
        return inner_wrapper
    return wrapper
