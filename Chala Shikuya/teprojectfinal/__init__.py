import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
app = Flask(__name__)

app.config['WTF_CSRF_SECRET_KEY'] = "4efca45cd63a4760871cad51d72e92c3"
app.config['SECRET_KEY'] = "4efca45cd63a4760871cad51d72e92c2"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:abc456@localhost/teproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'regilog'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from teprojectfinal import routes