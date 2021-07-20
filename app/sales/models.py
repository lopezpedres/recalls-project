#creating database for clients
from sqlalchemy.orm import defaultload
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
	def get_customer_by_name(name):
		return Customers.query.filter_by(name=name).first()
	
	@staticmethod
	def get_all_customers():
		return Customers.query.all() 

	
class Orders(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	customer_id = db.Column(db.String, db.ForeignKey('Customers.id', ondelete='CASCADE'), nullable=False)
	pay_method = db.Column(db.String, nullable=False)
	order_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	shipping_date = db.Column(db.DateTime)
	order_details_id = db.relationship('Order_details',
	backref='orders',
	lazy=True,
	cascade='all, delete-orphan',
	order_by='asc(Order_details.created)')

	status = db.Column(db.Boolean, default=False)

	def save(self):
		db.session.add(self)
		db.session.commit()

	def edit(self):
		pass

	def delete(self):
		pass


	@staticmethod
	def get_orders():
		return Orders.query.all()
	

class Order_details(db.Model):
	"""Creates a table with the products within an order"""
	id = db.Column(db.Integer, primary_key = True )
	product = db.Column(db.String, db.ForeignKey('products.id'), ondelete='CASCADE', nullable=False ) #TODO create products table with their sizes example: 'Chocolate-Hazelnut 100 G'
	quantity= db.Column(db.Integer, nullable=False)
	price = db.Column(db.Float)
	created = db.Column(db.DateTime, default= datetime.datetime.utcnow)

	

	


	
