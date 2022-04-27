title:mysql的安装
date:2020.05.09
category:mysql
tag:mysql安装

[TOC]

### Mysql的安装

以centos离线安装为例

### 下载mysql安装包

从Mysql官方网站内下载 <https://dev.mysql.com/downloads/mysql/>

选择以下版本进行安装

```
Red Hat Enterprice Linux / Oracle Linux
Red Hat Enterprice Linux 8 / Oracle Linux 8 (x86,64-bit)

下载包信息：mysql-8.0.20-1.el8.x86_64.rpm-bundle.tar|8.0.20|650.2M    
```

### 删除mariadb

查看系统中是否存的mariadb，如果存在，将其删除，即可以如下操作：

```
rpm -qa | grep mariadb
# 如果有返回信息，说明存在mariadb，如下：
mariadb-libs-5.5.56-2.el7.x86_64
# 删除命令为：
rpm -e --nodeps mariadb-libs-5.5.56-2.el7.x86_64
```

### 安装离线包

解压缩mysql离线安装包

```
cd /home/test
tar -xvf mysql-8.0.20-1.el8.x86_64.rpm-bundle.tar
```

解压缩之后，包含以下rpm包

```
mysql-community-libs-8.0.20-1.el8.x86_64.rpm
mysql-community-embedded-compat-8.0.20-1.el8.x86_64.rpm
mysql-community-devel-8.0.20-1.el8.x86_64.rpm
mysql-community-server-8.0.20-1.el8.x86_64.rpm
mysql-community-libs-compat-8.0.20-1.el8.x86_64.rpm
mysql-community-client-8.0.20-1.el8.x86_64.rpm
mysql-community-common-8.0.20-1.el8.x86_64.rpm
mysql-community-test-8.0.20-1.el8.x86_64.rpm
```

安装rmp包，逐个安装，命令如下：

```
# 必须安装
rpm -ivh mysql-community-common-8.0.20-1.el8.x86_64.rpm
rpm -ivh mysql-community-libs-8.0.20-1.el8.x86_64.rpm
rpm -ivh mysql-community-client-8.0.20-1.el8.x86_64.rpm
rpm -ivh mysql-community-server-8.0.20-1.el8.x86_64.rpm
# 非必须安装
rpm -ivh mysql-community-libs-compat-8.0.20-1.el8.x86_64.rpm
rpm -ivh mysql-community-embedded-compat-8.0.20-1.el8.x86_64.rpm
rpm -ivh mysql-community-devel-8.0.20-1.el8.x86_64.rpm
rpm -ivh mysql-community-test-8.0.20-1.el8.x86_64.rpm

注意：如果有依赖缺失的问题，请按照错误提示，自行安装缺失的依赖
```

### 创建mysql用户和组

```
groupadd mysql
useradd -g mysql mysql

# 设置用户的密码
passwd mysql
```

### Mysql配置

新建my.cnf文件

```
touch /etc/my.cnf
```

配置文件内容

