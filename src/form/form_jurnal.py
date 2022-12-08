from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.widgets import TextInput, TextArea

class JurnalForm(FlaskForm):
    name = StringField("Name", widget=TextInput())
    description = StringField("Description", widget=TextArea())