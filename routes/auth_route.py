from flask import Blueprint, render_template, request, redirect, url_for
from ..controllers.auth_controller import AuthController
from flask_login import logout_user, login_required

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    remember = True if request.form.get('remember') else False
    return AuthController.login(AuthController, request=request.form, remember=remember)
  elif request.method == 'GET':
    return render_template('auth/login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    
    return AuthController.register(AuthController, request=request.form)
  elif request.method == 'GET':
    return render_template('auth/register.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('company.home'))