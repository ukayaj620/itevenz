from flask import Blueprint, url_for, render_template
from flask_login import login_required, current_user

held = Blueprint('home', __name__, template_folder='templates')

@held.route('/')
@login_required
def open_class():
  return render_template('held/index.html')


@held.route('/create')
@login_required
def create():
  return render_template('held/create.html')