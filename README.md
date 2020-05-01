# docker_sample

## Examples

### Simple Docker Examples

- helloworld
Docker hello world!!    

- v17.12
Document of docker official.

- centos_sample
Docker of CentOS Image.

- ubuntu_sample
Docker of Ubuntu Image.



## Cheet sheet

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


## チートシート：docker

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


[公式サンプル](https://github.com/docker/labs)    
[ubuntu-nginx-phpfpm-redis-mysql](https://github.com/maemori/accon/blob/master/docker/ubuntu-nginx-phpfpm-redis-mysql/Dockerfile)    
[dockerfile](https://github.com/dockerfile)    


## チートシート：docker-compose


```
#ビルドしてup
docker-compose build
docker-compose up
#デーモンで動かす                                                                       
docker-compose up -d
#コンテナ消す
docker-compose kill
#コンテナ全消し
docker-compose down
#イメージも全削除
docker-compose down --rmi all
#ボリュームも削除
docker-compose down --volumes
#イメージ消す
docker-compose rm
#これやってもdocker ps -aとかdocker imagesには残ってるんだよね。
#イメージ確認
docker-compose images
```

## kubectl

kubenetesとkubectlのコマンド周りのバージョン合わないと動かんこともあるかも。    


- v1.10.0    

```:mac
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.10.0/bin/darwin/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```


```:linux
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.10.0/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```

この記事が結構まとまってる。    

[基礎](http://sassembla.github.io/Public/2018:03:22%2020-25-55/2018:03:22%2020-25-55.html)    

[公式](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-binary-using-curl)    

[k8sチートシート](https://kubernetes.io/docs/reference/kubectl/cheatsheet/#deleting-resources)    


## Minikube

```

brew update && brew install kubectl && brew cask install docker minikube virtualbox
brew install kubernetes-cli
brew cask install virtualbox
brew cask install docker

```

[公式インストール](https://github.com/kubernetes/minikube)


pod表示。    


```
kubectl get pods
```

動いてるサービス確認。    


```
minikube service list
```


[参考](https://kubernetes.io/docs/tasks/tools/install-minikube/)    
[kubectlを1.11にアップグレードしたらget podsができなくなった](https://qiita.com/hitochan777/items/40771f1acebcc5f5f538)    


## kubeflow


```
brew install ksonnet/tap/ks
ks version
```


# 参考

[Docker19.3](https://medium.com/nttlabs/docker-1903-5155754ff8ac)    


