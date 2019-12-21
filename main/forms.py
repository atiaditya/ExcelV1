from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length

class ViewMachine(FlaskForm):
	choices = [('msn', 'Machine id'), ('cust', 'Customer'), ('company', 'Company')]
	options = SelectField('Field name', choices = choices, validators = [InputRequired()])
	search_by_field = StringField('Enter your machine id', validators = [InputRequired()])
	enter = SubmitField('Enter')


'''
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
	msn = StringField('Machine Serial Number', validators = [InputRequired()])
	address = StringField('Address', validators = [InputRequired()])
	phn = StringField('Phone Number', validators = [InputRequired()])
	make_model = StringField('Make And Model', validators = [InputRequired()])
	install_date = StringField('Install Date', validators = [InputRequired()])
	per_copy_charges = StringField('Per Copy Charges', validators = [InputRequired()])
	submit = SubmitField('Submit')

class CallLog(FlaskForm):

	call_date = DateField('Call Date')
'''