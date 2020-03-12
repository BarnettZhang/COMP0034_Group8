from flask import render_template, Blueprint

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('homepage.html')


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

