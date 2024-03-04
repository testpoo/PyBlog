title: shell三剑客简介
date: 2024-02-29
category: linux
tag: awk grep sed

[TOC]

### 1. shell三剑客简介

awk、grep、sed是linux操作文本的三大利器，合称文本三剑客，也是必须掌握的linux命令之一。三者的功能都是处理文本，但侧重点各不相同，其中属awk功能最强大，但也最复杂。grep更适合单纯的查找或匹配文本，sed更适合编辑匹配到的文本，awk更适合格式化文本，对文本进行较复杂格式处理。

**三剑客的特点:**

| **命令** | **特点**    | **使用场景**           |
|:------ |:--------- |:------------------ |
| grep   | 擅长查找过滤    | 快速查找过滤             |
| sed    | 擅长取行和替换   | 需要快速进行替换/修改文件内容    |
| awk    | 擅长取列、统计计算 | 文件取列、数据切片、对比/比较和统计 |

### 2. 三剑客之grep

grep 命令是一种强大的文本搜索工具，它能使用正则表达式搜索文本，并把匹配的行打印出来。grep全称是 Global Regular Expression Print，表示全局正则表达式版本，它的使用权限是所有用户。

grep是文本查找或搜索工具，用于查找内容包含指定的范本样式的文本。它会一行一行循环匹配，匹配到相应的值时会先输出，然后换行继续匹配再换行直到所有的内容都匹配完。

命令格式：`grep [option] pattern file`

大家熟悉的命令：`ps -ef|grep xxxx`

#### 2.1. 常用参数

* -n：显示行号；

* -i：忽略大小写；

* -o：精准匹配；

* -f：从文件每一行获取匹配模式；

* -c：统计匹配的行数；

* -E：使用扩展正则表达式，相当于egrep；

* -v：反转查找，即输出与查找条件不相符合的行；

* -A：后面可加数字，为 after 的意思，除了列出该行外，后续的 n 行也列出来；

* -B：后面可加数字，为 before 的意思，除了列出该行外，前面的 n 行也列出来；

* -C：后面可加数字，为context 的意思，除了列出该行外，前后的n行也列出来。

#### 2.2. 示例

**1.** 查找多个文件中相同的内容

```Shell
$ grep "我们" one two

one:我们下午没有课
two:我们是祖国的花朵
```

**2.** 输出two文件和one文件中相同的行

    $ grep -n -f one two
    
    3:心情挺好的

**3.** 输出在two文件中不在one文件中的行

    $ grep -v -f one two
    
    我们是祖国的花朵
    每天好开心啊

**4.** 输出正则匹配到的内容

    $ echo "this is a test shell!" |grep -oE "[a-z]+"
    
    this
    is
    a
    test
    shell

**5.** 只显示匹配的字符串

    $ echo "this is a test" |grep -o "is"
    
    is
    is

**6.** 匹配显示所有IP

    $ ip a |grep -oE -0 "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
    127.0.0.1
    --
    192.168.214.2
    192.168.214.255

### 3. 三剑客之sed

`sed` 是一种流编辑器，是非常好用的文本处理工具，配合正则使用更加强大。处理时，把当前处理的行存储在临时的缓冲区中，称为“模式空间”，接着 `sed` 命令处理缓冲区的内容，完成后输出到屏幕，接着处理下一行。文件内容没有改变，除非使用 `-i` 选项。

`sed` 主要用来编辑一个或多个文件，简化对文件的反复操作或者用来编写转换程序等。还有一个空间叫保持空间，又称暂存空间，可以暂时存放一些处理的数据，但不能直接输出，只能放到模式空间输出。

**语法格式：**`sed [选项] [地址] [命令] file`

#### 3.1 常用参数

**1.** 选项描述

* -n：不打印模式空间；

* -e：执行脚本、表达式来处理；

* -f：执行动作从文件读取执行；

* -i：修改原文件；

* -r：使用扩展正则表达式。

**2.** 地址描述

* first~step：步长，每step行，从第first开始；

* $：匹配最后一行；

* /regexp/：正则表达式匹配行；

* number：只匹配指定行；

* addr1,addr2：开始匹配addr1行开始，直接addr2行结束；

* addr1,+N：从addr1行开始，向后的N行；

* addr1,~N：从addr1行开始，到N行结束。

**3.** 地址描述

* s/regexp/replacement/：替换字符串；

* p：打印当前模式空间；

* P：打印模式空间的第一行；

* d：删除模式空间，开始下一个循环；

* D：删除模式空间的第一行，开始下一个循环；

* =：打印当前行号；

* a：当前行下面追加文本；

* i：当前行上面插入文本；

* c：所选行替换新文本；

* q：立即退出sed脚本；

