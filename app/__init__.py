from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import jwt

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SECRET_KEY'] = "GazaHaveMoreFans"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://vzmxdkzvlzvqor:345f5c81405d9bccc3c12432947a32ad7ead9dd17f18f256daf751e925029318@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d5qvnef7dkrpv8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#Flask-Login login LoginManager
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views
