from flask import Flask

from app.main import main
from app.posts import posts
from app.questions import questions
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    # Register blueprints here

    app.register_blueprint(main)
    app.register_blueprint(posts, url_prefix='/posts/')
    app.register_blueprint(questions, url_prefix='/questions/')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
