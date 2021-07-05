from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class LoginForm():
    name = StringField("Name", validators=[DataRequired(), Length(max=64)])
    email = PasswordField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    admin = BooleanField("Admin", validators=[]






