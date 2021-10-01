from marshmallow import fields
from sqlalchemy.orm import load_only
from app.ext import ma

class InventorySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    product_id = fields.Integer()
    quantity= fields.Integer()
    type = fields.String()
    status = fields.Boolean()
    ext_code = fields.String()
    
    product_name = fields.String(load_only=True)
    batch_lot = fields.Integer(load_only=True)
    batch_code = fields.Integer(load_only=True)
    batch_type = fields.String(load_only=True)

    rsh_batch = fields.Nested('BatchSchema', many=True)

class BatchSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    lot_code =fields.Integer()
    batch_code = fields.Integer()
    
    rsh_inventory = fields.Nested('BatchSchema', many=True)




