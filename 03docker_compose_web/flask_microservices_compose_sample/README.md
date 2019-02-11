

# 動かし方


```
docker-compose build
docker-compose up -d
psql -h 127.0.0.1 -p 5432 -U postgres --password

#ここでエラーになるので一旦打ち切る
docker-compose run web /usr/local/bin/python create_db.py
```




# 環境

(py35) 192:flask_microservices_compose_sample miyamoto$ docker -v
Docker version 18.09.0-ce-beta1, build 78a6bdb

(py35) 192:flask_microservices_compose_sample miyamoto$ docker-compose -v
docker-compose version 1.22.0, build f46880f


# docker-compose.ymlについて

```:docker-compose.yml
web:
  restart: always
  build: ./web
  expose:
    - "8000"
  links:
    - postgres:postgres
  volumes:
    - /usr/src/app/static
  env_file: .env
  command: /usr/local/bin/gunicorn -w 2 -b :8000 app:app

nginx:
  restart: always
  build: ./nginx/
  ports:
    - "80:80"
  volumes:
    - /www/static
  volumes_from:
    - web
  links:
    - web:web

data:
  restart: always
  image: postgres:latest
  volumes:
    - /var/lib/postgresql
  command: true

postgres:
  restart: always
  image: postgres:latest
  volumes_from:
    - data
  ports:
    - "5432:5432"

```


# エラー


## data.command contains an invalid type, it should be a string, or an array

書き方が古いでは？いや　普通にyamlがわかってなかった。

```
(py35) 192:flask_microservices_compose_sample miyamoto$ docker-compose build
ERROR: The Compose file './docker-compose.yml' is invalid because:
data.command contains an invalid type, it should be a string, or an array
```

.:をつけた。


```
  volumes:
    - .:/usr/src/app/static
    # - /usr/src/app/static
```

Hydra用のdocker-compose.ymlでエラーが出た際の対処法
https://qiita.com/rinasan3/items/68ffa55a9cfaef27da6b

# 参考

http://containertutorials.com/docker-compose/nginx-flask-postgresql.html

