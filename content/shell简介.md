title: shell简介
date: 2022-04-18
category: linux
tag: shell

[TOC]

### 本文摘要

本文主要介绍Linux Shell编程的基础知识，包含下面8个方面：

1. Shell编程概述

2. Shell关键字

3. Shell变量

4. Shell运算

5. Shell语句

6. Shell函数

7. Shell调试

8. Shell易错点

### Shell编程概述

在Linux下有一门脚本语言叫做：Shell脚本。Shell 是外壳的意思，就是操作系统的外壳。我们可以通过 Shell 命令来操作和控制系统，比如 Linux 中的 Shell 命令就包括 ls、cd、pwd等等，Shell 是一个命令解释器，它通过接受用户输入的 Shell 命令来启动、暂停、停止的运行或对计算机进行控制。

Shell 是一个应用程序，它连接了用户和 Linux 内核，让用户能够更加高效、安全、低成本地使用 Linux 内核，这就是 Shell 的本质。

Shell 本身并不是内核的一部分，它中是站在内核的基础上编写的一个应用程序。

那什么是 Shell 脚本。Shell 脚本就是由 Shell 命令组成的执行文件，将一些命令整合到一个文件中，进行处理业务逻辑，脚本不用编译即可运行。它通过解释器运行，所以速度相对来主说比较慢。

一个简单的hello.sh脚本像下面这样，第一行#！/bin/bash标识该脚本由哪个Shell解释：

```shell
#!/bin/bash

echo "Hello World!"
```

**赋予权限才可以执行**

```shell
# 赋予可执行权限
chmod +x hello.sh

# 执行
./hello.sh

# 结果
Hello World!
```

Shell的编写流程：

1. 编写Shell脚本

2. 赋予可执行权限

3. 执行，调试

下面来介绍具体的用法。

### Shell 注释

- 单行注释：#
- 多行注释：:,<<

看个例子

```shell
# 这个是单行注释
```

```shell
<<COMMENT
    这个是多行注释
    这个是多行注释
    这个是多行注释
COMMENT

: '
这个也是多行注释(: + 空格 + 单引号)
这个也是多行注释(: + 空格 + 单引号)
这个也是多行注释(: + 空格 + 单引号)
'
```

### Shell关键字

常用的关键字如下：

1. echo: 打印文字到屏幕

2. exec: 执行另一个Shell脚本

3. read: 读标准输入

4. expr: 对整数型变量进行算术运算

5. test: 用于测试变量是否相等、是否为空、文件类型等

6. exit: 退出

看个例子：

```shell
#!/bin/bash

echo "hello Shell"

# 读入变量
read VAR
echo "VAE is $VAR"

# 计算变量
expr $VAR -5

# 测试字符串
test "Hello"="Helloword"

# 测试整数
test -d ./Android

# 执行其他Shell脚本
exec ./othershell.sh

# 退出
exit
```

运行前，你需要新建一个`othershell.sh`的文件，让它输出`I'm othershell`，并且中途需要一次输入，我这里输入的是10：

```shell
Hello Shell
10
VAR is 10
5
I'm othershell
```

学习任何一门语言都要了解它的变量定义方法，Shell也不例外。

### Shell变量

Shell变量分为3种：

1. 用户自定义变量

2. 预定义变量

3. 环境变量

定义变量需要注意下面2点：

1. 等号前后不要有空格：NUM=10

2. 一般变量名用大写：M=1

使用$VAR调用变量：

```shell
echo $VAR
```

#### 1. 用户自定义变量

这种变量只支持字符串类型，不支持其他字符，浮点等类型，常见有这3个前缀：

1. unset: 删除变量

2. readonly: 标记只读变量

3. export: 指定全局变量

一个例子：

```shell
#!/bin/bash

# 定义旁通变量
CITY=SHENZHEN

# 定义全局变量
export NAME=cdeveloper

# 定义只读变量
readonly AGE=21

# 打印变量的值
echo $CITY
```

运维结果：

```
SHENZHEN
cdeveloper
21
```

#### 2. 预定义变量

预定义变量常用来获取命令行的输入，有下面这些：

1. $0: 脚本文件名
2. $1-9: 第1-9命令行参数名
3. $#: 命令行参数个数
4. $@: 所有命令行参数
5. $*: 所有命令行参数
6. $?: 前一个命令的退出状态，可用于获取函数返回值
7. \$$: 执行的进程ID
8. $!: 后台运行的最后一个进程的ID

一个例子：

