FROM python:3.9.4-slim

RUN apt update; apt -y upgrade
RUN apt install -y vim less emacs
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install poetry

# ローカルのコマンド実行直下のファイル(.の意味)を、
# Dockerの中のappフォルダーへCOPY
COPY . /app

# WORKDIRがカレントディレクトリー
WORKDIR /app

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

