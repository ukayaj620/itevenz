from flask import flash, url_for, redirect
from flask_login import login_user
from ..models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class AuthController:

  def login(self, email, password, remember):
    user = User.query.filter_by(email=email).first()

    if not user or not (password == 'password'):
      flash('Please check your login details and try again.')
      return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('home.index'))

