from abc import abstractmethod

from .database import db
from uuid import uuid4

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String, primary_key = True, default = str(uuid4()))
    created_at = db.Column(db.DateTime(), default = db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(), default = db.func.current_timestamp(), onupdate = db.func.now())

    @abstractmethod
    def get_json_obj(self): pass

    def save():
        db.session.add(self)
        db.save()

    def delete():
        db.session.remove()
        db.save()
    
