# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
@app.route('/')
@app.route('/index', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')
    
@app.route('/results', methods = ['GET', 'POST'])
def results():
    if request.method == "POST":
        print(request.form)
        user_name = request.form["first_name"]
        user_task1 = request.form["task1"]
        user_task2 = request.form["task2"]
        user_task3 = request.form["task3"]
        return render_template('results.html', user_name = user_name, user_task1 = user_task1, user_task2 = user_task2, user_task3 = user_task3)
    else:
        return "please fill out the form:"


