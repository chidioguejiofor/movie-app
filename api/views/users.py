from api import api
from flask import request, jsonify, Response, json
from api.decorators.validate_user_format import validate_user_decorator 
from ..models.users import User
from ..schemas.user import UserSchema
from flask_restplus import Resource
from sqlalchemy.exc import IntegrityError

@api.route('/signup')
class UserResource(Resource):
        
    @validate_user_decorator
    def post(self):

        request_data = request.get_json()
        schema = UserSchema()
        user_data = schema.load_object_into_schema(request_data)
        user = User(**user_data)
        try:
            user.save()
            return user.get_json_object(), 201
        except IntegrityError:
            return {
                'errors':{
                    'message': 'username or email already exists'
                }
            }, 409
        