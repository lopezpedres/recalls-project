from app.db import db, BaseModelMixin
import datetime


class order_product(db.Model,BaseModelMixin):
    order_id = db.Column(db.Integer,db.ForeignKey('order.id', ondelete='CASCADE'), primary_key=True)
    product_id = db.Column(db.Integer,db.ForeignKey('products.id', ondelete='CASCADE'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    rsh_product = db.relationship('products', backref=db.backref('order', lazy=True), lazy=True, cascade="all, delete") 
    rsh_order = db.relationship('order', backref=db.backref('products', lazy=True), lazy=True, cascade="all, delete")

    @classmethod
    def get_by_order_id(cls,order_id):
        return cls.query.filter_by(order_id=order_id).all()




class order(db.Model,BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    order_unique= db.Column(db.String, nullable=False)
    contact = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, default= datetime.datetime.utcnow)

    rsh_product = db.relationship('products', secondary = 'order_product' )

    def __repr__(self):
        return f'<order_id: {self.id} {self.id}>'
    
    @classmethod
    def get_by_unique(cls, order_unique):
        return cls.query.filter_by(order_unique=order_unique).first()


class products(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_unique = db.Column(db.String, nullable=False)
    product_name = db.Column(db.String,nullable=False)

    rsh_orders = db.relationship('order', secondary = 'order_product')



    def __repr__(self):
        return f'<Unique Product Identifier: {self.product_unique}>'

    @classmethod
    def get_by_product_unique(cls,product_unique): 
        return cls.query.filter_by(product_unique=product_unique).first()
