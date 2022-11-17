from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.widgets import Input, TextInput, TextArea, PasswordInput
# from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", widget=TextInput())
    password = PasswordField("Password", widget=TextInput())