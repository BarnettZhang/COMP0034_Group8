from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=True, unique=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Text, nullable=False)
    ethnic = db.Column(db.Text, nullable=False)
    religion = db.Column(db.Text, nullable=False)
    nationality = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    institution = db.Column(db.Text, nullable=False)
    survey_id = db.relationship('Survey', backref='users')

    # respondent_id = db.relationship('Answer', backref='users')

    def __repr__(self):
        return '<User {}>'.format(self.id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=True)
    survey_name = db.Column(db.Text, nullable=False, unique=True)
    keyword = db.Column(db.Text, nullable=True)
    target_gender = db.Column(db.Text, nullable=True)
    target_minimum_age = db.Column(db.Text, nullable=True)
    target_maximum_age = db.Column(db.Text, nullable=True)
    respondent_number = db.Column(db.Integer, nullable=True)
    target_nationality = db.Column(db.Text, nullable=True)
    create_date = db.Column(db.Integer, nullable=True)
    end_date = db.Column(db.Integer, nullable=True)
    q1question_num = db.Column(db.Text, nullable=True)
    q1choice_one = db.Column(db.Text, nullable=True)
    q1choice_two = db.Column(db.Text, nullable=True)
    q1choice_three = db.Column(db.Text, nullable=True)
    q1choice_four = db.Column(db.Text, nullable=True)
    q1question_content = db.Column(db.Text, nullable=True)
    q1question_must = db.Column(db.Text, nullable=True)
    q2question_num = db.Column(db.Text, nullable=True)
    q2choice_one = db.Column(db.Text, nullable=True)
    q2choice_two = db.Column(db.Text, nullable=True)
    q2choice_three = db.Column(db.Text, nullable=True)
    q2choice_four = db.Column(db.Text, nullable=True)
    q2question_content = db.Column(db.Text, nullable=True)
    q2question_must = db.Column(db.Text, nullable=True)
    q3question_num = db.Column(db.Text, nullable=True)
    q3choice_one = db.Column(db.Text, nullable=True)
    q3choice_two = db.Column(db.Text, nullable=True)
    q3choice_three = db.Column(db.Text, nullable=True)
    q3choice_four = db.Column(db.Text, nullable=True)
    q3question_content = db.Column(db.Text, nullable=True)
    q3question_must = db.Column(db.Text, nullable=True)
    q4question_must = db.Column(db.Text, nullable=True)
    q4question_num = db.Column(db.Text, nullable=True)
    q4choice_one = db.Column(db.Text, nullable=True)
    q4choice_two = db.Column(db.Text, nullable=True)
    q4choice_three = db.Column(db.Text, nullable=True)
    q4choice_four = db.Column(db.Text, nullable=True)
    q4question_content = db.Column(db.Text, nullable=True)
    q5question_must = db.Column(db.Text, nullable=True)
    q5question_num = db.Column(db.Text, nullable=True)
    q5choice_one = db.Column(db.Text, nullable=True)
    q5choice_two = db.Column(db.Text, nullable=True)
    q5choice_three = db.Column(db.Text, nullable=True)
    q5choice_four = db.Column(db.Text, nullable=True)
    q5question_content = db.Column(db.Text, nullable=True)
    q6question_must = db.Column(db.Text, nullable=True)
    q6question_num = db.Column(db.Text, nullable=True)
    q6choice_one = db.Column(db.Text, nullable=True)
    q6choice_two = db.Column(db.Text, nullable=True)
    q6choice_three = db.Column(db.Text, nullable=True)
    q6choice_four = db.Column(db.Text, nullable=True)
    q6question_content = db.Column(db.Text, nullable=True)
    q7question_must = db.Column(db.Text, nullable=True)
    q7question_num = db.Column(db.Text, nullable=True)
    q7choice_one = db.Column(db.Text, nullable=True)
    q7choice_two = db.Column(db.Text, nullable=True)
    q7choice_three = db.Column(db.Text, nullable=True)
    q7choice_four = db.Column(db.Text, nullable=True)
    q7question_content = db.Column(db.Text, nullable=True)
    q8question_must = db.Column(db.Text, nullable=True)
    q8question_num = db.Column(db.Text, nullable=True)
    q8choice_one = db.Column(db.Text, nullable=True)
    q8choice_two = db.Column(db.Text, nullable=True)
    q8choice_three = db.Column(db.Text, nullable=True)
    q8choice_four = db.Column(db.Text, nullable=True)
    q8question_content = db.Column(db.Text, nullable=True)
    q9question_must = db.Column(db.Text, nullable=True)
    q9question_num = db.Column(db.Text, nullable=True)
    q9choice_one = db.Column(db.Text, nullable=True)
    q9choice_two = db.Column(db.Text, nullable=True)
    q9choice_three = db.Column(db.Text, nullable=True)
    q9choice_four = db.Column(db.Text, nullable=True)
    q9question_content = db.Column(db.Text, nullable=True)
    q10question_must = db.Column(db.Text, nullable=True)
    q10question_num = db.Column(db.Text, nullable=True)
    q10choice_one = db.Column(db.Text, nullable=True)
    q10choice_two = db.Column(db.Text, nullable=True)
    q10choice_three = db.Column(db.Text, nullable=True)
    q10choice_four = db.Column(db.Text, nullable=True)
    q10question_content = db.Column(db.Text, nullable=True)
    q11question_must = db.Column(db.Text, nullable=True)
    q11question_num = db.Column(db.Text, nullable=True)
    q11question_content = db.Column(db.Text, nullable=True)
    q12question_must = db.Column(db.Text, nullable=True)
    q12question_num = db.Column(db.Text, nullable=True)
    q12question_content = db.Column(db.Text, nullable=True)
    q13question_must = db.Column(db.Text, nullable=True)
    q13question_num = db.Column(db.Text, nullable=True)
    q13question_content = db.Column(db.Text, nullable=True)
    q15question_must = db.Column(db.Text, nullable=True)
    q15question_num = db.Column(db.Text, nullable=True)
    q15question_content = db.Column(db.Text, nullable=True)
    q14question_must = db.Column(db.Text, nullable=True)
    q14question_num = db.Column(db.Text, nullable=True)
    q14question_content = db.Column(db.Text, nullable=True)

    # question_id = db.relationship('Question', backref='surveys')
    # answer_id = db.relationship('Answer', backref='surveys')

    def __repr__(self):
        return '<Survey {}>'.format(self.survey_id)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    # question_id = db.Column(db.Integer, db.ForeignKey(Question.question_id), nullable=False)
    # survey_id = db.Column(db.Integer, db.ForeignKey(Survey.survey_id), nullable=False)
    answer_content = db.Column(db.Text, nullable=False)
    answer_time = db.Column(db.Integer, nullable=False)
    respondent_id = db.Column(db.Text, nullable=False)
    answer_pool = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Answer {}>'.format(self.answer_id)