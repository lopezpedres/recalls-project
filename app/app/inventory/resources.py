from .schemas import BatchSchema, InventorySchema
from .models import inventory, batch, table_batch_inventory
#from app.decorators import check_token
from flask import Blueprint, request
from flask_restful import Api, Resource
from app.products.models import products
from app.error_handler import ObjectNotFound

inventory_v1_bp=Blueprint('inventory_v1_bp',__name__)
batch_schema= BatchSchema()
inventory_schema = InventorySchema()

api = Api(inventory_v1_bp)


class BatchCode(Resource):
    def put(self):
        data=request.get_json()
        request_dict= batch_schema.load(data)
        if batch.get_by_lote_and_batch(lote_code = request_dict['lote_code'], batch_code =request_dict['batch_code']):
            raise 'There is a batch with that lotcode and batch_code'
        _batch = batch(
            lote_code = request_dict['lote_code'],
            batch_code = request_dict['batch_code'])
        _batch.save()
        resp = batch_schema.dump(_batch)
        return resp, 201
    def get(self, lote_code, batch_code):
        _batch = batch.get_by_lote_and_batch(lote_code=lote_code,batch_code=batch_code)
        resp=inventory_schema.dump(_batch.inventory)
        return batch_schema.dump(resp, many=True)




class InventoryNew(Resource):
    def put(self):
        data = request.get_json()
        request_dict=inventory_schema.load(data)
        product= products.get_by_name(product_name = request_dict['product_name'])

        Inventory= inventory(
            product_id = product.id, 
            quantity = request_dict['quantity'],
            ext_code = request_dict.get('ext_code') )
        Inventory.save()

        Batch_inventory= table_batch_inventory( type = request_dict['batch_type'] )
        Batch = batch.get_by_lote_and_batch(lote_code = request_dict['batch_lote'], batch_code =request_dict['batch_code'])
        Batch_inventory.rsh_batch = Batch
        Batch_inventory.rsh_inventory = Inventory
        Inventory.rsh_batch.append(Batch_inventory)
        Inventory.save()

        resp = inventory_schema.dump(Inventory)
        return resp, 201

class InventoryAll(Resource):
    def get(self):
        _inventory= inventory.get_all()
        if len(_inventory) == 0:
            raise ObjectNotFound('There are no Users')
        resp = InventorySchema.dump(_inventory, many=True)
        return resp, 200



api.add_resource(BatchCode, '/api/v1/batches', endpoint = 'new-batch')
api.add_resource(InventoryNew, '/api/v1/inventory', endpoint = 'new-inventory')
api.add_resource(InventoryAll, '/api/v1/inventory', endpoint = 'all-inventory')
api.add_resource(BatchCode, '/api/v1/batches/<int:lote_code>,<int:batch_code>', endpoint = 'batch-in-inventory')



