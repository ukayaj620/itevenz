from flask_login import UserMixin
from application.app import db
from datetime import datetime


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(255), unique=False, nullable=False)
  email = db.Column(db.String(255), unique=True, nullable=False)
  telephone = db.Column(db.String(255), unique=True, nullable=False)
  password = db.Column(db.String(255), unique=False, nullable=False)
  gender = db.Column(db.String(2), unique=False, nullable=False)
  is_verified = db.Column(db.Integer, unique=False, nullable=False)
  registered_date = db.Column(db.DateTime, nullable=False)
  events = db.relationship('Event', backref='user', lazy=True)
  verification = db.relationship('Verification', backref='user', lazy=True)
  participates = db.relationship('Participation', backref='user', lazy=True)

  def __repr__(self):
    return '<User %r>' % self.name

  def create(self, name, email, telephone, password, gender):
    user = User(
      name=name, 
      email=email, 
      telephone=telephone, 
      password=password,
      gender=gender,
      is_verified=0,
      registered_date=datetime.now()
    )
    db.session.add(user)
    db.session.commit()

  def verified_user(self, user_id):
    user = User.query.filter_by(id=user_id).first()
    user.is_verified = 1

    db.session.commit()
  
