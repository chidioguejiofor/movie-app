from api import api
from flask import request, jsonify, Response, json
from api.decorators.validate_user_format import validate_user_decorator 
from ..models.users import User
from ..schemas.user import SignupSchema, AuthSchema
from flask_restplus import Resource
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError


@api.route('/signup')
class SignUpResource(Resource):
        
    @validate_user_decorator
    def post(self):

        request_data = request.get_json()
        schema = SignupSchema()
        user_data, success = schema.load_object_into_schema(request_data)

        if success:
            user = User(**user_data)
            # # try:
            user.save()
            return user.get_json_object()
        

        return user_data, 406
        
    


@api.route('/login')
class LoginResource(Resource):
        
    @validate_user_decorator
    def post(self):

        request_data = request.get_json()
        schema = AuthSchema()
        user_data, success = schema.load_object_into_schema(request_data)

        if success:
            user =  User(**user_data)
            found_user = user.load_from_db(request_data.get('password'))
            if found_user:
                return found_user, 200
            else:
                return jsonify({
                    'errors':{
                        'message': 'the password and username combination was not found'
                    }
                })
        
        return user_data, 406
        
    
   