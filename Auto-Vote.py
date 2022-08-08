from flask import Flask, abort, request, render_template, redirect, url_for, session
from uuid import uuid4
import requests
import requests.auth
import urllib.parse
CLIENT_ID = "z1JXO0p5TF-W3I0q3LhE4Q"
CLIENT_SECRET = "6wPxWGoScMC93fIrIASUQC1fdWt19w,"
REDIRECT_URI = "https://localhost:65010/reddit_callback"

session["user_state"] = "none"

def user_agent(ajmccrory1):
    '''
    The user agent is used with the reddit API client information
    '''
    return "Auto-Vote by /u/%s" % ajmccrory1
    
    raise NotImplementedError()

def base_headers():
    return {"User-Agent": user_agent()}

app = Flask(__name__)
@app.route('/index')
def index():
    authurl =  make_authorization_url()
    return render_template("index.html", content=authurl)

def make_authorization_url():
    from uuid import uuid4
    state = str(uuid4())
    save_created_state(state)
    params = {"client_id": CLIENT_ID,
                    "response_type": "code",
                    "state": state,
                    "redirect_uri": REDIRECT_URI,
                    "duration": "temporary",
                    "scope": "identity, mysubreddits, read, vote"}
    url = "https://ssl.reddit.com/api/v1/authorize?" + urllib.parse.urlencode(params)
    return url

#these are empty now, but need to be updated later to store session state in db or memcache
def save_created_state(state):
    session.pop("user_state", state)
    return redirect(url_for("reddit_callback"))
def is_valid_state(state):
    return True

@app.route('/reddit_callback')
def reddit_callback():
    error = request.args.get('error', '')
    if error:
        return "Error: " + error
    state = request.args.get('state', '')
    if not is_valid_state(state):
        #if this request wasn't started by me
        abort(403)
    code = request.args.get('code')
    access_token = get_token(code)
    #PLEASE STORE THIS IN A SESSION JESUS CHRIST
    user = get_username(access_token)
    return render_template("reddit_callback.html", context=user)


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
    return token_json["access_token"]
    
def get_username(access_token):
    headers = base_headers()
    headers.update({"Authorization": "bearer " + access_token})
    response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
    me_json = response.json()
    return me_json['name']



if __name__ == '__main__':
    app.run(debug=True, port=65010)