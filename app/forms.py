from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import *
from wtforms.validators import DataRequired, Email

class SignUpForm(FlaskForm):
    firstname = StringField('First Name: ', validators=[DataRequired()])
    lastname = StringField('Last Name: ', validators=[DataRequired()])
    gender = SelectField('Gender: ', choices = [('Male','Male'),('Female','Female')])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    location = StringField('Locaton: ', validators=[DataRequired()])
    bio = TextAreaField('About me: ', validators=[DataRequired()])
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg','png','Images only'])
    ])
