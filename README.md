# Reddit-Vote-Flask
Requested was a locally runable reddit bot with an easily accessible and adaptable Frontend. Python best communicates with Reddit's API, thus the Front end is written in Flask.

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/Ajmccrory/Red-Vote-Flask
$ docker build -t python/docker .
```
### Create Reddit-App
```
https://old.reddit.com/prefs/apps
```
* scroll to bottom of page, and create a new app as a developer
* Make the app a personal use script
* Make the redirect URI http://localhost:65010/perform

### Run the container
Create a container from the image.
```
$ 
```

Now visit http://localhost:65010

### Use the bot
