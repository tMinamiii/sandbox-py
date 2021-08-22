FROM python:3.9.6-buster


RUN mkdir fastapi-mock && pip install fastapi uvicorn
WORKDIR /fastapi-mock

CMD ["uvicorn", "main:app", "--reload"]
