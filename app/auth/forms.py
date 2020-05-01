from flask_wtf import FlaskForm
from sqlalchemy.orm import with_polymorphic
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from app import db
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Username should be 2~20 characters"),
                                                   Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(message='Valid email address required')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password')
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    ethnic = SelectField('Ethnic', choices=[('white', 'White'), ('black', 'Black'), ('asian', 'Asian'),
                                            ('arab', 'Arab'), ('mixed', 'Mixed')], validators=[DataRequired()])
    religion = SelectField('Religion', choices=[('christianity', 'Christianity'), ('islam', 'Islam'),
                                                ('buddhism', 'Buddhism'), ('hinduism', 'Hinduism'),
                                                ('folk religion', 'Folk Religions'), ('irreligion', 'Irreligious')],
                           validators=[DataRequired()])
    nationality = StringField('Nationality', validators=[DataRequired()])
    institution = StringField('Institution', validators=[DataRequired()])

    def validate_username(self, username):
        results = User.query.filter_by(username=username.data).first()
        if results is not None:
            raise ValidationError('An account is already registered for that username')

    def validate_email(self, email):
        results = User.query.filter_by(email=email.data).first()
        if results is not None:
            raise ValidationError('An account is already registered for that email address')


class LoginForm(FlaskForm):
    # email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')



class ProfileForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Valid email address required')])
    age = StringField('Age', validators=[DataRequired()])
    institution = StringField('Institution', validators=[DataRequired()])
