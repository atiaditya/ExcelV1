from flask import Flask, render_template
from forms import MachineForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f5a117a3ab54a2f5476857b652a0c8a6'

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
	form = MachineForm()
	return render_template('home.html', form=form)
if(__name__ == '__main__'):
	app.run()