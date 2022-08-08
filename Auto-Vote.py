from flask import Flask, abort, request, render_template, redirect, url_for, session
from uuid import uuid4
import requests
import requests.auth
import urllib.parse
CLIENT_ID = "z1JXO0p5TF-W3I0q3LhE4Q"
CLIENT_SECRET = "6wPxWGoScMC93fIrIASUQC1fdWt19w,"
REDIRECT_URI = "http://localhost:65010/reddit_callback"
#might import these using a credentials.json call



def user_agent(ajmccrory1):
   #The user agent is used with the reddit API client information
    return "Auto-Vote by /u/%s" % ajmccrory1
    
    raise NotImplementedError()


def base_headers():
    #these should probably be updated to perform more complex api calls
    return {"User-Agent": user_agent()}



app = Flask(__name__)
app.secret_key = CLIENT_SECRET  #needed to create session
@app.route('/')
def homepage():
    authurl =  make_authorization_url()
    return render_template("index.html", content=authurl)


def make_authorization_url():
    #the authorization link on homepage
    state = str(uuid4())
    save_created_state(state)
    params = {"client_id": CLIENT_ID,
                    "response_type": "code",
                    "state": state,
                    "redirect_uri": REDIRECT_URI,
                    "duration": "temporary",
                    "scope": "identity, mysubreddits, read, vote"}
    url = "https://ssl.reddit.com/api/v1/authorize?" + urllib.parse.urlencode(params)
    session['oauth2_state'] = state
    return url


#session state saved to memcache
def save_created_state(state):
        state = request.args.get('state')
        session.pop('oauth2_state', state)
        return save_created_state

#checks validity of state
#this should be replaced with a database check
def is_valid_state(state):
    error = request.args.get('error', '')
    if state != 0:
        return True
    if error:
        return "Error: " + error



#where reddit will return information
@app.route('/reddit_callback')
def reddit_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    state = request.args.get('state', '')
    if not is_valid_state(state):
        #if this request wasn't started by me
        abort(403)
    return redirect(url_for('landing'))


def get_token(code):
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "authorization_code",
                 "code": code,
                 "redirect_uri": REDIRECT_URI}
    headers = base_headers()
    response = requests.post("https://ssl.reddit.com/api/v1/access_token",
                             auth=client_auth,
                             headers=headers,
                             data=post_data)
    token_json = response.json()
    #trying to save more information in session to see if that allows me to perform belated actions
    session["access_token"] = token_json
    return token_json["access_token"]

    
def get_username(access_token):
    headers = base_headers()
    headers.update({"Authorization": "bearer " + access_token})
    response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
    me_json = response.json
    #save user identity in session
    session["identity"] = me_json
    return me_json



@app.route('/landing', methods=['GET', 'POST'])
def landing():
    if request.method == 'POST':
        session['request'] = request.form['request']
    return redirect(url_for('get_karma'))
        


@app.route('/get_karma')
def get_karma(access_token):
    headers = base_headers()
    headers.update({"Authorization": "bearer " + access_token})
    response = requests.get("https://oauth.reddit.com/api/v1/me/karma", headers=headers)
    karma_json = response.json()
    #karma isn't saved in session because it is directly displayed on page
    return redirect(url_for("user", karma=karma_json))


@app.route('/user')
def user():
    context = get_karma()
    identity = get_username()
    return render_template("user.html", context=context, identity=identity)



if __name__ == '__main__':
    app.run(debug=True, port=65010)
