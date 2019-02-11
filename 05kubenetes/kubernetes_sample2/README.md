
gcpで動かすにあたって、こちらが非常に勉強になった。    


Kubernetesを用いてGoogle Container Engineでコンテナクラスタをデプロイする〜入門編〜    
https://qiita.com/yusukixs/items/11601607c629295d31a7


```
git clone https://github.com/yusukixs/kubernetes_demo.git
cd kubernetes_demo
npm install
node server.js
```

下記で動いてればOK
http://localhost:3000/


```
docker build -t kubernetes_demo:1.0 .
docker run -p 3000:3000 -d -it --rm --name nodejs kubernetes_demo:1.0
```

下記で動いてればOK
http://localhost:3000/

```
docker ps -a
docker images
```


```
gcloud init
#Create a new projectでいった 
gcloud components update
gcloud components update kubectl
```


```
#一覧
gcloud projects list
gcloud config set project [プロジェクト名]
```


````
gcloud container clusters create --num-nodes=2 nodejs-cluster \
--zone asia-northeast1-a \
--machine-type g1-small \
--enable-autoscaling --min-nodes=2 --max-nodes=5
````


```
GCP_PROJECT=$(gcloud config get-value project)
echo $GCP_PROJECT
docker build -t asia.gcr.io/$GCP_PROJECT/nodejs:1.0 .
docker images
gcloud docker -- push asia.gcr.io/$GCP_PROJECT/nodejs:1.0
```

# Deployment


```
kubectl run nodejs-deploy \
--image=asia.gcr.io/$GCP_PROJECT/nodejs:1.0 \
--replicas=1 \
--port=3000 \
--limits=cpu=200m \
--command -- node app/server.js
```

pod一覧


```
kubectl get pod
```

Serviceを作成し、ロードバランサでPodを外部に公開


```
kubectl get pod,endpoints,service
```


```
kubectl expose deployment nodejs-deploy --port=80 --target-port=3000 --type=LoadBalancer
brew install watch
watch kubectl get node
```

svc/nodejs-deployのEXTERNAL-IPのipを指定すると動くぽ

http://[ipアドレス]/
に入れる。


ファイヤーウォールは別に空いてるから大丈夫なんだよ    
https://cloud.google.com/vpc/docs/using-firewalls?hl=ja



スケールを１にしてみるぽ

```
kubectl scale deploy nodejs-deploy --replicas=1
```


全部消す

```
kubectl delete deployment,service,pod --all
gcloud container clusters delete nodejs-cluster --zone asia-northeast1-a
```



