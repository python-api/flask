from flask import render_template
from src.app.questions import questions

@questions.route('/')
def index():
    return render_template('questions/../templates/questions/index.html')