```
#!/bin/bash

echo "print $"
echo "\$0 = $0"
echo "\$1 = $1"
echo "\$2 = $2"
echo "\$# = $#"
echo "\$@ = $@"
echo "\$* = $*"
echo "\$$ = $$"
echo "\$? = $?"
```

执行`./hello.sh 1 2 3 4 5`的结果：

```
print $

# 程序名
$0 = ./hello.sh

# 第一个参数
$1 = 1

# 第二个参数
$2 = 2

# 一共有5个参数
$# = 5

# 打印出所有参数
$@ = 1 2 3 4 5

# 打印出所有参数
$* = 1 2 3 4 5

# 进程ID
$$ = 854

# 之前没有执行其他命令或者函数
$? = 0
```

#### 3. 环境变量

环境变量默认存在，常用的有下面这几个：

1. HOME：用户主目录
2. PATH：系统环境变量PATH
3. TERM：当前终端
4. UID: 当前用户ID
5. PWD：当前工作目录，绝对路径

还是看例子：

```
#!/bin/bash

echo "print env"

echo $HOME
echo $PATH
echo $TERM
echo $PWD
echo $UID
```

运行结果：

```
print env

# 当前主目录
/home/poo

# PATH环境变量
/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games

# 当前终端
xterm

# 当前目录
/home/poo/poo

# 用户ID
1000
```

#### 4.字符串变量

1）单引号

- 单引号变量var='test'，只能原样输出，变量无效
- 单引号不能出现一个单独的单引号，转义也不可以

2）双引号

- 双引号变量`var="my name is ${name}"`，变量有效
- 可以出现转义符

3）拼接字符串

- 中间无任何+,之类的字符
- `name="this is"" my name";name="this is my name";name="this" is "my name"等效`
- `name='this is'' my name'; name='this is my name'; name='this' is 'my name' 等效`

4）获取字符串长度

- 在${}中使用“#”获取长度
  
  ```
  name="test";
  echo ${#name}; # 输出为4
  ```

5）提取子字符串

- 1:4 从第2个开始 往后截取4个字符
- ::4 从第一个字符开始 往后截取4个字符
  
  ```
  name="this is my name";
  echo ${name:1:4} #输出 is i
  echo ${name::4} #输出 this
  ```

### 5. 数组

bash只支持一维数组，不支持多维数组

- 定义数组：array_name=(li wang xiang zhang) （小括号做边界、使用空格分离）
- 单独定义数组的元素： array_para[0]="w"; array_para[3]="s" （定义时下标不连续也可以）
- 赋值数组元素：array_name[0]="zhao";
- 获取数组元素：
  
  ```
  array_name[0]="li"
  array_name[3]="zhang"
  echo ${array_name[0]} # 输出"li"
  echo ${array_name[1]} # 输出" "
  echo ${array_name[3]} # 输出"zhang"
  echo ${array_name[@]} # 输出"li zhang" 输出数组所有元素，没有元素的下标省略
  取得元素个数：${#array_name[@]} 或者 ${#array_name}
  取得单个元素长度：${#array_name[1]}
  ```

Shell变量就介绍到这里，下面来介绍Shell的变量运算。

### Shell运算

#### 1. 算数运算

> \+ 、-、*、\ ： 乘号前必须加\进行转义才可以进行乘法运算

我们经常需要在Shell脚本中计算，掌握基本的运算方法很有必要，下面就是4种比较常见的运算方法，功能都是将m + 1:

1. m=$[m+1]
2. m=\`expr $m + 1\` # 用``字符包起来
3. let m=m+1
4. m=$(( m + 1 ))

来看一个实际的例子：

```
#!/bin/bash

m=1
m=$[ m + 1 ]
echo $m

m=`expr $m + 1`
echo $m

# 注意：+ 号左右不要加空格
let m=m+1
echo $m

