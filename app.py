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

@app.route('/results', methods=['GET', 'POST'])
def results():
  category = request.form['category']
  location = request.form['location']
  if request.method == 'GET':
    return "Here are your results"
  else: 
    return f"Here are {category} volunteering opportunities in {location}!"
  

app.run(host='0.0.0.0', port=81, debug=True)