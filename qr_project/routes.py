from qr_project import app
from flask import render_template, request, redirect
from qr_project import db, User


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    else:
        user = User(username=request.form.get('username'),
                    email=request.form.get('email'),
                    password=request.form.get('password'))

        db.session.add(user)
        db.session.commit()

        return redirect('/login')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

    return render_template('login.html')


@app.route('/account')
def user_account():
    return render_template('account.html')


@app.route('/generator')
def account():
    return render_template('generator.html')
