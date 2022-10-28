from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qr_project1.db'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    qr_codes = db.relationship('QRcode', backref='q_rcode', lazy=True)


    def __repr__(self):
        return f'User: {self.id}'

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def get_user_by_mail(email):
        data = db.session.query(User).filter_by(email=email).all()
        return data

    @staticmethod
    def get_user_by_id(user_id):
        data = db.session.query(User).filter_by(id=user_id).all()
        return data


class QRcode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qr_code = db.Column(db.LargeBinary, nullable=True)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))


from qr_project import routes