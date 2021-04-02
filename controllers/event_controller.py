from flask import redirect, url_for, flash
from ..models.event import Event
from ..config import Config
import os

class EventController:
  def create(self, title, description, start_date, end_date, category, start_time, end_time, due_date, poster_filename):
    new_event = Event.create(
      Event,
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

    if not new_event:
      flash('Event is not recorded, please create it again!', 'danger')
      redirect(url_for('held.create'))
    
    if os.path.exists(Config.UPLOAD_PATH + '/' + poster_filename):
      os.remove(Config.UPLOAD_PATH + '/' + poster_filename)
    
    flash('Event is successfully created', 'info')
    return redirect(url_for('held.open_class'))
