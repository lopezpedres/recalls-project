#creating database for clients
from app import db
import datetime

class Customers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, nullable=False)
	phone = db.Column(db.Integer, nullable=False)
	address = db.Column(db.String, nullable=False)
	date_creation = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	created_by = db.Column(db.String, nullable=False)

	def save(self):
		db.add(self)
		db.commit(self)
	
	@staticmethod
	def get_customer_by_name(name):
		return Customers.session.filter_by(name=name).first()
	
	@staticmethod
	def get_all_clients():
		return Customers.session.get_all() 