from flask import render_template

from app.posts import posts


@posts.route('/')
def index():
    return render_template('posts/index.html')


@posts.route('/categories/')
def categories():
    return render_template('posts/categories.html')