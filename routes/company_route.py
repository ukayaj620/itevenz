from flask import Blueprint, render_template

company = Blueprint('company', __name__, template_folder='templates')

@company.route('/')
def home():
  return render_template('company/home.html')

@company.route('/about')
def about():
  return render_template('company/about.html')

