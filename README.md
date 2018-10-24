# docker_sample

## Get started with Docker for Mac

※you should update newer version sometimes.

    docker --version
    docker-compose --version
    docker-machine --version


### run docker

    docker run -it ubuntu bash
    #docker run -it --privileged ubuntu bash

    apt-get update
    apt-get install emacs gcc


    #プロセスの確認
    docker ps -a
    #コンテナ全部操作！！便利だけど気をつけて。
    docker stop $(docker ps -aq)
    docker rm $(docker ps -aq)
    docker rmi $(docker images -aq)
    #イメージの確認
    docker image ls


##チートシート：docker

	## List Docker CLI commands
	docker
	docker container --help

	## Display Docker version and info
   	docker --version
	docker version
	docker info

	## Excecute Docker image
	docker run hello-world

	## List Docker images
	docker image ls

	## List Docker containers (running, all, all in quiet mode)
	docker container ls
	docker container ls --all
	docker container ls -aq


##チートシート：docker-compose


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