* r：追加文本来自文件；

* : label：label为b和t命令；

* b label：分支到脚本中带有标签的位置，如果分支不存在则分支到脚本的末尾；

* t label：如果s///是一个成功的替换，才跳转到标签；

* h H：复制/追加模式空间到保持空间；

* g G：复制/追加保持空间到模式空间；

* x：交换模式空间和保持空间内容；

* y：把一个字符翻译为另外的字符；

* l：打印模式空间的行，并显示控制字符\$；

* n N：读取/追加下一行输入到模式空间；

* w filename：写入当前模式空间到文件；

* !：取反、否定；

* &：引用已匹配字符串。

#### 3.2. 示例

**1.** 从第一个空格开始全局替换成 `-`

    $ echo "hello world" | sed 's/ /-/g'
    
    hello-world

**2.** 匹配替换字符串

    $ echo "hello world" | sed 's/world/[&]/'
    
    hello [world]

**3.** 打印指定行的内容

    $ cat -n one
         1  今天天气不错
         2  挺风和日丽的
         3  我们下午没有课
         4  心情挺好的
    
    $ sed -n '2,4p' one
    
    挺风和日丽的
    我们下午没有课
    心情挺好的

**4.** 读取一个文件的内容到另一个文件的匹配位置显示

    # 把one的内容插入从three文件中通过"测试"匹配的“测试一下”后面，并打印出来
    $ cat one
    今天天气不错
    挺风和日丽的
    我们下午没有课
    心情挺好的
    
    $ cat three
    测试一下
    
    $ sed "/测试/r one" three
    测试一下
    今天天气不错
    挺风和日丽的
    我们下午没有课
    心情挺好的

**5.** 匹配一个文件的内容写入到另一个文件

    # 把从one中通过“今天”匹配的“今天天气不错”写入four
    $ sed "/今天/w four" one
    今天天气不错
    挺风和日丽的
    我们下午没有课
    心情挺好的
    
    $ cat four
    今天天气不错

**6.** 在匹配行后追加插入内容

    # 把“测试两下”插入到“今天”匹配的“今天天气不错”下面
    $ sed "/^今天/a测试两下" one
    今天天气不错
    测试两下
    挺风和日丽的
    我们下午没有课
    心情挺好的

**7.** 读取一个文件的内容写入到另一个文件的匹配位置

    # 加“-i”会直接写入文件
    $ sed -i "/测试/r one" three
    $ cat one
    今天天气不错
    挺风和日丽的
    我们下午没有课
    心情挺好的
    $ cat three
    测试一下
    今天天气不错
    挺风和日丽的
    我们下午没有课
    心情挺好的

**8.** 用s///直接替换字符串

    $ sed "s/今天/昨天/" one
    昨天天气不错
    挺风和日丽的
    我们下午没有课
    心情挺好的

**9.** 分别用first~step语法和命令n语法打印奇数行

    $ cat -n one
         1  今天天气不错
         2  挺风和日丽的
         3  我们下午没有课
         4  心情挺好的
    $ sed -n "1~2p" one
    今天天气不错
    我们下午没有课



    $ cat -n one
         1  今天天气不错
         2  挺风和日丽的
         3  我们下午没有课
         4  心情挺好的
    $ sed -n "p;n" one
    今天天气不错
    我们下午没有课

**10.** 分别用first~step语法和命令n语法打印偶数行

    $ cat -n one
         1  今天天气不错
         2  挺风和日丽的
         3  我们下午没有课
         4  心情挺好的
    $ sed -n "2~2p" one
    挺风和日丽的
    心情挺好的
    
    
    
    $ cat -n one
         1  今天天气不错
         2  挺风和日丽的
         3  我们下午没有课
         4  心情挺好的
    $ sed -n "n;p" one
    挺风和日丽的
    心情挺好的

### 4. 三剑客之awk

`awk` 是一个处理文本的编程语言工具，能用简短的程序处理标准输入或文件、数据排序、计算以及生成报表等等。

**命令格式**：`awk option 'pattern {action}' file`

* 其中pattern表示AWK在数据中查找的内容，而action是在找到匹配内容时所执行的一系列命令。花括号用于根据特定的模式对一系列指令进行分组。

awk处理的工作方式与数据库类似，支持对记录和字段处理，这也是grep和sed不能实现的。

在awk中，缺省的情况下将文本文件中的一行视为一个记录，逐行放到内存中处理，而将一行中的某一部分作为记录中的一个字段。用1,2,3...数字的方式顺序的表示行（记录）中的不同字段。用\$后跟数字，引用对应的字段，以逗号分隔，0表示整个行。

#### 4.1. 常用参数

**1. 选项**

* -f program-file：从文件中读取awk程序源文件；

