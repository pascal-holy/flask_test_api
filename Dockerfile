FROM redis:3.2.11
FROM tiangolo/uwsgi-nginx-flask:python3.6



COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app


RUN pip install -r requirements.txt
