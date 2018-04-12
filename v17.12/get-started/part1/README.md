
#Test Docker version

      docker --version
      docker info

#Test Docker installation

      #簡単なDockerイメージを実行してインストールが動作することをテスト
      docker run hello-world
      docker image ls
      #コンテナ
      docker container ls --all
      

#Recap and cheat sheet


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
