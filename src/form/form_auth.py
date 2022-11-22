from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.widgets import TextInput


class LoginForm(FlaskForm):
    username = StringField("Username", widget=TextInput())
    password = PasswordField("Password", widget=TextInput())