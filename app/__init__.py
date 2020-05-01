from flask import Flask, render_template, url_for, flash, redirect, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from app.config import DevConfig
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# The SQLAlchemy object is defined globally
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


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
    app.config.from_object(DevConfig)

    # Initialise the database and create tables
    db.init_app(app)
    from app.models import Survey, Answer, User
    with app.app_context():
        db.create_all()
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    return app