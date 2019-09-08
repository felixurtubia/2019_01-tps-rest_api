FROM python:3.7-alpine
MAINTAINER Felix Urtubia Carrasco

ENV PYTHONUNBUFFERED 1


WORKDIR .


RUN apk update && apk add libpq
RUN apk add --virtual .build-deps gcc python-dev musl-dev postgresql-dev



COPY ./requirements.txt /requirements.txt
COPY ./api.py /api.py

RUN pip install -r requirements.txt

