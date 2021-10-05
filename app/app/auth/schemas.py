from marshmallow import fields
from app.ext import ma

class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    email =fields.String()
    password = fields.String(load_only=True) #load_only=False if we want to do a Login
    admin = fields.Boolean()

    
