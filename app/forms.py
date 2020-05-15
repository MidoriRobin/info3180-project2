from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import *
from wtforms.validators import DataRequired, Email, InputRequired

class SignUpForm(FlaskForm):
    firstname = StringField('First Name: ', validators=[DataRequired()])
    lastname = StringField('Last Name: ', validators=[DataRequired()])
    username = StringField('Username: ', validators=[DataRequired()])
    gender = SelectField('Gender: ', choices = [('Male','Male'),('Female','Female')])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    location = StringField('Locaton: ', validators=[DataRequired()])
    bio = TextAreaField('About me: ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg','png','Images only'])
    ])

class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[InputRequired()])
    password = PasswordField('Password: ', validators=[InputRequired()])

class PostForm(FlaskForm):
    """docstring for PostForm."""

    userid = IntegerField('',validators=[InputRequired()])
    description = TextAreaField('Description: ', validators=[DataRequired()])
    photopost = FileField('Photo: ', validators=[FileRequired(),
        FileAllowed(['jpg','png','Images only'])
    ])
