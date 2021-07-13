#creating clients/route.py
from .forms import customerForm
from .models import Customers
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