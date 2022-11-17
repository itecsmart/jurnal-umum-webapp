from flask import Blueprint, redirect, render_template
from models import *

transaction_bp = Blueprint('transaction_bp',__name__)

@transaction_bp.route('/jurnal/<int:id>/transaction')
def transaction(id):
    transactions = Transaction.query.filter_by()
    return render_template('transaction.html', id=id)