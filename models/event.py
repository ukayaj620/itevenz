from ..app import db
from datetime import datetime

class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False, nullable=False)
  title = db.Column(db.String(255), unique=False, nullable=False)
  description = db.Column(db.Text, unique=False, nullable=False)
  poster_filename = db.Column(db.String(255), unique=False, nullable=False)
  start_date = db.Column(db.Date, unique=False, nullable=False)
  end_date = db.Column(db.Date, unique=False, nullable=False)
  category = db.Column(db.String(255), unique=False, nullable=False)
  start_time = db.Column(db.Time, unique=False, nullable=False)
  end_time = db.Column(db.Time, unique=False, nullable=False)
  due_date = db.Column(db.Date, nullable=False)
  speaker = db.Column(db.String(255), unique=False, nullable=False)

  def __repr__(self):
    return '<Event %r>' % self.title

  def create(self, title, description, start_date, end_date, category, start_time, end_time, due_date, poster_filename, user_id, speaker):
    event = Event(
      title=title,
      description=description,
      start_date=start_date,
      end_date=end_date,
      category=category,
      start_time=start_time,
      end_time=end_time,
      due_date=due_date,
      poster_filename=poster_filename,
      user_id=user_id,
      speaker=speaker
    )
    db.session.add(event)
    db.session.commit()
  
  def update(self, title, description, start_date, end_date, category, start_time, end_time, due_date, event_id, speaker, poster_filename=None):
    event = Event.query.filter_by(id=event_id).first()
    event.title = title
    event.description = description
    event.start_date = start_date
    event.start_time = start_time
    event.end_date = end_date
    event.end_time = end_time
    event.due_date = due_date
    event.speaker = speaker
    event.category = category

    if poster_filename is not None:
      event.poster_filename = poster_filename
    
    db.session.commit()
  
  def delete(self, event_id):
    event = Event.query.filter_by(id=event_id).first()
    db.session.delete(event)
    db.session.commit()

