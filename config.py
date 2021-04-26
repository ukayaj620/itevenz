import os

# file konfigurasi dari flask

class Config:
    DEBUG = False
    SECRET_KEY = str(os.environ.get('SECRET_KEY'))
    SQLALCHEMY_DATABASE_URI = str(os.environ.get('DATABASE_URL'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_EXTENSIONS = str(os.environ.get('UPLOAD_IMAGE_PATH')).split(' ')
    UPLOAD_PATH = str(os.environ.get('UPLOAD_IMAGE_PATH'))


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False