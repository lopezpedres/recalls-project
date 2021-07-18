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
	
	@staticmethod
	def get_customer_by_name(name):
		return Customers.query.filter_by(name=name).first()
	
	@staticmethod
	def get_all_customers():
		return Customers.session.get_all() 
