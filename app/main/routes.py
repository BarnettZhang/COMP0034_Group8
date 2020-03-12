from flask import render_template, Blueprint, request, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from app import db
from app.main.forms import SignupForm
from app.models import Course, Student

bp_main = Blueprint('main', __name__)


@bp_main.route('/privacy_policy', methods=['GET'])
def privacy_policy():
    return render_template("privacy_policy.html")


@bp_main.route('/search_result', methods=['GET'])
def search_result():
    return render_template("search_result.html")