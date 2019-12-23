from flask import Flask, render_template, request, redirect, url_for, flash, session
from forms import GetMI, GetCI, GetMIByCI, AddMachine, CallLogForm
import psycopg2
import sqlalchemy as db
from sqlalchemy import *
from sqlalchemy.sql import select, and_, or_, not_

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f5a117a3ab54a2f5476857b652a0c8a6'

conn_string = 'postgresql+psycopg2://postgres:kamesh11@localhost/excel'
engine = db.create_engine(conn_string)
conn = engine.connect()
meta = MetaData()

engineers = db.Table('engineers', meta, autoload = True, autoload_with = engine)
services = db.Table('services', meta, autoload = True, autoload_with = engine)
customers = db.Table('customers', meta, autoload = True, autoload_with = engine)
machines = db.Table('machines', meta, autoload = True, autoload_with = engine)
call_log = db.Table('call_log', meta, autoload =True, autoload_with = engine)

@app.route('/', methods = ['GET', 'POST'])
def index():
	form1 = GetMI()
	form2 = GetCI()
	display = []
	if(form1.validate_on_submit() and ('submit' in request.form)):

		if(request.form['submit'] == 'login'):

			session['machine_id'] = form1.machine_id.data
			return redirect(url_for('call_log'))


	elif(form2.validate_on_submit() and ('submit' in request.form)):
		print('hii')
		if(request.form['submit'] == 'enter'):

			choice = form2.options.data
			display = []
			name = form2.search_by_field.data

			sel = select(
				[customers]
			)

			if(choice == 'customer'):

				st = sel.where( 
						customers.c.customer1 == name
					)
			else:
				st = sel.where( 
						customers.c.company1 == name
				)

			result = conn.execute(st)
			for row in result:
				display.append(row)

			result.close()

	return render_template('index.html', form1 = form1, form2 = form2, display = display)

@app.route('/get_mi_by_ci', methods = ['GET', 'POST'])
def get_mi_by_ci():

	form = GetMIByCI()
	display = []
	if('customers' in request.form):
		customer_id = request.form['customers']
		session['customer_id'] = customer_id
		st = select(
			[machines]
		).where(machines.c.customer_id == customer_id)

		result = conn.execute(st)
		for row in result:
			display.append(row)

		result.close()

	elif('submit' in request.form):
		if(request.form['submit'] == 'submit'):
			try:
				machine_id = request.form['machines']
				session['machine_id'] = machine_id
				return redirect(url_for('call_log'))
			except KeyError as k:
				flash('Please select a machine')

		elif(request.form['submit'] == 'Add Machine'):
			return redirect(url_for('add_machine'))

	return render_template('get_mi_by_ci.html', form = form, display = display)


@app.route('/add_machine', methods = ['GET', 'POST'])
def add_machine():

	form = AddMachine()
	if(form.validate_on_submit()):
		try:
			print('entered')
			customer_id = session['customer_id']
			session.pop('customer_id')
			machine_id = form.machine_id.data
			make = form.make.data
			model = form.model.data
			from_date = form.from_date.data
			to_date = form.from_date.data
			type_of_contract = form.type_of_contract.data
			amcv = form.amcv.data
			warranty = form.warranty.data
			initial_meter = form.initial_meter.data
			free_copies = form.free_copies.data
			per_copy_charges = form.per_copy_charges.data
			ins = machines.insert().values(machine_id = machine_id, customer_id = customer_id, 
			make = make,model = model, from_date = from_date, type_of_contract = type_of_contract,
			amcv = amcv, to_date = to_date, warranty = warranty,free_copies = free_copies,
			initial_meter = initial_meter, per_copy_charges = per_copy_charges)
			
			try:
				result = conn.execute(ins)
			except:
				print('There is exception')

		except KeyError as k:

			flash('Please select a customer')
			
	return render_template('add_machine.html', form = form)


@app.route('/add_customer', methods = ['GET', 'POST'])
def add_customer():

	form = AddCustomer()
	if(form.validate_on_submit()):
		customer_name = form.customer.data
		machine_serial_number = form.msn.data
		address = form.address.data
		phone = form.phn.data
		make_model = form.make_model.data
		instal_date = form.install_date.data
		per_copy_charges = form.per_copy_charges.data
		services = []

		insert_row = {"msn": machine_serial_number, "customer": customer_name, "address": address, "phn": phone, 
						"make_model": make_model, "install_date": instal_date, "per_copy_charges": per_copy_charges, "services": services}

		x = mongo.db.MRCObject.insert_one(insert_row)
		flash('Entered succesfully')
		return redirect(url_for('register'))

	return render_template('register_form.html', form = form, title = "RegisterForm")

@app.route('/calllog', methods = ['GET', 'POST'])
def calllog():
	try:
		m_id = '103'
		#m_id = request.form['machines']
		form = CallLogForm()

		sel = select(
			[call_log.c.call_date, customers.c.customer1, call_log.c.engineer_id, 
				engineers.c.engineer_name, call_log.c.present_mtr_rdg,
					services.c.docket_no]
		)

		st = sel.where(
			and_(
				call_log.c.machine_id == m_id,
				call_log.c.engineer_id == engineers.c.engineer_id,
				call_log.c.customer_id == customers.c.customer_id,
				call_log.c.call_id == services.c.call_id
			)
		)

		result = conn.execute(st)
		display = []
		for row in result:
			display.append(row)

		print(display)
		print(len(display))
		print(display[-3:])
		res = display[-3:]

	except KeyError as e:
		flash('Home page ki dobbey')
		
	return render_template('call_log.html', form = form, res = res)

if(__name__ == '__main__'):
	app.run(debug=True)
		
