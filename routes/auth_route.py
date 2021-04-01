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

  return AuthController.login(AuthController, email=email, password=password, remember=remember)


@auth.route('/signup')
def signup():
  return render_template('auth/register.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
  name = request.form.get('name')
  email = request.form.get('email')
  password = request.form.get('password')
  telephone = request.form.get('telephone')
  
  return AuthController.register(AuthController, name, email, telephone, password)