from marshmallow import Schema


class MovieSchema(Schema):

    title = db.Column(db.String)
    description = db.Column(db.String)
    url = db.Column(db.String)
    owner_id = db.Column(db.String, db.ForeignKey('users.id'))