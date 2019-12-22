from flask import Flask, render_template, request, redirect, url_for, flash, session
from forms import ViewMachine, AddMachine
import psycopg2
import sqlalchemy as db
from sqlalchemy import *
from sqlalchemy.sql import select, and_, or_, not_

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f5a117a3ab54a2f5476857b652a0c8a6'
conn_string = 'postgresql+psycopg2://postgres:aditya123@localhost/excel'

engine = db.create_engine(conn_string)
conn = engine.connect()
meta = MetaData()

customers = db.Table('customers', meta, autoload = True, autoload_with = engine)
machines = db.Table('machines', meta, autoload = True, autoload_with = engine)

@app.route('/', methods = ['GET', 'POST'])
def index():
	form1 = ViewMachine()
	display = []
	if(form1.validate_on_submit() and request.form['submit'] == 'Enter'):

		choice = form1.options.data
		display = []

		if(choice == 'msn'):
			return redirect(url_for('call_log'))

		else:
			name = form1.search_by_field.data

			sel = select(
				[customers.c.customer_id, customers.c.company1,
			 	machines.c.machine_id, machines.c.make, machines.c.model]
			)

			if(choice == 'cust'):

				st = sel.where( 
					and_(
						customers.c.customer1 == name, 
						customers.c.customer_id == machines.c.customer_id
					)
				)
			else:
				st = sel.where( 
					and_(
						customers.c.company1 == name, 
						customers.c.customer_id == machines.c.customer_id
					)
				)

			result = conn.execute(st)
			display = []
			for row in result:
				display.append(row)

			result.close()

	return render_template('index.html', form1 = form1, display = display)


@app.route('/add_machine', methods = ['GET', 'POST'])
def add_machine():

	form = AddMachine()
	display = []
	if('submit' in request.form and request.form['submit'] == 'Enter'):
		print(form.submit.data)
		choice = form.options.data
		if(choice == 'cust'):

			name = form.search_by_field.data
			sel = select([customers]).where(customers.c.customer1 == name)

			result = conn.execute(sel)
			for row in result:
				display.append(row)

			result.close()
		
		else:

			name = form.search_by_field.data
			sel = select([customers]).where(customers.c.company1 == name)

			result = conn.execute(sel)
			for row in result:
				display.append(row)

			result.close()

	elif('submit' in request.form and request.form['submit'] == 'Submit'):

		try:
			customer_id = request.form['customers']
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
			result = conn.execute(ins)

		except KeyError as k:

			flash('Please select a customer')
			
	return render_template('add_machine.html', form = form, display = display)



'''
@app.route('/call_log', methods = ['GET', 'POST'])
def call_log():

	form = CallLog()
	machine_id = request.form['machines']
	if(form.validate_on_submit() and form.submit.data):

@app.route('/insert_service', methods = ['GET', 'POST'])
def insert_service():
	#print(session)
	if('msn' in session):
		msn = session['msn']
		#print(msn,'this is insert page')
		#print(mrc['services'])
		form = InsertService()
		#print('insert ki ocham')
		mrc = mongo.db.MRCObject.find_one({"msn": msn})
		services = mongo.db.ServiceObject.find({"_id": { "$in" : mrc['services'] } })
		print('HI')
		if(form.validate_on_submit()):
			#session.pop('msn',None)
			id = objectid.ObjectId()
			challan = form.challan.data
			prev_mtr_rdng = form.prev_mtr_rdng.data
			present_mtr_rdng = form.present_mtr_rdng.data
			qty = form.qty.data
			yeild = form.yeild.data
			exec_name = form.exec_name.data
			remarks = form.remarks.data
			row = {"_id": id, "challan": challan, "prev_mtr_rdng": prev_mtr_rdng,
			"present_mtr_rdng": present_mtr_rdng, "qty": qty,
			 "yield": yeild, "exec_name": exec_name, "remarks": remarks}
			print('inserted')
			x = mongo.db.ServiceObject.insert_one(row)
			#print(x, 'hey hi')
			mongo.db.MRCObject.update({"msn": msn}, { "$addToSet" : { "services": id } })
			#flash('Row added succesfully')
			services = mongo.db.ServiceObject.find({"_id": { "$in" : mrc['services'] } })
			return redirect(url_for('insert_service'))
		return render_template('insert_service.html', form=form, title = "InsertService", services=services)
	else:
		return render_template('error_page.html')
'''


if(__name__ == '__main__'):
	app.run(debug=True)
		
