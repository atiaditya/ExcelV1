from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length

class MachineForm(FlaskForm):
	machine_serial_number= StringField('Machine Serial no', 
		validators = [InputRequired(), Length(min=5,max=20)])
	register = SubmitField('Register')
	enter = SubmitField('Enter')

class InsertService(FlaskForm):
	challan =  StringField('Challan', validators = [InputRequired()])
	prev_mtr_rdng = StringField('Previous Meter Reading', validators = [InputRequired()])
	present_mtr_rdng =  StringField('Present Meter Reading', validators = [InputRequired()])
	qty =  StringField('Quantity', validators = [InputRequired()])
	yeild = StringField('Yield', validators = [InputRequired()])
	exec_name = StringField('Engineer', validators = [InputRequired()])
	remarks = TextAreaField('Remarks', )
	submit = SubmitField('Submit')
