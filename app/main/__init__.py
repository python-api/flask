from flask import Blueprint

blue_print = Blueprint('main', __name__)

from . import routes

