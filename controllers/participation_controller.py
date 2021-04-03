from flask import redirect, url_for, flash, render_template
from ..models.participation import Participation
from ..models.event import Event


class ParticipationController:

  def fetch_participation(self, user_id, event_id):
    return Participation.query.filter_by(user_id=user_id, event_id=event_id).first()

  def fetch_participated_event(self, user_id):
    participated_events = Participation.get_participated_event(Participation, Event, user_id=user_id)
    return render_template('participate/index.html', participated_events=participated_events)

  def participate(self, user_id, event_id):
    Participation.create(
      Participation,
      user_id=user_id,
      event_id=event_id
    )
    return redirect(url_for('participation.index'))

  def delete(self, participation_id):
    Participation.delete(
      Participation,
      participation_id=participation_id
    )
    return redirect(url_for('participation.index'))

