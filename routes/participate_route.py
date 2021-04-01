from flask import Blueprint, url_for, render_template
from flask_login import login_required, current_user

participate = Blueprint('participate', __name__, template_folder='templates')

@participate.route('/')
@login_required
def index():
  return render_template('participate/index.html', name=current_user.name)
