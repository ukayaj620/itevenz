from flask import Blueprint, render_template, request
from ..controllers.auth_controller import AuthController

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login')
def login():
  return render_template('auth/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
  email = request.form.get('email')
  password = request.form.get('password')
  remember = True if request.form.get('remember') else False

  return AuthController().login(email=email, password=password, remember=remember)