title:Linux下SVN服务器的搭建
date:2020-01-01
category:笔记
tag:svn, linux

[TOC]

### Ubuntu下SVN服务器的配置及搭建

SVN是Subversion的简称，是一个开放源代码的版本控制系统，相较于RCS、CVS，它采用了分支管理系统，它的设计目标就是取代CVS。互联网上很多版本控制服务已从CVS迁移到Subversion。说得简单一点SVN就是用于多个人共同开发同一个项目，共用资源的目的。

#### 检查是否安装SVN

```
dpkg --get-selections|grep 'subversion'
```

如果安装了，会有如下提示

```
root@ubuntu:~$ dpkg --get-selections|grep 'subversion'
subversion                                      install
```

如果没有安装，使用以下命令安装

```
apt install subversion
```

#### 配置svn并启动svn服务

可以使用svnserve --help查看启动帮助

```
root@ubuntu:~# svnserve --help
usage: svnserve [-d | -i | -t | -X] [options]
Subversion repository server.
Type 'svnserve --version' to see the program version.

Valid options:
  -d [--daemon]            : 后台模式
  -i [--inetd]             : inetd 模式
  -t [--tunnel]            : 隧道模式
  -X [--listen-once]       : 监听一次方式(调试用)
  -r [--root] ARG          : 服务的根目录
  -R [--read-only]         : 强制只读；覆盖版本库配置文件
  --config-file ARG        : 从文件 ARG 读取配置
  --listen-port ARG        : listen port. The default port is 3690.
                             [mode: daemon, listen-once]
  --listen-host ARG        : listen hostname or IP address
                             By default svnserve listens on all addresses.
                             [mode: daemon, listen-once]
  -6 [--prefer-ipv6]       : 在使用主机名称监听时，首选 IPv6
                             [默认首选 IPv4。不支持在守护进程模式中同时使用 IPv4
                             和 IPv6。如果需要，请使用 inetd 模式或隧道模式。]
  -c [--compression] ARG   : 用于网络传输的压缩级别
                             [0 .. 不压缩, 5 .. 默认,
                              9 .. 最大压缩]
  -M [--memory-cache-size] ARG : size of the extra in-memory cache in MB used to
                             minimize redundant operations.
                             Default is 16.
                             0 switches to dynamically sized caches.
                             [used for FSFS and FSX repositories only]
  --cache-txdeltas ARG     : enable or disable caching of deltas between older
                             revisions.
                             Default is yes.
                             [used for FSFS and FSX repositories only]
  --cache-fulltexts ARG    : enable or disable caching of file contents
                             Default is yes.
                             [used for FSFS and FSX repositories only]
  --cache-revprops ARG     : enable or disable caching of revision properties.
                             Consult the documentation before activating this.
                             Default is no.
                             [used for FSFS and FSX repositories only]
  --client-speed ARG       : Optimize network handling based on the assumption
                             that most clients are connected with a bitrate of
                             ARG Mbit/s.
                             Default is 0 (optimizations disabled).
  --block-read ARG         : Parse and cache all data found in block instead
                             of just the requested item.
                             Default is no.
                             [used for FSFS repositories in 1.9 format only]
  -T [--threads]           : 使用线程代替进程 [方式: daemon]
  --min-threads ARG        : Minimum number of server threads, even if idle.
                             Capped to max-threads; minimum value is 0.
                             Default is 1.
                             [used only with --threads]
  --max-threads ARG        : Maximum number of server threads, even if there
                             are more connections.  Minimum value is 1.
                             Default is 256.
                             [used only with --threads]
  --foreground             : 在前台运行(调试用)
                             [方式: daemon]
  --single-thread          : handle one connection at a time in the parent
                             process (useful for debugging)
  --log-file ARG           : svnserve 日志文件
  --pid-file ARG           : 写进程 PID 到文件 ARG
                             [方式: daemon, listen-once]
  --tunnel-user ARG        : 隧道用户名(默认是当前UID对应的用户名)
                             [方式: tunnel]
  -h [--help]              : 显示本帮助
  --virtual-host           : virtual host mode (look for repo in directory
                             of provided hostname)
  --version                : 显示程序版本信息
  -q [--quiet]             : 在标准错误输出不显示进度 (仅错误)
```

