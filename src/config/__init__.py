import os

from flask import Blueprint

config = Blueprint('config', __name__)

class Config(object):
    TESTING = os.environ.get('TESTING')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATE_FOLDER = 'src/templates'  # đường dẫn đến thư mục templates
