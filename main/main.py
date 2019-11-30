from flask import Flask, render_template, requests
from forms import MachineForm, InsertService

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f5a117a3ab54a2f5476857b652a0c8a6'

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
	form = MachineForm()
	return render_template('home.html', form=form)

@app.route('/insertservice', methods = ['GET', 'POST'])
def insert_service():
	form = InsertService()
	if(form.validate_on_submit()):
		print(requests)
	return render_template('insert_service.html', form=form)

if(__name__ == '__main__'):
	app.run(debug=True)