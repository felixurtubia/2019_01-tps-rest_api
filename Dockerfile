FROM python:3.7-alpine
MAINTAINER Felix Urtubia Carrasco

ENV PYTHONUNBUFFERED 1


WORKDIR .




COPY ./requirements.txt /requirements.txt
COPY ./api.py /api.py

RUN pip install -r requirements.txt

