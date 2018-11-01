from dotenv import load_dotenv
import os
load_dotenv()

DEBUG=os.getenv('DEBUG')
SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
SECRET_KEY=os.getenv('SECRET_KEY')
FLASK_ENV=os.getenv('FLASK_ENV')
SQLALCHEMY_TRACK_MODIFICATIONS=False
