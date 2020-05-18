from . import db
from werkzeug.security import generate_password_hash
from datetime import date

class UserProfile(db.Model):

    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    location = db.Column(db.String(80))
    gender = db.Column(db.String(6))
    password = db.Column(db.String(255))
    biography = db.Column(db.Text)
    photoname = db.Column(db.String(50))
    joindate = db.Column(db.DateTime)

    def __init__(self, user_name, first_name, last_name, password, email, location, gender,
                    bio, photoname, joindate):

        self.username = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.location = location
        self.gender = gender
        self.biography = bio
        self.photoname = photoname
        self.joindate = joindate

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def getdate(self):
        return self.joindate.strftime("%B %d, %Y")

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)


class Posts(db.Model):
    """docstring for Posts."""

    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(80))
    caption = db.Column(db.Text)
    created_on = db.Column(db.DateTime)

    def __init__(self, user_id, photo, caption, created_on):

        self.user_id = user_id
        self.photo = photo
        self.caption = caption
        self.created_on = created_on


class Follows(db.Model):
    """docstring for Follows."""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    follower_id = db.Column(db.Integer)


    def __init__(self, user_id, follower_id):

        self.user_id = user_id
        self.follower_id = follower_id


class Likes(db.Model):
    """docstring for Likes."""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    post_id = db.Column(db.Integer)

    def __init__(self, user_id, post_id):

        self.user_id = user_id
        self.post.id = post_id
