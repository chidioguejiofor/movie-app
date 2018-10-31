from flask import Flask
from api import api_blueprint, views


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    
    app.run()