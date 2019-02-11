
# 動かし方


```
#ビルドしてup
docker-compose build
docker-compose up
#コンテナ消す
docker-compose kill
#イメージ消す
docker-compose rm
#これやってもdocker ps -aとかdocker imagesには残ってるんだよね。
#イメージ
docker-compose images
```

コンテナがupしたままになる。


# docker-compose.ymlについて

linksでdbと繋がってる。imageが書いてるので、pullして引っ張ってくる。


```:docker-compose.yml
web:
  build: .
  command: python -u app.py
  ports:
    - "5000:5000"
  volumes:
    - .:/todo
  links:
    - db
db:
  image: mongo:3.0.2
```


