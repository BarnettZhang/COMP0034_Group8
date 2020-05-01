import sys

from flask import Blueprint, request, make_response, redirect, url_for, flash, render_template, session, abort
from sqlalchemy import engine, and_
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, current_user, login_required
from app import db, sess, models
from app.main.forms import CreateSurvey, AnswerSurvey
from app.models import Survey, User, Answer

bp_main = Blueprint('main', __name__)


@bp_main.route('/', methods=['GET'])
def index():
    if current_user.is_anonymous:
        return render_template('homepage.html')

    else:
        name = request.cookies.get('username')
        validuser = db.session.query(User.religion, User.ethnic, User.gender).filter_by(username=name).all()
        religion = list(validuser)[0][0]
        ethnic = list(validuser)[0][1]
        gender = list(validuser)[0][2]
        result = []
        allsurvey = db.session.query(Survey.target_religion, Survey.target_ethnic, Survey.target_gender, Survey.survey_name, Survey.description, Survey.id).all()
        print(allsurvey)
        for surveys in allsurvey:
            if surveys[0] == 'all' and surveys[1] == 'all' and surveys[2] == 'all':
                result.append(surveys)
            elif surveys[0] == 'all' and surveys[1] == 'all':
                if surveys[2] == gender:
                    result.append(surveys)
            elif surveys[0] == 'all' and surveys[2] == 'all':
                if surveys[1] == ethnic:
                    result.append(surveys)
            elif surveys[1] == 'all' and surveys[2] == 'all':
                if surveys[0] == religion:
                    result.append(surveys)
            elif surveys[0] == 'all':
                if surveys[1] == ethnic and surveys[2] == gender:
                    result.append(surveys)
            elif surveys[1] == 'all':
                if surveys[0] == religion and surveys[2] == gender:
                    result.append(surveys)
            elif surveys[2] == 'all':
                if surveys[0] == religion and surveys[1] == ethnic:
                    result.append(surveys)
            elif surveys[0] == religion and surveys[1] == ethnic and surveys[2] == gender:
                result.append(surveys)
        #result = db.session.query(Survey).filter(
         #   and_(Survey.target_religion == user.religion, Survey.target_ethnic == user.ethnic,
         #        Survey.target_gender == user.gender)).all()

        return render_template('homepage.html', results=result)


@bp_main.route('/edit_personal_info/', methods=['GET'])
def edit_personal_info():
    return render_template("personal_info_edit.html")


@bp_main.route('/create_survey/', methods=['POST', 'GET'])
def create_survey():
    form = CreateSurvey(request.form)
    name = request.cookies.get('username')
    if request.method == 'POST' and form.validate():
        survey = Survey(user_username=name, target_gender=form.target_gender.data,
                        target_nationality=form.target_nationality.data,
                        description=form.description.data, keyword=form.keyword.data,
                        end_date=form.end_date.data, respondent_number=form.respondent_number.data,
                        survey_name=form.survey_name.data, target_ethnic=form.target_ethnic.data,
                        target_religion=form.target_religion.data,
                        q1question_num=str(1), q1question_must=form.q1question_must.data,
                        q1question_content=form.q1question_content.data, q1choice_one=form.q1choice_one.data,
                        q1choice_two=form.q1choice_two.data, q1choice_three=form.q1choice_three.data,
                        q1choice_four=form.q1choice_four.data,
                        q2question_num=str(2), q2question_must=form.q2question_must.data,
                        q2question_content=form.q2question_content.data, q2choice_one=form.q2choice_one.data,
                        q2choice_two=form.q2choice_two.data, q2choice_three=form.q2choice_three.data,
                        q2choice_four=form.q2choice_four.data,
                        q3question_num=str(3), q3question_must=form.q3question_must.data,
                        q3question_content=form.q3question_content.data, q3choice_one=form.q3choice_one.data,
                        q3choice_two=form.q3choice_two.data, q3choice_three=form.q3choice_three.data,
                        q3choice_four=form.q3choice_four.data,
                        q4question_num=str(4), q4question_must=form.q4question_must.data,
                        q4question_content=form.q4question_content.data, q4choice_one=form.q4choice_one.data,
                        q4choice_two=form.q4choice_two.data, q4choice_three=form.q4choice_three.data,
                        q4choice_four=form.q4choice_four.data,
                        q5question_num=str(5), q5question_must=form.q5question_must.data,
                        q5question_content=form.q5question_content.data, q5choice_one=form.q5choice_one.data,
                        q5choice_two=form.q5choice_two.data, q5choice_three=form.q5choice_three.data,
                        q5choice_four=form.q5choice_four.data,
                        q6question_num=str(6), q6question_must=form.q6question_must.data,
                        q6question_content=form.q6question_content.data, q6choice_one=form.q6choice_one.data,
                        q6choice_two=form.q6choice_two.data, q6choice_three=form.q6choice_three.data,
                        q6choice_four=form.q6choice_four.data,
                        q7question_num=str(7), q7question_must=form.q7question_must.data,
                        q7question_content=form.q7question_content.data, q7choice_one=form.q7choice_one.data,
                        q7choice_two=form.q7choice_two.data, q7choice_three=form.q7choice_three.data,
                        q7choice_four=form.q7choice_four.data,
                        q8question_num=str(8), q8question_must=form.q8question_must.data,
                        q8question_content=form.q8question_content.data, q8choice_one=form.q8choice_one.data,
                        q8choice_two=form.q8choice_two.data, q8choice_three=form.q8choice_three.data,
                        q8choice_four=form.q8choice_four.data,
                        q9question_num=str(9), q9question_must=form.q9question_must.data,
                        q9question_content=form.q9question_content.data, q9choice_one=form.q9choice_one.data,
                        q9choice_two=form.q9choice_two.data, q9choice_three=form.q9choice_three.data,
                        q9choice_four=form.q9choice_four.data,
                        q10question_num=str(10), q10question_must=form.q10question_must.data,
                        q10question_content=form.q10question_content.data, q10choice_one=form.q10choice_one.data,
                        q10choice_two=form.q10choice_two.data, q10choice_three=form.q10choice_three.data,
                        q10choice_four=form.q10choice_four.data,
                        q11question_num=str(11), q11question_must=form.q11question_must.data,
                        q11question_content=form.q11question_content.data,
                        q12question_num=str(12), q12question_must=form.q12question_must.data,
                        q12question_content=form.q12question_content.data,
                        q13question_num=str(13), q13question_must=form.q13question_must.data,
                        q13question_content=form.q13question_content.data,
                        q14question_num=str(14), q14question_must=form.q14question_must.data,
                        q14question_content=form.q14question_content.data,
                        q15question_num=str(15), q15question_must=form.q15question_must.data,
                        q15question_content=form.q15question_content.data)
        try:
            db.session.add(survey)
            db.session.commit()
            print('Create Survey : ' + str(survey), file=sys.stderr)
            flash('You have successfully created a survey! We are delivering it to appropriate respondents.')
            return redirect(url_for('main.index'))
        except IntegrityError:
            db.session.rollback()
            flash('There is something wrong with your survey. Try a different title?')
    return render_template("create_survey.html", form=form)


