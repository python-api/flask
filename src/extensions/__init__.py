from flask import Blueprint
from src.extensions.sqlalchemy import database
extensions = Blueprint('extensions', __name__)


class Extension:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.before_request(...)
