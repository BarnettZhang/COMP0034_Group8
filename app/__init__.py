from flask import Flask, render_template, url_for, flash, redirect, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
from flask_session import Session

# The SQLAlchemy object is defined globally
db = SQLAlchemy()
login_manager = LoginManager()
sess = Session()


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

    # Initialise plugins
    db.init_app(app)
    login_manager.init_app(app)

    # Initialise the database and create tables
    db.init_app(app)
    from app.models import Survey, Answer, User
    with app.app_context():
        #db.drop_all()
        db.create_all()

    # Register error handlers
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    # Register Blueprints
    from app.main.routes import bp_main
    app.register_blueprint(bp_main)

    from app.auth.routes import bp_auth
    app.register_blueprint(bp_auth)

    return app