from ..models.movie import Movie
from ..schemas.movie  import MovieSchema
from flask_restplus import Resource 
from api import api
from flask import request
from ..decorators.token_decorator import token_required
from ..decorators.json_validator_decorator import check_json_decorator

@api.route('/movies')
class MovieResource(Resource):

    @token_required
    @check_json_decorator('the title, description and url must be provided in request')

    def post(self, decoded={}):
        schema = MovieSchema()

        validation_obj, success = schema.load_object_into_schema(request.get_json())
    
        if success:
            validation_obj['owner_id'] = decoded['id']
            movie_model = Movie(**validation_obj)
            movie_model.save()
            
            return movie_model.get_json_obj(), 201
        
        return {
            'errors': validation_obj
        }, 400



