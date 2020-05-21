from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import jwt

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SECRET_KEY'] = "IHaveBeenAtUWIForTooLongINeedToLeave"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://proj2:proj2@localhost/proj2"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yugkiswqtwyxdp:801b2ad8f8ed929dad860261a06ec9de6692b4316dfec738bb0b8d5becbc3226@ec2-3-91-139-25.compute-1.amazonaws.com:5432/dd3482on5hq33d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#Flask-Login login LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views
