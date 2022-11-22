from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.widgets import TextInput

class JurnalForm(FlaskForm):
    name = StringField("Jurnal Name", widget=TextInput())
    description = StringField("Jurnal Description", widget=TextInput())