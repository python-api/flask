from flask import Blueprint

from src.extensions.marshmallow import marshmallow
from src.extensions.sqlalchemy import db

extensions = Blueprint('extensions', __name__)


class Extensions:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.before_request(...)
