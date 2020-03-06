from flask import render_template, Blueprint

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('homepage.html')


@bp_main.route('/take_survey_profile/', methods=['GET'])
def take_survey_profile():
    return render_template("tsp.html")


@bp_main.route('/survey_review_profile/', methods=['GET'])
def survey_review_profile():
    return render_template("srp.html")
