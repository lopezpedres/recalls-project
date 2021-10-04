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
    
    #I need this inputs to get the objects for my Resource
    product_name = fields.String(load_only=True)
    batch_lote = fields.Integer(load_only=True)
    batch_code = fields.Integer(load_only=True)





class BatchSchema(ma.Schema):
    lote_code =fields.Integer()
    batch_code = fields.Integer()

    '''I wont be able to get the bext line because I dont have anything stored in the rsh_inventory relationship.
    The relationship works through the table_batch_inventory'''
    #rsh_inventory = fields.Nested('InventorySchema', many=True) 




