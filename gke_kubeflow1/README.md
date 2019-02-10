
# 基礎

OAuth client credentialsを設定しておくこと。    
ここで必要なのかは不明だがgoとksも先に入れておいた。    
GKEにKubeflowをデプロイする方法にはGUIとcmdでの方法がある。    


```
export CLIENT_ID=<CLIENT_ID from OAuth page>
export CLIENT_SECRET=<CLIENT_SECRET from OAuth page>
#実例
export CLIENT_ID=hogehoge.apps.googleusercontent.com
export CLIENT_SECRET=hogehoge
```

名前決める。    

```
export KUBEFLOW_SRC="$HOME/kubeflow"
export KFAPP="kubeflow1"
```

kubeflow環境設定    


```
mkdir ${KUBEFLOW_SRC}
cd ${KUBEFLOW_SRC}
export KUBEFLOW_TAG=v0.4.1
curl https://raw.githubusercontent.com/kubeflow/kubeflow/${KUBEFLOW_TAG}/scripts/download.sh | bash
```

デプロイする。    


```
${KUBEFLOW_SRC}/scripts/kfctl.sh init ${KFAPP} --platform gcp --project ${PROJECT}
cd ${KFAPP}
${KUBEFLOW_SRC}/scripts/kfctl.sh generate platform
${KUBEFLOW_SRC}/scripts/kfctl.sh apply platform
${KUBEFLOW_SRC}/scripts/kfctl.sh generate k8s
${KUBEFLOW_SRC}/scripts/kfctl.sh apply k8s
```

動いてること確認。すごいいっぱいデプロイされてる。    


```
kubectl -n kubeflow get  all
```

全部削除


```
${KUBEFLOW_SRC}/scripts/kfctl.sh delete all
```


# 参考

https://www.kubeflow.org/docs/started/getting-started-gke/
