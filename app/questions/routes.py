from flask import render_template
from app.questions import questions

@questions.route('/')
def index():
    return render_template('questions/index.html')