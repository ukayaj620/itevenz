from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from application.config import Config
from flask_mail import Mail


db = SQLAlchemy()
mail = Mail()

def create_app():

  app = Flask(__name__)

  app.config.from_object(Config)

  db.init_app(app)
  migrate = Migrate(app, db)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.login_message_category = "danger"
  login_manager.init_app(app)

  mail.init_app(app)

  from application.models.user import User
  from application.models.verification import Verification

  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id))

  from application.models.event import Event
  from application.models.participation import Participation


  from application.routes.auth_route import auth
  app.register_blueprint(auth, url_prefix='/auth')

  from application.routes.participation_route import participation
  app.register_blueprint(participation, url_prefix='/participation')

  from application.routes.held_route import held
  app.register_blueprint(held, url_prefix='/held')

  from application.routes.company_route import company
  app.register_blueprint(company, url_prefix='/')

  return app

