from flask import flash, url_for, redirect
from flask_login import login_user
from ..models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class AuthController:

  def login(self, email, password, remember):
    user = User.query.filter_by(email=email).first()

    print(type(user))

    if not user or not check_password_hash(user.password, password):
      flash('Please check your login details and try again.', 'danger')
      return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('participate.index'))


  def register(self, name, email, telephone, gender, password):
    user = User.query.filter_by(email=email).first()

    if user:
      flash('Email has already existed')
      return redirect(url_for('auth.signup'))
    
    new_user = User.create(
      User,
      name=name,
      email=email,
      telephone=telephone,
      gender=gender,
      password=generate_password_hash(password, method='sha256')
    )
    flash('User has been successfully registered, proceed to login', 'info')
    return redirect(url_for('auth.login'))

