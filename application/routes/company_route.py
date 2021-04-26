from flask import Blueprint, render_template
from application.controllers.event_controller import EventController
from application.controllers.participation_controller import ParticipationController
from flask_login import current_user

company = Blueprint('company', __name__, template_folder='templates')

@company.route('/')
def about():
  return render_template('company/about.html')

@company.route('/event')
def event():
  return EventController.fetch_all(EventController, current_user.id if current_user.is_authenticated else None)

@company.route('event/view/<int:event_id>')
def event_detail(event_id):
  event = EventController.fetch_by_id(EventController, event_id=event_id)

  participated_event = None
  if current_user.is_authenticated:
    participated_event = ParticipationController.fetch_participation(ParticipationController, user_id=current_user.id, event_id=event_id)

  return render_template('company/event_detail.html', event=event, participated_event=participated_event)