m=$(( m + 1 ))
echo $m
```

运行结果：

```
2
3
4
5
```

#### 2. 数字关系运算符

> 关系运算符只支持数字，不支持字符串，除非字符串的值是数字。下面假定变量 a 为 10，变量 b 为 20

- -eq ：检测两个数是否相等，相等返回 true。 [ $a -eq $b ] 返回 false。
- -ne： 检测两个数是否不相等，不相等返回 true。 [ $a -ne $b ] 返回 true。
- -gt： 检测左边的数是否大于右边的，如果是，则返回 true。 [ $a -gt $b ] 返回 false。
- -lt ： 检测左边的数是否小于右边的，如果是，则返回 true。 [ $a -lt $b ] 返回 true。
- -ge： 检测左边的数是否大于等于右边的，如果是，则返回 true。 [ $a -ge $b ] 返回 false。
- -le ： 检测左边的数是否小于等于右边的，如果是，则返回 true。 [ $a -le $b ] 返回 true。

#### 3. 字符串运算符

> 下表列出了常用的字符串运算符，假定变量 a 为 "abc"，变量 b 为 "efg"：

- = ：检测两个字符串是否相等，相等返回 true。 [ $a = $b ] 返回 false。
- != ：检测两个字符串是否相等，不相等返回 true。 [ $a != $b ] 返回 true。
- -z ：检测字符串长度是否为0，为0返回 true。 [ -z $a ] 返回 false。
- -n ：检测字符串长度是否为0，不为0返回 true。 [ -n "$a" ] 返回 true。
- $ ：检测字符串是否为空，不为空返回 true。 [ $a ] 返回 true。

#### 4. 布尔运算符

> 下表列出了常用的布尔运算符，假定变量 a 为 10，变量 b 为 20：

- ! ：非运算，表达式为 true 则返回 false，否则返回 true。 [ ! false ] 返回 true。
- -o ：或运算，有一个表达式为 true 则返回 true。 [ $a -lt 20 -o $b -gt 100 ] 返回 true。
- -a ：与运算，两个表达式都为 true 才返回 true。 [ $a -lt 20 -a $b -gt 100 ] 返回 false。

#### 5. 逻辑运算符

> 以下介绍 Shell 的逻辑运算符，假定变量 a 为 10，变量 b 为 20:

- && ：逻辑的 AND [[ $a -lt 100 && $b -gt 100 ]] 返回 false
- || ：逻辑的 OR [[ $a -lt 100 || $b -gt 100 ]] 返回 true

#### 6. 文件运算符

- -b file ：检测文件是否是块设备文件，如果是，则返回 true。 [ -b $file ] 返回 false。
- -c file ：检测文件是否是字符设备文件，如果是，则返回 true。 [ -c $file ] 返回 false。
- -d file ：检测文件是否是目录，如果是，则返回 true。 [ -d $file ] 返回 false。
- -f file ：检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。 [ -f $file ] 返回 true。
- -g file ：检测文件是否设置了 SGID 位，如果是，则返回 true。 [ -g $file ] 返回 false。
- -k file ：检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。 [ -k $file ] 返回 false。
- -p file ：检测文件是否是有名管道，如果是，则返回 true。 [ -p $file ] 返回 false。
- -u file ：检测文件是否设置了 SUID 位，如果是，则返回 true。 [ -u $file ] 返回 false。
- -r file ：检测文件是否可读，如果是，则返回 true。 [ -r $file ] 返回 true。
- -w file ：检测文件是否可写，如果是，则返回 true。 [ -w $file ] 返回 true。
- -x file ：检测文件是否可执行，如果是，则返回 true。 [ -x $file ] 返回 true。
- -s file ：检测文件是否为空（文件大小是否大于0），不为空返回 true。 [ -s $file ] 返回 true。
- -e file ：检测文件（包括目录）是否存在，如果是，则返回 true。 [ -e $file ] 返回 true。

了解了基本的运算方法，下面进一步来学习shell的语句。

### Shell语句

Shell语句跟高级语言有些类似，也包括分支、跳转、循环，下面就带大家一个一个突破。

#### 1. if语句

这个跟高级语言的`if - else - if`类似，只是格式有些不同而已，也来看个例子吧：

```
#!/bin/bash

read VAR

# 下面这两种判断方法都可以，使用 [] 注意左右加空格
# if test $VAR -eq 10
if [ $VART -eq 10 ]
then 
    echo "true"
else
    echo "false"
fi
```

#### 2. case语句

case语句有些复杂，要注意格式：

```
#!/bin/bash

read NAME
# 格式有点复杂，一定要注意
case $NAME in
    "Linux")
        echo "Linux"
        ;;
    "cdeveloper")
        echo "cdeveloper"
        ;;
    *)
        echo "other"
        ;;
esac
```

运行结果：

```
# 输入 Linux
Linux
Linux

# 输入 cdeveloper
cdeveloper
cdeveloper

# 输入其他的字段
hello
other
```

#### 3. for循环

这是一个for循环的使用例子，挺简单的，有点类似Python：

```
#!/bin/bash

