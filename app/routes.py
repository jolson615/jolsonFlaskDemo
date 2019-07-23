from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
    
@app.route('/results', methods = ['GET','POST'])
def results():
    print("RAW FORM DATA:")
    print(request.form)
    userdata = dict(request.form)
    print("PYTHON3 DICT DATA:")
    print(userdata)
    print("NICKNAME FROM MULTI-DICT:")
    print(request.form["nickname"])
    print("NICKNAME FROM DICTIONARY")
    print(userdata["nickname"])
    return "hello!"