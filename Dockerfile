FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt 
RUN pip install -r requirements.txt 
COPY . /app


CMD python downtime_monitor/manage.py runserver 0.0.0.0:8000
