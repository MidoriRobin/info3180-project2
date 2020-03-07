from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "GazaHaveMoreFans"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pro1:pro1@localhost/pro1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from app import views
