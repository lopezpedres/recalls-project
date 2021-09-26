from marshmallow import fields
from app.ext import ma

class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    email =fields.String()
    password = fields.String(load_only=True)
    admin = fields.Boolean()

    
