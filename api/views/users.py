from api import api_blueprint


@api_blueprint.route('/login')
def login():
    return 'Logging Out!!!'