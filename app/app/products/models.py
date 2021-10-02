from app.db import db, BaseModelMixin
import datetime


class products(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_unique = db.Column(db.String, nullable=False)
    product_name = db.Column(db.String,nullable=False)

    rsh_inventory = db.relationship('inventory', viewonly=True, lazy=True,  backref=db.backref('products'))
    rsh_orders = db.relationship('order_product',viewonly=True, lazy=True, backref=db.backref('products'))

    #rsh_products = db.relationship('products', lazy=True, backref=db.backref('type', lazy=True))


    def __repr__(self):
        return f'<Unique Product Identifier: {self.product_unique}>'

    @classmethod
    def get_by_name(cls,product_name): #TODO: FInish this method
        return cls.query.filter_by(product_name=product_name).first()


class order(db.Model,BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default= datetime.datetime.utcnow)

    rsh_product = db.relationship('order_product', backref=db.backref('order', lazy=True), lazy=True, cascade="all, delete")

    def __repr__(self):
        return f'<order_id: {self.id} {self.id}>'


class order_product(db.Model,BaseModelMixin):
    order_id = db.Column(db.ForeignKey('order.id'), primary_key=True)
    product_id = db.Column(db.ForeignKey('products.id'), primary_key=True)
    type = db.Column(db.String, nullable=False) #output or input

    rsh_product = db.relationship('order', backref=db.backref('products', lazy=True), lazy=True, cascade="all, delete") 
    rsh_order = db.relationship('products', backref=db.backref('order', lazy=True), lazy=True, cascade="all, delete")