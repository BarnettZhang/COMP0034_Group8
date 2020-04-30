from flask_wtf import FlaskForm
from sqlalchemy import or_
from sqlalchemy.orm import with_polymorphic
from wtforms import SelectField, StringField, PasswordField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


from app import db
from app.models import Survey, User, Answer


class CreateSurvey(FlaskForm):
    target_gender = SelectField('Gender*', choices=[('male', 'Male'), ('female', 'Female'), ('all', 'All')],
                                validators=[DataRequired()])
    target_minimum_age = StringField('Minimum Age')
    target_maximum_age = StringField('Maximum Age')
    target_nationality = StringField('Nationality')
    target_ethnic = SelectField('Ethnic*', choices=[('white', 'White'), ('black', 'Black'), ('asian', 'Asian'),
                                            ('arab', 'Arab'), ('mixed', 'Mixed'), ('all', 'All')], validators=[DataRequired()])
    target_religion = SelectField('Religion*', choices=[('christianity', 'Christianity'), ('islam', 'Islam'),
                                                ('buddhism', 'Buddhism'), ('hinduism', 'Hinduism'),
                                                ('folk religion', 'Folk Religions'), ('irreligious', 'Irreligious'), ('all', 'All')],
                           validators=[DataRequired()])
    keyword = StringField('Keywords')
    description = StringField('Description')
    end_date = StringField('End date')
    respondent_number = StringField('Number of Required Responses')
    q1question_num = StringField('Question Number')
    q1question_content = StringField('Question Content')
    q1choice_one = StringField('Choice one')
    q1choice_two = StringField('Choice two')
    q1choice_three = StringField('Choice three')
    q1choice_four = StringField('Choice four')
    q1question_must = BooleanField('Compulsory or not')
    q2question_num = StringField('Question Number')
    q2question_content = StringField('Question Content')
    q2choice_one = StringField('Choice one')
    q2choice_two = StringField('Choice two')
    q2choice_three = StringField('Choice three')
    q2choice_four = StringField('Choice four')
    q2question_must = BooleanField('Compulsory or not')
    q3question_num = StringField('Question Number')
    q3question_content = StringField('Question Content')
    q3choice_one = StringField('Choice one')
    q3choice_two = StringField('Choice two')
    q3choice_three = StringField('Choice three')
    q3choice_four = StringField('Choice four')
    q3question_must = BooleanField('Compulsory or not')
    q4question_num = StringField('Question Number')
    q4question_content = StringField('Question Content')
    q4choice_one = StringField('Choice one')
    q4choice_two = StringField('Choice two')
    q4choice_three = StringField('Choice three')
    q4choice_four = StringField('Choice four')
    q4question_must = BooleanField('Compulsory or not')
    q5question_num = StringField('Question Number')
    q5question_content = StringField('Question Content')
    q5choice_one = StringField('Choice one')
    q5choice_two = StringField('Choice two')
    q5choice_three = StringField('Choice three')
    q5choice_four = StringField('Choice four')
    q5question_must = BooleanField('Compulsory or not')
    q6question_num = StringField('Question Number')
    q6question_content = StringField('Question Content')
    q6choice_one = StringField('Choice one')
    q6choice_two = StringField('Choice two')
    q6choice_three = StringField('Choice three')
    q6choice_four = StringField('Choice four')
    q6question_must = BooleanField('Compulsory or not')
    q7question_num = StringField('Question Number')
    q7question_content = StringField('Question Content')
    q7choice_one = StringField('Choice one')
    q7choice_two = StringField('Choice two')
    q7choice_three = StringField('Choice three')
    q7choice_four = StringField('Choice four')
    q7question_must = BooleanField('Compulsory or not')
    q8question_num = StringField('Question Number')
    q8question_content = StringField('Question Content')
    q8choice_one = StringField('Choice one')
    q8choice_two = StringField('Choice two')
    q8choice_three = StringField('Choice three')
    q8choice_four = StringField('Choice four')
    q8question_must = BooleanField('Compulsory or not')
    q9question_num = StringField('Question Number')
    q9question_content = StringField('Question Content')
    q9choice_one = StringField('Choice one')
    q9choice_two = StringField('Choice two')
    q9choice_three = StringField('Choice three')
    q9choice_four = StringField('Choice four')
    q9question_must = BooleanField('Compulsory or not')
    q10question_num = StringField('Question Number')
    q10question_content = StringField('Question Content')
    q10choice_one = StringField('Choice one')
    q10choice_two = StringField('Choice two')
    q10choice_three = StringField('Choice three')
    q10choice_four = StringField('Choice four')
    q10question_must = BooleanField('Compulsory or not')
    q11question_num = StringField('Question Number')
    q11question_content = StringField('Question Content')
    q11question_must = BooleanField('Compulsory or not')
    q12question_num = StringField('Question Number')
    q12question_content = StringField('Question Content')
    q12question_must = BooleanField('Compulsory or not')
    q13question_num = StringField('Question Number')
    q13question_content = StringField('Question Content')
    q13question_must = BooleanField('Compulsory or not')
    q14question_num = StringField('Question Number')
    q14question_content = StringField('Question Content')
    q14question_must = BooleanField('Compulsory or not')
    q15question_num = StringField('Question Number')
    q15question_content = StringField('Question Content')
    q15question_must = BooleanField('Compulsory or not')
    survey_name = StringField('Survey title*', validators=[DataRequired(message='You need a survey title!')])


class AnswerSurvey(FlaskForm):
    q1answer = StringField('Question 1 Answer')
    q2answer = StringField('Question 2 Answer')
    q3answer = StringField('Question 3 Answer')
    q4answer = StringField('Question 4 Answer')
    q5answer = StringField('Question 5 Answer')
    q6answer = StringField('Question 6 Answer')
    q7answer = StringField('Question 7 Answer')
    q8answer = StringField('Question 8 Answer')
    q9answer = StringField('Question 9 Answer')
    q10answer = StringField('Question 10 Answer')
    q11answer = StringField('Question 11 Answer')
    q12answer = StringField('Question 12 Answer')
    q13answer = StringField('Question 13 Answer')
    q14answer = StringField('Question 14 Answer')
    q15answer = StringField('Question 15 Answer')
