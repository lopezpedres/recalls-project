from marshmallow import fields
from app.ext import ma

class InventorySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    product_id = fields.Integer()
    quantity= fields.Integer()
    type = fields.String()
    status = fields.Boolean()
    ext_code = fields.String()

    rsh_batch = fields.Nested('BatchSchema', many=True)

class BatchSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    lot_code = id = fields.Integer()
    batch_code = id = fields.Integer()
    
    rsh_inventory = fields.Nested('BatchSchema', many=True)



