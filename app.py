from flask import Flask, abort, request, render_template, redirect, url_for, session
from uuid import uuid4
import reddit_client
import json

app = Flask(__name__)
app.secret_key = str(uuid4())
@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        session['redditor'] = request.form['redditor']
        session['Number'] = request.form['Number']
        return redirect(url_for('vote_req', session=session))

    return render_template("index.html")


@app.route('/vote_req', methods=['GET', 'POST'])
def vote_req():
    if request.method == 'POST':
        return redirect(url_for('get_credentials', session=session))
    if 'username' not in session:
        return redirect(url_for('homepage'))

@app.route('/get_credentials',methods=['GET','POST'])
def get_credentials():
    render_template("credntials.html")
    if request.method == 'POST':
        session['client_id'] = request.form['client_id']
        session['client_secret'] = request.form['client_secret']
        return create_request(session)

def create_request():
    render_template("creating.html")
    user_name = str(session['username'])
    password = str(session['password'])
    redditor = str(session['redditor'])
    Number = int(session['Number'])
    client_id = str(session['client_id'])
    client_secret = str(session['client_secret'])
    user_agent = "Auto-Vote by /u/%s" % user_name
    credentials = {
        "user_name": user_name,
        "password": password,
        "redditor": redditor,
        "Number": Number,
        "client_id": client_id,
        "client_secret": client_secret,
        "user_agent": user_agent,
    }
    with open("credentials.json", "w") as jsonFile:
        json.dump(credentials, jsonFile)
    return redirect(url_for('perform_actions'))


@app.route('/perform_actions')
def perform_actions():
    render_template("performing.html")
    return reddit_client.main()

@app.route('/actions_performed', methods=['POST'])
def actions_performed():
    render_template("performed.html")
    if request.form['continue'] == True:
        print('running again')
        return reddit_client.main()

    return render_template("thank.html")
        
if __name__ == '__main__':
    app.run(debug=True, port=65010)
