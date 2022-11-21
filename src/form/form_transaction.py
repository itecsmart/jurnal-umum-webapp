from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.widgets import TextInput, TextArea

class TransactionForm(FlaskForm):
    date = StringField("Date",[validators.DataRequired()], widget=TextInput())
    description = StringField("Description", [validators.DataRequired()],  widget=TextArea())
    debt = StringField("Debt", widget=TextInput())
    kredit = StringField("Kredit", widget=TextInput())