# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results')
def results():
    return render_template("results.html")


app.run(host='0.0.0.0', port=81, debug=True)