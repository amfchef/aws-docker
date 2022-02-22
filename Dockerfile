ARG REPO=233125504132.dkr.ecr.us-east-1.amazonaws.com/python-alpine:latest

FROM ${REPO}
# FROM python:3.8-alpine
WORKDIR /app

COPY . .
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]