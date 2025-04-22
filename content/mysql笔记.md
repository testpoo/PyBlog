title:mysql笔记
date:2019-10-11
category: 技术
tag:mysql

[TOC]

### 创建用户

非本地登录

```
CREATE USER 'test'@'%' IDENTIFIED BY 'test';
```

本地登录

```
CREATE USER 'test'@'127.0.0.1' IDENTIFIED BY 'test';
CREATE USER 'test'@'localhost' IDENTIFIED BY 'test';
```

创建数据库

```
CREATE database testrcb default character set utf8 collate utf8_general_ci;
```

给用户授权

```
grant select,delete,update,create,drop on testrcb.* to test@"%" identified by "test"; -- 增删改查
grant all privileges on testrcb.* to test@localhost identified by 'test'; -- all
```

修改密码

```
UPDATE mysql.user SET PASSWORD=PASSWORD('test') WHERE User = 'test'
```

### MYSQL配置

```
[mysql]

# 设置mysql客户端默认字符集

default-character-set=utf8 

[mysqld]

#设置3306端口
port = 3306 

# 设置mysql的安装目录
basedir=C:\Program Files\MySQL\MySQL Server 5.6

# 设置mysql数据库的数据的存放目录
datadir=C:\Program Files\MySQL\MySQL Server 5.6\data

# 允许最大连接数
max_connections=200

# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8

# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
Access denied for user 'test'@'localhost' (using password: YES)
```

### 字段增加删除修改

```
添加字段的语法：alter table tablename add (column datatype [default value][null/not null],….);
修改字段的语法：alter table tablename modify (column datatype [default value][null/not null],….);
删除字段的语法：alter table tablename drop (column);

mysql修改字段类型：
--能修改字段类型、类型长度、默认值、注释
--对某字段进行修改
ALTER  TABLE 表名 MODIFY COLUMN 字段名 新数据类型 新类型长度  新默认值  新注释; -- COLUMN可以省略
alter  table table1 modify  column column1  decimal(10,1) DEFAULT NULL COMMENT '注释'; -- 正常，能修改字段类型、类型长度、默认值、注释

mysql修改字段名：
ALTER  TABLE 表名 CHANGE 旧字段名 新字段名 新数据类型;     
alter  table table1 change column1 column1 varchar(100) DEFAULT 1.2 COMMENT '注释'; -- 正常，此时字段名称没有改变，能修改字段类型、类型长度、默认值、注释
alter  table table1 change column1 column2 decimal(10,1) DEFAULT NULL COMMENT '注释' -- 正常，能修改字段名、字段类型、类型长度、默认值、注释
alter  table table1 change column2 column1 decimal(10,1) DEFAULT NULL COMMENT '注释' -- 正常，能修改字段名、字段类型、类型长度、默认值、注释
alter  table table1 change column1 column2; -- 报错  
```

### 替换特定字段的值

```
update hoyi_zfb_activity_enroll set shop_name = replace(shop_name,'Test',''); 
```

### 查找库中含有特定字段的表

```
SELECT * FROM information_schema.columns WHERE column_name='shop_name' AND table_schema = 'tyrcb14'; 
SELECT * FROM information_schema.tables WHERE TABLE_NAME LIKE '%shop%' AND table_schema = 'tyrcb14'; 
```

### 修改auto_increment

```
alter table hoyi_etc_order auto_increment=38;
```

### 查询FOREIGN_KEY_CHECKS的值

```
SELECT @@FOREIGN_KEY_CHECKS; 
```

### 备份数据库

```
mysqldump -utest -p123 --databases test  > testdp.sql
mysqldump -utest -p123 --databases test  < testdp.sql
```

### MYSQL卡死了就这样搞

```
SHOW PROCESSLIST;
SELECT * FROM information_schema.innodb_trx;
SELECT * FROM  performance_schema.events_statements_current WHERE sql_text LIKE '%video%';
KILL XXX;
```

### Mysql复制表结构、表数据的方法

```
1、复制表结构及数据到新表（不包含主键、索引、分区等）

CREATE TABLE 新表 SELECT * FROM 旧表

或 CREATE TABLE 新表 AS SELECT * FROM 旧表

这种方法将旧表基本结构和数据复制到新表。

不过这种方法的一个最不好的地方就是新表中没有了旧表的主键、索引、Extra（auto_increment，字符集编码及排序）、注释、分区等属性 以及触发器、外键等。

2、只复制表结构到新表

CREATE TABLE 新表 SELECT * FROM 旧表 WHERE 1=2 （只是第一种方式去除掉数据）

CREATE TABLE 新表 LIKE 旧表

这种方式的复制可以复制旧表的主键、索引、Extra（auto_increment，字符集编码及排序）、注释、分区等属性。但是不包含触发器、外键等

3、复制旧表的数据到新表

INSERT INTO 新表 SELECT * FROM 旧表

INSERT INTO 新表(字段1,字段2,.......) SELECT 字段1,字段2,...... FROM 旧表

上面两条语句的前提是新表已经存在

4、复制表结构及数据到新表（包含主键、索引、分区等）

结合上述第2、3点，即：

先 CREATE TABLE 新表 LIKE 旧表

然后 INSERT INTO 新表 SELECT * FROM 旧表
```

### 导出表结构和数据

```
1.导出结构不导出数据
mysqldump -d 数据库名 -uroot -p > xxx.sql

2.导出数据不导出结构
mysqldump -t 数据库名 -uroot -p > xxx.sql

3.导出数据和表结构
mysqldump 数据库名 -uroot -p > xxx.sql

4.导出特定表的结构
mysqldump -uroot -p -B数据库名 --table 表名 > xxx.sql
```
