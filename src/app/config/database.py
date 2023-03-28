from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
