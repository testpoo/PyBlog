title:svn命令全解
date:2019-10-11
category:笔记
tag:svn

[TOC]

#### 将文件checkout到本地

```
svn checkout path(path是服务器的目录)

例如 ：svn checkout svn://192.168.214.1/pro/domain
```

#### 往版本库中添加新的文件

```
svn add filename

例如：svn add test.cpp
```

#### 将改动的文件提交到版本库

```
svn commit -m "注释" [-N] [--no-unlock] PATH(如果选择了保持锁，就使用--no-unlock开关)

例如：svn commit -m "注释" test.cpp

简写：svn ci
```

#### 加锁/解锁

```
svn lock -m "注释" path

例如: svn lock -m "注释" test.cpp

svn unlock path
```

#### 更新到某个版本

```
svn update -r 版本号 path

svn update 更新当前目录以及子目录下的所有文件到最新版本

svn upate -r 200 test.cpp 将版本库中的test.cpp还原到版本200

简写 svn up
```

#### 查看文件或者目录状态

```
（1）svn status path （显示目录下的文件和子目录下的文件状态,正常状态不显示）

【?:不在svn控制中;M:内容被修改;C：发生冲突;A:预定义加入到版本库;K:被锁定】

（2）svn status -v path （显示文件和子目录状态）

注意：svn status、svn diff和svn revert这三条命令在没有网络情况下可以执行，因为svn在本地.svn中保留了本地版本原始拷贝。

简写： svn st
```

#### 删除文件

```
svn delete path -m "注释"

例如: svn delete svn://192.168.####1/pro/domain/test.cpp -m "delete test file"

或者直接svn delete test.php 然后再svn ci -m 'delete test file‘，推荐使用这种

简写： svn (del、remove、rm)
```

#### 查看日志

```
svn log path
```

#### 查看文件详细信息

```
svn info path
```

#### 比较差异

```
svn diff path（将修改的文件与基础版本比较）

svn diff -r m:n （将修改的文件m版本和n版本比较）

简写 svn di
```

#### 将两个版本的文件的差异合并到当前文件

```
svn merge -r m:n path

 例如：svn merge -r 20:25 test.cpp（将版本20与25之间的差异合并到当前文件，但一般会发生冲突，需要处理一下）
```

#### SVN帮助

```
svn help

以上为常用命令，下面为不常用命令
```

#### 查看版本库下的文件和列表

```
svn list path （显示path目录下的所属于版本的文件和目录）

简写: svn ls
```

#### 创建纳入版本控制下的新目录

```
svn mkdir: 创建纳入版本控制下的新目录。

用法: 1、mkdir PATH...
         2、mkdir URL...
创建版本控制的目录。
1、每一个以工作副本 PATH 指定的目录，都会创建在本地端，并且加入新增调度，以待下一次的提交。
2、每个以URL指定的目录，都会透过立即提交于仓库中创建。在这两个情况下，所有的中间目录都必须事先存在。
```

#### 恢复本地修改

```
svn revert：恢复原始未改变的工作副本文件（恢复大部分的本地修改）revert用法：revert path

注意：本子命令不会存储网络，并且会解除冲突的情况。但它不会恢复被创建的目录
```

#### 代码库URL变更

```
svn switch(sw): 更新工作副本到不同的URL。

用法 
1、switch URL [PATH]

2、switch --relocate FROM TO [PATH]

1、更新工作副本，映射到一个新的URL，会将服务上的文件与本地文件合并。这是将工作副本对应到同一创库的某个分支或者标记的方法。

2、改写工作副本URL元数据，以反映URL的变更，创库URL变动但工作副本仍旧对映同一创库的同一目录时使用该命令更新工作副本与创库的对应关系。
```

#### 解决冲突

```
svn resolved：移除工作副本的目录或文件的“冲突”状态。

用法 resolved path

注意：本子命令不会依语法来解决冲突或是移除冲突标记；它只是移除冲突的相关文件，然后让path可以再次提交。
```

#### 输出指定文件的URL内容

```
svn cat 目标[@版本] 如果指定了版本将从指定的版本开始查找。
```