# 普通 for 循环
for ((i = 1; i <= 3; i++))
do
    echo $i
done

# VAR 依次代表每个元素
for VAR in 1 2 3
do
    echo $VAR
done
```

运行结果：

```
1
2
3
1
2
3
```

#### 4. while 循环

注意与 for 循环的区别：

```
#!/bin/bash

VAR=1

# 如果 VAR 小于 10，就打印出来
while [ $VAR -lt 10 ]
do
    echo $VAR
    # VAR  自增 1
    VAR=$[ $VAR + 1 ]
done
```

运行结果：

```
1
2
3
4
5
6
7
8
9
```

#### 5.until 循环

until 语句与上面的循环的不同点是它的结束条件为1：

```
#!/bin/bash

i=0

# i 大于 5 时，循环结束
until [[ "$i" -gt 5 ]]
do
    echo $i
    i=$[ $i + 1 ]
done
```

运行结果：

```
0
1
2
3
4
5
```

#### 6. break

Shell 中的 `break` 用法与高级语言相同，都是跳出循环，来看个例子：

```
#!/bin/bash

for VAR in 1 2 3
do
# 如何 VAR 等于 2 就跳出循环
    if [ $VAR -eq 2 ]
    then
        break
    fi

    echo $VAR
done
```

运行结果：

```
1
```

#### 7. continue

`continue`用来跳过本次循环，进入下一次循环，再来看看上面的例子：

```
#!/bin/bash

for VAR in 1 2 3
do
# 如果 VAR 等于 2，就跳过，直接进入下一次 VAR = 3 的循环
    if [ $VAR -eq 2 ]
    then
        continue
    fi

    echo $VAR
done
```

运行结果：

```
1
3
```

下面介绍 Shell 编程中比较重要的函数，好像每种编程语言的函数都很重要。

### Shell 函数

函数可以用一句话解释：带有输入输出的具有一定功能的黑盒子，相信有过编程经验的同学不会陌生。那么，我们先来看看 Shell 中函数定义的格式。

#### 1. 定义函数

有 2 种常见格式：

```
function fun_name()
{

}

fun_name()
{

}
```

例如：

```
#!/bin/bash

function hello_world()
{
    echo "hello world fun"
    echo $1 $2
    return 1
}

hello()
{
    echo "hello fun"
}
```

#### 2. 调用函数

如何调用上面的 2 个函数

```
# 1. 直接用函数名调用 hello 函数
hello

# 2. 使用[函数名 函数参数]来传递参数
hello_world 1 2

# 3. 使用[FUN=`函数名 函数参数`]来间接调用
FUN=`hello_world 1 2`
echo $FUN
```

#### 3. 获取返回值

如何获取 `hello_world` 函数的返回值？还记得 `$?` 吗？

```
hello_world 1 2
# $? 可用于获取前一个函数的返回值，这里的结果是1
echo $?
```

#### 4. 定义本地变量

使用 `local` 来在函数中定义本地变量：

```
fun()
{
    local x=1
    echo $x
}
```

俗话说，程序 3 分靠写，7 分靠调，下面我们就来看看如何调试 Shell 程序。

### 调试

使用下面的命令来检查是否有语法错误：

```
sh -n script_name.sh
```

使用下面的命令来执行并调试 Shell 脚本：

```
sh -x script_name.sh
```

来看个实际的例子，我们来调试下面这个 `test.sh` 程序：

```
#!/bin/bash

for VAR in 1 2 3
do
    if [ $VAR -eq 2 ]
    then
        continue
    fi
    echo $VAR
done
```

首先检查有无语法错误：

```
sh -n test.sh
```

没有输出，说明没有错误，开始实际高度：

```
sh -x test.sh
```

调试结果如下：

```
+ [ 1 -eq 2 ]
+ echo 1
1
+ [ 2 -eq 2 ]
+ continue
+ [ 3 -eq 2 ]
+ echo 3
3
```

其中**带有 `+` 表示的是 Shell 调试器的输出，不带 `+` 表示我们程序的输出。**

### Shell 易错点

这里我总结了一些初学 Shell 编程容易犯的错误，大多都是语法错误：

1. `[]` 内不能嵌套 `()`，可以嵌套 `[]`
2. `$[ val + 1 ]` 是变量加 1 的常用方法
3. `[]` 在测试或者计算中里面的内容最好都加空格
4. 单引号和双引号差不多，单引号更加严格，双引号可以嵌套单引号
5. 一定要注意语句的格式，例如缩进