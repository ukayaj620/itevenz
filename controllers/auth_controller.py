from flask import flash, url_for, redirect
from flask_login import login_user
from ..models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class AuthController:

  def login(self, request, remember):
    user = User.query.filter_by(email=request['email']).first()

    if not user or not check_password_hash(user.password, request['password']):
      flash('Please check your login details and try again.', 'danger')
      return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('participation.index'))


  def register(self, request):
    user = User.query.filter_by(email=request['email']).first()

    if user:
      flash('Email has already existed', 'warning')
      return redirect(url_for('auth.signup'))

    user = User.query.filter_by(telephone=request['telephone']).first()
    if user:
      flash('Telephone has already existed', 'warning')
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

