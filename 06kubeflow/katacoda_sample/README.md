

# kubeflow with tf

kubeflowはk8s機械学習環境を簡単にセットアップするライブラリ。

- TF Job Operator and Controller    
- TF Hub    
- Model Server    

## kubeflowデプロイ


```
export GITHUB_TOKEN=99510f2ccf40e496d1e97dbec9f31cb16770b884
export KUBEFLOW_VERSION=0.2.5
curl https://raw.githubusercontent.com/kubeflow/kubeflow/v${KUBEFLOW_VERSION}/scripts/deploy.sh | bash
```

pods確認    


```
kubectl get pods
```


Katacodaの永続的なボリュームとサービスを作成する    
Kubeflowに必要なLoadBalancerとPersistent Volumeが作成    

```
kubectl apply -f ~/kubeflow/katacoda.yaml
```


## TensorFlow サンプル

Kubeflowの主な機能は、Docker Imageとしてパッケージ化されたTensorFlowコードを簡単にデプロイすること。    

- Master    
workerを調整する。    
- Worker    
ジョブは0〜N個のWorkerをもてる。各ワーカープロセスは同じモデルを実行し、処理用のパラメータをパラメータサーバに提供する。    
- PS    
ジョブは0〜N個のパラメータサーバー(PS)をもてる。パラメータサーバーを使用すると、複数のマシンにまたがってモデルを拡張できます。    



```:example.yaml
apiVersion: "kubeflow.org/v1alpha2"
kind: "TFJob"
metadata:
  name: "example-job"
spec:
  tfReplicaSpecs:
    Master:
      replicas: 1
      restartPolicy: Never
      template:
        spec:
          containers:
            - name: tensorflow
              image: gcr.io/tf-on-k8s-dogfood/tf_sample:dc944ff
    Worker:
      replicas: 1
      restartPolicy: Never
      template:
        spec:
          containers:
            - name: tensorflow
              image: gcr.io/tf-on-k8s-dogfood/tf_sample:dc944ff
    PS:
      replicas: 2
      restartPolicy: Never
      template:
        spec:
          containers:
            - name: tensorflow
              image: gcr.io/tf-on-k8s-dogfood/tf_sample:dc944ffmaster
```


TFJobをデプロイする。    


```
kubectl apply -f example.yaml
```

TensorFlow jobsの状態を見れる。    


```
kubectl get tfjob
```




```
kubectl get pods | grep Completed
```

kubectlログで確認する。    


```
kubectl logs $(kubectl get pods | grep Completed | tr -s ' ' | cut -d ' ' -f 1)
```

ロードバランサーのIPアドレスを確認    


```
kubectl get svc
```


```
MODEL_COMPONENT=model-server
MODEL_NAME=inception
MODEL_PATH=/serving/inception-export
```

Ksonnetを使用してtf-servingを拡張する。    


```
cd ~/kubeflow_ks_app
ks generate tf-serving ${MODEL_COMPONENT} --name=${MODEL_NAME}
ks param set ${MODEL_COMPONENT} modelPath $MODEL_PATH

ks param set ${MODEL_COMPONENT} modelServerImage katacoda/tensorflow_serving
```


```
ks param list
```

デプロイ    


```
ks apply default -c ${MODEL_COMPONENT}
```

## 画像分類



```:model-client-job.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: model-client-job-katacoda
spec:
  template:
    metadata:
      name: model-client-job-katacoda
    spec:
      containers:
      - name: model-client-job-katacoda
        image: katacoda/tensorflow_serving
        imagePullPolicy: Never
        command:
        - /bin/bash
        - -c
        args:
        - /serving/bazel-bin/tensorflow_serving/example/inception_client
          --server=inception:9000 --image=/data/katacoda.jpg
        volumeMounts:
        - name: inception-persistent-storage-katacoda
          mountPath: /data
      volumes:
      - name: inception-persistent-storage-katacoda
        hostPath:
          path: /root
      restartPolicy: Never
```



```
kubectl apply -f ~/model-client-job.yaml
```


```
kubectl logs $(kubectl get pods | grep Completed | tail -n1 |  tr -s ' ' | cut -d ' ' -f 1)
```



## 参考

https://www.katacoda.com/kubeflow/scenarios/deploying-kubeflow
