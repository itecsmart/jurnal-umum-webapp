from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.widgets import TextInput, TextArea

class TransactionForm(FlaskForm):
    date = StringField("Date", widget=TextInput())
    description = StringField("Description", widget=TextArea())
    debt = StringField("Debt", widget=TextInput())
    kredit = StringField("Kredit", widget=TextInput())