* -F fs：指定fs为输入字段分隔符；

* -v var=value：变量赋值；

* --posix：兼容POSIX正则表达式；

* --dump-variables=[file]：把awk命令时的全局变量写入文件，默认文件是awkvars.out；

* --profile=[file]：格式化awk语句到文件，默认是awkprof.out。

**2. 常用模式**

| **Pattern**          | **Description**          |
|:-------------------- |:------------------------ |
| BEGIN{ }             | 给程序赋予初始状态，先执行的工作         |
| END{ }               | 程序结束之后执行的一些扫尾工作          |
| /regular expression/ | 为每个输入记录匹配正则表达式           |
| pattern && pattern   | 逻辑and，满足两个模式             |
| pattern              |                          |
| ! pattern            | 逻辑not，不满足模式              |
| pattern1, pattern2   | 范围模式，匹配所有模式1的记录，直到匹配到模式2 |

#### 4.2. 示例

**1.** 从文件读取awk程序处理文件

    $ nano test.awk
    {print $2}
    $ tail -n3 /etc/services |awk -f test.awk
    60179/tcp
    
    Local

**2.** 指定分隔符，打印指定字段，默认以空格分隔

    $ tail -n3 /etc/services |awk '{print $2}'
    60179/tcp
    
    Local

**3.** 指定冒号为分隔符打印

    # 这里要用单印号
    $ tail -n5 /etc/passwd | awk -F ':' '{print $1}'
    polkitd
    rtkit
    colord
    poo
    sshd

#### 4.3. BEGIN和END

**语法结构:** `awk 'BEGIN{ print "start" } pattern{ commands } END { print "end" }' filename` ，BEGIN语句+模式匹配+END语句三个部分组成，这三个部分都是可选项。

**工作原理**

* 第一步执行BEGIN语句；

* 第二步从文件或标准输入读取一行，然后再执行行pattern语句，逐行扫描文件到文件全部被读取；

* 第三步执行END语句。

**示例**

**1.** 通过print参数打印

    $ echo "hello" | awk 'BEGIN{print "welcome"} {print} END{print "this is a test of awk"}'
    welcome
    hello
    this is a test of awk

**2.** 初始化标题打印

    $ tail /etc/services | awk 'BEGIN{print "Service\t\tPort\t\t\tDescription\n"}{print $0}'
    Service         Port                    Description
    
    sgi-cad         17004/tcp                       # Cluster Admin daemon
    binkp           24554/tcp                       # binkp fidonet protocol
    asp             27374/tcp                       # Address Search Protocol
    asp             27374/udp
    csync2          30865/tcp                       # cluster synchronization tool
    dircproxy       57000/tcp                       # Detachable IRC Proxy
    tfido           60177/tcp                       # fidonet EMSI over telnet
    fido            60179/tcp                       # fidonet EMSI over TCP
    
    # Local services

**3.** 使用print逗号分隔时，打印则是以空格分界

    $ echo | awk '{a="This is"; b="a test"; c="of awk";print a,b,c}'
    
    This is a test of awk

#### 4.4. 内置变量

| **变量名**    | **描述**                                         |
|:---------- |:---------------------------------------------- |
| $0         | 当前记录                                           |
| $1~$n    | 当前记录的第N个字段                                     |
| FS         | 输入字段分隔符（-F作用相同）默认空格                            |
| OFS        | 输出字段分隔符，默认是空格                                  |
| RS         | 输入记录分隔符，默认换行符\n                                |
| ORS        | 输出记录分隔符，默认是换行符\n                               |
| NF         | 字段个数/列个数                                       |
| NR         | 统计记录编号，每处理一行记录，编号就会+1                          |
| FNR        | 统计记录编号，每处理一行记录，编号也会+1，与NR不同的是，处理第二个文件时，编号会重新计数 |
| OFS        | 输出字段分隔符，默认空格                                   |
| IGNORECASE | 忽略大小写                                          |



**示例**

**1.** FS

创建带空格的测试文件，查看前赋值FS变量，改变默认分空隔符为冒号。

    $ cat test1.awk
    aa:bb:cc
    dd:ee:ff
    $ awk 'BEGIN{FS=":"}{print $1,$2,$3}' test1.awk
    aa bb cc
    dd ee ff

**2.** OFS，`OFS` 可以理解为 `FS` 的逆向过程，即将输出字段的分隔符改为空格

创建带：的测试文件，查看前赋值 `OFS` 变量，改变默认：隔符为空格。

    $ cat test2.awk
    aa bb cc
    dd ee ff
    $ awk 'BEGIN{OFS=":"}{print $1,$2,$3}' test2.awk
    aa:bb:cc
    dd:ee:ff

**3.** RS，匹配分隔符号，默认以\n分隔每行

