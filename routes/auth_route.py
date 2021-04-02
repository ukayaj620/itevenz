from flask import Blueprint, render_template, request, redirect, url_for
from ..controllers.auth_controller import AuthController
from flask_login import logout_user, login_required

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    return AuthController.login(AuthController, email=email, password=password, remember=remember)
  elif request.method == 'GET':
    return render_template('auth/login.html')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    telephone = request.form.get('telephone')
    gender = request.form.get('gender')
    
    return AuthController.register(
      AuthController, 
      name=name, 
      email=email, 
      telephone=telephone, 
      password=password, 
      gender=gender
    )
  elif request.method == 'GET':
    return render_template('auth/register.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('company.home'))