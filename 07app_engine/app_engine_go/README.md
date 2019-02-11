

```
sudo apt-get install google-cloud-sdk-app-engine-go
sudo apt-get install google-cloud-sdk-app-engine-python google-cloud-sdk-app-engine-go google-cloud-sdk-datastore-emulator
```

```
go get "google.golang.org/appengine"
go get -u -d github.com/GoogleCloudPlatform/golang-samples/appengine/helloworld/...
```

## ローカルで動かしてみる


```
dev_appserver.py app.yaml
```


## デプロイ



```
gcloud app deploy --project [project_id] --version [version]
```


```
gcloud app deploy --project des2code --version go-server-1
```

uriを確認する。


```
gcloud app browse --project=[project_id]
```

uri    

```
http://VERSION_ID.SERVICE_ID.YOUR_PROJECT_ID.appspot.com
```