将/替换为换行（\n）输出：

    $ echo "RS/test/of/awk" | awk 'BEGIN{RS="/"}{print $0}'
    RS
    test
    of
    awk

**4.** ORS，匹配每个记录的换行符（\n）,替换为指定的符号

将换行（\n）替换为+：

    $ seq 10 | awk 'BEGIN{ORS="+"}{print $0} END{print "\n"}'
    
    1+2+3+4+5+6+7+8+9+10+

**5.** NF，字段个数/列个数

打印字段个数：

    $ echo "a b c d e f" | awk '{print NF}'
    
    6

打印最后一个字段：

    $ echo "a b c d e f" | awk '{print $NF}'
    
    f

打印倒数第二个字段：

    $ echo "a b c d e f" | awk '{print $(NF-1)}'
    e

排除最后两个字段：

    $ echo "a b c d e f" | awk '{$NF="";$(NF-1)="";print $0}'
    a b c d

排除第一个字段：

    $ echo "a b c d e f" | awk '{$1="";print $0}'
     b c d e f

#### 4.5. 运算符

| **运算符**             | **描述**                                                  |
|:------------------- |:------------------------------------------------------- |
| （....）              | 分组                                                      |
| $                   | 字段引用                                                    |
| ++ --               | 递增和递减                                                   |
| + - !               | 加号，减号，和逻辑否定                                             |
| * / %               | 乘，除和取余                                                  |
| + -                 | 加法，减法                                                   |
|                     |                                                         |
| < > <= >= != ==     | 关系运算符                                                   |
| ~ !~                | 正则表达式匹配，否定正则表达式匹配                                       |
| in                  | 数组成员                                                    |
| &&                  |                                                         |
| ?:                  | 简写条件表达式：expr1 ? expr2 : expr3第一个表达式为真，执行expr2，否则执行expr3 |
| = += -= *= /= %= ^= | 变量赋值运算符                                                 |

示例:

**1.** 求和

    $ awk 'BEGIN{a=2;b=3; print a+b }'
    
    5

**2.** 感叹号 否定匹配

    $ tail /etc/services |awk '!/blp5/{print $0}'
    
    sgi-cad         17004/tcp                       # Cluster Admin daemon
    binkp           24554/tcp                       # binkp fidonet protocol
    asp             27374/tcp                       # Address Search Protocol
    asp             27374/udp
    csync2          30865/tcp                       # cluster synchronization tool
    dircproxy       57000/tcp                       # Detachable IRC Proxy
    tfido           60177/tcp                       # fidonet EMSI over telnet
    fido            60179/tcp                       # fidonet EMSI over TCP
    
    # Local services

**3.** 求余

打印偶数行

    $ seq 5 |awk '$0%2==0{print $0}'
    
    2
    4

打印奇数行

    $ seq 5 |awk '$0%2!=0{print $0}'
    1
    3
    5

**4.** 正则表达式匹配

    $ seq 5 |awk '$0%2!=0{print $0}'
    1
    3
    5
    
    $ seq 5 |awk '$0!~/[34]/{print $0}'
    1
    2
    5
    
    $ seq 5 |awk '$0!~/[^34]/{print $0}'
    3
    4

**5.** ?: 条件表达式，也叫三目运算

    $ awk 'BEGIN{print 1==1?"yes":"no"}'
    yes
    
    $ awk 'BEGIN{print 1==2?"yes":"no"}'
    no

**6.** 变量赋值

    $ seq 5 |awk '{sum+=$0}END{print sum}'
    
    15

**6. 流程控制**

* `if` 语句

**格式：**`if (condition) statement [ else statement ]`

    $ seq 5 |awk '{if($0==3)print $0}'
    3
    
    $ seq 5 |awk '{if($0==3)print $0;else print "no"}'
    no
    no
    3
    no
    no

* `while` 语句

**格式：**`while (condition) statement`

遍历打印所有字段。

```Shell
$ awk '{i=1;while(i<=NF){print $i;i++}}' one

今天天气不错
挺风和日丽的
我们下午没有课
心情挺好的
```

* `for` 语句

**格式：**`for (expr1; expr2; expr3) statement`

遍历打印所有字段。

```Shell
$ awk '{for(i=1;i<=NF;i++)print $i}' one

今天天气不错
挺风和日丽的
我们下午没有课
心情挺好的
```

* `break` 和 `continue` 语句

`break` 跳过所有循环，`continue` 跳过当前循环。

```Shell
$ awk 'BEGIN{for(i=1;i<=5;i++){if(i==3){break};print i}}'
1
2

$ awk 'BEGIN{for(i=1;i<=5;i++){if(i==3){continue};print i}}'
1
2
4
5
```
