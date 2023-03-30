from flask import Blueprint

questions = Blueprint('questions', __name__)

from src.app.questions import routes