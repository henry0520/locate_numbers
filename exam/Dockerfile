FROM python:3.8.2
WORKDIR /opt/exam
RUN apt-get update && apt-get install build-essential openssl libssl-dev python3-dev -y

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /opt/exam/

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requires/base.pip
