from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    email = db.Column(db.Text, nullable=False)
    institution = db.Column(db.Text, nullable=False)
    credit = db.Column(db.Integer, nullable=False)
    survey_id = db.relationship('Survey', backref='users')
    respondent_id = db.relationship('Answer', backref='users')

    def __repr__(self):
        return '<User {}>'.format(self.user_id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Survey(db.Model):
    survey_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    survey_name = db.Column(db.Text, nullable=False)
    keyword = db.Column(db.Text, nullable=False)
    target_respondent = db.Column(db.Text, nullable=False)
    respondent_number = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.Integer, nullable=False)
    end_date = db.Column(db.Integer, nullable=False)
    privacy_states = db.Column(db.Text, nullable=False)
    question_id = db.relationship('Question', backref='surveys')
    answer_id = db.relationship('Answer', backref='surveys')

    def __repr__(self):
        return '<Survey {}>'.format(self.survey_id)


class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)
    q_mult = db.Column(db.Text, nullable=False)
    q_shortAnswer = db.Column(db.Text, nullable=False)
    question_content = db.Column(db.Text, nullable=False)
    question_must = db.Column(db.Integer, nullable=False)
    answer_id = db.relationship('Answer', backref='questions')

    def __repr__(self):
        return '<Question {}>'.format(self.question_id)


class Answer(db.Model):
    answer_id = db.Column(db.Integer, primary_key=False, nullable=False, unique=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'), nullable=False)
    answer_content = db.Column(db.Text, nullable=False)
    answer_time = db.Column(db.Integer, nullable=False)
    respondent_id = db.Column(db.Integer, nullable=False)
    answer_pool = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Answer {}>'.format(self.answer_id)