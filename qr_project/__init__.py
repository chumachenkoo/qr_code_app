from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qr_project.db'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from qr_project import routes