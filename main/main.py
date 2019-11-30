from flask import Flask, render_template, requests
from forms import MachineForm, InsertService

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f5a117a3ab54a2f5476857b652a0c8a6'

@app.route('/', methods = ['GET', 'POST'])

def index():
	form = MachineForm()
<<<<<<< HEAD
	return render_template('home.html', form=form)

@app.route('/insertservice', methods = ['GET', 'POST'])
def insert_service():
	form = InsertService()
	if(form.validate_on_submit()):
		print(requests)
	return render_template('insert_service.html', form=form)

if(__name__ == '__main__'):
	app.run(debug=True)
=======
	return render_template('index.html', form=form)
		
@app.route('/4options', methods = ['GET','POST'])
def options():
	return render_template('options.html')

if(__name__ == '__main__'):
	app.run()
>>>>>>> 41dd210aa50aaed3a1c5d1dc2c83d94cb522448c
