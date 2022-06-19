
appフォルダーの中のDockerファイルをビルド。



```
docker-compose build

docker-compose up
#デーモンで動かす
docker-compose up -d

docker-compose exec web /bin/sh

docker image ls
docker-compose down
# イメージも削除
docker-compose down --rmi all
```


