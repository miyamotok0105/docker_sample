
# 概要

minikubeのサンプル。    


# 環境

minikubeとkubectlが入ってること。



```
minikube delete
minikube start
```

kubectl delete service hello-minikube

[googleが提供してるコンテナくん](https://console.cloud.google.com/gcr/images/google-containers/GLOBAL)



```
kubectl run hello-minikube --image=k8s.gcr.io/echoserver:1.10 --port=8080 deployment.apps/

kubectl expose deployment hello-minikube --type=NodePort
```


- curlしてみる    


```
curl $(minikube service hello-minikube --url)
```

- 動いてるサービス確認。    


```
minikube service list
```

hello-minikubeってサービスが立ち上がってる。    

```
|-------------|----------------------|-----------------------------|
|  NAMESPACE  |         NAME         |             URL             |
|-------------|----------------------|-----------------------------|
| default     | hello-minikube       | http://192.168.99.101:30037 |
| default     | kubernetes           | No node port                |
| kube-system | kubernetes-dashboard | http://192.168.99.101:30000 |
|-------------|----------------------|-----------------------------|
```

- スケースする    


```
kubectl scale deployment hello-minikube --replicas 3
```


- pod表示。    


```
kubectl get pods
```

3つのpodが出来てる。    

```
NAME                              READY     STATUS    RESTARTS   AGE
hello-minikube-6b959956bf-4dbhr   1/1       Running   0          5m
hello-minikube-6b959956bf-kf5z2   1/1       Running   0          21m
hello-minikube-6b959956bf-qjqct   1/1       Running   0          5m
```

- サービスを消す    


```
kubectl delete service hello-minikube
kubectl delete deployment hello-minikube
```

- podsを消す    


```
kubectl delete pods hogehoge
```


- クラスタを止める    


```
minikube stop
```



# 参考

https://qiita.com/Manjiii/items/88699c52f5ade2bf4b6f

http://kakts-tec.hatenablog.com/entry/2018/02/28/143338
