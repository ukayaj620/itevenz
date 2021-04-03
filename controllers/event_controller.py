from flask import redirect, url_for, flash, render_template
from ..config import Config
from ..models.event import Event
from ..models.participation import Participation
from ..utils.images import delete_image, save_image
import os
from datetime import datetime
from ..utils.time import check_form_time

class EventController:

  def fetch_all(self, user_id=None):
    events = None
    if user_id is not None:
      events = Event.query.filter(Event.user_id != user_id).all()
    else:
      events = Event.query.all()

    return render_template('company/event.html', events=events)
  
  def fetch_user_assoc_event(self, user_id):
    return Event.query.filter_by(user_id=user_id).all()

  def fetch_by_id(self, event_id):
    return Event.query.filter_by(id=event_id).first()

  def create(self, request, photo, user_id):
    check_message = check_form_time(request, False)
    if check_message != '':
      flash(check_message, 'warning')
      return redirect(url_for('held.create'))

    photo_filename = save_image(photo)

    Event.create(
      Event,
      title=request['title'],
      description=request['description'],
      start_date=request['start-date'],
      end_date=request['end-date'],
      category=request['category'],
      start_time=request['start-time'],
      end_time=request['end-time'],
      due_date=request['due-date'],
      poster_filename=photo_filename,
      user_id=user_id,
      speaker=request['speaker']
    )
    
    return redirect(url_for('held.open_class'))

  def update(self, request, photo, event_id):
    check_message = check_form_time(request, True)
    if check_message != '':
      flash(check_message, 'warning')
      return redirect(url_for('held.update', id=event_id))

    event = self.fetch_by_id(self, event_id=event_id)

    photo_filename = save_image(photo) if photo else None

    delete_image(event.poster_filename) if photo_filename is not None else None
    
    Event.update(
      Event,
      title=request['title'],
      description=request['description'],
      start_date=request['start-date'],
      end_date=request['end-date'],
      category=request['category'],
      start_time=request['start-time'],
      end_time=request['end-time'],
      due_date=request['due-date'],
      poster_filename=photo_filename,
      event_id=event_id,
      speaker=request['speaker']
    )

    return redirect(url_for('held.open_class'))

  def delete(self, event_id):
    Participation.delete_by_event(Participation, event_id=event_id)
    event = self.fetch_by_id(self, event_id=event_id)

    delete_image(event.poster_filename)
    Event.delete(Event, event_id=event_id)

    return redirect(url_for('held.open_class'))
