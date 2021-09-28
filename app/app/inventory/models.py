from app.db import db, BaseModelMixin

class batch_inventory(db.Model,BaseModelMixin):
    batch_id = db.Column(db.ForeignKey('batch.id'), primary_key=True)
    inventory_id = db.Column(db.ForeignKey('inventory.id'), primary_key=True)
    type = db.Column(db.String, nullable=False) #output or input
    
    batch = db.Relationship('batch', back_populates='inventory')
    inventory = db.Relationship('inventory', back_populates='batch')




class batch(db.model,BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    lot_code = db.Column(db.Integer, nullable=False)
    batch = db.Column(db.Integer, nullable=False)

    rsh_inventory= db.relationship('batch_inventory', back_populates='batch')

    def __repr__(self):
        return f'<Batch_code: {self.lot_code} {self.batch}>'



class inventory(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_id = db.Column(db.String, db.ForeignKey('products.id'))
    quantity= db.Column(db.Integer,nullable=False)
    type = db.Column(db.String, nullable=False) #ingredient or product
    status = db.Column(db.Boolean, default=True) #False if empty
    ext_code = db.Column(db.String, nullable=False) 

    rsh_batch= db.relationship('batch_inventory',back_populates='inventory')
    rsh_products= db.relationship('product',back_populates='inventory')


    def __repr__(self):
        return f'<item_id: {self.id}>'


