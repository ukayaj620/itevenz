from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import Config


db = SQLAlchemy()

def create_app():

  app = Flask(__name__)

  app.config.from_object(Config)

  db.init_app(app)
  migrate = Migrate(app, db)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  from .models.user import User

  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id))

  from .models.event import Event


  from .routes.auth_route import auth
  app.register_blueprint(auth, url_prefix='/auth')

  from .routes.participate_route import participate
  app.register_blueprint(participate, url_prefix='/participate')

  from .routes.held_route import held
  app.register_blueprint(held, url_prefix='/held')

  from .routes.company_route import company
  app.register_blueprint(company, url_prefix='/')

  return app

