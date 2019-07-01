FROM python:3.6.8-alpine

MAINTAINER Marcelo Cueto "cueto@live.cl"

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /web/requirements.txt

WORKDIR /web

RUN pip3 install -r requirements.txt

COPY . /web

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000" ]
