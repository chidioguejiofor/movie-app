from marshmallow.exceptions import ValidationError
from ..models.users import User


def username_validator(username):
    user = User.query.filter_by(username=username).first()

    if user:
        raise ValidationError({
            'errors':{
                'message': 'The username is already in use'
            }
        }, 400)

    

def string_60_validator(value):
    if len(value) > 60:
        raise ValidationError({
            'errors':{
                'message': 'The username must be less that 60'
            }
        }, 400)
