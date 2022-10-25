from qr_project import app
from flask import render_template, request, redirect, session, url_for
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

        return redirect(url_for('get_login'))


@app.route('/login', methods=['POST'])
def post_login():
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']

        user = User.get_user(email=user_email)

        if user is not None and user_password == user[0].password:
            session['email'] = user[0].email
            return redirect(url_for('index'))

        return redirect(url_for('get_login'))


@app.route('/login', methods=['GET'])
def get_login():
    if 'email' in session:
        return redirect(url_for('user_account'))
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("get_login"))


@app.route('/account')
def user_account():
    if 'email' in session:
        user_email = session.get('email')
        user_data = User.get_user(email=user_email)
        print(user_data)
        return render_template('account.html', user=user_data)

    return redirect(url_for('get_login'))


@app.route('/generator')
def generator():
    return render_template('generator.html')
