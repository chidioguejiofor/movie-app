from .database import db
from uuid import uuid4
import datetime
from .base_model import BaseModel

class Movie(BaseModel):
    __tablename__ = 'movies'
    title = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    owner_id = db.Column(db.String, db.ForeignKey('users.id'))

    def get_json_obj(self):
        return {
            'id': self.id, 
            'title': self.title, 
            'description':self.description, 
            'url': self.url
        }
    
    



