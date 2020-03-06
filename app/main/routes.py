from flask import render_template, Blueprint

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('homepage.html')

@bp_main.route('/edit_personal_info/', method = ['GET'])
def edit_personal_info():
    return render_template("personal_info_edit.html")


