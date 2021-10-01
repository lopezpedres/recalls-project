from app.decorators import check_token
from flask.json import jsonify
from app.error_handler import ObjectNotFound
from flask import request, Blueprint
from flask_restful import Api, Resource
import jwt
import os

from .schemas import ProductSchema
from .models import products
#Create a blueprint to connect to the app from another file that is not the app location
product_v1_bp=Blueprint('product_v1_bp',__name__)
#instance of the Schema
product_schema = ProductSchema()
#Instance of the api with the schema
api =Api(product_v1_bp)

class NewProduct(Resource):
    def put(self):
        data = request.get_json()
        request_dict = product_schema.load(data)
        product = products.get_by_name(product_name=request_dict['product_name'])

        if product:
            raise ObjectNotFound('There is a product with that name, try again')

        product = products(
            product_unique = request_dict['product_unique'],
            product_name = request_dict['product_name'])
        product.save()
        resp=product_schema.dump(product)
        return resp, 201



api.add_resource(NewProduct, '/api/v1/product', endpoint = 'new-product')