# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /reddit-flask

COPY requirements.txt requirements.txt

RUN pip3 install praw

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
