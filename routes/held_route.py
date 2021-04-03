from flask import Blueprint, url_for, render_template, request
from ..controllers.event_controller import EventController
from flask_login import login_required, current_user
from ..utils.images import save_image

held = Blueprint('held', __name__, template_folder='templates')

@held.route('/')
@login_required
def open_class():
  return render_template('held/index.html', events=EventController.fetch_all(EventController, user_id=current_user.id))

@held.route('/view/<int:id>')
@login_required
def view(id):
  return render_template('held/view.html', event=EventController.fetch_by_id(EventController, event_id=id))

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
    speaker = request.form.get('speaker')
    photo = request.files['photo']

    photo_filename = save_image(photo)

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
      poster_filename=photo_filename,
      speaker=speaker,
      user_id=current_user.id
    )

  return render_template('held/create.html')

@held.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
  if request.method == 'POST':
    id = request.form.get('id')
    title = request.form.get('title')
    description = request.form.get('description')
    due_date = request.form.get('due-date')
    category = request.form.get('category')
    start_date = request.form.get('start-date')
    start_time = request.form.get('start-time')
    end_date = request.form.get('end-date')
    end_time = request.form.get('end-time')
    speaker = request.form.get('speaker')
    photo = request.files['photo']

    photo_filename = save_image(photo) if photo else None

    return EventController.update(
      EventController,
      title=title,
      description=description,
      start_date=start_date,
      end_date=end_date,
      category=category,
      start_time=start_time,
      end_time=end_time,
      due_date=due_date,
      poster_filename=photo_filename,
      speaker=speaker,
      event_id=id
    )

  return render_template('/held/update.html', event=EventController.fetch_by_id(EventController, id))


@held.route('/delete/<int:id>')
@login_required
def delete(id):
  return EventController.delete(EventController, event_id=id)
