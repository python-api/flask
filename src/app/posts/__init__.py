from flask import Blueprint

posts = Blueprint('posts', __name__)



from src.app.posts import routes