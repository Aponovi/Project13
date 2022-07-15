# syntax=docker/dockerfile:1
# Base Image
FROM python:3.10

# Python Interpreter Flags
ENV PYTHONUNBUFFERED=1 \
    DEBUG=True

RUN mkdir /app
WORKDIR ./app

COPY requirements.txt . /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD python3 manage.py runserver 0.0.0.0:8000