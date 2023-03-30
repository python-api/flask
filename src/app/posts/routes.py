from flask import render_template

from src.app.posts import posts


@posts.route('/')
def index():
    return render_template('posts/../templates/posts/index.html')


@posts.route('/categories/')
def categories():
    return render_template('posts/../templates/posts/categories.html')