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
	search_by_field = StringField('Enter name', validators = [InputRequired()])
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
	phone_no = StringField('Phone no', validators = [InputRequired()])
	landline = StringField('Landline')
	email = StringField('Email')
	submit = SubmitField('Submit')

class AddService(FlaskForm):
	customer_id = StringField('Customer ID', validators = [InputRequired()])
	call_id = StringField('Call ID', validators = [InputRequired()])
	machine_id = StringField('Machine ID', validators = [InputRequired()])
	docket_no = IntegerField('Docket no', validators = [InputRequired()])
	ccd = DateField('CCD', validators = [InputRequired()])
	challan = StringField('Challan', validators = [InputRequired()])
	present_mtr_rdg = DecimalField('Present meter reading', validators = [InputRequired()])
	engineer_id = SelectField('Engineer', coerce = int, validators = [InputRequired()])
	time_dispatched = TimeField('Time Dispatched', validators = [InputRequired()])
	time_arrived = TimeField('Time Arrived', validators = [InputRequired()])
	symptom = TextAreaField('Symptom', validators = [InputRequired()])
	cause = TextAreaField('Cause', validators = [InputRequired()])
	action = TextAreaField('Action', validators = [InputRequired()])
	remarks = TextAreaField('Remarks')
	submit = SubmitField('Submit')

class CallLog(FlaskForm):
	call_id = StringField('Call Id', validators = [InputRequired()])
	present_mtr_rdg = DecimalField('Present meter reading', )
	engineer_name = StringField('Engineer name', validators = [InputRequired()])
	submit = SubmitField('enter')
	call_time = TimeField('Call Time', validators = [InputRequired()])
	call_reason = TextAreaField('Call reason')
	region = StringField('Region', validators = [InputRequired()])
	broken_call_date = DateField('Broken call date')
	broken_call_code = StringField('Broken call code')
	cmrs = DecimalField('cmrs')
	remarks = TextAreaField('Remarks')