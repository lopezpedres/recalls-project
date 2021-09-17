#creating database for clients
from app import db
import datetime

class Customers(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False) 
	email = db.Column(db.String, nullable=False)
	phone = db.Column(db.Integer, nullable=False)
	address = db.Column(db.String, nullable=False)
	date_creation = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	created_by = db.Column(db.String, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

	def save(self):
		db.session.add(self)
		db.session.commit()

	def edit(self):
		pass

	def delete(self):
		pass
	
	@staticmethod
	def get_by_name(name):
		return Customers.query.filter_by(name=name).first()
	
	@staticmethod
	def get_all():
		return Customers.query.all() 


"""Link table for the many-to-many relation between Product table and Order table, note necesary because we need the quantity calomn in that table"""

'''rsh_product_order = db.Table('product_order',
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True))'''


'''class Order_products(db.Model):
	__tablename__ = "order_products"
	id = db.Column(db.Integer, primary_key=True)
	order_id = db.Column(db.Integer, db.Foreingkey('order.id', ondelete='CASCADE'),nullable=False)
	product_id = db.Column(db.Integer, db.Foreingkey('product.id', ondelete='CASCADE'),nullable=False)
	quantity = db.Column(db.Integer, nullable=False)

	order = db.relationship('order', backref = db.backref('order_products', cascade='all, delete-orphan')) 

	def save(self):
		db.session.add(self)
		db.session.commit()
	
class Order(db.Model):
	__tablename__ = "order"
	id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.String, db.ForeignKey('Customers.id', ondelete='CASCADE'), nullable=False)
	pay_method = db.Column(db.String, nullable=False)
	order_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	shipping_date = db.Column(db.DateTime)
	status = db.Column(db.Boolean, default=False)

	order_products = db.relationship('product',
						secondary= 'order_products'
						)


	def save(self):
		db.session.add(self)
		db.session.commit()

	def edit(self):
		pass

	def delete(self):
		pass


	@staticmethod
	def get_all():
		return Order.query.all()
	@staticmethod
	def get_by_id():
		return Order.query.get(id)
	

class Product(db.Model):
	"""Creates a table with the products within an order"""
	id = db.Column(db.Integer, primary_key = True )
	name = db.Column(db.String, nullable = False)
	key_string = db.Column(db.String, nullable = False)
	price = db.Column(db.Float)

	def save(self):
		db.session.add(self)
		db.session.commit()

	@staticmethod
	def get_by_name(name):
		return Product.query.filter_by(name=name).first()

	@staticmethod
	def get_all():
		return Product.query.all()'''




	

	


	
