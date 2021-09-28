from app.db import db, BaseModelMixin


class order_product(db.Model,BaseModelMixin):
    order_id = db.Column(db.ForeignKey('order.id'), primary_key=True)
    product_id = db.Column(db.ForeignKey('product.id'), primary_key=True)
    type = db.Column(db.String, nullable=False) #output or input

    product_rsh = db.Relationship('order', back_populates='products') 
    order_rsh = db.Relationship('product', back_populates='order')




class order(db.model,BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    contact = db.Column(db.Integer, nullable=False)

    rsh_product = db.relationship('order_product', back_populates= 'order')

    def __repr__(self):
        return f'<Batch_code: {self.lot_code} {self.batch}>'




