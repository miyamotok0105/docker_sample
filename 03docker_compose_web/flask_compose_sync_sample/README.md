
# docker-sync

docker for macのvolume同期が遅いので、syncで早くする。
ホスト側とdockerコンテナで同期したい場合にvolumeを使うが、
反映されるのに時間がかかりすぎる問題がある。
ホスト側で変更をするたびにdockerをdown upをすれば反映されるけど遅い。
docker-sync startを叩くと少し早くなる。


## 環境構築


```
gem install docker-sync
brew install eugenmayer/dockersync/unox
brew install fswatch unison rsync
```

## syncする




```
docker-sync start
docker-compose build --no-cache web
docker-compose -f ./docker-compose.yml up -d
```


http://localhost:80


何か変更して同期
docker-sync start



docker-compose exec web sh


```
docker-compose down --volumes
docker-compose stop
docker-compose rm

docker-sync stop
```

