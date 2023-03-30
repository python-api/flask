from flask import Flask

from src.app.main import main
from src.app.posts import posts
from src.app.questions import questions
from src.config import Config
from src.extensions import Extension, database

extensions = Extension()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    print(app.config)

    # Initialize Flask extensions here
    database.init_app(app)


    # Register blueprints here

    app.register_blueprint(main)
    app.register_blueprint(posts, url_prefix='/posts/')
    app.register_blueprint(questions, url_prefix='/questions/')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app
