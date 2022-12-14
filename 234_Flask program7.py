from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, I am abhishank"

@app.route("/abhi")
def dello():
    return "<html><body><h1>Hello, I am learning data science<h1><body><html>"
    
#@app.route("/<name>")
#def helloname(name):
#    return "Hello  " + name
    
app.run(debug = True)