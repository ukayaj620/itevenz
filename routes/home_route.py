from flask import Blueprint, url_for, render_template
from flask_login import login_required, current_user

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/')
@login_required
def index():
  return render_template('home/index.html', name=current_user.name)
