from marshmallow import fields
from app.ext import ma
#from inventory.schemas import InventorySchema

class Order_Schema(ma.Schema):
    id = fields.Integer(dump_only=True)
    contact = fields.String()
    created =fields.Date()

    rsh_product = fields.Nested('InventorySchema', many=True)
