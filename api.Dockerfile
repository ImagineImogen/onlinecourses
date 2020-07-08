FROM python:3.7-alpine3.11


RUN apk update \
	&& apk add --virtual build-deps \
	&& apk add bash gcc g++ curl gettext python3-dev jpeg-dev zlib-dev libjpeg \
	&& apk del build-deps

RUN mkdir -p /code

RUN mkdir -p /static

WORKDIR /code

# set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B)
ENV PYTHONDONTWRITEBYTECODE 1  
# Prevents Python from buffering stdout and stderr (equivalent to python -u)
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r /tmp/requirements.txt

COPY web_entrypoint.sh /tmp/web_entrypoint.sh

EXPOSE 8000