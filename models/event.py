from ..app import db
from datetime import datetime

class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(255), unique=False, nullable=False)
  description = db.Column(db.Text, unique=False, nullable=False)
  poster_filename = db.Column(db.String(255), unique=False, nullable=False)
  start_date = db.Column(db.Date, unique=False, nullable=False)
  end_date = db.Column(db.Date, unique=False, nullable=False)
  category = db.Column(db.String(255), unique=False, nullable=False)
  start_time = db.Column(db.Time, unique=False, nullable=False)
  end_time = db.Column(db.Time, unique=False, nullable=False)
  due_date = db.Column(db.DateTime, nullable=False)

  def __repr__(self):
    return '<Event %r>' % self.title

  def create(self, title, description, start_date, end_date, category, start_time, end_time, due_date, poster_filename):
    event = Event(
      title=title,
      description=description,
      start_date=start_date,
      end_date=end_date,
      category=category,
      start_time=start_time,
      end_time=end_time,
      due_date=due_date,
      poster_filename=poster_filename
    )
    db.session.add(event)
    db.session.commit()
  