@bp_main.route('/search', methods=['POST', 'GET'])
def search_result():
    if request.method == 'POST':
        term = request.form['term']
        if term == "":
            flash("Enter a survey id")
            return redirect('/')
        results: object = Survey.query.filter(Survey.id.is_(term)).all()
        if not results:
            flash("No survey with this id")
            return redirect('/')

        return render_template('search_result.html', results=results)
    else:
        return redirect(url_for('main.index'))


@bp_main.route('/answer_survey', methods=['POST', 'GET'])
def answer_survey():
    answer = AnswerSurvey(request.form)
    if request.method == 'POST':
        answer = Answer(q1answer=answer.q1answer.data, q2answer=answer.q2answer.data, q3answer=answer.q3answer.data,
                        q4answer=answer.q4answer.data, q5answer=answer.q5answer.data, q6answer=answer.q6answer.data,
                        q7answer=answer.q7answer.data, q8answer=answer.q8answer.data, q9answer=answer.q9answer.data,
                        q10answer=answer.q10answer.data, q11answer=answer.q11answer.data,
                        q12answer=answer.q12answer.data,
                        q13answer=answer.q13answer.data, q14answer=answer.q14answer.data,
                        q15answer=answer.q15answer.data, survey_id=answer.survey_id.data)
        db.session.add(answer)
        db.session.commit()
        print('Answer : ' + str(answer), file=sys.stderr)
        flash('You have finished answering')
        return redirect(url_for('main.index'))
    return render_template("answer_survey.html", answer=answer)


@bp_main.route('/take_survey_profile/', methods=['GET'])
def take_survey_profile(name=""):
    if 'username' in request.cookies:
        name = request.cookies.get('username')
    return render_template("tsp.html", name=name)


@bp_main.route('/survey_review_profile/', methods=['GET'])
def survey_review_profile():
    if 'username' in request.cookies:
        name = request.cookies.get('username')
        print('name : ' + name, file=sys.stderr)
        results_only = db.session.query(Survey.survey_name, Survey.user_username,
                                        Survey.id.label('survey_id')).filter_by(user_username=name).all()
        # print('results only : ' + str(results_only), file=sys.stderr)
        # print('results only : ' + str(type(results_only)), file=sys.stderr)
        if not results_only:
            flash("You have not created any survey")
            return redirect('/')
        return render_template('srp.html', results=results_only)
    else:
        return redirect('main.index')


@bp_main.route('/privacy_policy', methods=['GET'])
def privacy_policy():
    return render_template("privacy_policy.html")
