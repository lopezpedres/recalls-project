from marshmallow import fields
from app.ext import ma

class ProductSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    product_unique = fields.String()
    product_name =fields.String()

