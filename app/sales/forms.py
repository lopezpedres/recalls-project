#creating the form for clients

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, Length

class customerForm(FlaskForm):
 
	name = StringField('name', validators=[DataRequired(), Length(max=64)])
	email = StringField('email', validators=[DataRequired(), Email()])
	phone = IntegerField('phone_number', validators=[DataRequired()])
	address = StringField('address', validators=[DataRequired(), Length(max=64)])
	submit = SubmitField('Create')

class orderForm(FlaskForm):
	customer = StringField('customer', validators=[DataRequired(), Length(max=64)])
	pay_method =StringField('Pay Method', validators=[DataRequired(), Length(max=64)])
	shipping_date= DateField('shipping_date',validators=[DataRequired])



	
	
	