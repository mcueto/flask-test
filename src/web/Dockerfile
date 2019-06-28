FROM ubuntu:18.04

ENV FLASK_APP=hello_world.py MONGO_URI=mongodb://localhost:27017/flask-test

MAINTAINER Marcelo Cueto "cueto@live.cl"

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /web/requirements.txt

WORKDIR /web

RUN pip3 install -r requirements.txt

COPY . /web

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "hello_world.py" ]
