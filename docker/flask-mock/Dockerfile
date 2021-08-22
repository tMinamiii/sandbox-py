FROM python:3.9.6-buster

WORKDIR /flask-mock

RUN mkdir flask-mock && pip install flask flask-httpauth
ENV FLASK_DEBUG 1
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

