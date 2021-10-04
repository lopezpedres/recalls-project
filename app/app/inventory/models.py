from app.db import db, BaseModelMixin
import datetime

'''class batch_inventory(db.Model,BaseModelMixin):
    inventory_id = db.Column(db.Integer,db.ForeignKey('inventory.id'), primary_key=True, nullable=False)
    batch_id = db.Column(db.Integer,db.ForeignKey('batch.id'), primary_key=True, nullable=False)
    type = db.Column(db.String, nullable=False) #output or input
    #test = db.Column(db.String)
    
    rsh_batch = db.relationship('batch', backref=db.backref('inventory', lazy=True), lazy=True, cascade="all, delete")
    rsh_inventory = db.relationship('inventory', backref= db.backref('batch', lazy=True), lazy=True, cascade="all, delete")'''

table_batch_inventory= db.Table( 'table_batch_inventory',
db.Column('inventory_id', db.Integer,db.ForeignKey('inventory.id'), primary_key=True),
db.Column('batch_id', db.Integer,db.ForeignKey('batch.id'), primary_key=True),
#db.Column('type', db.String, nullable=False)

)

class inventory(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity= db.Column(db.Integer,nullable=False)
    status = db.Column(db.Boolean, default=True) #False if empty
    ext_code = db.Column(db.String)
    added = db.Column(db.DateTime, default= datetime.datetime.utcnow)

    rsh_batch= db.relationship('batch', secondary='table_batch_inventory', backref=db.backref('inventory', lazy=True), lazy=True, cascade="all, delete")
    #rsh_products= db.relationship('products',backref= db.backref('inventory'), lazy=True, cascade="all, delete")


    def __repr__(self):
        return f'<item_id: {self.id}>'




class batch(db.Model,BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    lote_code = db.Column(db.Integer, nullable=False)
    batch_code = db.Column(db.Integer, nullable=False)

    rsh_inventory= db.relationship('inventory',secondary='table_batch_inventory', backref=db.backref('batch', lazy=True), lazy=True, cascade="all, delete")

    def __repr__(self):
        return f'<Batch_code: {self.lote_code} {self.batch_code}>'

    def get_by_lot():
        pass
    def get_by_batch():
        pass
    @classmethod
    def get_by_lote_and_batch(cls, lote_code, batch_code):
        #this might not work!
        print('you are the fucking boss')
        return cls.query.filter(cls.lote_code==lote_code, cls.batch_code ==batch_code).first()