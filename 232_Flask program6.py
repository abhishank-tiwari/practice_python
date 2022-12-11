from flask import Flask , redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello , I am Abhishank"
	
@app.route('/<int:date>')
def hellod(date):
	return "date = %d" % date

@app.route('/student')
def student():
	return "Hello students"
    
 
@app.route('/faculty')
def faculty():
	return "Hello faculty"

@app.route('/user/<name>')
def user(name):
    
    if name == 'student':
        return redirect(url_for('student'))
    
    if name == 'faculty':
        return redirect(url_for('faculty'))


app.run(debug = True)