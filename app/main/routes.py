from flask import render_template, Blueprint, request

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('homepage.html')


@bp_main.route('/take_survey_profile/', methods=['GET'])
def take_survey_profile(name=""):
    if 'username' in request.cookies:
        name = request.cookies.get('username')
    return render_template("tsp.html", name=name)


@bp_main.route('/survey_review_profile/', methods=['GET'])
def survey_review_profile(name=""):
    if 'username' in request.cookies:
        name = request.cookies.get('username')
    return render_template("srp.html", name=name)
