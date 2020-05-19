"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import jwt
import base64
from functools import wraps
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, jsonify, g, _request_ctx_stack
from flask_login import login_user, logout_user, current_user, login_required
from .forms import *
from app.models import *
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from datetime import date


###
# Routing for your application.
###

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    """Render website's home page."""
    return render_template('index.html')

def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

###
#Project 2 Routes
###

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None)
    if not auth:
      return jsonify({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'}), 401

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}), 401
    elif len(parts) == 1:
      return jsonify({'code': 'invalid_header', 'description': 'Token not found'}), 401
    elif len(parts) > 2:
      return jsonify({'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}), 401

    token = parts[1]
    try:
         payload = jwt.decode(token, app.config['SECRET_KEY'])

    except jwt.ExpiredSignature:
        return jsonify({'code': 'token_expired', 'description': 'token is expired'}), 401
    except jwt.DecodeError:
        return jsonify({'code': 'token_invalid_signature', 'description': 'Token signature is invalid'}), 401

    g.current_user = user = payload
    return f(*args, **kwargs)

  return decorated

@app.route('/api/users/register', methods=['POST'])
def register():

    regForm = SignUpForm()

    if request.method == 'POST':

        fname = request.form['firstname']
        lname = request.form['lastname']
        uname = request.form['username']
        gender = request.form['gender']
        email = request.form['email']
        location = request.form['location']
        password = request.form['password']
        bio = request.form['bio']
        photo = request.files['photo']
        joindate = date.today()

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


        user = UserProfile(uname, fname,lname,password,email,location,gender,bio,filename,joindate)
        db.session.add(user)
        db.session.commit()

        status = [{
            "message": "Registration successful",
            "firstname": fname,
            "lastname": lname,
            "username": uname,
            "password": password,
            "email": email,
            "location": location,
            "bio": bio,
            "profile_photo": filename
        }]

        return jsonify(status=status)

    else:
        status = {
            "errors": [
                form_errors(regForm)
            ]
        }
    return jsonify(status=status)

@app.route('/api/auth/login', methods=['POST'])
def login():
    lForm = LoginForm()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = UserProfile.query.filter_by(username=username).first()
        if user is not None and user.password == password:
        #check_password_hash(user.password,password):
            #Rev.Kob
            login_user(user)
            #flash('Successful Login!')

            # status = [{
            #     "message": "User successfully loggged in",
            #     "username": username,
            #     "password": password
            # }]

            token = generate_token(user.id)
            status = {
                "token": token,
                "message": "User successfully logged in"
            }
            #return jsonify(status=status)

        else:
            print(form_errors(lForm))

            status = {
                "errors":[
                    form_errors(lForm)
                ]
            }

    return jsonify(status=status)

@app.route('/api/auth/logout', methods=['GET'])
@login_required
@requires_auth
def logout():
    logout_user()
    flash('Logout successful!')

    status = [{
        "message": "User successfully logged out"
    }]

    return jsonify(status=status)

@app.route('/api/users/<user_id>/posts', methods=['POST'])
def usr_add_post(user_id):

    pForm = PostForm()

    if request.method == 'POST':

        uid = user_id
        description = request.form['description']
        photo = request.files['photopost']

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        #post class accepting the above values would go here

        status = [{
            "message": "Successfully created a new post",
            "user": uid,
            "description": description,
            "photo": filename
        }]

    else:
        status = {
            "errors": [
                #form_errors(pForm)
                "Nothing entered"
            ]
        }

    return jsonify(status=status)


@app.route('/api/users/<user_id>/posts', methods=['GET'])
def usr_fetch_post(user_id):

    user = UserProfile.query.filter_by(id=user_id).first()
    posts = Posts.query.filter_by(user_id=user_id).all()
    print("List of posts: ", posts)
    print("User: ", user)

    data ={
        "user": user.as_dict(),
        "posts": [post.as_dict() for post in posts]
    }

    return jsonify(data=data)

@app.route('/api/users/<user_id>/follow', methods=['POST'])
def usr_follow(user_id):
    pass

@app.route('/api/posts', methods=['GET'])
@requires_auth
def get_all_posts():

    defPosts = [
    {
      "id": 1,
      "user_id": 1,
      "photo": "cool-photo.jpg",
      "caption": "This is such an awesome photo from high school",
      "created_on": "2018-04-05 14:25:00",
      "likes": 10
    },
    {
      "id": 2,
      "user_id": 3,
      "photo": "another-photo.jpg",
      "caption": "Best friends from wen!",
      "created_on": "2018-04-05 10:14:23",
      "likes": 5
    },
    {
      "id": 3,
      "user_id": 3,
      "photo": "beautiful-blue-mountains.jpg",
      "caption": "Amazing photo of the Blue Mountain Peak",
      "created_on": "2018-03-31 12:58:12",
      "likes": 3
    }
  ]

    posts = Posts.query.filter_by().all()
    print([post.as_dict() for post in posts])
    if posts == []:
        dictPosts = defPosts
    else:
        dictPosts = [post.as_dict() for post in posts]


    return jsonify(error=None, posts=dictPosts, message="Success"), 201

@app.route('/api/posts/<post_id>/like', methods=['POST'])
def like_post(post_id):

    like = Likes(g.current_user,post_id)

    db.session.add(like)
    db.session.commit()

    pass



def generate_token(user_id):

    payload = {"user_id": user_id}
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    #return jsonify(error=None, data={'token': token}, message="Token generated")
    return token

###
# The functions below should be applicable to all Flask apps.
###

@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
