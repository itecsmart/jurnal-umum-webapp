from flask import Blueprint, render_template, request
from flask_login import login_required
from models.jurnal import Jurnal

jurnal_bp = Blueprint('jurnal_bp', __name__)

@jurnal_bp.route('/jurnal')
@login_required
def jurnal():
    jurnals = Jurnal.query.all()
    return render_template('jurnal.html', jurnals=jurnals)