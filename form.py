from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class VehiclePlateForm(FlaskForm):
    VehiclePlate = StringField('Vehicle Plate', validators=[InputRequired()])
    submit = SubmitField('Search')
