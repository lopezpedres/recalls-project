from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from flask_migrate import Migrate
from flask_login import LoginManager
from .error_handler import configure_logging


login_manager = LoginManager()
db=SQLAlchemy()
migrate = Migrate()

def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)

#creating db instance
    login_manager.init_app(app)
    configure_logging(app)
    logger= logging.getLogger(__name__)
    db.init_app(app)
    migrate.init_app(app, db)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    logger.info('Registering Auth Blueprint')

    from .sales import sales_bp
    app.register_blueprint(sales_bp)
    logger.info('Registering Sales Blueprint')
    

    


    return app


