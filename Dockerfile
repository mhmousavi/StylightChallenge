FROM docker.repos.balad.ir/python:3.9


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update

RUN python -m pip install -r requirements.txt

COPY . /code/
