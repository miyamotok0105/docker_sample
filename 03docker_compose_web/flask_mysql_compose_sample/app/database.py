import sys
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8mb4' % (
    "python",  #ユーザーID
    "python",  #パスワード
    "mysql",# コンテナ名  IPはダメだった→"192.168.99.100",  #MySQLサーバ(http:\/\/127.0.0.1:3306)に接続し
    "sample", #データベース「sample」にアクセスします
)

#DB接続用のインスタンスを作成
ENGINE = create_engine(
    DATABASE,
    convert_unicode=True,
    echo=True  #SQLをログに吐き出すフラグ
)

#上記のインスタンスを使って、MySQLとのセッションを張ります
session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

#以下に書いていくDBモデルのベース部分を作ります
Base = declarative_base()
Base.query = session.query_property()

#DBとデータをやり取りするためのモデルを定義
class User(Base):
    __tablename__ = 'users2'
    id = Column('id', Integer, primary_key = True)
    name = Column('name', String(200))
    age = Column('age', Integer)
    email = Column('email', String(100))

#このPythonスクリプトを実行したとき、テーブルを一旦削除して新規作成する
def main(args):
    Base.metadata.drop_all(bind=ENGINE)
    Base.metadata.create_all(bind=ENGINE)

#このファイルを直接実行したとき、mainメソッドでテーブルを作成する
if __name__ == "__main__":
    main(sys.argv)
