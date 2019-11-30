from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

class MachineForm(FlaskForm):
	machine_serial_number= StringField('Machine Serial no', 
		validators = [InputRequired(), Length(min=10,max=20)])
	submit = SubmitField('Submit')

class InsertService(FlaskForm):
	model = StringField('Model', validators = [InputRequired()])
	engineer_name = StringField('Engineer', validators = [InputRequired()])
	prev_mtr_rdng = StringField('Previous Meter Reading', validators = [InputRequired()])
	present_mtr_rdng =  StringField('Present Meter Reading', validators = [InputRequired()])
	submit = SubmitField('Submit')
