from flask import render_template, Blueprint, request, flash, redirect, url_for, make_response, abort
bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('homepage.html')


@bp_main.route('/create_survey')
def create_survey():
    return render_template("create_survey.html")


@bp_main.route('/')
def finish_create_survey():
    flash('You have created a survey')
    return render_template('homepage.html')