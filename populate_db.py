from app import db
from app.models import User, Survey, Question, Answer


def populate_db():

    if not User.query.first():
