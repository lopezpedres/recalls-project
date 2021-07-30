#creating clients/route.py
from .forms import customerForm, productForm, orderForm,
from .models import Customers, Product, Order
from werkzeug.urls import url_parse
from flask import render_template, redirect, url_for, request
from . import sales_bp

@sales_bp.route('/sales/new_customer/', methods= ['GET', 'POST'])
def go_new_customer():
    form= customerForm()
    error=None
    if form.validate_on_submit():
	    if Customers.get_customer_by_name(form.name.data) is not None: 
		    error='There is already a client with that name'
		    return error

	    else:
		    client=Customers( name=form.name.data,
							email=form.email.data,
							phone=form.phone.data,
							address=form.address.data )

		    client.save()
		    next_page = request.args.get('next',None)
		    if not next_page or url_parse(next_page).netlog!='':
			    return redirect(url_for('sales.go_customers'))
    return render_template("sales/new_customer.html", form=form, error=error)

@sales_bp.route('/sales/customers/', methods= ['GET', 'POST'])
def go_customers():
	return render_template("sales/customers.html")

@sales_bp.route('/sales/new_product', methods=['GET','POST'])
def go_new_product():
	form = productForm()
	error=None
	if form.validate_on_submit():
	    if Product.get__by_name(form.name.data) is not None: 
		    error='There is already a client with that name'
		    return error

	    else:
		    product=Product( name=form.name.data,
							key_string=form.key_string.data,
							price=form.price.data
							)

		    product.save()
		    next_page = request.args.get('next',None)
		    if not next_page or url_parse(next_page).netlog!='':
			    return redirect(url_for('sales.go_products'))
	return render_template("sales/new_product.html", form=form, error=error)


@sales_bp.route('/sales/customers/', methods= ['GET', 'POST'])
def go_products():
	produts = Product.get_all()
	return render_template("sales/products.html", produts=produts)

@sales_bp.route('/sales/new_order/', methods= ['GET', 'POST'])
def go_new_order():
	form = orderForm()
	customer = Customers.get_all()
	if form.validate_on_submit():
		if customer is not None:
			customer = Customers.get_by_name(form.customer.data)
			if customer is not None:
				pay_method = form.pay_method.data
				shipping_date = form.shipping_date.data

				order = Order(customer_id=customer.id,
				pay_method=pay_method,
				shipping_date=shipping_date)

				order.save()
				next_page = request.args.get('next',None)
		    	if not next_page or url_parse(next_page).netlog!='':
			    return redirect(url_for('sales.go_orders')) #TODO create orders route
			else:
				error = 'There is no customer with that name.'
				return error
		else: 
			error = 'There are no customers'
			return error

@sales_bp.route('/sales/orders/')
def go_orders():
	orders=Order.get_all()
	return render_template("sales/orders.html", orders=orders)

@sales_bp.route('/sales/order_details/', methods=['GET', 'POST'])
def go_order_details(order_id):
	order = Order.get_by_id()


@sales_bp.route('/sales/product_list') # TODO añadir numero de orden en el path de
def go_product_order():
	products= Product.get_all() #TODO TERMINAR LA SELECCION DEL PRODUCTO Y AÑADIRLO A LA BASE DE DATOS 
