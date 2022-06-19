
# 起動

```
# 起動
docker network create --driver bridge docker-network
docker-compose build
docker-compose up -d

# hostsファイル

macだと/private/etc/hostsを修正。

```
127.0.0.1   web1.test web2.test
```

これは通らない
curl localhost:8080    
バーチャルホストに.comを入れても通らない。    

# これは通る。
web1.test

# 滅びのコマンド
docker-compose down --rmi all --volumes
```


## 個別で動かす
    


```
cd web1
docker build -t flask .
docker run -p 80:80 --rm --name web1 flask
```

