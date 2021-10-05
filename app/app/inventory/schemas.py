from marshmallow import fields
from app.ext import ma

class InventorySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    product_id = fields.Integer()
    quantity= fields.Integer()
    type = fields.String()
    status = fields.Boolean()
    ext_code = fields.String()
    
    product_unique = fields.String(load_only=True)
    batch_lote = fields.Integer(load_only=True)
    batch_code = fields.Integer(load_only=True)
    batch_type = fields.String(load_only=True)

    #batch = fields.Nested('BatchSchema') #IF I ADD many=True wont work with my 127.0.0.1:5000/api/v1/batches/1,1 API



class BatchSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    lote_code =fields.Integer()
    batch_code = fields.Integer()
    type = fields.String()
    
    #rsh_inventory = fields.Nested('InventorySchema', many=True) 




