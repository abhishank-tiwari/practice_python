from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, I am abhishank"

@app.route("/<int:date>")
def hellod(date):
    return "date = %d" % date
    
@app.route("/abhi")
def dello():
    return "Hello, I am learning data science"
    
@app.route("/<name>")
def helloname(name):
    return "Hello  " + name
    
app.run(debug = True)