title:安装docker-swarm
date:2025-03-12
category: 技术
tag:docker swarm

[TOC]

### 1.Debian下安装docker依赖

```
apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common -y
```

### 2.安装证书，docker官网访问不了，用ubuntu的，网络不行，多试几次

```
gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7EA0A9C3F273FCD8
gpg --export 7EA0A9C3F273FCD8 | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

### 3.添加docker清华源

```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```


### 4.安装docker

```
apt install docker-ce docker-ce-cli containerd.io -y
```

### 5.初始化 Docker Swarm 集群

#### 5.1 选择一台主机作为管理节点，在该主机上执行以下命令初始化 Swarm 集群：

```
docker swarm init --advertise-addr 192.168.214.34
===============================================================================
Swarm initialized: current node (************************) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-************************************************ 192.168.214.34:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
===============================================================================
```

#### 5.2 添加工作节点

```
docker swarm join --token SWMTKN-1-************************************************ 192.168.214.34:2377

重新加入swarm
docker swarm join-token manager # 管理节点
docker swarm join-token worker  # 工作节点
```

#### 5.3 验证 Swarm 集群

```
docker node ls
```


### 6.安装mysql服务

```
# 添加清华源
sudo nano /etc/docker/daemon.json

{
    "registry-mirrors": ["https://docker.mirrors.tuna.tsinghua.edu.cn"]
}

systemctl restart docker
```

#### 6.1 拉取 MySQL 镜像

```
docker pull mysql:8.0  # 直接拉取镜像

docker pull docker.mirrors.tuna.tsinghua.edu.cn/library/mysql:8.0  # 通过清华源拉取镜像

docker save -o xvlan-mysql.tar sicap-repo.com/library/mysql:5.7.43  # 从SiCAP导出一个  # 从别的地方导出一个镜像
docker load -i /home/poo/xvlan-mysql.tar  # 导入镜像
```

#### 6.2 创建网络(overlay)

```
# 在管理节点上执行以下命令来创建一个网络
docker network create -d overlay mysql-net

# 参数说明：-d overlay：指定网络驱动为 overlay，这是 Docker Swarm 用于跨节点通信的网络类型。
```

#### 6.3 创建 MySQL 服务

```
docker service create \
  --name mysql-service \
  --network mysql-net \
  -e MYSQL_ROOT_PASSWORD=123456 \
  -p 3306:3306 \
  --mount type=volume,source=mysql-data,target=/var/lib/mysql \
sicap-repo.com/library/mysql:5.7.43

# 参数说明：
# --name mysql-service：为服务指定名称，这里是 mysql-service。
# --network mysql-net：将服务连接到之前创建的 mysql-net 网络。
# -e MYSQL_ROOT_PASSWORD=your_password：设置 MySQL 的 root 用户密码，你需要将 your_password 替换为实际密码。
# -p 3306:3306：将容器内的 3306 端口映射到宿主机的 3306 端口，以便外部可以访问 MySQL 服务。
# --mount type=volume,source=mysql-data,target=/var/lib/mysql：使用 Docker 卷 mysql-data 进行数据持久化，将其挂载到容器内的 /var/lib/mysql 目录，该目录是 MySQL 存储数据的默认位置。
# mysql:8.0：指定使用的 MySQL 镜像版本。
```

#### 6.4 验证服务是否正常运行

```
docker service ls
docker service ps mysql-service
```

### 7.安装mysql客户端

#### 7.1 拉取 MySQL 镜像

同6.1

#### 7.2 创建网络(overlay)

同6.2

#### 7.3 创建 MySQL Client 服务

在管理节点上执行以下命令来创建一个临时的 MySQL Client 服务，以连接到 MySQL 数据库：

```
docker service create \
    --name mysql-client-service \
    --network mysql-net \
    --mode replicated \
    --replicas 1 \
    --constraint "node.role==worker" \
    sicap-repo.com/library/mysql:5.7.43 \
    mysql -h 192.168.214.34 -P 3306 -u root -p123456
    
docker service create \
    --name mysql-client-service \
    --network mysql-net \
    sicap-repo.com/library/mysql:5.7.43 \
    mysql -h 192.168.214.35 -P 3306 -u root -p123456

# 参数解释：
# --name mysql-client-service：为服务指定名称，便于后续管理。
# --network mysql-net：将服务连接到之前创建的 Overlay 网络。
# --mode replicated：指定服务模式为副本模式，即创建多个相同的副本。
# --replicas 1：设置副本数量为 1，即只创建一个 MySQL Client 实例。
# --constraint "node.role==worker"：约束服务只能在工作节点上运行。
# mysql:8.0：使用的 MySQL 镜像版本。
# mysql -h <MySQL 服务主机地址> -P <端口> -u <用户名> -p<密码>：容器启动后执行的命令，用于连接到 MySQL 服务。请将 <MySQL 服务主机地址>、<端口>、<用户名> 和 <密码> 替换为实际的值。
```

### 8. Docker Swarm 集群环境删除服务

```
docker service ls
docker service rm <服务 ID 或名称>
```

### 9. 进入docker

```
docker exec -it <窗口 ID> bash
```