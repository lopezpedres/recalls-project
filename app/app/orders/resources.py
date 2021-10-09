from .schemas import Order_Schema, ProductSchema, ProductFromOrder, OrderProduct
from .models import order, order_product, products
#from app.decorators import check_token
from flask import Blueprint, request
from flask_restful import Api, Resource
from app.error_handler import ObjectNotFound

orders_v1_bp=Blueprint('orders_v1_bp',__name__)
order_schema= Order_Schema()
product_schema = ProductSchema()
product_order= ProductFromOrder()
#_order_product= OrderProduct()

api = Api(orders_v1_bp)

class NewOrder(Resource):
    def put(self):
        data = request.get_json()
        r_d= order_schema.load(data)
        #Ideally this order_unique will autogenerate 
        _order = order.get_by_unique(r_d['order_unique'])
        if _order:
            raise 'There already an order with that unique id '

        _order = order(
            order_unique=r_d['order_unique'],
            contact = r_d['contact']
            )

        #adding the products to the order
        products_dict = r_d['products_dict']
        #we can create a function to have lines 32 to 35 somehwere else
        for prod_qty in products_dict:
            product= products.get_by_product_unique(prod_qty)
            o=order_product(rsh_order=_order,rsh_product=product, quantity=products_dict[prod_qty])
            o.save()
        _order.save()
        resp = order_schema.dump(_order)
        return resp, 201
        
    def get(self,order_unique):
        _order = order.get_by_unique(order_unique)
        _order_product = order_product.get_by_order_id(order_id=_order.id)
        order_dict={"Products":{}, "Order_Products":{}}
        for x in _order_product:
            order_dict['Products'][x.rsh_product.id]=x.rsh_product
            order_dict['Order_Products'][x.product_id]= x
            print(x.product_id)
        print(order_dict)
        resp = product_order.dump(order_dict)
        return resp, 200

class NewProduct(Resource):
    def put(self):
        data = request.get_json()
        request_dict = product_schema.load(data)
        product = products.get_by_product_unique(product_unique=request_dict['product_unique'])

        if product:
            raise ObjectNotFound('There is a product with that unique id, try again')

        product = products(
            product_unique = request_dict['product_unique'],
            product_name = request_dict['product_name'])
        product.save()
        resp=product_schema.dump(product)
        return resp, 201



api.add_resource(NewProduct, '/api/v1/product', endpoint = 'new-product')
api.add_resource(NewOrder,'/api/v1/orders', endpoint = 'new-orders')
api.add_resource(NewOrder,'/api/v1/orders/<string:order_unique>', endpoint = 'check-order')


        
        

        
