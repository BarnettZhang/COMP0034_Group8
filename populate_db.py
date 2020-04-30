from app import db
from app.models import User, Survey, Answer


def populate_db():

    if not User.query.first():
