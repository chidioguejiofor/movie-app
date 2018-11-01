from .database import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), default=db.func.current_timestamp())


    def check_password(self, password_value):
        return check_password_hash(self.password_hash, password_value)
    
    @property
    def password(self):
        raise AttributeError('the password is not accessible')


    def get_json_object(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'createdAt': str(self.created_at)
        }
    
    @password.setter
    def password(self, value):
       self.password_hash = generate_password_hash(value)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()
        