from flask import Flask
from flask_migrate import Migrate

from src.config import Config
from src.extensions import database
from src.routes import version

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Flask extensions here
    database.init_app(app)
    Migrate(app, database)

    # Register blueprints here
    app.register_blueprint(version, url_prefix='/v1')
    return app
