from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

class Extensions(object):
    marshmallow = Marshmallow()
    database = SQLAlchemy()