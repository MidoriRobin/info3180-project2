"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from .forms import *
from app.models import UserProfile
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

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
        user = UserProfile(firstname,lastname,email,location,gender,biography,picname)
        db.session.add(user)
        db.session.commit()
        flash('New user added!')
        return redirect(url_for('profiles'))
    return render_template('signup.html', form=proform)

@app.route('/profile/<userid>')
def show_profile(userid):
    if userid != '':
        user=UserProfile.query.filter_by(id=userid).first()
    else:
        flash("No such user exists")
        return redirect(url_for("profiles"))
    return render_template("profile.html", user=user)


@app.route('/profiles')
def profiles():
    users = UserProfile.query.filter_by().all()
    return render_template("profiles.html", profiles=users)

###
# The functions below should be applicable to all Flask apps.
###

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
