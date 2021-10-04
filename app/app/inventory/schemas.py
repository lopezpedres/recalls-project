from marshmallow import fields
from app.ext import ma

class InventorySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    product_id = fields.Integer()
    quantity= fields.Integer()
    type = fields.String()
    status = fields.Boolean()
    ext_code = fields.String()
    added = fields.Date()
    product_name = fields.String(load_only=True)
    print('1 ok')
    batch_lote = fields.Integer(load_only=True)
    print('2 ok')
    batch_code = fields.Integer(load_only=True)
    print('3 ok')
    batch_type = fields.String(load_only=True)
    print('4 ok')

    rsh_batch = fields.Nested('BatchSchema', many=True)



class BatchSchema(ma.Schema):
    #id = fields.Integer(dump_only=True)
    lote_code =fields.Integer()
    batch_code = fields.Integer()
    
    #rsh_inventory = fields.Nested('BatchSchema', many=True) 




