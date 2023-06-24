import os

from flask import Blueprint

config = Blueprint('config', __name__)

class Config(object):
    TESTING = os.environ.get('TESTING')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_ECHO = False
    DB_CONNECTION = os.environ.get('DB_CONNECTION')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_DATABASE = os.environ.get('DB_DATABASE')
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    SQLALCHEMY_DATABASE_URI = f'{DB_CONNECTION}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATE_FOLDER = 'src/templates'  # đường dẫn đến thư mục templates
