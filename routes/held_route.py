from flask import Blueprint, url_for, render_template, request
from ..controllers.event_controller import EventController
from flask_login import login_required, current_user
from ..utils.images import save_image

held = Blueprint('held', __name__, template_folder='templates')

@held.route('/')
@login_required
def open_class():
  return render_template(
    'held/index.html', 
    events=EventController.fetch_user_assoc_event(EventController, user_id=current_user.id)
  )

@held.route('/view/<int:id>')
@login_required
def view(id):
  return render_template('held/view.html', event=EventController.fetch_by_id(EventController, event_id=id))

@held.route('/create', methods=['GET', 'POST'])
@login_required
def create():
  if request.method == 'POST':
    return EventController.create(
      EventController, 
      request=request.form, 
      photo=request.files['photo'], 
      user_id=current_user.id
    )

  return render_template('held/create.html')

@held.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
  if request.method == 'POST':
    return EventController.update(
      EventController,
      request=request.form,
      photo=request.files['photo'],
      event_id=id
    )

  return render_template('/held/update.html', event=EventController.fetch_by_id(EventController, id))


@held.route('/delete/<int:id>')
@login_required
def delete(id):
  return EventController.delete(EventController, event_id=id)
