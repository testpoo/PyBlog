title: 使用tar包安装mysql
date: 2025-04-22
category: 技术
tag: mysql,安装

[TOC]

文章来源：<https://blog.csdn.net/wang20010104/article/details/142485238>

### 1.官网下载mysql

<https://downloads.mysql.com/archives/community/>


### 2. 添加用户

先检查是否有mysql用户组和mysql用户,没有就添加有就忽略：

```bash
groups mysql
```

&nbsp;添加用户组和用户

```bash
groupadd mysql && useradd -r -g mysql mysql
```

### 3.上传到服务器解压

解压tar包

```bash
tar -zxvf mysql-5.7.44-linux-glibc2.12-x86_64.tar.gz
```

将解压后的包改名为mysql，这样更加简易（也可不改）

将mysql目录包移动到/usr/local/，并赋予mysql用户权限

```bash
chown mysql:mysql -R mysql
```

### 4.创建数据目录并赋予权限

此为mysql存放数据地方，可设置内存较多的磁盘

```bash
mkdir -p /data/mysql
chown mysql:mysql -R /data/mysql
```

### 5.修改配置文件

`vim /etc/my.cnf`（没有就新建）

```XML
[mysqld]
#skip-grant-tables
lower_case_table_names=1
bind-address = 0.0.0.0
port=3306
basedir=/usr/local/mysql
datadir=/data/mysql
socket=/tmp/mysql.sock
log-error=/data/mysql/mysql.err
pid-file=/data/mysql/mysql.pid
symbolic-links=0
character_set_server=utf8mb4
```

这个MySQL配置文件通常位于`my.cnf`或`my.ini`文件中，具体取决于操作系统。包含了多个关键的设置，用于控制MySQL服务器的行为。下面是对这些设置的解释：

1.  **`#skip-grant-tables`**: 这一行被注释掉了（因为它前面有一个`#`号），意味着这个选项没有被启用。`skip-grant-tables`选项通常用于紧急情况，允许任何用户无需密码即可连接到MySQL服务器，但这会禁用所有的权限检查。由于安全风险，通常不建议在生产环境中使用。
    
2.  **`lower_case_table_names=1`**: 这个设置指定了MySQL在存储表名时应如何区分大小写。设置为`1`时，MySQL在Linux系统上也会将表名以小写形式存储在磁盘上，并且查询时不区分大小写。这对于跨平台的数据库迁移非常有用，因为Windows系统默认不区分大小写，而Linux系统默认区分。
    
3.  **`bind-address = 0.0.0.0`**: 这个设置允许MySQL服务器监听所有IPv4地址上的连接。这意呀着MySQL可以接受来自任何IP地址的连接请求，这在需要将MySQL服务器设置为可从远程访问时非常有用。但请注意，出于安全考虑，应确保通过防火墙规则或MySQL的`user`表中的权限设置来限制哪些IP地址可以访问MySQL服务器。
    
4.  **`port=3306`**: 这个设置指定了MySQL服务器监听的端口号。默认情况下，MySQL服务器使用3306端口。如果需要更改此端口号，可以在这里进行设置。
    
5.  **`basedir=/usr/local/mysql`**: 这个设置指定了MySQL安装的基础目录。MySQL服务器会从这个目录加载其可执行文件和库文件。
    
6.  **`datadir=/data/mysql`**: 这个设置指定了MySQL数据文件的存储目录。所有的数据库、表和其他相关数据都将存储在这个目录下。
    
7.  **`socket=/tmp/mysql.sock`**: 当MySQL客户端和服务器在同一台机器上运行时，它们可以通过UNIX域套接字进行通信，而不是通过网络套接字。这个设置指定了套接字的路径。
    
8.  **`log-error=/data/mysql/mysql.err`**: 这个设置指定了MySQL服务器错误日志文件的路径。如果服务器在运行时遇到错误，错误信息将被写入这个文件中。
    
9.  **`pid-file=/data/mysql/mysql.pid`**: 这个设置指定了MySQL服务器进程ID（PID）文件的路径。该文件包含了MySQL服务器主进程的ID，可以用来监控或杀死MySQL服务器进程。
    
10. **`symbolic-links=0`**: 这个设置禁用了MySQL服务器中的符号链接。由于安全原因，通常不建议使用符号链接。
    
11. **`character_set_server=utf8mb4`**: 这个设置指定了MySQL服务器的默认字符集为`utf8mb4`。`utf8mb4`是`utf8`的超集，支持更多的Unicode字符，包括一些特殊的表情符号（emoji）。使用`utf8mb4`可以确保数据库能够存储和处理更广泛的字符集。

### 6. 初始化

解压后的mysql-5.7.44-linux-glibc2.12-x86_64移动到/usr/local/mysql （文件夹名称修改为mysql不带版本号信息）

移动后初始化mysql

```bash
cd /usr/local/mysql/bin/
```

```bash
./mysqld --defaults-file=/etc/my.cnf --basedir=/usr/local/mysql/ --datadir=/data/mysql/ --user=mysql --initialize
```

### 7.启动mysql

进入到启动mysql的目录下

```bash
cd /usr/local/mysql/support-files/
```

```bash
./mysql.server start
```

### 8.查看密码

```bash
cat /data/mysql/mysql.err
```

这里可以看到临时密码

### 9.修改密码

```bash
./mysql -u root -p
```

输入临时密码登录登录，修改密码为1234

```bash
ALTER USER 'root'@'localhost' IDENTIFIED BY '1234';
```

刷新

```bash
FLUSH PRIVILEGES;
```

查看发现只有本地可访问，修改可访问的主机为所有

```bash
update mysql.user set host = '%' where user ='root';
```

再次查看发现修改成功，同时刷新

```bash
FLUSH PRIVILEGES;
```

### 10.报错

如果连接mysql报错，以使用命令查看错误，可见有的为空

```bash
ldd /usr/local/mysql/bin/mysql
```

缺少什么安装什么即可