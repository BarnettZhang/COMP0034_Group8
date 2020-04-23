from flask_wtf import FlaskForm
from sqlalchemy import or_
from sqlalchemy.orm import with_polymorphic
from wtforms import SelectField, StringField, PasswordField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


from app import db
from app.models import Survey, User, Question, Answer


class CreateSurveyRequest(FlaskForm):
    target_gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('all gender', 'All Gender')])
    target_minimum_age = StringField('Minimum Age')
    target_maximum_age = StringField('Maximum Age')
    nationality = StringField('Nationality')
    end_date = StringField('End date')
    respondent_number = StringField('Number of Required Responses')

    def validate_age(self, target_minimum_age, target_maximum_age):
        if target_minimum_age > target_maximum_age:
            raise ValidationError('The target maximum age must be higher than the minimum.')

