FROM python:3.14-slim

ENV PORT=8080

COPY requirements.txt /tmp
RUN python -m pip install --disable-pip-version-check --no-cache-dir -r /tmp/requirements.txt

COPY . /app
WORKDIR /app
ENTRYPOINT gunicorn -b :$PORT app.app:app --threads=4
