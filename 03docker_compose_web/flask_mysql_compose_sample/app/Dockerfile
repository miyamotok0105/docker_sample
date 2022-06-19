FROM python:3.9.4-slim

RUN apt update; apt -y upgrade
RUN apt install -y vim less emacs python3-mysqldb libmariadb-dev gcc
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install poetry

# 直下のファイルを、Dockerのcodeへコピー
COPY . /code
WORKDIR /code

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]



#CMD ["/bin/bash"]

# # # Pythonは公式イメージ
# # FROM python:3.5.2
# FROM ubuntu:18.04
# #Check recent info
# #https://hub.docker.com/_/ubuntu

# # オリジナルはJoshua Conner氏
# # MAINTAINER Joshua Conner <joshua.conner@gmail.com>
# MAINTAINER Ryosuke Kamei <sr2smail@gmail.com>

# RUN apt-get update -y
# RUN apt-get install -y python-pip python-dev build-essential

# # RUN apt-get install -y 	sudo \
# # 						python3-dev \
# 						# zlib1g-dev \
# 						# libsqlite3-dev \
# 						# libreadline6-dev \
# 						# libgdbm-dev \
# 						# libbz2-dev

# # RUN apt-get update -y

# # # RUN apt-get upgrade -y
# # RUN apt-get install -y 	sudo \
# # 						python3-dev \
# # 						zlib1g-dev \
# # 						libsqlite3-dev \
# # 						libreadline6-dev \
# # 						libgdbm-dev \
# # 						libbz2-dev \
# # 						tk-dev
# # #                        python3-mysql.connector

# # # ユーザ作成
# RUN groupadd web
# RUN useradd -d /home/python -m python

# # pipでインストール
# # virtualenv Pythonの仮想環境構築コマンド
# # flake8 コーディングスタイル/シンタックスのチェック
# # ipython Pythonのインタラクティブモード拡張
# # Flask Pytrhonの軽量フレームワーク
# RUN pip install virtualenv \
# 				ipython \
# 				flake8 \
#                 Flask

# #SQLAlchemy
# #  \Flask-Migrate
# # mysqlclient
# #mysql-connector-python
# # MySQLドライバ"mysql-connector-python"をインストール
# # pipのを使うとうまくいかない。
# # git cloneしてビルド、インストール
# # RUN git clone https://github.com/mysql/mysql-connector-python.git
# # WORKDIR mysql-connector-python
# # RUN python ./setup.py build
# # RUN python ./setup.py install

# # ユーザを変更
# USER python


# # vim の設定ファイル
# #ADD ./vim/.vimrc /home/python/
# #WORKDIR /home/python
# #RUN mkdir /home/python/.vim
# #RUN mkdir /home/python/.vim/ftplugin
# #ADD ./vim/python.vim /home/python/.vim/ftplugin/
# #RUN mkdir /home/python/.vim/bundle
# #RUN git clone https://github.com/Shougo/neobundle.vim /home/python/.vim/bundle/neobundle.vim

# # bottleの場合
# # ポートを解放（bottleのデフォルトのポート番号:8080）
# # EXPOSE 8080
# # サーバ起動
# # ENTRYPOINT ["/usr/local/bin/python", "/home/python/bottle_sample.py"]

# # Flaskの場合
# # ポートを解放（Flaskのデフォルトのポート番号:5001）
# EXPOSE 5001
# # サーバ起動
# # ENTRYPOINT ["/usr/local/bin/python", "/home/python/flask_sample.py"]

# ENTRYPOINT ["python"]
# CMD ["/home/python/flask_sample.py"]


# # フレームワークを指定しない時や、サーバにログインしてから実行したい場合
# # ENTRYPOINT ["/usr/bin/tail", "-f", "/dev/null"]
