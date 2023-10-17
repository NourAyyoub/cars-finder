from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired,Length

class VehiclePlateForm(FlaskForm):
    VehiclePlate = StringField('Vehicle Plate', validators=[InputRequired(),Length(min=7, max=7)])
    submit = SubmitField('Search')
