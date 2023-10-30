from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField
from wtforms.validators import InputRequired,Length,Email

class VehiclePlateForm(FlaskForm):
    VehiclePlate = StringField('Vehicle Plate', validators=[InputRequired(),Length(min=7, max=7)])
    submit = SubmitField('Search')

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    submit = SubmitField('Login')