指定svn的数据存储路径

```
mkdir -p /home/poo/svn/data
```

指定svn的配置文件信息路径

```
mkdir -p /home/poo/svn/passwd
```

启动svn服务

```
svnserve -d -r /home/poo/svn/data
```

#### 检测svn服务是否正常启动

第一通过进程检测

```
root@ubuntu:~# ps -ef|grep svn
root        76     1  0 21:15 ?        00:00:00 svnserve -d -r /home/poo/svn/data/
root        78    52  0 21:15 tty1     00:00:00 grep --color=auto svn
```

第二通过端口3690检测

```
netstat -lntup | grep 3690
```

第三通过文件检测

```
lsof -i :3690
```

#### 使用svnadmin建立svn项目版本库

查看创建项目版本库命令

```
svnadmin --help
```

```
root@ubuntu:~# svnadmin --help
general usage: svnadmin SUBCOMMAND REPOS_PATH  [ARGS & OPTIONS ...]
Subversion repository administration tool.
Type 'svnadmin help <subcommand>' for help on a specific subcommand.
Type 'svnadmin --version' to see the program version and FS modules.

Available subcommands:
   crashtest
   create
   delrevprop
   deltify
   dump
   freeze
   help (?, h)
   hotcopy
   info
   list-dblogs
   list-unused-dblogs
   load
   lock
   lslocks
   lstxns
   pack
   recover
   rmlocks
   rmtxns
   setlog
   setrevprop
   setuuid
   unlock
   upgrade
   verify
```

```
svnadmin help create
```

```
root@ubuntu:~# svnadmin help create
create: 用法: svnadmin create REPOS_PATH

在 REPOS_PATH 创建一个新的空版本库。

有效选项:
  --bdb-txn-nosync         : 在提交事务时禁用fsync [BDB]
  --bdb-log-keep           : 禁用自动删除日志文件 [BDB]
  --config-dir ARG         : 从目录 ARG 读取用户配置文件
  --fs-type ARG            : type of repository:
                             'fsfs' (default), 'bdb' or 'fsx'
                             CAUTION: FSX is for EXPERIMENTAL use only!
  --compatible-version ARG : use repository format compatible with Subversion
                             version ARG ("1.5.5", "1.7", etc.)
  --pre-1.4-compatible     : 已经淘汰; 参见 --compatible-version
  --pre-1.5-compatible     : 已经淘汰; 参见 --compatible-version
  --pre-1.6-compatible     : 已经淘汰; 参见 --compatible-version
```

创建testdoc版本库

```
root@ubuntu:~# svnadmin create /home/poo/svn/data/testdoc
root@ubuntu:~# ll /home/poo/svn/data/testdoc/
总用量 0
drwxr-xr-x 0 root root 512 12月  9 21:26 conf/
drwxr-sr-x 0 root root 512 12月  9 21:26 db/
-r--r--r-- 1 root root   2 12月  9 21:26 format
drwxr-xr-x 0 root root 512 12月  9 21:26 hooks/
drwxr-xr-x 0 root root 512 12月  9 21:26 locks/
-rw-r--r-- 1 root root 246 12月  9 21:26 README.txt
```

#### 配置testdoc版本可的权限

进入testdoc版本库配置目录,并备份配置文件

```
cd /home/poo/svn/data/testdoc/conf/
cp -p svnserve.conf svnserve.conf.default
```

进行详细配置

```
anon-access = none //禁止匿名访问
auth-access = write //认证后有读的权限
password-db = /home/poo/svn/passwd/passwd //指定密码文件
authz-db = /home/poo/svn/passwd/authz //指定权限认证文件
```

svnserve.conf文件general的一部分

