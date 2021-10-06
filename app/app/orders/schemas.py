from marshmallow import fields
from app.ext import ma
#from inventory.schemas import InventorySchema

class Order_Schema(ma.Schema):
    id = fields.Integer(dump_only=True)
    order_unique=fields.String()
    contact = fields.String()
    created = fields.Date()
    products_dict = fields.Dict(fields.String(),load_only=True)

    #rsh_product = fields.Nested('ProductSchema', many=True)

class ProductSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    product_unique = fields.String()
    product_name =fields.String()

#class ProductFromOrder(ma.Schema):
 #   all_products

