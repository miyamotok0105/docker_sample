FROM python:alpine3.6

WORKDIR /usr/src/app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir flask flask-api ifaddr
EXPOSE 80 443

COPY app.py ./

CMD [ "python", "app.py"]