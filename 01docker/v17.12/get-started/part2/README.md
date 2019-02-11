

#Dockerfileコンテナを定義する


```:Dockerfile
# Use an official Python runtime as a parent image
FROM python:2.7-slim
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
ADD . /app
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# Make port 80 available to the world outside this container
EXPOSE 80
# Define environment variable
ENV NAME World
# Run app.py when the container launches
CMD ["python", "app.py"]
```

#appをビルドする

アプリケーションを実行して、マシンのポート4000を、以下を使用してコンテナの公開ポート80にマッピング

    docker build -t friendlyhello .
    docker run -p 4000:80 friendlyhello

Pythonがあなたのアプリケーションを提供しているというメッセージが表示されます。http://0.0.0.0:80    
しかしそのメッセージはコンテナ内部から来ています。
コンテナのポート80を4000にマップして、正しいURLを作成しているかどうかはわかりません。
なのでブラウザで接続する。    

http://150.95.145.170:4000/    

これでも確認できる。    
curl http://localhost:4000

分離モードで起動    

    docker run -d -p 4000:80 friendlyhello
    #いることを確認
    docker container ls
    #stopもできる
    docker container stop 1fa4ab2cf395hogehoge



```
docker build -t friendlyhello .  # Create image using this directory's Dockerfile
docker run -p 4000:80 friendlyhello  # Run "friendlyname" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyhello         # Same thing, but in detached mode
docker container ls                                # List all running containers
docker container ls -a             # List all containers, even those not running
docker container stop <hash>           # Gracefully stop the specified container
docker container kill <hash>         # Force shutdown of the specified container
docker container rm <hash>        # Remove specified container from this machine
docker container rm $(docker container ls -a -q)         # Remove all containers
docker image ls -a                             # List all images on this machine
docker image rm <image id>            # Remove specified image from this machine
docker image rm $(docker image ls -a -q)   # Remove all images from this machine
docker login             # Log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag  # Tag <image> for upload to registry
docker push username/repository:tag            # Upload tagged image to registry
docker run username/repository:tag                   # Run image from a registry
```
