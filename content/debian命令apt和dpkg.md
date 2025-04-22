title: debian命令apt和dpkg用法
date: 2019-07-05
category: 技术
tag: debian,apt,dpkg

[TOC]

### 1. apt命令用法

#### 从软件源服务器获取最新的软件信息并缓存到本地

```
apt update
```

因为很多apt的其他命令都是要通过比对版本信息来进行操作的，如果每次都去对比线上的版本信息效率肯定不理想，也没必要，所以做了一个缓存的机制。

#### 从本地仓库中对比系统中所有已安装的软件，如果有新版本的话则进行升级

```
apt upgrade
```

#### 列出本地仓库中所有的软件包名

```
apt list
```

#### 从本地仓库中查找指定的包名

```
apt list [package]
```

支持通配符，比如"apt list zlib*"就能列出以zlib开头的所有包名

#### 列出系统中所有已安装的包名

```
apt list --installed
```

#### 与list类似，通过给出的关键字进行搜索，列出所有的包和其描述

```
apt search [key]
```

#### 列出指定包的详细情况

```
apt show [package]
```

列出指定包的详细情况，包名要填写完整。

可以看到非常完整的信息，比如版本、大小、依赖的其他包等。

#### 安装指定的包，并同时安装其依赖的其他包

```
apt install [package]
```

#### 卸载包，但不删除相关配置文件

```
apt remove [package]
```

包名支持通配符

#### 卸载因安装软件自动安装的依赖，而现在又不需要的依赖包

```
apt autoremove
```

#### 卸载包，同时删除相关配置文件

```
apt purge [package]
```

包名支持通配符

#### 删除所有已下载的软件包

```
apt clean
```

#### 类似clean，但删除的是过期的包（即已不能下载或者是无用的包）

```
apt autoclean
```

### 2. dpkg命令用法

dpkg是一个Debian的一个命令行工具，它可以用来安装、删除、构建和管理Debian的软件包。
下面是它的一些命令解释：

#### 安装软件

```
命令行：dpkg -i <.deb file name>
示例：dpkg -i avg71flm_r28-1_i386.deb
```

#### 安装一个目录下面所有的软件包

```
命令行：dpkg -R
示例：dpkg -R /usr/local/src
```

#### 释放软件包，但是不进行配置

```
命令行：dpkg –unpack package_file 如果和-R一起使用，参数可以是一个目录
示例：dpkg –unpack avg71flm_r28-1_i386.deb
```

#### 重新配置和释放软件包

```
命令行：dpkg –configure package_file
如果和-a一起使用，将配置所有没有配置的软件包
示例：dpkg –configure avg71flm_r28-1_i386.deb
```

#### 删除软件包（保留其配置信息）

```
命令行：dpkg -r
示例：dpkg -r avg71flm
```

#### 替代软件包的信息

```
命令行：dpkg –update-avail <Packages-file>
```

#### 合并软件包信息

```
dpkg –merge-avail <Packages-file>
```

#### 从软件包里面读取软件的信息

```
命令行：dpkg -A package_file
```

#### 删除一个包（包括配置信息）

```
命令行：dpkg -P
```

#### 丢失所有的Uninstall的软件包信息

```
命令行：dpkg –forget-old-unavail
```

#### 删除软件包的Avaliable信息

```
命令行：dpkg –clear-avail
```

#### 查找只有部分安装的软件包信息

```
命令行：dpkg -C
```

#### 比较同一个包的不同版本之间的差别

```
命令行：dpkg –compare-versions ver1 op ver2
```

#### 显示帮助信息

```
命令行：dpkg –help
```

#### 显示dpkg的Licence

```
命令行：dpkg –licence (or) dpkg –license
```

#### 显示dpkg的版本号

```
命令行：dpkg –version
```

#### 建立一个deb文件

```
命令行：dpkg -b direc×y [filename]
```

#### 显示一个Deb文件的目录

```
命令行：dpkg -c filename
```

#### 显示一个Deb的说明

```
命令行：dpkg -I filename [control-file]
```

#### 搜索Deb包

```
命令行：dpkg -l package-name-pattern
示例：dpkg -I vim
```

#### 显示所有已经安装的Deb包，同时显示版本号以及简短说明

```
命令行：dpkg -l
```

#### 报告指定包的状态信息

```
命令行：dpkg -s package-name
示例：dpkg -s ssh
```

#### 显示一个包安装到系统里面的文件目录信息

```
命令行：dpkg -L package-Name
示例：dpkg -L apache2
```

#### 搜索指定包里面的文件（模糊查询）

```
命令行：dpkg -S filename-search-pattern
```

#### 显示包的具体信息

```
命令行：dpkg -p package-name
示例：dpkg -p cacti
```
