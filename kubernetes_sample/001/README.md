
Kubernetes 速習会(2016-08-23)    
https://qiita.com/koudaiii/items/d0b3b0b78dc44d97232a    

```
#ubuntu
curl -O https://storage.googleapis.com/kubernetes-release/release/v1.3.4/bin/linux/amd64/kubectl
#mac
curl -O https://storage.googleapis.com/kubernetes-release/release/v1.3.4/bin/darwin/amd64/kubectl

chmod +x kubectl

```



```
git clone https://github.com/koudaiii/docker-hello-world.git
cd docker-hello-world
kubectl get pod
kubectl create -f kubernetes/namespace.yaml
#kubernetes 上で作られる pod の一覧を表示
kubectl get po --namespace=kube-system
# すべての namespace の一覧を表示
kubectl get namespace
```



cat kubernetes/pod.yaml
```
apiVersion: v1
kind: Pod
metadata:
  name: docker-hello-world
  namespace: docker-hello-world
  labels:
    name: docker-hello-world
    role: web
spec:
  containers:
    - image: koudaiii/hello-world:latest
      name: docker-hello-world
      ports:
        - containerPort: 8080
      env:
        - name: MESSAGE
          value: Hello Wantedly
```




# コマンド

- すべての namespace の一覧を表示

```
kubectl get namespace
```

- namespaceのdevを消す

```
kubectl delete namespaces dev
```

- namespaceを全部消す

```
kubectl delete namespace --all
```

Podを終了

```
kubectl delete name
```

