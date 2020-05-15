"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import jwt
from app import app, db
from flask import render_template, request, redirect, url_for, flash, jsonify
from .forms import *
from app.models import UserProfile
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

"""@app.route('/home')
def index():
    "Index enuh"
    return render_template('index.html')"""

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('/convert/about.html', name="Mary Jane")

@app.route('/profile/', methods=['GET','POST'])
def profile():
    """Form to add a new profile"""
    proform = SignUpForm()
    if request.method == 'POST' and proform.validate_on_submit():
        firstname = proform.firstname.data
        lastname = proform.lastname.data
        email = proform.email.data
        location = proform.location.data
        gender = proform.gender.data
        biography = proform.bio.data
        joindate = date.today()

    # Get file data and name
        photofile = proform.photo.data
        picname = photofile.filename
    # Saving filename and data to uploads folder
        filename = secure_filename(picname)
        photofile.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))
        flash('Photo saved!')
    # Adding user info to database
        user = UserProfile(firstname,lastname,email,location,gender,biography,picname,joindate)
        db.session.add(user)
        db.session.commit()
        flash('New user added!')
        return redirect(url_for('profiles'))
    return render_template('/convert/signup.html', form=proform)

@app.route('/profile/<userid>')
def show_profile(userid):
    if userid != '':
        user=UserProfile.query.filter_by(id=userid).first()
    else:
        flash("No such user exists")
        return redirect(url_for("profiles"))
    return render_template("/convert/profile.html", user=user)


@app.route('/profiles')
def profiles():
    users = UserProfile.query.filter_by().all()
    return render_template("/convert/profiles.html", profiles=users)

def format_date_joined(sDate):
    jDate = sDate.strftime("%B, %Y")
    return jDate

###
#Project 2 Routes
###

@app.route('/api/users/register', methods=['POST'])
def register(arg):

    regForm = SignUpForm()

    if request.method == 'POST' and regForm.validate_on_submit():

        fname = request.form['firstname']
        lname = request.form['lastname']
        uname = request.form['username']
        gender = request.form['gender']
        email = request.form['email']
        location = request.form['location']
        bio = request.form['bio']
        photo = request.files['photo']

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        user = UserProfile(firstname,lastname,email,location,gender,biography,picname,joindate)
        #user = UserProfile(firstname,lastname,email,location,gender,biography,picname,joindate)
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
            "profile_photo": photo
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
def login(arg):
    lForm = LoginForm()

    if request.method == 'POST' and lForm.validate_on_submit():
        username = request.form['username']
        password = request.form['password']

        user = UserProfile.query.filter_by(username=username).first()
        if user is not None and check_password_hash(user.password,password):

            #login_user(user)
            flash('Successful Login!')

            status = [{
                "message": "User successfully loggged in",
                "username": username,
                "password": password
            }]

            return jsonify(status=status)

        else:
            status = {
                "errors":[
                    form_errors(lForm)
                ]
            }

        return jsonify(status=status)
    pass


@app.route('/api/auth/logout', methods=['GET'])
#@login_required
def logout(arg):
    logout_user()
    flash('Logout successful!')

    status = [{
        "message": "User successfully logged out"
    }]

    return jsonify(status=status)
    pass

@app.route('/api/users/<user_id>/posts', methods=['POST'])
def usr_add_post(arg):

    pForm = PostForm()

    if request.method == 'POST' and pForm.validate_on_submit():

        uid = request.form['userid']
        description = request.form['description']
        photo = request.file['photopost']

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        #post class accepting the above values would go here

        status = [{
            "message": "Successfully created a new post"
        }]

    else:
        status = {
            "errors": [
                form_errors(pForm)
            ]
        }

    return jsonify(status=status)
    pass

@app.route('/api/users/<user_id>/posts', methods=['GET'])
def usr_fetch_post(arg):
    pass

@app.route('/api/users/<user_id>/follow', methods=['POST'])
def usr_follow(arg):
    pass

@app.route('/api/posts', methods=['GET'])
def get_all_posts(arg):
    pass

@app.route('/api/posts/<user_id>/like', methods=['POST'])
def like_post(arg):
    pass
###
# The functions below should be applicable to all Flask apps.
###
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

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
