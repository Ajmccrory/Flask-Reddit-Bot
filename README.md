# Reddit-Vote-Flask
Requested was a locally runable reddit bot with an easily accessible and adaptable Frontend. Python best communicates with Reddit's API, thus the Front end is written in Flask.

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/Ajmccrory/Red-Vote-Flask
$ docker build -t reddit-flask .
```
### Create Reddit-App
* The script should be created on the account you intend to use the bot with.
```
https://old.reddit.com/prefs/apps
```
* Scroll to bottom of page, and create a new app as a developer
* Make the app a personal use script
* Make the redirect URI http://localhost:65010/perform
### Run the container
Create a container from the image.
```
$ docker run <name of container>
```
* Now visit http://172.17.0.3:5000
![run-in-cli](https://user-images.githubusercontent.com/93270610/191367840-6f040530-1265-4449-a601-38a8c3858aad.png)

### Use the bot

![app-homepage](https://user-images.githubusercontent.com/93270610/191361501-282eebf2-729f-43a0-8572-1cdaaaced16a.png)

* Fill out the bot with your reddit information used to set up your personal use script.
* I reccomend using FreeKarma4u, as a subreddit for the bot to search through.

![app-homepage-filled](https://user-images.githubusercontent.com/93270610/191364902-2b3914f1-23d0-4f5a-b65b-72dfb432f6c4.png)

* Fill out the vote request page with the Client ID and Secret obtained from the reddit app

![app-vote-req](https://user-images.githubusercontent.com/93270610/191364934-42a969bf-9775-4591-891e-912ced2bc0d3.png)

* The app will then begin to return information in the CLI
* You can see the Karma return and comments appearing in your Reddit after the app has run.
### To stop
* open a seperate terminal window and execute the following command
```
$ docker stop <name of container>
```


