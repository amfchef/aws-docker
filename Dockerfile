ARG REPO=233125504132.dkr.ecr.us-east-1.amazonaws.com/python-alpine:latest

FROM ${REPO}
# FROM python:3.8-alpine
WORKDIR /app

RUN python3 -m pip install --upgrade pip
COPY . .
RUN pip install python-dotenv
RUN python3 -m pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=server.py
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
CMD ["flask", "run"]
# docker login -u AWS -p $(aws ecr get-login-password --region us-east-1) 233125504132.dkr.ecr.us-east-1.amazonaws.com/python-alpine:latest