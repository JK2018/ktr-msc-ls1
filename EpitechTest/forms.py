from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

# Form for loggin in the app
class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Form to add a new user to the db
class NewUserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    companyName = StringField('Company name')
    emailAddress = StringField('Email Address')
    telephoneNumber = StringField('Telephone Number')
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Form to add new buisness cards for the user
class AddCard(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    companyName = StringField('Company name')
    emailAddress = StringField('Email Address')
    telephoneNumber = StringField('Telephone Number')
    submit = SubmitField('Add Card')