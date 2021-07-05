from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    admin = db.Column(db.Boolean)

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password():
        pass

    def check_password():
        pass

    def get_by_email():
        pass

    def save():
        pass




