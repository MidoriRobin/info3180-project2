from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import jwt

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SECRET_KEY'] = "GazaHaveMoreFans"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://proj2:proj2@localhost/proj2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#Flask-Login login LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views
