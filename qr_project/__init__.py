from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import qrcode
from io import BytesIO
import base64

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

    @staticmethod
    def generate(data, user):
        image = qrcode.make(data)
        buffer = BytesIO()
        image.save(buffer, format='png')

        inf = base64.b64encode(buffer.getvalue())

        qr = QRcode(qr_code=inf, owner=user)
        return qr

    @staticmethod
    def decode(user_data):
        result = []
        for data in user_data[0].qr_codes:
            qr = data.qr_code
            info = f'data:image/png;base64,{qr.decode("UTF-8")}'
            result.append(info)
        return result


from qr_project import routes