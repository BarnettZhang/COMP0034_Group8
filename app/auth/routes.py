from datetime import timedelta
from urllib.parse import urlparse, urljoin

from flask import render_template, Blueprint, request, flash, redirect, url_for, make_response, abort, session
from flask_login import login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, current_user, login_required

from app import db, login_manager
from app.auth.forms import RegistrationForm, LoginForm
from app.models import User

bp_auth = Blueprint('auth', __name__)


def is_safe_url(target):
    host_url = urlparse(request.host_url)
    redirect_url = urlparse(urljoin(request.host_url, target))
    return redirect_url.scheme in ('http', 'https') and host_url.netloc == redirect_url.netloc


def get_safe_redirect():
    url = request.args.get('next')
    if url and is_safe_url(url):
        return url

    url = request.referrer
    if url and is_safe_url(url):
        return url
    return '/'


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@bp_auth.route('/unauthorized', methods=['GET', 'POST'])
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth.login'))


@bp_auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.username.data, email=form.email.data, gender=form.gender.data, age=form.age.data,
                    ethnic=form.ethnic.data, religion=form.religion.data, nationality=form.nationality.data,
                    institution=form.institution.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            response = make_response(redirect(url_for('main.index')))
            response.set_cookie("username", form.username.data)
            return response
        except IntegrityError:
            db.session.rollback()
            flash('ERROR! Unable to register {}. Please check your details are correct and resubmit'.format(
                form.email.data), 'error')
    return render_template('signup.html', form=form)


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember.data, duration=timedelta(minutes=1))
        flash('{} logged in successfully'.format(user.username))
        next = request.args.get('next')
        if not is_safe_url(next):
            return abort(400)
        return redirect(next or url_for('main.index'))
    return render_template('login.html', form=form)


@bp_auth.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))