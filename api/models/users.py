from .database import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import UUID
import uuid
from ..helpers.auth_helpers import generate_token

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String, primary_key = True, default = str(uuid.uuid4()))
    username = db.Column(db.String(60), nullable = False, unique = True)
    password_hash = db.Column(db.String, nullable = False)
    email = db.Column(db.String(256), nullable = False, unique = True)
    created_at = db.Column(db.DateTime(), default = db.func.current_timestamp())


    def check_password(self, password_value):
        return check_password_hash(self.password_hash, password_value)
    
    @property
    def password(self):
        raise AttributeError('the password is not accessible')


    def get_json_object(self):
        json_obj = {
            'id': self.id, 
            'username': self.username, 
            'email': self.email, 
            'createdAt': str(self.created_at)
        }

        return {
            **json_obj,
            'token': generate_token(json_obj)
        }

    
    @password.setter
    def password(self, value):
        print('the golden password:')
        
        self.password_hash = generate_password_hash(value)
        print(self.password_hash)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def load_from_db(self, user_password):
        found_user = User.query.filter_by(username = self.username).first()
        if found_user and check_password_hash(self.password_hash, user_password):
            return found_user.get_json_object()

        return False



    def delete(self):
        db.session.remove(self)
        db.session.commit()
    
        