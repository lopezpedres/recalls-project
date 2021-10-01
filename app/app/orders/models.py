from sqlalchemy.orm import backref
from app.db import db, BaseModelMixin
import datetime

'''class order_product(db.Model,BaseModelMixin):
    order_id = db.Column(db.ForeignKey('order.id', ondelete='CASCADE'), primary_key=True)
    product_id = db.Column(db.ForeignKey('products.id', ondelete='CASCADE'), primary_key=True)
    type = db.Column(db.String, nullable=False) #output or input

    rsh_product = db.relationship('order', backref=db.backref('products', lazy=True), lazy=True, cascade="all, delete") 
    rsh_order = db.relationship('products', backref=db.backref('order', lazy=True), lazy=True, cascade="all, delete")'''




'''class order(db.Model,BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default= datetime.datetime.utcnow)

    rsh_product = db.relationship('order_product', backref=db.backref('order', lazy=True), lazy=True, cascade="all, delete")

    def __repr__(self):
        return f'<order_id: {self.id} {self.id}>'''