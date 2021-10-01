from .schemas import BatchSchema, InventorySchema
from .models import inventory, batch, batch_inventory
#from app.decorators import check_token
from flask import Blueprint, request
from flask_restful import Api, Resource
from app.products.models import products
from app.error_handler import ObjectNotFound

inventory_v1_bp=Blueprint('inventory_v1_bp',__name__)
batch_schema= BatchSchema()
inventory_schema = InventorySchema()

api = Api(inventory_v1_bp)


class BatchCodeNew(Resource):
    def put(self):
        data=request.get_json()
        request_dict= batch_schema.load(data)
        if batch.get_by_lote_and_batch(lote_code = request_dict['lot_code'], batch_code =request_dict['batch_code']):
            raise 'There is a batch with that lotcode and batch_code'
        _batch = batch(
            lot_code = request_dict['lot_code'],
            batch_code = request_dict['batch_code'])
        _batch.save()
        resp = batch_schema.dump(_batch)
        return resp, 201


class InventoryNew(Resource):
    def put(self):
        data = request.get_json()
        request_dict=inventory_schema.load(data)
        product= products.get_by_name(product_name = request_dict['product_name'])


        _inventory= inventory(
            product_id = product.id, # or product.id 
            quantity = request_dict['quantity'],
            ext_code = request_dict.get('ext_code') )
        _inventory.save()
        #Once my inventory object is created, i need to link the batch of that object
        #To do that, i need to create the extra info of my intermidate table and then add it
        # to the batch object. Once that batch object has the extra info I can append it to the inventory object

        #TODO: How the fuck can I get the batch info ? // The solution i came with was to add more fields to my json body and then filter those 

        _batch_inventory= batch_inventory( type = request_dict['type'] )
        #_batch_inventory.save()
        _batch= batch.get_by_lote_and_batch(lote_code = request_dict['lot_code'], batch_code =request_dict['batch_code'])
        _batch_inventory.rsh_batch = _batch
        _inventory.append(_batch)
        _inventory.save()

        resp = inventory_schema.dump(_inventory)
        return resp, 201

class InventoryAll(Resource):
    def get(self):
        _inventory= inventory.get_all()
        if len(_inventory) == 0:
            raise ObjectNotFound('There are no Users')
        resp = InventorySchema.dump(_inventory, many=True)
        return resp, 200


api.add_resource(BatchCodeNew, '/api/v1/batches', endpoint = 'new-batch')
api.add_resource(InventoryNew, '/api/v1/inventory', endpoint = 'new-inventory')
api.add_resource(InventoryAll, '/api/v1/inventory', endpoint = 'all-inventory')




