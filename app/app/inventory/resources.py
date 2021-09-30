from .schemas import BatchSchema, InventorySchema
from .models import inventory, batch
from app.decorators import check_token
from flask import Blueprint, request
from flask_restful import Api, Resource

inventory_v1_bp=Blueprint('inventory_v1_bp',__name__)
batch_schema= BatchSchema
inventory_schema = InventorySchema

api = Api(inventory_v1_bp)


class BatchCodeNew(Resource):
    @check_token
    def post():
        data=request.get_json
        request_dict= batch_schema
