from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# The SQLAlchemy object is defined globally
db = SQLAlchemy()
bcrypt = Bcrypt()


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

    login_manager = LoginManager(app)
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'

    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app