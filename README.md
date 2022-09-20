# Reddit-Vote-Flask
Requested was a locally runable reddit bot with an easily accessible and adaptable Frontend. Python best communicates with Reddit's API, thus the Front end is written in Flask.

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/Ajmccrory/Red-Vote-Flask
$ docker build -t reddit-flask .
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
$ docker run --name my-container -d -p 65010:65010 reddit-flask
```
![app-homepage](https://user-images.githubusercontent.com/93270610/191359764-4656991e-cf0a-4686-a68c-72c360c9cd5a.png)

Now visit http://localhost:65010

### Use the bot
