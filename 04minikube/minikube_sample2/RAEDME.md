

minikubeのk8s上でdockerを動かす。

https://qiita.com/sin_tanaka/items/53e158dabe2644278796

Dockerfile2がどこかミスってるので、docker公式のdockerfileに変更した。


- minikube起動    

```
minikube start
```

- dockerをビルドして起動    


```
docker build -t "docker-sample2" .
docker images
docker run -d -p 8080:80 docker-sample2
docker exec -it f3d57c8b477a /bin/ash
```

- k8sにdockerを載せる    

```
kubectl run sample2-nginx --image=docker-sample2 --port=80
kubectl get pod
```

サービス立てる    

```
kubectl expose deployment sample2-nginx --name my-sample2 --port 80 --type NodePort
kubectl get service
```

>30531番ポートが2048コンテナの80番ポートにフォワーディングされているイメージ


ダッシュボードを立ち上げる    


```
minikube dashboard
```


- curlしてみる    


```
curl $(minikube service my-sample2 --url)
```

- 動いてるサービス確認。    


```
minikube service list
```


# 削除


```
# クラスタを確認
kubectl get service
kubectl get pod
# クラスタ止める
minikube stop
# k8s消す
kubectl delete service my-sample2
kubectl delete deployment sample2-nginx
kubectl delete pods sample2-nginx-fcfd4f6d4-bdpz9
# docker消す
docker rmi image
docker rm contena
```

