from qr_project import app
from flask import render_template


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/account')
def user_account():
    return render_template('account.html')


@app.route('/generator')
def account():
    return render_template('generator.html')
