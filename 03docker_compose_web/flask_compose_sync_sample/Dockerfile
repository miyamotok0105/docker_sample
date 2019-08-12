FROM python:3.7-alpine3.7

ADD . /my-web-app
WORKDIR /my-web-app

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]