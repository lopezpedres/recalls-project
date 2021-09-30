from app.db import db, BaseModelMixin
import datetime

class order_product(db.Model,BaseModelMixin):
    order_id = db.Column(db.ForeignKey('order.id', ondelete='CASCADE'), primary_key=True)
    product_id = db.Column(db.ForeignKey('product.id', ondelete='CASCADE'), primary_key=True)
    type = db.Column(db.String, nullable=False) #output or input

    rsh_product = db.Relationship('order', back_populates='products', lazy=True, cascade="all, delete") 
    rsh_order = db.Relationship('product', back_populates='order', lazy=True, cascade="all, delete")




class order(db.model,BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default= datetime.datetime.utcnow)

    rsh_product = db.relationship('order_product', back_populates= 'order', lazy=True, cascade="all, delete")

    def __repr__(self):
        return f'<Batch_code: {self.lot_code} {self.batch}>'




