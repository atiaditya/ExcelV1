from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField, DateField, IntegerField, FloatField, DecimalField, TimeField, TextAreaField
from wtforms.validators import InputRequired, Length
from wtforms.fields.html5 import DateTimeField, DateField, TimeField

class GetMI(FlaskForm):
	machine_id = StringField('Machine Id', validators = [InputRequired()])
	submit = SubmitField('login')

class GetCI(FlaskForm):
	choices = [('customer', 'Customer'), ('company', 'Company')]
	options = SelectField('Select Field', choices = choices, validators = [InputRequired()])
	search_by_field = StringField('', validators = [InputRequired()])
	submit = SubmitField('enter')

class GetMIByCI(FlaskForm):
	submit = SubmitField('login')

class AddMachine(FlaskForm):
	machine_id = StringField('Machine Id', validators = [InputRequired()])
	make = StringField('Make', validators = [InputRequired()])
	model = StringField('Model', validators = [InputRequired()])
	from_date = DateField('From', validators = [InputRequired()])
	to_date = DateField('To', validators = [InputRequired()])
	type_of_contract = StringField('Type of Contract', 
		validators = [InputRequired()])
	amcv = IntegerField('AMCV', validators = [InputRequired()])
	warranty = IntegerField('Warranty', validators = [InputRequired()])
	initial_meter = IntegerField('Initial meter', 
		validators = [InputRequired()])
	free_copies = IntegerField('Free Copies', 
		validators = [InputRequired()])
	per_copy_charges = DecimalField('Per Copy Charges',
		validators = [InputRequired()])

class AddCustomer(FlaskForm):
	company1 = StringField('Company1', validators = [InputRequired()])
	company2 = StringField('Company2')
	customer1 = StringField('Customer1', validators = [InputRequired()])
	customer2 = StringField('Customer2')
	phn = StringField('Phone no', validators = [InputRequired()])
	landline = StringField('Landline')
	email = StringField('Email')
	submit = SubmitField('Submit')

class AddService(FlaskForm):
	docket_no = IntegerField('Docket no', validators = [InputRequired()])
	challan = StringField('Challan', validators = [InputRequired()])
	prev_mtr_rdg = DecimalField('Previous meter reading', validators = [InputRequired()])
	present_mtr_rdng = DecimalField('Present meter reading', validators = [InputRequired()])
	yield_ = DecimalField('Yield', validators = [InputRequired()])
	engineer_id = IntegerField('Engineer id')
	time_dispatched = TimeField('Time Dispatched', validators = [InputRequired()])
	time_arrived = TimeField('Time Arrived', validators = [InputRequired()])
	ccd = DateField('CCD', validators = [InputRequired()])
	symptom = StringField('Symptom', validators = [InputRequired()])
	cause = StringField('Cause', validators = [InputRequired()])
	action = StringField('Action', validators = [InputRequired()])

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

class ScnForm(FlaskForm):
	time_dispatched = TimeField('Time Dispatched', validators = [InputRequired()])
	time_arrived = TimeField('Time Arrived', validators = [InputRequired()])
	ccd = DateField('CCD', validators = [InputRequired()])
	symptom = StringField('Symptom', validators = [InputRequired()])
	cause = StringField('Cause', validators = [InputRequired()])
	Action = StringField('Action', validators = [InputRequired()])