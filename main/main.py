from flask import Flask, render_template
from forms import MachineForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f5a117a3ab54a2f5476857b652a0c8a6'

@app.route('/', methods = ['GET', 'POST'])

def index():
	form = MachineForm()
	return render_template('index.html', form=form)
		
@app.route('/4options', methods = ['GET','POST'])
def options():
	return render_template('options.html')

if(__name__ == '__main__'):
	app.run()
