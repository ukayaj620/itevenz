from flask_login import UserMixin
from ..app import db

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(255), unique=False, nullable=False)
  email = db.Column(db.String(255), unique=True, nullable=False)
  telephone = db.Column(db.String(255), unique=True, nullable=False)
  password = db.Column(db.String(255), unique=False, nullable=False)
  registeredDate = db.Column(db.DateTime, nullable=False)

  def __repr__(self):
    return '<User %r>' % self.name

  def create(name, email, telephone, password, registeredData):
    user = User(name, email, telephone, password, registeredData)
    db.session.add(user)
    db.session.commit()

  
