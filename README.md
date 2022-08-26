*** current download/run process ***

--> download the flask app 

--> delete the example file for credentials and create your own credentials.json and submission.json



** Dependencies **

pip install flask

--> create the virtual enviornment

python3 -m venv venv

--> activate the virutal enviornment

source venv/bin/activate


** in venv dependencies **

pip install praw

pip install pickle

pip install requests


** to run the app **

flask run -p 65010

access on http://localhost:65010


** reddit credentials **

navigate to reddit.com/prefs/apps

create a reddit script app

copy and paste your client id and client secret into app when prompted








