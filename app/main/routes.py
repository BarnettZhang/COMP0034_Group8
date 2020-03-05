from flask import render_template, Blueprint, request, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from app import db
from app.main.forms import SignupForm
from app.models import Course, Student

bp_main = Blueprint('main', __name__)
