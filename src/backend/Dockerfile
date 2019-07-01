FROM ubuntu:18.04

MAINTAINER Marcelo Cueto "cueto@live.cl"

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /backend/requirements.txt

WORKDIR /backend

RUN pip3 install -r requirements.txt

COPY . /backend

EXPOSE 5001

# CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0", "--port=${PORT}" ]
CMD [ "flask", "run", "--host=0.0.0.0", "--port=5001" ]
