from flask import Blueprint, render_template, request, redirect
from flask_login import login_required
from models.jurnal import Jurnal
from form.form_jurnal import JurnalForm
from extensions import *

jurnal_bp = Blueprint('jurnal_bp', __name__)

@jurnal_bp.route('/jurnal')
@login_required
def jurnal():
    jurnals = Jurnal.query.all()
    return render_template('jurnal.html', jurnals=jurnals)


@jurnal_bp.route('/jurnal/create', methods=['GET', 'POST'])
def create_jurnal():
    if request.method == 'POST':
        form = JurnalForm()
        jurnal = Jurnal(name=form.name.data, description=form.description.data)
        db.session.add(jurnal)
        db.session.commit()
        return redirect('/jurnal')
    form = JurnalForm()
    return render_template('jurnal_form.html', form=form)