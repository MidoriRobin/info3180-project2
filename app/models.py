from . import db
from werkzeug.security import generate_password_hash

class UserProfile(db.Model):

    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    location = db.Column(db.String(80))
    gender = db.Column(db.String(6))
    biography = db.Column(db.Text)
    photoname = db.Column(db.String(50))

    def __init__(self, first_name, last_name, username, email, location, gender,
                    bio, photoname):
        self.firstname = first_name
        self.lastname = last_name
        self.username = username
        self.email = email
        self.location = location
        self.gender = gender
        self.biography = bio
        self.photo = photoname

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
