import imghdr
import string
import random

def validate_image(stream):
  header = stream.read(512)
  stream.seek(0)
  format = imghdr.what(None, header)
  if not format:
      return None
  return '.' + (format if format != 'jpeg' else 'jpg')


def generate_photoname(ext):
  return ''.join(random.choices(string.ascii_uppercase + string.digits, k=20)) + ext