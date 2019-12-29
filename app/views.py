from flask import Flask, render_template, request, redirect, url_for, flash, session
from app import app
from app.forms import GetMI, GetCI, GetMIByCI, AddMachine, CallLog, AddService, AddCustomer
import psycopg2
import sqlalchemy as db
from sqlalchemy import *
from sqlalchemy.sql import select, and_, or_, not_

engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
conn = engine.connect()
meta = db.MetaData()

engineers = db.Table('engineers', meta, autoload = True, autoload_with = engine)
services = db.Table('services', meta, autoload = True, autoload_with = engine)
customers = db.Table('customers', meta, autoload = True, autoload_with = engine)
machines = db.Table('machines', meta, autoload = True, autoload_with = engine)
calls = db.Table('calls', meta, autoload =True, autoload_with = engine)


@app.route('/', methods = ['GET', 'POST'])
def index():
	form1 = GetMI()
	form2 = GetCI()
	display = []
	if(form1.validate_on_submit() and ('submit' in request.form)):

		if(request.form['submit'] == 'login'):

			session['machine_id'] = form1.machine_id.data
			return redirect(url_for('calllog'))


	elif(form2.validate_on_submit() and ('submit' in request.form)):
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

		if(request.form['submit'] == 'login'):
			try:
				machine_id = request.form['machines']
				session['machine_id'] = machine_id
				return redirect(url_for('calllog'))
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

		customer1 = form.customer1.data
		customer2 = form.customer2.data
		company1 = form.company1.data
		company2 = form.company2.data
		phone_no = form.phone_no.data
		landline = form.landline.data
		email = form.email.data
		ins = customers.insert().values(company1 = company1, company2 = company2, customer1 = customer1,
			customer2 = customer2, phone_no = phone_no, landline = landline, email = email)
		try:
			result = conn.execute(ins)
		except Exception as e:
			flash('Customer not inserted')

	return render_template('add_customer.html', form=form)

@app.route('/calllog', methods = ['GET', 'POST'])
def calllog():
	form = CallLog()
	call_records = []
	eng_records = []
	
	try:

		machine_id = session['machine_id']
		customer_id = session['customer_id']
		
		if(form.validate_on_submit()):

			print('inserting')

			call_id = form.call_id.data
			present_mtr_rdg = form.present_mtr_rdg.data
			engineer_id = request.form['engineers']
			call_time = form.call_time.data
			call_reason = form.call_reason.data
			region = form.region.data
			broken_call_code = form.broken_call_code.data
			broken_call_date = form.broken_call_date.data
			cmrs = form.cmrs.data
			remarks = form.remarks.data

			ins = calls.insert().values(call_id = call_id, customer_id= customer_id,
			 machine_id = machine_id, present_mtr_rdg = present_mtr_rdg, engineer_allocated_id = engineer_id,
			  call_time = call_time, call_reason = call_reason, region = region, broken_call_date = broken_call_date,
			   broken_call_code = broken_call_code, cmrs = cmrs, remarks = remarks)

			result = conn.execute(ins)

		elif(('submit' in request.form) and request.form['submit'] == 'enter'):
			print('entering')
			name = form.engineer_name.data
			st = select([engineers]).where(engineers.c.engineers_name == name)

			result = conn.execute(st)
			for row in result:
				eng_records.append(row)

			result.close()

		sel = select([calls]).where(calls.c.machine_id == machine_id)
		result = conn.execute(sel)

		for row in result:
			call_records.append(row)

		call_records = call_records[-3:]

		result.close()

	except KeyError as k:
		flash('Please go to homepage')
		
	return render_template('call_log.html', form = form, call_records = call_records, eng_records = eng_records)

@app.route('/scn', methods = ['GET', 'POST'])
def scn():
	form = AddService()
	m_id = session['machine_id']
	cust_id = session['customer_id']
	pre = {'machine_id': m_id, 'customer_id': cust_id}

	sel = select(
		[engineers]
	)
	result = conn.execute(sel)
	lis = []
	for row in result:
		lis.append(row)

	form.engineer_id.choices = lis

	if(form.validate_on_submit()):
		docket_no = form.docket_no.data
		ccd = form.ccd.data
		challan = form.challan.data
		present_mtr_rdg = form.present_mtr_rdg.data
		engineer_id = form.engineer_id.data
		time_dispatched = form.time_dispatched.data
		time_arrived = form.time_arrived.data
		symptom = form.symptom.data
		cause = form.cause.data
		action = form.action.data
		total_qty = 10
		total_cost = 1000
		remarks = form.remarks.data

		insert_query = services.insert().values(customer_id = cust_id, machine_id = m_id,
			docket_no = docket_no, ccd = ccd, challan = challan, present_mtr_rdg = present_mtr_rdg,
			engineer_id = engineer_id, time_dispatched = time_dispatched, time_arrived = time_arrived,
			symptom = symptom, cause = cause, action = action, total_qty =total_qty, total_cost = total_cost,remarks = remarks)

		try:
			result = conn.execute(insert_query)
		except:
			flash('Exception')

	return render_template('scn.html', form = form, pre = pre)


@app.route('/mrc', methods = ['GET', 'POST'])
def mrc():
	machine_id = session['machine_id']
	sel = select([services]).where(services.c.machine_id == machine_id)
	result = conn.execute(sel)
	display = []
	for row in result:
		display.append(row)

	return render_template('mrc.html', display = display)
