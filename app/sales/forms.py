#creating the form for clients

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField, FloatField
from wtforms.validators import DataRequired, Email, Length

class customerForm(FlaskForm):
 
	name = StringField('name', validators=[DataRequired(), Length(max=64)])
	email = StringField('email', validators=[DataRequired(), Email()])
	phone = IntegerField('phone_number', validators=[DataRequired()])
	address = StringField('address', validators=[DataRequired(), Length(max=64)])
	submit = SubmitField('Create')

class orderForm(FlaskForm):
	customer = StringField('Customer', validators=[DataRequired(), Length()])
	pay_method =StringField('Pay Method', validators=[DataRequired(), Length(max=64)])
	shipping_date = DateField('Shipping Date',validators=[DataRequired()])
	submit = SubmitField('Create')

	
class productForm(FlaskForm):
	name = StringField('Product Type', validators=[DataRequired(), Length(max=64)])
	key_string = StringField('key_string',validators=[DataRequired()]) 
	price = FloatField('price',validators=[DataRequired()])
	submit = SubmitField('Create')

class orderProductForm(FlaskForm):
	product = StringField('Product', validators=[DataRequired(), Length(max=64)])
	quantity = IntegerField('Quantity',validators=[DataRequired()]) 
	submit = SubmitField('Add Product')





	
	
	