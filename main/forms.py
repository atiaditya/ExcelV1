from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class MachineForm(FlaskForm):
	machine_serial_number= StringField('Machine Serial no', 
		validators = [DataRequired(), Length(min=10,max=20)])
	submit = SubmitField('Submit')