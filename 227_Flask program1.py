from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, I am abhishank"

@app.route("/abhi")
def dello():
    return "Hello, I am learning data science"

app.run(debug = True)