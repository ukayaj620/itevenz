from flask import Blueprint, url_for, render_template, redirect
from flask_login import login_required, current_user
from ..controllers.participation_controller import ParticipationController

participation = Blueprint('participation', __name__, template_folder='templates')


@participation.route('/')
@login_required
def index():
  return ParticipationController.fetch_participated_event(ParticipationController, user_id=current_user.id)

@participation.route('/participate/<int:event_id>')
@login_required
def participate(event_id):
  return ParticipationController.participate(
    ParticipationController,
    event_id=event_id, 
    user_id=current_user.id
  )

@participation.route('/unparticipate/<int:participation_id>')
@login_required
def unparticipate(participation_id):
  return ParticipationController.delete(ParticipationController, participation_id=participation_id)

