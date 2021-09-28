from app.db import db, BaseModelMixin

class products(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_unique = db.Column(db.String, nullable=False)
    product_name= db.Column(db.String,nullable=False)

    inventory_rsh= db.Relationship('inventory', back_populates='products')
    orders_rsh = db.Relationship('order_product', back_populates='products')

    def __repr__(self):
        return f'<Unique Product Identifier: {self.product_unique}>'
