from flask import Blueprint, redirect, request, render_template
from models.user import User
from form.form_auth import LoginForm
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from extensions import login_manager


auth_blueprint = Blueprint("auth_blueprint", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        form = LoginForm()
        print(form.username.data)
        print(form.password.data)
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect('/jurnal')
        return redirect('/login')
    form = LoginForm()
    return render_template('login.html',title='Jurnal Umum | Login', form=form)



@auth_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect('/login')