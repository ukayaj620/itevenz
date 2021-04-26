from flask import flash, url_for, redirect
from flask_login import login_user
from ..models.user import User
from ..models.verification import Verification
from werkzeug.security import generate_password_hash, check_password_hash
from ..utils.mailer import send_signup_verification
from ..utils.time import is_expire
import random
import string

class AuthController:

  def fetch_user_by_id(self, email):
    user = User.query.filter_by(email=email).first()
    return user

  def sent_verification_email(self, email, msg='', reset=False):
    fetched_user = self.fetch_user_by_id(self, email=email)

    token = ''.join(random.choice(string.ascii_letters) for i in range(20))
    link = f'http://127.0.0.1:5000/auth/verify/{fetched_user.id}/{token}'

    hashed_token = token=generate_password_hash(token, method='sha256')

    if reset == True:
      Verification.update(Verification, token=hashed_token,user_id=fetched_user.id)
    else:
      Verification.create(Verification, token=hashed_token, user_id=fetched_user.id)

    send_signup_verification(to=fetched_user.email, link=link)

    flash(f'{msg}. Verification link has been sent to your email, please check it out', 'info')
    return redirect(url_for('auth.email_verification', email=email))

  def login(self, request, remember):
    user = User.query.filter_by(email=request['email']).first()

    if bool(user.is_verified) == False:
      return self.sent_verification_email(self, email=request['email'], msg='Your email has not been verified')

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

    return self.sent_verification_email(self, email=request['email'])


  def verify(self, token, user_id):
    verification = Verification.query.filter_by(user_id=user_id).first()

    if (not token or\
      check_password_hash(verification.token, token)) and\
      is_expire(expire=verification.valid):
      flash('Link has expire, request for other link', 'warning')
      return redirect(url_for('auth.email_verification'))

    Verification.delete(Verification, token_id=verification.id)
    User.verified_user(User, user_id=user_id)
    
    flash('Your account has been verified, please login', 'info')
    return redirect(url_for('auth.login'))
    