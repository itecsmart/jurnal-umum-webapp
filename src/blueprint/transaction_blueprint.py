from flask import Blueprint, redirect, render_template, url_for, request
from models import *
from form import *
import datetime

transaction_bp = Blueprint('transaction_bp',__name__)

@transaction_bp.route('/jurnal/<int:id>/transaction')
def transaction(id):
    form = TransactionForm()
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
    return render_template('transaction.html', id=id, list_transaction=list_transaction, jurnal=jurnal, kas=kas, form=form)



@transaction_bp.route('/jurnal/<int:id>/transaction/<int:t_id>/delete')
def transaction_delete(id, t_id):
    transaction=Transaction.query.filter_by(id=t_id).first()
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for('transaction_bp.transaction', id=id))


@transaction_bp.route('/jurnal/<int:id>/transaction/create', methods=['POST'])
def transaction_create(id):
    if request.method=='POST':        
        form = TransactionForm()
        date= datetime.datetime.strptime(form.date.data, "%Y/%M/%d")
        transaction = Transaction(jurnal_id=id, date=date, description=form.description.data, kredit=form.kredit.data, debt=form.debt.data )
        db.session.add(transaction)
        db.session.commit()
        return redirect(url_for('transaction_bp.transaction', id=id))


@transaction_bp.route('/jurnal/<int:id>/transaction/<int:t_id>/edit', methods=['GET', 'POST'])
def edit(id, t_id):
    transaction = Transaction.query.filter_by(id=t_id).first()
    if request.method=='POST':
        form = TransactionForm()
        transaction.date = datetime.datetime.strptime(form.date.data, "%Y/%M/%d")
        transaction.description = form.description.data
        transaction.debt = form.debt.data
        transaction.kredit = form.kredit.data
        db.session.add(transaction)
        db.session.commit()
        return redirect(url_for('transaction_bp.transaction', id=id))
    form = TransactionForm(
        date = datetime.datetime.strftime(transaction.date, '%Y/%m/%d'),
        description= transaction.description,
        kredit= transaction.kredit,
        debt= transaction.debt
        )
    return render_template('edit_transaction.html', form=form, id=id, t_id=t_id)