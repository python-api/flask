from flask import Flask
from flask_migrate import Migrate

from src.config import Config
from src.extensions import Extensions, db
from src.routes import version


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Flask extensions here
    db.init_app(app=app)
    Migrate(app=app, db=db)
    db.Session()

    # Register blueprints here
    app.register_blueprint(version, url_prefix='/v1')
    return app
