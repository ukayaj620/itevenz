from flask import Blueprint, url_for, render_template, request, abort
from ..controllers.event_controller import EventController
from flask_login import login_required, current_user
from ..utils.images import validate_image, generate_photoname
from werkzeug.utils import secure_filename
from ..config import Config
import os

held = Blueprint('held', __name__, template_folder='templates')

@held.route('/')
@login_required
def open_class():
  return render_template('held/index.html')


@held.route('/create', methods=['GET', 'POST'])
@login_required
def create():
  if request.method == 'POST':
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = request.form.get('due-date')
    category = request.form.get('category')
    start_date = request.form.get('start-date')
    start_time = request.form.get('start-time')
    end_date = request.form.get('end-date')
    end_time = request.form.get('end-time')
    photo = request.files['photo']

    filename = secure_filename(photo.filename)
    photo_filename = ''
    if filename != '':
      file_ext = os.path.splitext(filename)[1]
      photo_filename = generate_photoname(file_ext)
      if file_ext not in Config.UPLOAD_EXTENSIONS or \
          file_ext != validate_image(photo.stream):
        abort(400)
      photo.save(os.path.join(Config.UPLOAD_PATH, photo_filename))

    print(title, description, due_date, category, start_date, start_time, end_date, end_time, photo_filename)
    return EventController.create(
      EventController,
      title=title,
      description=description,
      start_date=start_date,
      end_date=end_date,
      category=category,
      start_time=start_time,
      end_time=end_time,
      due_date=due_date,
      poster_filename=photo_filename
    )

  return render_template('held/create.html')