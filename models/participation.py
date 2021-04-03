from ..app import db
from datetime import datetime


class Participation(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), unique=False, nullable=False)
  event_id = db.Column(db.Integer, db.ForeignKey('event.id', ondelete='CASCADE'), unique=False, nullable=False)
  register_time = db.Column(db.Date, unique=False, nullable=False)

  def __repr__(self):
    return '<Participation %r>' % self.id

  def get_participated_event(self, Event, user_id, event_id=None):
    return db.session.query(self, Event).join(Event).filter(self.user_id == user_id, self.event_id == event_id)

  def create(self, user_id, event_id):
    participation = Participation(
      user_id=user_id,
      event_id=event_id,
      register_time=datetime.now()
    )
    db.session.add(participation)
    db.session.commit()

  def delete(self, participation_id):
    participation = Participation.query.filter_by(id=participation_id).first()
    db.session.delete(participation)
    db.session.commit()

