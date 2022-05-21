
# docker build


```
#イメージが作り直される
docker-compose build

or

#dockerを直接いじるより、composeからいじるほうが楽
docker build -t flask-sample-one:latest .
docker run -d -p 5001:5001 flask-sample-one
docker ps -a
```

これでプロセスまではできるね。buildでimage作って、runする。


# docker-compose upしてみる。


```
#デーモン状態でイメージからコンテナ起動
docker-compose up -d
```

buildでwebフォルダ指定してる。
imageが書かれてないので、ローカルのDockerfileを使用してビルド。
volumesでマウント。ローカルのカレントディレクトリとコンテナの/code。


```
web:
  build: ./web
  ports:
   - "5001:5001"
  volumes:
   - .:/code


```

http://localhost:5001

が動く。



```
#Dockerに入る
docker-compose exec web /bin/bash

#Dockerを抜ける。
Control + d
```



```
#フォルダー直下のcompose全部消えます。
#気をつけて消してください。
#全部残しとくと容量圧迫しますので、定期的に掃除をしてください。
docker-compose down --rmi all --volumes --remove-orphans
```

