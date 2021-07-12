from flask import Blueprint

sales_bp=Blueprint('sales', __name__, template_folder='templates')

from . import routes