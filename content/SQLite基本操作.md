title:SQLite基本操作
date:2020-01-02
category:笔记
tag:sqlite, 笔记

[TOC]

```
# 查看当前数据库所有表
sqlite>.tables

# 查看当前数据库指定表
sqlite>.tablestable_name

# 查看当前数据库所有表的建表(CREATE)语句
sqlite>.schema

# 查看指定数据表的建表语句
sqlite>.schematable_name

# 查看所有表结构及索引信息
sqlite>select*fromsqlite_masterfrom;

# 查看所有表结构信息
sqlite>select*fromsqlite_masterwheretype='table';

# 对于表来说，name字段指表名，查询所有表
sqlite>selectnamefromsqlite_masterwheretype='table';

# 查看指定表结构信息
sqlite>select*fromsqlite_masterwheretype='table'andname='table_name';

# 查看所有表索引信息，查询所有索引
sqlite>select*fromsqlite_masterwheretype='index';

# 对于索引来说，name字段指索引名
sqlite>selectnamefromsqlite_masterwheretype='table';

# 查看指定表索引信息
sqlite>select*fromsqlite_masterwheretype='index'andname='table_name';

# 查看指定表所有字段信息，类似于msyql：desctable_name
sqlite>pragmatable_info('table_name')

# 查看指定表字段【column】类型，括号内可不输引号
sqlite>selecttypeof('column')fromtable_name;
```