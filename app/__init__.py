from flask import Flask, render_template, url_for, flash, redirect, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABC54321'


@app.route('/')
@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('register'))
    return render_template('signup.html', title='Register', form=form)


if __name__ == '__main__':
    app.run()
