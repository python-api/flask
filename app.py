# save this as app.py
from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    name = request.args.get("name", "<script>alert(\"bad\")</script>")
    return f'Hellzzzo, {escape(name)}!'


@app.route('/hello')
def hello():
    return '<h1>hello</h1>'


@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/abount')
def abount():
    return 'The abount page'
