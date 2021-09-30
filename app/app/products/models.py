from app.db import db, BaseModelMixin

class products(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_unique = db.Column(db.String, nullable=False)
    product_name= db.Column(db.String,nullable=False)

    rsh_inventory = db.Relationship('inventory', back_populates='products', lazy=True, cascade="all, delete")
    rsh_orders = db.Relationship('order_product', back_populates='products', lazy=True, cascade="all, delete")

    #rsh_products = db.relationship('Products', lazy=True, backref=db.backref('type', lazy=True))


    def __repr__(self):
        return f'<Unique Product Identifier: {self.product_unique}>'
