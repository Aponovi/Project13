# syntax=docker/dockerfile:1
# Base Image
FROM python:3.10

# Python Interpreter Flags
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBUG=True

RUN mkdir /app
WORKDIR ./app

RUN pip install --upgrade pip
COPY requirements.txt . /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

# CMD python3 manage.py runserver 0.0.0.0:8000
CMD gunicorn --bind 0.0.0.0:8000 config.wsgi