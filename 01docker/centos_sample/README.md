

# centosのサンプル

## シンプルな例


```
sudo docker build -f ./Dockerfile1.txt -t centos_sample1 .
```

## webもあげてみる例

```
sudo docker build -f ./Dockerfile2.txt -t centos_sample2 .
sudo docker run -p 8080:80 -d centos_sample2
```

http://localhost:8080/




# command memo


```
sudo docker kill [contaner id]
sudo docker run -i -t centos_sample2 /bin/bash
docker image prune
```



