from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SECRET_KEY'] = "GazaHaveMoreFans"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pro1:pro1@localhost/pro1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
