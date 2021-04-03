from datetime import datetime

def check_form_time(request, with_seconds=False):
  time_format = '%Y-%m-%d %H:%M:%S' if with_seconds else '%Y-%m-%d %H:%M'
  registration = datetime.strptime(request['due-date'], '%Y-%m-%d')
  start = datetime.strptime(request['start-date'] + ' ' + request['start-time'], time_format)
  end = datetime.strptime(request['end-date'] + ' ' + request['end-time'], time_format)

  if start > end:
    return 'Start date should happened before end date'

  if registration > start:
    return 'Registration date should happened before start date'

