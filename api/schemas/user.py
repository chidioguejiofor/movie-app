from marshmallow import fields, Schema
from ..utilities.validator import username_validator, string_60_validator
from marshmallow.exceptions import ValidationError

class UserSchema(Schema):
    username = fields.String(
        required = True, 
        validators = (username_validator, string_60_validator), 
        error_messages = {
            'required': 'the username is a required field'
        }
    )


    email = fields.String(
        required = True, 
        validators = ( string_60_validator), 
        error_messages = {
            'required': 'the email is a required field'
        }
    )

    password = fields.String(
        required = True,  
        error_messages = {
            'required': 'the password is a required field'
        }
    )

    def load_object_into_schema(self, data, partial = False):
        """Helper function to load python objects into schema"""
        data, errors = self.load(data, partial = partial)

        if errors:
            raise ValidationError(
                dict(errors = errors, message = 'An error occurred'), 400)

        return data
