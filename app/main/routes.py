from flask import render_template, Blueprint, request, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('homepage.html')


@bp_main.route('/privacy policy 3', methods=['GET'])
def pp():
    return render_template("privacy policy 3.html")


@bp_main.route('/searchresult3', methods=['GET'])
def sr():
    return render_template("searchresult3.html")


@bp_main.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Student(name=form.name.data, email=form.email.data, student_ref=form.student_ref.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('You are now a registered user!')
            return redirect(url_for('main.index'))
        except IntegrityError:
            db.session.rollback()
            flash('ERROR! Unable to register {}. Please check your details are correct and resubmit'.format(form.email.data), 'error')
    return render_template('signup.html', form=form)
