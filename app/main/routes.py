from flask import render_template, url_for, flash, redirect, request, session
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import login_user, current_user

bp_main = Blueprint('main', __name__)


@bp_main.route('/home')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('homepage.html')


@bp_main.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', title='signup', form=form)


@bp_main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            session['logged_in'] = True
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@bp_main.route('/edit_personal_info/', methods=['GET'])
def edit_personal_info():
    return render_template("personal_info_edit.html")


@bp_main.route('/create_survey')
def create_survey():
    return render_template("create_survey.html")


@bp_main.route('/')
def finish_create_survey():
    return render_template('homepage.html')


@bp_main.route('/search_result', methods=['GET'])
def search_result():
    return render_template("search_result.html")


@bp_main.route('/take_survey_profile/', methods=['GET'])
def take_survey_profile():
    return render_template("tsp.html")


@bp_main.route('/survey_review_profile/', methods=['GET'])
def survey_review_profile():
    return render_template("srp.html")


@bp_main.route('/privacy_policy', methods=['GET'])
def privacy_policy():
    return render_template("privacy_policy.html")