```
[mysqld]
########basic settings########
federated
user=mysql
datadir = /data/mysql
transaction_isolation = READ-COMMITTED
explicit_defaults_for_timestamp = 1
#bind-address = 0.0.0.0  # 表示允许任何主机登陆MySQL
port = 3306
socket = /tmp/mysql.sock
federated
########log settings##########
log-bin=mysql-bin
expire_logs_days = 5
log-error = /data/mysql_log/error.log
long_query_time = 10
slow_query_log = 1
slow_query_log_file = /data/mysql_log/slowquery.log
log_throttle_queries_not_using_indexes = 10
binlog_format=ROW
########innodb settings########
#索引和数据缓冲区大小，一般设置物理内存的60%-70%
innodb_buffer_pool_size=6G
innodb_buffer_pool_instances = 8
innodb_buffer_pool_load_at_startup = 1
innodb_buffer_pool_dump_at_shutdown = 1
#innodb_page_size = 8192
innodb_lock_wait_timeout = 50
innodb_file_format = Barracuda
innodb_file_format_max = Barracuda
innodb_purge_threads = 4
innodb_large_prefix = 1
innodb_print_all_deadlocks = 1
innodb_strict_mode = 1
innodb_sort_buffer_size = 32M
#默认值为 48M. 有很高写入吞吐量
innodb_log_file_size=1G
#InnoDB 存储引擎的事务日志所使用的缓冲区
innodb_log_buffer_size = 16M
innodb_flush_log_at_trx_commit=2
#修改InnoDB为独立表空间模式,每个数据库的每个表都会生成一个数据空间
innodb_file_per_table=1
#限制Innodb能打开的表的数据
#innodb_file_io_threads=4
#5.6以后分为读和写，根据事务特性进行修改，原则为总数加起来<=cpu个数*每个cpu核数
innodb_read_io_threads=4
innodb_write_io_threads=4
#如果使用硬件RAID磁盘控制器, 需要设置为 O_DIRECT
#innodb_flush_method=O_DIRECT
#设置会影响InnoDB每秒在后台执行多少操作
innodb_io_capacity=800
[mysqld]
########basic settings########
federated
user=mysql
datadir = /data/mysql
transaction_isolation = READ-COMMITTED
explicit_defaults_for_timestamp = 1
#bind-address = 0.0.0.0  # 表示允许任何主机登陆MySQL
port = 3306
socket = /tmp/mysql.sock
federated
########log settings##########
log-bin=mysql-bin
expire_logs_days = 5
log-error = /data/mysql_log/error.log
long_query_time = 10
slow_query_log = 1
slow_query_log_file = /data/mysql_log/slowquery.log
log_throttle_queries_not_using_indexes = 10
binlog_format=ROW
########innodb settings########
#索引和数据缓冲区大小，一般设置物理内存的60%-70%
innodb_buffer_pool_size=6G
innodb_buffer_pool_instances = 8
innodb_buffer_pool_load_at_startup = 1
innodb_buffer_pool_dump_at_shutdown = 1
#innodb_page_size = 8192
innodb_lock_wait_timeout = 50
innodb_file_format = Barracuda
innodb_file_format_max = Barracuda
innodb_purge_threads = 4
innodb_large_prefix = 1
innodb_print_all_deadlocks = 1
innodb_strict_mode = 1
innodb_sort_buffer_size = 32M
#默认值为 48M. 有很高写入吞吐量
innodb_log_file_size=1G
#InnoDB 存储引擎的事务日志所使用的缓冲区
innodb_log_buffer_size = 16M
#关键参数，0代表大约每秒写入到日志并同步到磁盘，数据库故障会丢失1秒左右事务数据。1为每执行一条SQL后写入到日志并同步到磁盘，I/O开销大，执行完SQL要等待日志读写，效率低。2代表只把日志写入到系统缓存区，再每秒同步到磁盘，效率很高，如果服>务器故障，才会丢失事务数据。对数据安全性要求不是很高的推荐设置2，性能高，修改后效果明显。
innodb_flush_log_at_trx_commit=2
#修改InnoDB为独立表空间模式,每个数据库的每个表都会生成一个数据空间
innodb_file_per_table=1
#限制Innodb能打开的表的数据
#innodb_file_io_threads=4
#5.6以后分为读和写，根据事务特性进行修改，原则为总数加起来<=cpu个数*每个cpu核数
innodb_read_io_threads=4
innodb_write_io_threads=4
#如果使用硬件RAID磁盘控制器, 需要设置为 O_DIRECT
#innodb_flush_method=O_DIRECT
#设置会影响InnoDB每秒在后台执行多少操作
innodb_io_capacity=800
innodb_io_capacity_max=1000
#这个参数必须要和innodb_io_capacity设置一样
innodb_lru_scan_depth=800
#限制了一次有多少线程能进入内核,0表示不限制进入内核的数量
innodb_thread_concurrency = 32
#除了缓存表数据和索引外,可以为操作所需的其他内部项分配缓存来提升InnoDB的性能,这些内存就可以通过此参数来分配
innodb_additional_mem_pool_size=8M
#修改为基于行的复制
innodb_autoinc_lock_mode = 2

secure_file_priv=""
##############cache#############
max_allowed_packet = 2048M
#内部内存临时表的最大值
tmp_table_size=128M
tmpdir = /data/mysql/mysql_tmp
collation_server=utf8_general_ci
character_set_server=utf8
#即跳过外部锁定
skip-external-locking
skip-name-resolve
#MySQL能暂存的连接数量(根据实际设置)
back_log=1024
#指定索引缓冲区的大小,只对MyISAM表起作用,这里写上也没有关系
key_buffer_size=128M
#这条指令限定用于每个数据库线程的栈大小
thread_stack=256k
#当一个查询不断地扫描某一个表,MySQL会为它分配一段内存缓冲区
read_buffer_size=128M
#线程缓存
thread_cache_size=16
#查询缓存大小
query_cache_size=128M
#内部内存临时表的最大值,每个线程都要分配
max_heap_table_size=128M
#将查询结果放入查询缓存中
query_cache_limit = 3M
query_cache_min_res_unit = 2k
bulk_insert_buffer_size = 64M
query_cache_type=1
#代表在事务过程中容纳二进制日志SQL语句的缓存大小
binlog_cache_size = 2M
#同样是缓存表大小
table_open_cache=128
#缓存线程
#thread_cache=16000
#推荐设置为服务器 CPU核数的2倍
thread_concurrency=16
interactive_timeout=28800
wait_timeout=28800
#表和表联接的缓冲区的大小
join_buffer_size = 32M
#是一个connection级参数,在每个connection第一次需要使用这个buffer的时候,一次性分配设置的内存
sort_buffer_size = 32M
#随机读取数据缓冲区使用内存
read_rnd_buffer_size = 32M
group_concat_max_len = 102400 #你要的最大长度
##################################################
#connect 是一个MySQL中与安全有关的计数器值,它负责阻止过多尝试失败的客户端以防止暴力破解密码
max-connect-errors=1000
#连接数
max-connections=1000
##################################################
#开启查询缓存
explicit_defaults_for_timestamp=true
###################################################
[client]
socket=/tmp/mysql.sock
```

### 服务启停

- 查看服务状态

```
systemctl status mysqld
```

- 停止服务

```
service mysqld stop
```

- 初始化数据库

```
mysqld --initialize --console
```

- 目录授权

```
chown -R mysql:mysql /var/lib/mysql/
```

- 启动mysql服务

```
systemctl start mysqld
systemctl status mysqld
```

### 数据库操作

- 查看临时密码：

```
grep 'password' /var/log/mysqld.log |head -n 1
```

- 用临时密码登录数据库

```
mysql -u root -p 回车键
然后输入临时密码（输入时不会显示出来，输入完直接回车）
```

- 修改mysql密码

```
alter USER 'root'@'localhost' IDENTIFIED BY '123456';
```