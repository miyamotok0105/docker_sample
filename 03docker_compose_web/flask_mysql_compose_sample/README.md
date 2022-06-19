

```
docker-compose build

#エラーチェックしたい時はupだけする。-dするとエラーが見えない
docker-compose up

#デーモンで動かす
docker-compose up -d

docker-compose exec application /bin/bash

docker-compose exec data /bin/sh

docker-compose exec mysql /bin/sh

mysql -u python -p
python


docker image ls
docker-compose down
# イメージも削除
docker-compose down --rmi all
```




# 参考

https://qiita.com/RyosukeKamei/items/5e834fef3b5a187e50c4
