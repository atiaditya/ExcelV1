from flask import Flask, render_template, request, redirect, url_for, flash, session
from forms import MachineForm, InsertService, RegisterForm, CallLogForm
from flask_pymongo import PyMongo
from bson import objectid

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f5a117a3ab54a2f5476857b652a0c8a6'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/test'

mongo = PyMongo(app)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
	form = MachineForm()
	if(form.validate_on_submit()):
		msn = form.machine_serial_number.data
		#print(msn)
		session['msn'] = msn
		#print(request.form.keys())
		if('enter' in request.form):
			if(mongo.db.MRCObject.find_one({"msn": msn})):
				#print('vachindi roy')
				return redirect(url_for('call_log'))
			
		elif('register' in request.form):
			return redirect(url_for('register'))

	#flash('Enter correct machine serial number')
	return render_template('index.html', form=form)

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

@app.route('/register', methods = ['GET', 'POST'])
def register():
	form = RegisterForm()
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

@app.route('/call_log', methods = ['GET', 'POST'])
def call_log():
	form = CallLogForm()
	return render_template('call_log.html', form = form)
	#if(form.validate_on_submit()):

		

if(__name__ == '__main__'):
	app.run(debug=True)
		
