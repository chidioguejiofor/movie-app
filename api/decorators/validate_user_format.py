from flask import request
from marshmallow.exceptions import ValidationError

def validate_user_decorator(f):
    def inner_wrapper(*args, **kwargs):
        if request.get_json():
            return f(*args, **kwargs)
        else:
            # return 'the user you specified is invalid'
            raise ValidationError({
                'errors': {
                    'message':  'the json object with username, password and email is required'
                }
            }, 400)
    return inner_wrapper
