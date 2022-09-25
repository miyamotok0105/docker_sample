



sudo docker pull python:3.7.5-slim
sudo docker container run --name base -it -p 8080:80 python:3.7.5-slim bash

docker start base

sudo docker exec -it base bash

docker exec -it <コンテナ名> bash

sudo docker cp <コンテナID>:/etc/my.cnf my.cnf


docker commit -m "flask intall" base



