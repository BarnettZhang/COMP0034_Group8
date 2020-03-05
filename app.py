from flask import Flask, render_template, url_for, flash, redirect, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABC54321'


@app.route('/')
@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run()
