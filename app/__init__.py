from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig

# The SQLAlchemy object is defined globally
db = SQLAlchemy()


def page_not_found(e):
    return render_template('404.html'), 404


def internal_server_error(e):
    return render_template('500.html'), 500


def create_app(config_class=DevConfig):
    """
    Creates an application instance to run
    :return: A Flask object
    """
    app = Flask(__name__)

    # Configure app wth the settings from config.py
    app.config.from_object(config_class)

    # Initialise the database and create tables
    db.init_app(app)

    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app