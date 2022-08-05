# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import volunteer

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods=['GET', 'POST'])
def results():
  # category = request.form['category']
  # location = request.form['location']
  # if request.method == 'GET':
  #   return "Here are your results"
  # else: 
  #   return f"Here are {category} volunteering opportunities in {location}!"

  
  user_input = request.form
  choice = volunteer(user_input['location'], user_input['category'])
  user_info = {
    'location': user_input['location'],
    'category': user_input['category'],
    'opportunities': choice
  }

  return render_template('results.html', user_info=user_info)
  
app.run(host='0.0.0.0', port=81, debug=True)