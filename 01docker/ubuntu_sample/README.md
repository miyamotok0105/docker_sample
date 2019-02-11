

# ubuntuのサンプル

## シンプルな例


```
sudo docker build -f ./Dockerfile1.txt -t ubuntu_sample1 .
```

## webもあげてみる例

ここはまだ動かせてない！！！

```
sudo docker build -f ./Dockerfile2.txt -t ubuntu_sample2 .
docker run -it -p 8080:80 -d ubuntu_sample2 /bin/bash
#docker run -it -p 8080:80 ubuntu_sample2 /bin/bash
#docker run -it -p 80:80 -d ubuntu_sample2 /bin/bash
```

/etc/init.d/nginx start
http://localhost:8080/


# command memo


```
sudo docker kill [contaner id]
sudo docker rm [contaner id]
sudo docker run -i -t centos_sample2 /bin/bash
```

全削除系    

```
docker container prune
docker rm -f `docker ps -a -q`
docker image prune
docker rmi `docker images -q`
```


