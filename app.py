from flask import Flask
from api import views, api_blueprint
from api.models.database import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(api_blueprint, url_prefix='/api/v1')


if __name__ == '__main__':
    app.run()