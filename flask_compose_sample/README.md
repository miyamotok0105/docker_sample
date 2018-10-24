


# docker build


```
docker build -t flask-sample-one:latest .
docker run -d -p 5000:5000 flask-sample-one
docker ps -a
```

これでプロセスまではできるね。buildでimage作って、runする。


# docker-compose upしてみる。



```
docker-compose up
```

buildでwebフォルダ指定してる。
imageが書かれてないので、ローカルのDockerfileを使用してビルド。
volumesでマウント。ローカルのカレントディレクトリとコンテナの/code。


```
web:
  build: ./web
  ports:
   - "5000:5000"
  volumes:
   - .:/code


```

http://localhost:5000

が動く。




