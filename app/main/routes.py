from flask import Blueprint, request, make_response, redirect, url_for, flash, render_template, session, abort
from sqlalchemy.exc import IntegrityError

from app import db
from app.main.forms import CreateSurvey
from app.models import Survey, User, Question, Answer

bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def index():
    return render_template('homepage.html')


@bp_main.route('/edit_personal_info/', methods=['GET'])
def edit_personal_info():
    return render_template("personal_info_edit.html")


@bp_main.route('/create_survey/', methods=['POST', 'GET'])
def create_survey():
    form = CreateSurvey(request.form)
    if request.method == 'POST':
        survey = Survey(target_gender=form.target_gender.data, target_maximum_age=form.target_maximum_age.data,
                        target_minimum_age=form.target_minimum_age.data, target_nationality=form.target_nationality.data,
                        end_date=form.end_date.data, respondent_number=form.respondent_number.data,
                        survey_name=form.survey_name.data,
                        q1question_num=form.q1question_num.data, q1question_must= form.q1queastion_must.data, q1question_content=form.q1question_content.data, q1choice_one=form.q1choice_one.data, q1choice_two=form.q1choice_two.data, q1choice_three=form.q1choice_three.data, q1choice_four=form.q1choice_four.data,
                        q2question_num=form.q2question_num.data, q2question_must= form.q2queastion_must.data, q2question_content=form.q2question_content.data, q2choice_one=form.q2choice_one.data, q2choice_two=form.q2choice_two.data, q2choice_three=form.q2choice_three.data, q2choice_four=form.q2choice_four.data,
                        q3question_num=form.q3question_num.data, q3question_must= form.q3queastion_must.data, q3question_content=form.q3question_content.data, q3choice_one=form.q3choice_one.data, q3choice_two=form.q3choice_two.data, q3choice_three=form.q3choice_three.data, q3choice_four=form.q3choice_four.data,
                        q4question_num=form.q4question_num.data, q4question_must= form.q4queastion_must.data, q4question_content=form.q4question_content.data, q4choice_one=form.q4choice_one.data, q4choice_two=form.q4choice_two.data, q4choice_three=form.q4choice_three.data, q4choice_four=form.q4choice_four.data,
                        q5question_num=form.q5question_num.data, q5question_must= form.q5queastion_must.data, q5question_content=form.q5question_content.data, q5choice_one=form.q5choice_one.data, q5choice_two=form.q5choice_two.data, q5choice_three=form.q5choice_three.data, q5choice_four=form.q5choice_four.data,
                        q6question_num=form.q6question_num.data, q6question_must= form.q6queastion_must.data, q6question_content=form.q6question_content.data, q6choice_one=form.q6choice_one.data, q6choice_two=form.q6choice_two.data, q6choice_three=form.q6choice_three.data, q6choice_four=form.q6choice_four.data,
                        q7question_num=form.q7question_num.data, q7question_must= form.q7queastion_must.data, q7question_content=form.q7question_content.data, q7choice_one=form.q7choice_one.data, q7choice_two=form.q7choice_two.data, q7choice_three=form.q7choice_three.data, q7choice_four=form.q7choice_four.data,
                        q8question_num=form.q8question_num.data, q8question_must= form.q8queastion_must.data, q8question_content=form.q8question_content.data, q8choice_one=form.q8choice_one.data, q8choice_two=form.q8choice_two.data, q8choice_three=form.q8choice_three.data, q8choice_four=form.q8choice_four.data,
                        q9question_num=form.q9question_num.data, q9question_must= form.q9queastion_must.data, q9question_content=form.q9question_content.data, q9choice_one=form.q9choice_one.data, q9choice_two=form.q9choice_two.data, q9choice_three=form.q9choice_three.data, q9choice_four=form.q9choice_four.data,
                        q10question_num=form.q10question_num.data, q10question_must= form.q10queastion_must.data, q10question_content=form.q10question_content.data, q10choice_one=form.q10choice_one.data, q10choice_two=form.q10choice_two.data, q10choice_three=form.q10choice_three.data, q10choice_four=form.q10choice_four.data,
                        q11question_num=form.q11question_num.data, q11question_must= form.q11queastion_must.data, q11question_content=form.q11question_content.data,
                        q12question_num=form.q12question_num.data, q12question_must= form.q12queastion_must.data, q12question_content=form.q12question_content.data,
                        q13question_num=form.q13question_num.data, q13question_must= form.q13queastion_must.data, q13question_content=form.q13question_content.data,
                        q14question_num=form.q14question_num.data, q14question_must= form.q14queastion_must.data, q14question_content=form.q14question_content.data,
                        q15question_num=form.q15question_num.data, q15question_must= form.q15queastion_must.data, q15question_content=form.q15question_content.data)
        try:
            db.session.add(survey)
            db.session.commit()
            flash('You have successfully created a survey! We are delivering it to appropriate respondents.')
            return redirect(url_for('main.index'))
        except IntegrityError:
            db.session.rollback()
            flash('There is something wrong with your survey. Try a different title?')
    return render_template("create_survey.html", form=form)


@bp_main.route('/')
def finish_create_survey():
    return render_template('homepage.html')


@bp_main.route('/search', methods=['POST', 'GET'])
def search_result():
    if request.method == 'POST':
        term = request.form['search_term']
        if term == "":
            flash("Enter a survey name to search for")
            return redirect('/')
        results: object = Survey.query.filter(Survey.keyword.contains(term)).all()
        if not results:
            flash("No survey related")
            return redirect('/')
        return render_template('search_result.html', results=results)
    else:
        return redirect(url_for('main.index'))


@bp_main.route('/take_survey_profile/', methods=['GET'])
def take_survey_profile():
    return render_template("tsp.html")


@bp_main.route('/survey_review_profile/', methods=['GET'])
def survey_review_profile():
    return render_template("srp.html")


@bp_main.route('/privacy_policy', methods=['GET'])
def privacy_policy():
    return render_template("privacy_policy.html")



