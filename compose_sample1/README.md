


mkdir composetest
cd composetest

touch app.py


Redisのデフォルトポート6379

```py:app.py

import time

import redis
from flask import Flask


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```


```
touch requirements.txt
```

```:requirements.txt
flask
redis
```

```
touch Dockerfile
```


```:Dockerfile
FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```


```
touch docker-compose.yml
```

カレントディレクトリのDockerfileを使用する。
コンテナの5000番を5000番にポートフォワード。
flaskは5000をデフォルトで使う。


```:docker-compose.yml

version: '3'
services:
  web:
    build: .
    ports:
     - "5000:5000"
  redis:
    image: "redis:alpine"
```


```
docker-compose up
#デーモンで動かす
docker-compose up -d
docker image ls
docker-compose down
# イメージも削除
docker-compose down --rmi all
```


docker外のフォルダとマウントしても良い。


```:docker-compose.yml
version: '3'
services:
  web:
    build: .
    ports:
     - "5000:5000"
    volumes:
     - .:/code
  redis:
    image: "redis:alpine"
```


