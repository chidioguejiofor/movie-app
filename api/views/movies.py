from api import api_blueprint

@api_blueprint.route('/movies')
def get_movie():
    return 'Here are all your movies'