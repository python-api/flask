from flask import Blueprint

models = Blueprint('models', __name__)

from src.app.models import post

