from flask import *

app = Flask(__name__)


@app.route('/home')
def index():
	return render_template('page1.html')


if(__name__ =="__main__"):
	app.run()