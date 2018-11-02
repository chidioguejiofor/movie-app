from marshmallow.exceptions import ValidationError


    

def string_60_validator(value):
    if len(value) > 60:
        raise ValidationError({
            'errors':{
                'message': 'The username must be less that 60'
            }
        }, 400)
