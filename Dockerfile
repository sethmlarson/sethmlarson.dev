FROM python:3.7-slim

WORKDIR /
ENV PORT 8080

COPY requirements.txt /tmp
RUN python -m pip install -r /tmp/requirements.txt

COPY app.py /
ENTRYPOINT gunicorn -b :$PORT app:app
