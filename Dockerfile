FROM python:3.7-slim

WORKDIR /
ENV PORT 8080

RUN apt-get update && apt-get install --yes --no-install-recommends git

COPY requirements.txt /tmp
RUN python -m pip install --disable-pip-version-check --no-cache-dir -r /tmp/requirements.txt

COPY . /app
WORKDIR /app
ENTRYPOINT gunicorn -b :$PORT app.app:app -w 5 -k gevent
