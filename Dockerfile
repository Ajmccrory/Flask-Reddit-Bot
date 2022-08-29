# syntax=docker/dockerfile:1
FROM python:3.8-alpine

# copy the requirements file into image
COPY ./requirements.txt /app/requirements.txt

# switch to working dir
WORKDIR /app

# install dependencies and packages
RUN pip install -r requirements.txt

# copy from local to image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD [ "python3", "-m", "flask", "run", "-p", "65010", "--host=0.0.0.0"]
