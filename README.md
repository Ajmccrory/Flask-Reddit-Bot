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
$ docker run --name my-container -d -p 65010:65010 reddit-flask
```
* Now visit http://localhost:65010

![app-homepage](https://user-images.githubusercontent.com/93270610/191361501-282eebf2-729f-43a0-8572-1cdaaaced16a.png)

### Use the bot
* Fill out the bot with your reddit information used to set up your personal use script.
* I reccomend using FreeKarma4u, as a subreddit for the bot to search through.

![app-homepage-filled](https://user-images.githubusercontent.com/93270610/191362070-fe964e48-d5da-4fca-8b90-718ac0cb5afd.png)

* Fill out the vote request page with the Client ID and Secret obtained from the reddit app
![app-vote-req](https://user-images.githubusercontent.com/93270610/191362420-7d669df4-f88b-4797-a65a-80bbe4c4a62f.png)

The app will then begin to return information in the CLI
You can see the Karma return and comments appearing in your Reddit after the app has run.


