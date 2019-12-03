from flask import Flask, render_template, request, redirect, url_for, flash, session
from forms import MachineForm, InsertService
from flask_pymongo import PyMongo

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
		'''
		if('Enter' in request.form):
			if(mongo.db.mrc.find_one({"machine_serial_number": msn})):
				return redirect(url_for('insert_service'))
			
		elif('Register' in request.form);
			return redirect(url_for('register'))
		'''
		return redirect(url_for('insert_service'))
	flash('Enter correct machine serial number')
	return render_template('index.html', form=form)

@app.route('/insert_service', methods = ['GET', 'POST'])
def insert_service():
	if('msn' in session):
		msn = session['msn']
		print(msn)
		mrc = mongo.db.mrc.find({"machine_serial_number": msn})
		session.pop('msn',None)
		form = InsertService()
		#print('insert ki ocham')
		if(form.validate_on_submit()):
			model = form.model.data
			engineer_name = form.engineer_name.data
			prev_mtr_rdng = form.prev_mtr_rdng.data
			present_mtr_rdng = form.present_mtr_rdng.data
			insert_row = {"machine_serial_number": msn, "model": model, "engineer_name": engineer_name, 
			"prev_mtr_rdng": prev_mtr_rdng, "present_mtr_rdng": present_mtr_rdng}
			#print('inserted')
			x = mongo.db.mrc.insert_one(insert_row)
			flash('Row added succesfully')
		return render_template('insert_service.html', form=form, title = "InsertService", mrc=mrc)
	else:
		return render_template('error_page.html')

'''
@app.route('/register', methods = ['GET', 'POST'])
def register():
	if('msn' in session):
		msn = session['msn']
		print(msn)
		mrc = mongo.db.mrc.find({"machine_serial_number": msn})
		session.pop('msn',None)
		form = InsertService()
		#print('insert ki ocham')
		if(form.validate_on_submit()):
			model = form.model.data
			engineer_name = form.engineer_name.data
			prev_mtr_rdng = form.prev_mtr_rdng.data
			present_mtr_rdng = form.present_mtr_rdng.data
			insert_row = {"machine_serial_number": msn, "model": model, "engineer_name": engineer_name, 
			"prev_mtr_rdng": prev_mtr_rdng, "present_mtr_rdng": present_mtr_rdng}
			#print('inserted')
			x = mongo.db.mrc.insert_one(insert_row)
			flash('Row added succesfully')
		return render_template('insert_service.html', form=form, title = "InsertService", mrc=mrc)
	else:
		return render_template('error_page.html')
'''

if(__name__ == '__main__'):
	app.run(debug=True)
		
