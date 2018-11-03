from .users import User

from flask_restplus import Resource
import flask_excel as excel 
from api import api

@api.route('/users/export')
class ExportUserResource(Resource):

    def get(self):
        users = User.query.all()
        user_data = ({
            'username': user.username,
            'email': user.email,
            'createdAt': str(user.created_at),
            'updatedAt': str(user.updated_at)
        } for user in users)
        return excel.make_response_from_records(user_data, 'csv')