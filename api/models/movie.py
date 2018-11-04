from .database import db
from uuid import uuid4
import datetime
from .base_model import BaseModel
from .users import User

class Movie(BaseModel):
    __tablename__ = 'movies'
    title = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    owner_id = db.Column(db.String, db.ForeignKey('users.id'))


    @property 
    def owner(self):
        if self.owner_cache and self.owner_cache.id == self.owner_id:
            return self.owner_cache
        
        owner_obj = User.query.filter_by(id=self.owner_id).first()
        self.owner_cache = owner_obj

        if owner_obj:
            return owner_cache

        raise ValidationError('the owner_id was not found in the db' )


    def get_json_obj(self):

        owner = self.owner
        return {
            'id': self.id, 
            'title': self.title, 
            'description':self.description, 
            'url': self.url,
            'owner': {
                'id': owner.id,
                'username': owner.username,
                'email': owner.email
            }
        }
    
