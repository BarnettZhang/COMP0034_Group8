from flask import render_template, Blueprint, request, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('homepage.html')


@bp_main.route('/privacy policy 3', methods=['GET'])
def pp():
    return render_template("privacy policy 3.html")


@bp_main.route('/searchresult2', methods=['GET'])
def sr():
    return render_template("searchresult2.html")
