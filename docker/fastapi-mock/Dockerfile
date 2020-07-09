FROM python:3.7.7-buster


RUN mkdir fastapi-mock && pip install fastapi uvicorn
WORKDIR /fastapi-mock

CMD ["uvicorn", "main:app", "--reload"]
