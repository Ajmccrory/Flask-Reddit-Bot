# Reddit-Vote-Flask
This is a locally runnable Reddit bot built using flask that connects to a webserver and Reddit's API. This bot allows the user to perform different Reddit actions for the purpose of building Karma. This was designed for corporate use for a private client.
- [Build](#build)
- [Usage](#usage)
- [FAQ](#faq)



## Build
Build the Docker image manually by cloning the Git repo, and set up the venv with the necessary dependencies.
```
$ git clone https://github.com/Ajmccrory/Red-Vote-Flask
$ cd Red-Vote-Flask
$ python3 -m venv venv
$ source venv/bin/activate
$ sudo docker build -t reddit-flask .
```
### Create Reddit-App
* The script should be created on the account you intend to use the bot with.
```
https://old.reddit.com/prefs/apps
```
* Scroll to bottom of page, and create a new app as a developer
* Make the app a personal use script
* Make the redirect URI http://<local container url>/perform
### Run the container
Create a container from the image.
```
$ sudo docker run reddit-flask
```
* Now visit http://<address from docker cli>
![run-in-cli](https://user-images.githubusercontent.com/93270610/191367840-6f040530-1265-4449-a601-38a8c3858aad.png)

## Usage

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
### or
* Simply exit the CLI window to stop processes.

## FAQ
* ERROR- "looks like you've been doing that a lot. Take a break for 9 minutes before trying again." on field 'ratelimit'
** This error is because the account was too new, try with an older account. Or exit the bot, and run again in 5 minutes.
* ERROR - prawcore.exceptions.ResponseException: recieved 401 HTTP response
** This error is indicates an authorization issue. Check your password, usernmae, client id, and client secret in your credentials.json to verify they are correct. If they are correct, try installing praw inside of the venv and container the instance is running in.
