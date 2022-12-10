from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello , I am Abhishank"
	
@app.route('/<int:date>')
def hellod(date):
	return "date = %d" % date
	
app.run(debug = True)