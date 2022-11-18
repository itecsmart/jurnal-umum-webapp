from flask import Blueprint, redirect, render_template, url_for
from models import *

transaction_bp = Blueprint('transaction_bp',__name__)

@transaction_bp.route('/jurnal/<int:id>/transaction')
def transaction(id):
    transactions = Transaction.query.filter(Transaction.jurnal_id==id).all()
    jurnal = Jurnal.query.filter_by(id=id).first()
    list_transaction = []
    kas = 0
    for t in transactions:
        kas = kas + (t.debt-t.kredit)
        data = {
            'id': t.id,
            'date': t.date,
            'description': t.description,
            'debt': t.debt,
            'kredit': t.kredit,
            'kas':kas
        }
        list_transaction.append(data)
    return render_template('transaction.html', id=id, list_transaction=list_transaction, jurnal=jurnal, kas=kas)



@transaction_bp.route('/jurnal/<int:id>/transaction/<int:t_id>/delete')
def transaction_delete(id, t_id):
    transaction=Transaction.query.filter_by(id=t_id).first()
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for('transaction_bp.transaction', id=id))