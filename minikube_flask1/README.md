
# 概要

[注意]これまだエラーになってる。    
minikube flaskのサンプル。    


# 環境

minikubeとkubectlが入ってること。    
flask：マイクロサーバー    
gunicorn：appサーバー    
gevent：    

# 実行手順


```
bash ./deploy.sh
```

# ファイル構成


```
.
├── Dockerfile
├── README.md
├── app
│   └── server.py
├── deploy.sh
├── deployment.yaml
├── gunicorn.cfg
├── requirements.txt
└── service.yaml
```


- Dockerファイル    

FROM python:3.6-alpineではAlpine Linuxっていう軽量linuxを使用している。alpine linuxのパッケージマネージャはapkを使用する。    
デプロイ用のフォルダを作成して必要ファイルをコピーする。    
パッケージを入れてpipでpython環境を整える。    
WORKDIRでディレトリを指定。    
全ファイルをデプロイ用のフォルダ（deploy）にコピー。    
EXPOSEでポート開ける？    
gunicornコマンド実行    



```:Dockerfile
FROM python:3.6-alpine

RUN mkdir -p /deploy/app

COPY requirements.txt /deploy/
RUN apk --update add --virtual build-base \
  && python3 -m ensurepip \
  && pip install --upgrade pip \
  && pip install -r /deploy/requirements.txt 

WORKDIR /deploy/app
COPY . /deploy/

EXPOSE 5000

CMD ["gunicorn", "--config", "/deploy/gunicorn.cfg", "server:app"]

```


- gunicorn    

geventを使用するように指定。    

```:gunicorn.cfg
bind = "0.0.0.0:5000"
workers = 3
worker_class = "gevent"
```

設定ファイルを指定して実行。    


```
gunicorn --config /deploy/gunicorn.cfg server:app
```

デプロイ用のコマンド    

- 1.シェルスクリプトにオプションをつける    
つけといた方がいいオプション。    
set -eはエラーが出たら止めてくれる。    
set -uは未定義の環境変数が出たら止めてくれる。    

- 2.docker構築    

docker buildする。    

- 3.dockerをk8sに載せる    

kubectl runする。    

- 4.minikubeに載ってることを確認    

curl minikube serviceする。    



```:deploy.sh
#!/bin/bash -x

set -e
set -u

app_name="flask-kubernetes-example"

docker build . -t ${app_name}:latest && \

kubectl run ${app_name} --image=${app_name}:latest --port=5000 --image-pull-policy=Never && \

curl -IL $(minikube service ${app_name} --url)

```



