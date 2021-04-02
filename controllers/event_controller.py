from flask import redirect, url_for, flash
from ..models.event import Event
from ..config import Config
import os

class EventController:
  
  def fetch_all(self, user_id):
    return Event.query.filter_by(user_id=user_id).all()

  def fetch_by_id(self, event_id):
    return Event.query.filter_by(id=event_id).first()

  def create(self, title, description, start_date, end_date, category, start_time, end_time, due_date, poster_filename, user_id, speaker):
    Event.create(
      Event,
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
    
    flash('Event is successfully created', 'info')
    return redirect(url_for('held.open_class'))
