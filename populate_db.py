from app import db
from app.models import Answer, Survey, User


def populate_db():
    if not User.query.first():
        s1 = Survey(survey_name='COMP0034 student survey', keyword='UCL Computer Science', description='This is a survey for student to give suggestions to lectures of COMP0034 to help improve the quality of teaching in the future.',
                    q1question_content='Are you a student of COMP0034', q1question_must='True', q1question_num='1', q1choice_one='Yes', q1choice_two='No')

        db.session.add(s1)
        db.session.commit()