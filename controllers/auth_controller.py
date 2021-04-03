from flask import flash, url_for, redirect
from flask_login import login_user
from ..models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class AuthController:

  def login(self, request):
    user = User.query.filter_by(email=request['email']).first()

    print(type(user))

    if not user or not check_password_hash(user.password, request['password']):
      flash('Please check your login details and try again.', 'danger')
      return redirect(url_for('auth.login'))

    remember = True if request['remember'] else False
    login_user(user, remember=remember)
    return redirect(url_for('participate.index'))


  def register(self, request):
    user = User.query.filter_by(email=request['email']).first()

    if user:
      flash('Email has already existed', 'warning')
      return redirect(url_for('auth.signup'))
    
    User.create(
      User,
      name=request['name'],
      email=request['email'],
      telephone=request['telephone'],
      gender=request['gender'],
      password=generate_password_hash(request['password'], method='sha256')
    )
    
    flash('User has been successfully registered, proceed to login', 'info')
    return redirect(url_for('auth.login'))

