from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import secrets
import logging

logger= logging.getLogger(__name__)
db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
#This values are going to be moved to the config folder
    app.config['SECRET_KEY']= secrets.token_hex(16)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#creating db instance
    db.init_app(app)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    logger.info('Registering Auth Blueprint')

    return app


