from flask import Flask, render_template, request, redirect, url_for, flash
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
		print(msn)
		if(mongo.db.mrc.find_one({"machine_serial_number": msn})):
			return redirect(url_for('insert_service'))
	flash('Enter correct machine serial number')
	return render_template('index.html', form=form)

@app.route('/insertservice', methods = ['GET', 'POST'])
def insert_service():
	form = InsertService()

	return render_template('insert_service.html', form=form)


if(__name__ == '__main__'):
	app.run(debug=True)
		
