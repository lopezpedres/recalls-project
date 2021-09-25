from app.db import db, BaseModelMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, BaseModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, default=False)
    session_token= db.Column(db.String, nullable=True)

    '''def __init__(self,id,name,email,password,admin,session_token):
        self.id=id,
        self.name=name,
        self.email=email,
        self.password=password,
        self.admin=admin,
        self.session_token=session_token'''


    def __repr__(self):
        return f'<User: {self.email}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)
        

    def check_password(self, password):
       return check_password_hash(self.password, password)

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()
