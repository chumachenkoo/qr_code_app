from qr_project import app
from flask import render_template, request, redirect, session, url_for, flash
from qr_project import db, User, QRcode


@app.route('/registration', methods=['GET'])
def get_registration():
    if 'id' in session:
        return redirect(url_for('user_account'))

    return render_template('registration.html')


@app.route('/registration', methods=['POST'])
def post_registration():
    if request.method == "POST":
        user = User(username=request.form.get('username'),
                    email=request.form.get('email'),
                    password=request.form.get('password'))

        if User.get_user_by_mail(user.email):
            flash('User has been already registered!')
            return render_template('registration.html')

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('user_account'))


@app.route('/', methods=['POST'])
@app.route('/login', methods=['POST'])
def post_login():
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']

        user = User.get_user_by_mail(user_email)

        if user is not None and user_password == user[0].password:
            session['id'] = user[0].id
            return redirect(url_for('user_account'))

        return redirect(url_for('get_login'))


@app.route('/', methods=['GET'])
@app.route('/login', methods=['GET'])
def get_login():
    if 'id' in session:
        return redirect(url_for('user_account'))
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("get_login"))


@app.route('/account')
def user_account():
    if 'id' in session:
        user_id = session.get('id')
        user_data = User.get_user_by_id(user_id)
        qr = QRcode.decode(user_data)
        return render_template('account.html', user=user_data, qr_codes=qr)

    return redirect(url_for('get_login'))


@app.route('/generator', methods=['POST', 'GET'])
def qr_generator():
    if 'id' in session:
        if request.method == 'POST':
            data = request.form['qr_code']
            user = session.get('id')
            qr = QRcode.generate(data, user)

            db.session.add(qr)
            db.session.commit()

            return redirect(url_for('user_account'))
        else:
            return render_template('generator.html')
    return redirect(url_for('get_login'))



