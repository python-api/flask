from flask import Flask
from flask_migrate import Migrate

from src.config import Config
from src.extensions import Extensions, database
from src.routes import version


extension = Extensions()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Flask extensions here
    database.init_app(app)
    migrate = Migrate(app, database)
    from src.database import models


    # Initialize Flask extensions here
    extension.database.init_app(app=app)
    session = extension.database.Session()


    Migrate(app, extension.database)

    # Register blueprints here
    app.register_blueprint(version, url_prefix='/v1')
    return app
