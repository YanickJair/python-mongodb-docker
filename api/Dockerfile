FROM python:3.9-slim

ENV TZ=Europe/Lisbon
ENV VIRTUAL_ENV=/opt/venv

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y --no-install-recommends
RUN apt-get -y install libpq-dev gcc
RUN apt-get -y upgrade
RUN apt-get install -y uuid

ADD ./app /usr/app
WORKDIR /usr/app

RUN python3 -m venv $VIRTUAL_ENV
RUN PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