```
[general]
### The anon-access and auth-access options control access to the
### repository for unauthenticated (a.k.a. anonymous) users and
### authenticated users, respectively.
### Valid values are "write", "read", and "none".
### Setting the value to "none" prohibits both reading and writing;
### "read" allows read-only access, and "write" allows complete
### read/write access to the repository.
### The sample settings below are the defaults and specify that anonymous
### users have read-only access to the repository, while authenticated
### users have read and write access to the repository.
anon-access = none
auth-access = write
### The password-db option controls the location of the password
### database file.  Unless you specify a path starting with a /,
### the file's location is relative to the directory containing
### this configuration file.
### If SASL is enabled (see below), this file will NOT be used.
### Uncomment the line below to use the default password file.
password-db = /home/poo/svn/passwd/passwd
### The authz-db option controls the location of the authorization
### rules for path-based access control.  Unless you specify a path
### starting with a /, the file's location is relative to the
### directory containing this file.  The specified path may be a
### repository relative URL (^/) or an absolute file:// URL to a text
### file in a Subversion repository.  If you don't specify an authz-db,
### no path-based access control is done.
### Uncomment the line below to use the default authorization file.
authz-db = /home/poo/svn/passwdauthz
```

复制passwd和authz文件到passwd目录并修改权限

```
cp -p passwd authz /home/poo/svn/passwd/
cd /home/poo/svn/passwd/
chmod 700 authz passwd
```

#### 为Svn版本库创建用户并授权访问指定项目版本库

编辑passwd文件配置用户和密码

```
vi passwd 
xiaowei = 123456
shenyi = 123456
```

passwd文件

```
### This file is an example password file for svnserve.
### Its format is similar to that of svnserve.conf. As shown in the
### example below it contains one section labelled [users].
### The name and password for each user follow, one account per line.

[users]
# harry = harryssecret
# sally = sallyssecret

# 等号前是用户名，后面是密码
xiaowei = 123456
shenyi = 123456

# 测试账号
test1 = 123456
test2 = 123456
test3 = 123456
```

编辑authz文件配置读取权限

```
[<版本库>:/项目/目录]
@<用户组名> = <权限>
<用户名>  = <权限>
```

authz文件

```
### This file is an example authorization file for svnserve.
### Its format is identical to that of mod_authz_svn authorization
### files.
### As shown below each section defines authorizations for the path and
### (optional) repository specified by the section name.
### The authorizations follow. An authorization line can refer to:
###  - a single user,
###  - a group of users defined in a special [groups] section,
###  - an alias defined in a special [aliases] section,
###  - all authenticated users, using the '$authenticated' token,
###  - only anonymous users, using the '$anonymous' token,
###  - anyone, using the '*' wildcard.
###
### A match can be inverted by prefixing the rule with '~'. Rules can
### grant read ('r') access, read-write ('rw') access, or no access
### ('').

[aliases]
# joe = /C=XZ/ST=Dessert/L=Snake City/O=Snake Oil, Ltd./OU=Research Institute/CN=Joe Average

[groups]
# harry_and_sally = harry,sally
# harry_sally_and_joe = harry,sally,&joe
# 这里可以定义组，多个用户这间用逗号隔开
test = test1,test2,test3

# [/foo/bar]
# harry = rw
# &joe = r

[testdoc:/]
@test = rw
xiaowei = rw
shenyi = r
```

#### 重新启动svn服务进行验证

杀死svn服务

```
pkill svnserve
```

启动svn

```
svnserve -d -r /home/poo/svn/data/
```

备注：修改passwd和authz文件不需要重启svn服务，而修改svnserve.conf则需要

最后安装客户端进行testdoc的配置是否正确

```
svn --username=xiaowei co svn://127.0.0.1/testdoc
```

```
root@ubuntu:# svn --username=xiaowei co svn://127.0.0.1/testdoc
认证领域: <svn://127.0.0.1:3690> f36acfd9-8e0c-4973-bd35-44e75440e1c3
“xiaowei”的密码: ******


-----------------------------------------------------------------------
注意!  你的密码，对于认证域:

   <svn://127.0.0.1:3690> f36acfd9-8e0c-4973-bd35-44e75440e1c3

只能明文保存在磁盘上!  如果可能的话，请考虑配置你的系统，让 Subversion
可以保存加密后的密码。请参阅文档以获得详细信息。

你可以通过在“/root/.subversion/servers”中设置选项“store-plaintext-passwords”为“yes”或“no”，
来避免再次出现此警告。
-----------------------------------------------------------------------
保存未加密的密码(yes/no)? yes
取出版本 0。
```