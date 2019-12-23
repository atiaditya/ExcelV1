from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateTimeField
from wtforms.validators import InputRequired, Length
from wtforms.fields.html5 import DateTimeField, DateField, TimeField

'''class MachineForm(FlaskForm):
	machine_serial_number= StringField('Machine Serial no', validators = [InputRequired(), Length(min=5,max=20)])
	register = SubmitField('Register')
	enter = SubmitField('Enter')

class InsertService(FlaskForm):
	challan =  StringField('Challan', validators = [InputRequired()])
	qty =  StringField('Quantity', validators = [InputRequired()])
	yeild = TextAreaField('Yield', validators = [InputRequired()])
	remarks = StringField('Remarks')
	exec_name = StringField('Engineer', validators = [InputRequired()])
	prev_mtr_rdng = StringField('Previous Meter Reading', validators = [InputRequired()])
	present_mtr_rdng =  StringField('Present Meter Reading', validators = [InputRequired()])
	submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
	customer = StringField('Customer Name', validators = [InputRequired()])
	#msn = StringField('Machine Serial Number', validators = [InputRequired()])
	address = StringField('Address', validators = [InputRequired()])
	phn = StringField('Phone Number', validators = [InputRequired()])
	make_model = StringField('Make And Model', validators = [InputRequired()])
	install_date = StringField('Install Date', validators = [InputRequired()])
	per_copy_charges = StringField('Per Copy Charges', validators = [InputRequired()])
	submit = SubmitField('Submit')'''

class CallLogForm(FlaskForm):
	customer_name = StringField('Customer Name', validators = [InputRequired()])
	phone_no = StringField('Phone Number', validators = [InputRequired()])
	call_type = StringField('Call Type', validators = [InputRequired()])
	#model_no = StringField('Model Number', validators = [InputRequired()])
	call_reason = StringField('Call Reason', validators = [InputRequired()])
	present_mtr_rdg = StringField('Meter Reading', validators = [InputRequired()])
	call_time = TimeField('Call Time', format = '%Y-%m-%d')
	engineer_name = StringField('Engineer Name', validators = [InputRequired()])
	remarks = TextAreaField('Remarks')
	submit = SubmitField('Submit')