title: Python正则表达式
date: 2021-06-23
category: 技术
tag: python, 正则表达式

[TOC]

**Python正则表达式**
今天我们主要来讲解一下正则表达式在Python语言中的应用！
大多数编程语言的正则表达式设计都师从Perl，所以语法基本相似，不同的是每种语言都有自己的函数去支持正则，今天我们就来学习 Python中关于正则表达式的函数。

### 一、正则表达式语法

一个正则表达式指定了一集与之匹配的字符串；模块内的函数可以让你检查某个字符串是否跟给定的正则表达式匹配。

#### 1.表达式全集

| 字符                             | 描述                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .                              | 匹配除“\n”之外的任何单个字符。如果指定了标签 DOTALL ，它将匹配包括换行符的任意字符。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ^                              | 匹配输入字符串的开始位置，并且在 MULTILINE 模式也匹配换行后的首个符号。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| $                              | 匹配输入字符串的结束位置。在 MULTILINE 模式下也会匹配换行符之前的文本。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| *                              | 匹配前面的子表达式零次或多次。例如，ab* 会匹配 'a'，'ab'，或者 'a' 后面跟随任意个 'b'。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| +                              | 匹配前面的子表达式一次或多次。例如， ab+ 会匹配 'a' 后面跟随1个以上到任意个 'b'，它不会匹配 'a'。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ?                              | 匹配前面的子表达式零次或一次。例如，ab? 会匹配 'a' 或者 'ab'。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *?, +?, ??                     | '*', '+'，和 '?' 修饰符都是贪婪的；它们在字符串进行尽可能多的匹配。有时候并不需要这种行为。如果正则式 <.*> 希望找到 '<a> b <c>'，它将会匹配整个字符串，而不仅是 '<a>'。在修饰符之后添加 ? 将使样式以非贪婪方式或者最小方式进行匹配；尽量少的字符将会被匹配。使用正则式 <.*?> 将会仅仅匹配 '<a>'。                                                                                                                                                                                                                                                                                                                                                                                             |
| {m}                            | m是一个非负整数。匹配确定m次。例如， a{6} 将匹配6个 'a' , 但是不能是5个。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| {m,n}                          | 对正则式进行 m 到 n 次匹配，在 m 和 n 之间取尽量多。例如，a{3,5} 将匹配 3 到 5个 'a'。忽略 m 意为指定下界为0，忽略 n 指定上界为无限次。 比如 a{4,}b 将匹配 'aaaab' 或者1000个 'a' 尾随一个 'b'，但不能匹配 'aaab'。逗号不能省略，否则无法辨别修饰符应该忽略哪个边界。                                                                                                                                                                                                                                                                                                                                                                                                 |
| {n,m}?                         | 前一个修饰符的非贪婪模式，只匹配尽量少的字符次数。比如，对于 'aaaaaa'， a{3,5} 匹配 5个 'a' ，而 a{3,5}? 只匹配3个 'a'。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| \                              | 将下一个字符标记为一个特殊字符、或一个原义字符、或一个向后引用、或一个八进制转义符。例如，“n”匹配字符“n”。“\n”匹配一个换行符。串行“\\”匹配“\”而“\(”则匹配“(”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                             | 字符可以单独列出，比如 [amk] 匹配 'a'， 'm'， 或者 'k'。<br/>可以表示字符范围，通过用 '-' 将两个字符连起来。比如 [a-z] 将匹配任何小写ASCII字符， [0-5][0-9] 将匹配从 00 到 59 的两位数字， [0-9A-Fa-f] 将匹配任何十六进制数位。 如果 - 进行了转义 （比如 [a\-z]）或者它的位置在首位或者末尾（如 [-a] 或 [a-]），它就只表示普通字符 '-'。<br/>特殊字符在集合中，失去它的特殊含义。比如 [(+*)] 只会匹配这几个文法字符 '(', '+', '*', or ')'。<br/>字符类如 \w 或者 \S (如下定义) 在集合内可以接受，它们可以匹配的字符由 ASCII 或者 LOCALE 模式决定。<br/>不在集合范围内的字符可以通过取反来进行匹配。如果集合首字符是 '^' ，所有不在集合内的字符将会被匹配，比如 [^5] 将匹配所有字符，除了'5'，[^^] 将匹配所有字符，除了'^'。^ 如果不在集合首位，就没有特殊含义。<br/>在集合内要匹配一个字符 ']'，有两种方法，要么就在它之前加上反斜杠，要么就把它放到集合首位。比如， [()[\]{}] 和 []()[{}] 都可以匹配括号。 |
| \|                             | A\|B， A 和 B 可以是任意正则表达式，创建一个正则表达式，匹配 A 或者 B. 任意个正则表达式可以用 '\|' 连接。它也可以在组合（见下列）内使用。扫描目标字符串时， '\|' 分隔开的正则样式从左到右进行匹配。当一个样式完全匹配时，这个分支就被接受。意思就是，一旦 A 匹配成功， B 就不再进行匹配，即便它能产生一个更好的匹配。或者说，'\|' 操作符绝不贪婪。 如果要匹配 '\|' 字符，使用 \\\|， 或者把它包含在字符集里，比如 [\|].                                                                                                                                                                                                                                                                                                                               |
| (pattern)                      | 匹配pattern并获取这一匹配。要匹配圆括号字符，请使用“\(”或“\)”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| (?:pattern)                    | 匹配pattern但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用。这在使用或字符“(\|)”来组合一个模式的各个部分是很有用。例如“industr(?:y\|ies)”就是一个比“industry\|industries”更简略的表达式。                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| (?=pattern)                    | 正向肯定预查，在任何匹配pattern的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如，“Windows(?=95\|98\|NT\|2000)”能匹配“Windows2000”中的“Windows”，但不能匹配“Windows3.1”中的“Windows”。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始。                                                                                                                                                                                                                                                                                                                                                    |
| (?!pattern)                    | 正向否定预查，在任何不匹配pattern的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如“Windows(?!95\|98\|NT\|2000)”能匹配“Windows3.1”中的“Windows”，但不能匹配“Windows2000”中的“Windows”。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始                                                                                                                                                                                                                                                                                                                                                     |
| (?<=pattern)                   | 反向肯定预查，与正向肯定预查类拟，只是方向相反。例如，“(?<=95\|98\|NT\|2000)Windows”能匹配“2000Windows”中的“Windows”，但不能匹配“3.1Windows”中的“Windows”。                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| (?<!pattern)                   | 反向否定预查，与正向否定预查类拟，只是方向相反。例如“(?<!95\|98\|NT\|2000)Windows”能匹配“3.1Windows”中的“Windows”，但不能匹配“2000Windows”中的“Windows”。                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \number                        | 匹配数字代表的组合。每个括号是一个组合，组合从1开始编号。比如 (.+) \1 匹配 'the the' 或者 '55 55', 但不会匹配 'thethe' (注意组合后面的空格)。这个特殊序列只能用于匹配前面99个组合。如果 number 的第一个数位是0， 或者 number 是三个八进制数，它将不会被看作是一个组合，而是八进制的数字值。在 '[' 和 ']' 字符集合内，任何数字转义都被看作是字符。                                                                                                                                                                                                                                                                                                                                                           |
| \A                             | 只匹配字符串开始                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| \b                             | 匹配一个单词边界，也就是指单词和空格间的位置。例如，“er\b”可以匹配“never”中的“er”，但不能匹配“verb”中的“er”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| \B                             | 匹配非单词边界。“er\B”能匹配“verb”中的“er”，但不能匹配“never”中的“er”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \d                             | 匹配一个数字字符。等价于[0-9]。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \D                             | 匹配一个非数字字符。等价于[^0-9]。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| \s                             | 匹配任何空白字符，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \S                             | 匹配任何非空白字符。等价于[^ \f\n\r\t\v]。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| \w                             | 匹配包括下划线的任何单词字符。等价于“[A-Za-z0-9_]”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \W                             | 匹配任何非单词字符。等价于“[^A-Za-z0-9_]”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| \Z                             | 只匹配字符串尾。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

绝大部分Python的标准转义字符也被正则表达式分析器支持:

```
\a，\b，\f，\n，\N，\r，\t，\u，\U，\v，\x，\\
```

#### 2.常用正则表达式

| 名称    | 内容                                                                                                                     |
| ----- | ---------------------------------------------------------------------------------------------------------------------- |
| 用户名   | `/^[a-z0-9_-]{3,16}$/`                                                                                                |
| 密码    | `/^[a-z0-9_-]{6,18}$/`                                                                                                   |
| 十六进制值 | `/^#?([a-f0-9]{6}`                                                                                                       |
| 电子邮箱  | `/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/<br />/^[a-z\d]+(\.[a-z\d]+)*@([\da-z](-[\da-z])?)+(\.{1,2}[a-z]+)+$/` |
| URL   | `/^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/`                                                       |
| IP 地址 | `/((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)/` <br /> `/^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/`|

### 二、re模块简介

re模块主要定义了9个常量、12个函数、1个异常！

关于Python正则表达式的支持，首先肯定会想到re库，这是一个Python处理文本的标准库。

标准库的意思表示这是一个Python内置模块，不需要额外下载，目前Python内置模块大概有300个。可以在这里查看Python所有的内置模块：https://docs.python.org/3/py-modindex.html

因为re是内置模块，所以不需要再下载，使用时直接引入即可：`import re`

re模块官方文档：<https://docs.python.org/zh-cn/3.8/library/re.html>

re模块库源码：<https://github.com/python/cpython/blob/3.8/Lib/re.py>

### 三、re模块常量

常量即表示不可更改的变量，一般用于做标记。

re模块中有9个常量，如下。
```
ASCII = A = sre_compile.SRE_FLAG_ASCII # assume sacii "locale"
IGNORECASE = I = sre_compile.SRE_FLAG_IGNORECASE # ignore case
LOCALE = L = sre_compile.SRE_FLAG_LOCALE # assume current 8-bit locale
UNICODE = U = sre_compile.SRE_FLAG_UNICODE # assume unicode "locale"
MUJLTILINE = M = sre_compile.SRE_FLAG_MULTILINE # make anchors look for newline
DOTALL = S = sre_compile.SRE_FLAG_DOTALL # make dot match newline
VERBOSE = X = sre_compile.SRE_FLAG_VERBOSE # ignore whitespace and comments
# sre extensions (experimental, don't rely on these)
TEMPLATE = T = sre_compile.SRE_FLAG_TEMPLATE # disable backtracking
DEBUG = sre_compile.SRE_FLAG_DEBUG # dump pattern after compilation
```


int(re.I) == 2 == 2<sup>1</sup><br />
int(re.A) == 256 == 2<sup>8</sup><br />
int(re.L) == 4 == 2<sup>2</sup><br />
int(re.U) == 32 == 2<sup>5</sup><br />
int(re.M) == 8 == 2<sup>3</sup><br />
int(re.S) == 16 == 2<sup>4</sup><br />
int(re.X) == 64 == 2<sup>6</sup><br />
int(re.T) == 1 == 2<sup>0</sup><br />
int(re.DEBUG) == 128  = 2<sup>7</sup><br />


下面我们来快速学习这些常量的作用及如何使用他们，按常用度排序！

#### 1. IGNORECASE

语法： re.IGNORECASE 或简写为 re.I

作用： 进行忽略大小写匹配。

代码案例：

```
def regexFlag():
    """
    演示re模块常量的使用
    re.IGNORECASE
    """
    text = '测试test'
    pattern = '测试TEST'
    print('默认模式：', re.findall(pattern, text))
    print('忽略大小写模式', re.findall(pattern, text, re.IGNORECASE))
    print('忽略大小写模式', re.findall(pattern, text, re.I))
```

执行结果：

```
默认模式： []
忽略大小写模式 ['测试test']
忽略大小写模式 ['测试test']
```

在默认匹配模式下大写字母B无法匹配小写字母b，而在忽略大小写模式下是可以的。

#### 2. ASCII

语法： re.ASCII 或简写为 re.A

作用： 顾名思义，ASCII表示ASCII码的意思，让\w, \W, \b, \B, \d, \D, \s 和 \S只匹配ASCII，而不是Unicode。

代码案例：

```
def regexFlag():
    """
    演示re模块常量的使用
    re.ASCII
    """
    text = 'a测b试c'
    pattern = r'\w+'
    print('Unicode:', re.findall(pattern, text))
    print('ASCII:', re.findall(pattern, text, re.ASCII))
    print('ASCII:', re.findall(pattern, text, re.A))
```

执行结果：

```
Unicode： ['a测b试c'] 
ASCII: ['a', 'b', 'c']
ASCII: ['a', 'b', 'c']
```

在默认匹配模式下\w+匹配到了所有字符串，而在ASCII模式下，只匹配到了a、b、c（ASCII编码支持的字符）。

注意：这只对字符串匹配模式有效，对字节匹配模式无效。

#### 3. DOTALL

语法： re.DOTALL 或简写为 re.S

作用： DOT表示.，ALL表示所有，连起来就是.匹配所有，包括换行符\n。默认模式下.是不能匹配行符\n的。

代码案例：

```
def regexFlag():
    """
    演示re模块常量的使用
    re.DOTALL
    """
    text = '测\n试'
    pattern = r'.*'
    print('默认模式：', re.findall(pattern, text))
    print('.匹配所有模式：', re.findall(pattern, text, re.DOTALL))
    print('.匹配所有模式：', re.findall(pattern, text, re.S))
```

执行结果：

```
默认模式： ['测', '', '试', '']
.匹配所有模式： ['测\n试', '']
.匹配所有模式： ['测\n试', '']
```

在默认匹配模式下.并没有匹配换行符\n，而是将字符串分开匹配；而在re.DOTALL模式下，换行符\n与字符串一起被匹配到。

注意：默认匹配模式下.并不会匹配换行符\n。

#### 4. MULTILINE

语法： re.MULTILINE 或简写为 re.M

作用： 多行模式，当某字符串中有换行符\n，默认模式下是不支持换行符特性的，比如：行开头和行结尾，而多行模式下是支持匹配行开头的。

代码案例：

```
def regexFlag():
    """
    演示re模块常量的使用
    re.MULTILINE
    """
    text = '测\n试'
    pattern = r'^试'
    print('默认模式：', re.findall(pattern, text))
    print('多行模式：', re.findall(pattern, text, re.MULTILINE))
    print('多行模式：', re.findall(pattern, text, re.M))
```

执行结果：

```
默认模式： []
多行模式： ['试']
多行模式： ['试']
```

正则表达式中^表示匹配行的开头，默认模式下它只能匹配字符串的开头；而在多行模式下，它还可以匹配换行符\n后面的字符。

注意：正则语法中^匹配行开头、\A匹配字符串开头，单行模式下它两效果一致，多行模式下\A不能识别\n。

#### 5. VERBOSE

语法： re.VERBOSE 或简写为 re.X

作用： 详细模式，可以在正则表达式中加注解！

代码案例：

```
def regexFlag():
    """
    演示re模块常量的使用
    re.VERBOSE
    """
    text = '测试'
    pattern = r'''^测    # 第一个字
                   试    # 第二个字
                '''
    print('默认模式：', re.findall(pattern, text))
    print('详细模式：', re.findall(pattern, text, re.VERBOSE))
    print('详细模式：', re.findall(pattern, text, re.X))
```

执行结果：

```
默认模式： []
详细模式： ['测试']
详细模式： ['测试']
```

默认模式下并不能识别正则表达式中的注释，而详细模式是可以识别的。当一个正则表达式十分复杂的时候，详细模式或许能为你提供另一种注释方式，但它不应该成为炫技的手段，建议谨慎考虑后使用！

#### 6. LOCALE

语法： re.LOCALE 或简写为 re.L

作用： 由当前语言区域决定 \w, \W, \b, \B 和大小写敏感匹配，这个标记只能对byte样式有效。这个标记官方已经不推荐使用，因为语言区域机制很不可靠，它一次只能处理一个 "习惯”，而且只对8位字节有效。

注意： 由于这个标记官方已经不推荐使用！

#### 7. UNICODE

语法： re.UNICODE 或简写为 re.U

作用： 与 ASCII 模式类似，匹配unicode编码支持的字符，但是 Python 3 默认字符串已经是Unicode，所以有点冗余。

#### 8. DEBUG

语法： re.DEBUG

作用： 显示编译时的debug信息。

代码案例：

```
def regexFlag():
    """
    演示re模块常量的使用
    re.DEBUG
    """
    text = '测试'
    pattern = r'试'
    print('debug模式：', re.findall(pattern, text, re.DEBUG))
```

执行结果：

```
LITERAL 35797

 0. INFO 8 0b11 1 1 (to 9)  
      prefix_skip 1
      prefix [0x8bd5] ('试')
      overlap [0]
       9: LITERAL 0x8bd5 ('试')   
11. SUCCESS
debug模式： ['试']

虽然debug模式下确实会打印编译信息，但我并不理解表达的含义。
```

#### 9. TEMPLATE

语法： re.TEMPLATE 或简写为 re.T

作用： 暂时没搞懂TEMPLATE的具体用处，源码注释中写着：disable backtracking(禁用回溯)！

#### 10. 常量总结

① 9个常量中，前5个（IGNORECASE、ASCII、DOTALL、MULTILINE、VERBOSE）有用处，两个（LOCALE、UNICODE）官方不建议使用、两个（TEMPLATE、DEBUG）试验性功能，不能依赖。

② 常量在re常用函数中都可以使用，查看源码可得知。

③ 常量可叠加使用，因为常量值都是2的幂次方值，所以是可以叠加使用的，叠加时请使用 | 符号，请勿使用+ 符号！

```
def regexFlag():
    """
    演示re模块常量的使用
    re.ASCII
    """
    text = '测\n试b'
    pattern = r'^试B'
    print('默认模式：', re.findall(pattern, text))
    print('忽略大小写+多行模式：', re.findall(pattern, text, re.IGNORECASE|re.MULTILINE))
    print('忽略大小写+多行模式：', re.findall(pattern, text, re.I|re.M))
```

执行结果：

```
默认模式： []
忽略大小写+多行模式： ['试b']
忽略大小写+多行模式： ['试b']
```

### 四、re模块函数

re模块有12个函数，我们以功能分类来讲解；这样更具有比较性，同时也方便记忆。

#### 1. 查找一个匹配项

查找并返回一个匹配项的函数有3个：search、match、fullmatch，他们的区别分别是：

① search： 查找任意位置的匹配项

② match： 必须从字符串开头匹配

③ fullmatch： 整个字符串与正则完全匹配

我们再来根据实际的代码案例比较：

案例1:

```
import re

# 1.查找一个匹配项
text = 'a功能测试b，功能测试b'
pattern = r'功能测试b'
# 查找任意位置
print('search:', re.search(pattern, text).group())
# 从字符串开头匹配
print('match:',  re.match(pattern, text))
# 整个字符串完全匹配
print('fullmatch:', re.fullmatch(pattern, text))
```

执行结果：

```
search: 功能测试b
match: None
fullmatch: None
```

案例1中search函数是在字符串中任意位置匹配，只要有符合正则表达式的字符串就匹配成功，其实有两个匹配项，但search函数值返回一个。

而match函数是要从头开始匹配，而字符串开头多了个字母a，所以无法匹配，fullmatch函数需要完全相同，故也不匹配！

案例2:

```
import re

# 1.查找一个匹配项
text = '功能测试b，功能测试b'
pattern = r'功能测试b'
# 查找任意位置
print('search:', re.search(pattern, text).group())
# 从字符串开头匹配
print('match:',  re.match(pattern, text).group())
# 整个字符串完全匹配
print('fullmatch:', re.fullmatch(pattern, text))
```

执行结果：

```
search: 功能测试b
match: 功能测试b
fullmatch: None
```

案例2删除了text最开头的字母a，这样match函数就可以匹配啦，而fullmatch函数依然不能完全匹配！

案例3:

```
import re

# 1.查找一个匹配项
text = '功能测试b'
pattern = r'功能测试b'
# 查找任意位置
print('search:', re.search(pattern, text).group())
# 从字符串开头匹配
print('match:',  re.match(pattern, text).group())
# 整个字符串完全匹配
print('fullmatch:', re.fullmatch(pattern, text).group())
```

执行结果：

```
search: 功能测试b
match: 功能测试b
fullmatch: 功能测试b
```

案例3中，我们只留下一段文字，并且与正则表达式一致；这时fullmatch函数终于可以匹配了。

注意：查找一个匹配项返回的都是一个匹配对象（Match）。

#### 2.查找多个匹配项

讲完查找一项，现在来看看查找多项吧，查找多项函数主要有：findall函数 与 finditer函数：

① findall： 从字符串任意位置查找，返回一个列表

② finditer：从字符串任意位置查找，返回一个迭代器

两个方法基本类似，只不过一个是返回列表，一个是返回迭代器。我们知道列表是一次性生成在内存中，而迭代器是需要使用时一点一点生成出来的，内存使用更优。

```
import re

text = 'a功能测试b，功能测试b'
pattern = r'功能测试b'
# 查找所有匹配项，返回一个list
print('findall:', re.findall(pattern, text))
# 查找所有匹配项，返回一个迭代器
print('finditer:',  list(re.finditer(pattern, text)))
```

执行结果：

```
findall: ['功能测试b', '功能测试b']
finditer: [<re.Match object; span=(1, 6), match='功能测试b'>, <re.Match object; span=(7, 12), match='功能测试b'>]
```

如果可能存在大量的匹配项的话，建议使用finditer函数，一般情况使用findall函数基本没啥影响。

#### 3. 分割

`re.split(pattern, string, maxsplit=0, flags=0)` 函数：用 pattern 分开string ， maxsplit表示最多进行分割次数， flags表示模式，就是上面我们讲解的常量！

```
import re

text = 'a功能测试b，b功能测试b，c功能测试b'
pattern = r'，'
# 正则切割
print('split:', re.split(pattern, text, maxsplit=1, flags=re.IGNORECASE))
```

执行结果：

```
split: ['a功能测试b', 'b功能测试b，c功能测试b']
```

注意：str模块也有一个 split函数 ，str.split函数功能简单，不支持正则分割，而re.split支持正则。大数据量下re.split花费的时间比str.split少。所以在不需要正则支持且数据量和数次不多的情况下使用str.split函数更合适，反之则使用re.split函数。

#### 4. 替换

替换主要有sub函数 与 subn函数，他们功能类似！

先来看看sub函数的用法：

`re.sub(pattern, repl, string, count=0, flags=0)` 函数参数讲解：repl替换掉string中被pattern匹配的字符，count表示最大替换次数，flags表示正则表达式的常量。

值得注意的是：sub函数中的入参：repl替换内容既可以是字符串，也可以是一个函数！ 如果repl为函数时，只能有一个入参：Match匹配对象。

```
import re

text = '1功能测试b，2功能测试b，3功能测试b'
pattern = r', '
# repl为字符串
repl = r'、'
# 替换
print('sub-repl为字符串:', re.sub(pattern, repl, text, count=2, flags=re.IGNORECASE))
```

执行结果：

```
sub-repl为字符串: 1功能测试b、2功能测试b、3功能测试b
```

```
import re

text = '1功能测试b，2功能测试b。3功能测试b'
pattern = r'，|。'
# repl为函数
repl = lambda matchobj: ' ' if matchobj.group(0) != '，' else '、'
# 替换
print('sub-repl为字符串:', re.sub(pattern, repl, text, count=2, flags=re.IGNORECASE))
```

执行结果：

```
sub-repl为字符串: 1功能测试b、2功能测试b 3功能测试b
```

`re.subn(pattern, repl, string, count=0, flags=0)` 函数与 re.sub函数 功能一致，只不过返回一个元组 (字符串, 替换次数)。

```
import re

text = '1功能测试b，2功能测试b，3功能测试b'
pattern = r'，'
# repl为字符串
repl = r'、'
# 替换
print('sub-repl为字符串:', re.subn(pattern, repl, text, count=2, flags=re.IGNORECASE))
```

执行结果：

```
sub-repl为字符串: ('1功能测试b、2功能测试b、3功能测试b', 2)
```

#### 5. 编译正则对象

`compile`函数 与 `template`函数 将正则表达式的样式编译为一个正则表达式对象（正则对象Pattern），这个对象与re模块有同样的正则函数。

```
import re

text = 'a功能测试b，功能测试b'
pattern = r'功能测试b'
pattern_obj = re.compile(pattern)
# 查找任意位置
print('pattern_obj.search:', pattern_obj.search(text).group())
```

执行结果：

```
pattern_obj.search: 功能测试b
```

而template函数 与 compile函数 类似，只不过是增加了我们之前说的re.TEMPLATE 模式，我们可以看看源码。

#### 6. 其他

`re.escape(pattern)` 可以转义正则表达式中具有特殊含义的字符，比如：. 或者 * ，举个实际的案例：

```
import re

text = '功.能测*试'
pattern = r'功\.能测\*试'
# 查找任意位置
print('search:', re.search(pattern, text))
```

执行结果：

```
search: <re.Match object; span=(0, 6), match='功.能测*试'>

import re

text = '功.能测*试'
pattern = re.escape('功.能测*试')
# 查找任意位置
print('转义后的正则：', pattern)
print('search:', re.search(pattern, text))
```

执行结果：

```
转义后的正则： 功\.能测\*试
search: <re.Match object; span=(0, 6), match='功.能测*试'>
```

`re.escape(pattern)` 看似非常好用省去了我们自己加转义，但是使用它很容易出现转义错误的问题，所以并不建议使用它转义，而建议大家自己手动转义！

`re.purge()` 函数作用就是清除 正则表达式缓存，具体有什么缓存呢？我们来看看源码就知道它背地里干了什么：

看方法大概是清除缓存吧，我们再来看看具体的案例：

```
import re

text = '功.能测*试'
pattern = r'功\.能测\*试'
# 查找任意位置
print('search:', re.search(pattern, text))
print('_cache:', re._cache)
re.purge()
print('_cache:', re._cache)
```

执行结果：

```
search: <re.Match object; span=(0, 6), match='功.能测*试'>
_cache: {(<class 'str'>, '功\\.能测\\*试', 0): re.compile('功\\.能测\\*试')}
_cache: {}
```

在函数re.purge()前后打印_cache的结果，第二个_cache很明显被清理了！

### 五、re模块异常

re模块还包含了一个正则表达式的编译错误，当我们给出的正则表达式是一个无效的表达式（就是表达式本身有问题）时，就会raise一个异常！

我们来看看具体的案例吧：

```
import re

text = '功.能测*试'
pattern = r'(测试))'
# 查找任意位置
print('search:', re.search(pattern, text))
```

执行结果：

```
Traceback (most recent call last):
  File "c:/Users/dell/Desktop/test/re/3/11.py", line 8, in <module>
    print('search:', re.search(pattern, text))
  File "C:\Program Files\Python38\lib\re.py", line 201, in search
    return _compile(pattern, flags).search(string)
  File "C:\Program Files\Python38\lib\re.py", line 304, in _compile
    p = sre_compile.compile(pattern, flags)
  File "C:\Program Files\Python38\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "C:\Program Files\Python38\lib\sre_parse.py", line 962, in parse
    raise source.error("unbalanced parenthesis")
re.error: unbalanced parenthesis at position 4
```

上面案例中我们可以看到，在编写正则表达式中我们多写了一个括号，这导致执行结果报错。

注意：这个异常一定是正则表达式本身是无效的，与要匹配的字符串无关！

### 六、注意事项

Python 正则表达式知识基本讲解完毕，最后稍微给大家提一提需要注意的点。

#### 1. 字节串与字符串

模式和被搜索的字符串既可以是Unicode字符串(str)，也可以是8位字节串(bytes)。但是，Unicode字符串与8位字节串不能混用！

#### 2.r 的作用

正则表达式使用反斜杠（\）来表示特殊形式，或者把特殊字符转义成普通字符。

而反斜杠在普通的 Python 字符串里也有相同的作用，所以就产生了冲突。

解决办法是对于正则表达式样式使用 Python 的原始字符串表示法；在带有‘r’前缀的字符串字面值中，反斜杠不必做任何特殊处理。

#### 3.正则查找函数 返回匹配对象

查找一个匹配项`（search、match、fullmatch）`的函数返回值都是一个匹配对象Match ，需要通过match.group()获取匹配值，这个很容易忘记。

另外还需要注意：`match.group()` 与`match.groups()` 函数的差别！

#### 4.重复使用某个正则

如果要重复使用某个正则表达式，推荐先使用 `re.compile(pattern)`函数 返回一个正则对象，然后复用这个正则对象，这样会更快！
