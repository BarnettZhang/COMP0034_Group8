from flask import render_template, Blueprint, request

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('homepage.html')


@bp_main.route('/edit_personal_info/', methods=['GET'])
def edit_personal_info(name=""):
    if 'username' in request.cookies:
        name = request.cookies.get('username')
    return render_template('personal_info_edit.html', username=name)
