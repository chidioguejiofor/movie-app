from marshmallow import fields, Schema, post_load, validates, ValidationError
from ..utilities.validator import string_60_validator
from ..models.users import User




class AuthSchema(Schema):
    username = fields.String(
        required = True, 
        validators = (string_60_validator), 
        error_messages = {
            'required': 'the username is a required field'
        }
    )


    password = fields.String(
        required = True,  
        error_messages = {
            'required': 'the password is a required field'
        }
    )

    def load_object_into_schema(self, user, partial = False):
        """Helper function to load python objects into schema"""
        data, errors = self.load(user, partial = partial)
        if errors:
            return errors, False
           
        return data, True


class SignupSchema(AuthSchema):
    email = fields.Email(
        required = True, 
        # validators = ( string_60_validator), 
        # email = True, 
        error_messages = {
            'required': 'the email is a required field', 
            'email': 'the format you inserted is not a valid email'
        }, 
        
    )
    
    @validates('username')
    def username_does_not_exist_validator(self, username):
        user = User.query.filter_by(username = username).first()

        if user:
            raise ValidationError('The username is already in use', 400)
