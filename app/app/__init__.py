from flask import Flask, jsonify

from app.error_handler import ObjectNotFound, AppErrorBaseClass
from .ext import ma, migrate, login_manager
from .db import db
import logging
from .error_handler import configure_logging
from flask_restful import Api
from .auth.resources import user_v1_bp
from .products.resources import product_v1_bp
from .inventory.resources import inventory_v1_bp



def create_app(settings_module):
    app = Flask(__name__)
    
    app.config.from_object(settings_module)

    login_manager.init_app(app)
    configure_logging(app)
    logger = logging.getLogger(__name__)
    logger.info('app, modules and logs created')

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    logger.info('db,ma and migration initialized')

    Api(app,catch_all_404s=True)
    #logger.info('404 erores catched')
    
    app.url_map.strict_slashes = False

    app.register_blueprint(user_v1_bp)
    logger.info('user blueprint registered')

    app.register_blueprint(product_v1_bp)
    logger.info('product blueprint registered')

    app.register_blueprint(inventory_v1_bp)
    logger.info('inventory blueprint registered')

    #register_error_handlers(app)
    
    return app


def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        print(e)
        return jsonify({'msg': 'Internal server error'}), 500
    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405
    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403
    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': 'Not Found error'}), 404
    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500
    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': str(e)}), 404


