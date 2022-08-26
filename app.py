from flask import Flask, request, render_template, redirect, url_for, session
from uuid import uuid4
import json
import execute

"""
This is a flask program that executes bot functions through
a frontend interface. 

Author: AJ McCrory
Version: 4.0.1 8/25/2022
"""



app = Flask(__name__)
app.secret_key = str(uuid4())
@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['user']
        session['password'] = request.form['password']
        session['subreddit_name'] = request.form['subreddit_name']
        session['Number'] = request.form['Number']
        return redirect(url_for('vote_req'))



@app.route('/vote_req', methods=['GET', 'POST'])
def vote_req():
    if request.method == 'POST':
        session['client_id'] = request.form['client_id']
        session['client_secret'] = request.form['client_secret']
        return create_request()
    return render_template("credentials.html")

def create_request():
    render_template("creating.html")
    user_name = str(session['username'])
    password = str(session['password'])
    subreddit_name = str(session['subreddit_name'])
    Number = int(session['Number'])
    client_id = str(session['client_id'])
    client_secret = str(session['client_secret'])
    credentials = {
        "user_name": user_name,
        "password": password,
        "subreddit_name": subreddit_name,
        "Number": Number,
        "client_id": client_id,
        "client_secret": client_secret,
    }
    with open("credentials.json", "w") as jsonFile:
        json.dump(credentials, jsonFile)
    return redirect(url_for('perform'))

@app.route('/perform', methods=['GET', 'POST'])
def perform():
    if request.method == 'GET':
        execute.main_execution()
    else:
        return ('there seems to be a problem')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=65010)
