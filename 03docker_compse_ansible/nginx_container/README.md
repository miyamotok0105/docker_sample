

```
# 実行
ansible-playbook playbook.yml

後からdocker stopして削除してね。
```



docker_containerでコンテナを選択。

[公式資料](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html#examples)


```
# playbook.yml
---
- hosts: localhost
  connection: local
  tasks:
    - name: deploy nginx docker container
      docker_container:
        image: nginx:stable
        name: nginx
        state: started
        auto_remove: true
        ports:
          - "8080:80"

```

