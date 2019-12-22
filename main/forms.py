from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, RadioField, DateField, IntegerField, FloatField, DecimalField
from wtforms.validators import InputRequired, Length

class ViewMachine(FlaskForm):
	choices = [('msn', 'Machine id'), ('cust', 'Customer'), ('company', 'Company')]
	options = SelectField('Field name', choices = choices, validators = [InputRequired()])
	search_by_field = StringField('Enter here', validators = [InputRequired()])
	submit = SubmitField('Enter')

class AddMachine(FlaskForm):
	machine_id = StringField('Machine Id', validators = [InputRequired()])
	choices = [('cust', 'Customer'), ('company', 'Company')]
	options = SelectField('Field name', choices = choices, 
		validators = [InputRequired()])
	search_by_field = StringField('Enter here', validators = [InputRequired()])
	submit = SubmitField('Enter')
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
