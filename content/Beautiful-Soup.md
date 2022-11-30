title:Beautiful Soup简介
date:2022-11-30
category:python
tag:Beautiful Soup,笔记

[TOC]

### 1. Beautiful Soup简介

Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.

#### 1.1 举个例子

```
html_doc = """
<html><head><title>这是一个例子</title></head>
<body>
<p class="title"><b>这是一个例子</b></p>

<p class="story">从前有三个人;他们的名字是
<a href="http://example.com/zhangsan" class="peopele" id="link1">张三</a>,
<a href="http://example.com/lisi" class="peopele" id="link2">李四</a> 和
<a href="http://example.com/wangwu" class="peopele" id="link3">王五</a>;
他们住在一个四合院。</p>

<p class="example">...</p>
"""
```

- 格式化输出`html_doc`

```
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify)

# 输出结果：
<bound method Tag.prettify of 
<html><head><title>这是一个例子</title></head>
<body>
<p class="title"><b>这是一个例子</b></p>
<p class="story">从前有三个人;他们的名字是
<a class="peopele" href="http://example.com/zhangsan" id="link1">张三</a>,
<a class="peopele" href="http://example.com/lisi" id="link2">李四</a> 和
<a class="peopele" href="http://example.com/wangwu" id="link3">王五</a>;
他们住在一个四合院。</p>
<p class="example">...</p>
</body></html>>
```

- 输出标题

```
print(soup.title)

# 输出结果：
<title>这是一个例子</title>
```

- 输出标题标签

```
print(soup.title.name)

# 输出结果：
title
```

- 输出标题内容

```
print(soup.title.string)

# 输出结果：
这是一个例子
```

- 输出标题的父标签

```
print(soup.title.parent.name)

# 输出结果：
head
```

- 查找第一个`p`元素

```
print(soup.p)

# 输出结果：
<p class="title"><b>这是一个例子</b></p>
```

- 查找第一个`p`元素的`class`属性内容

```
print(soup.p['class'])

# 输出结果：
['title']
```

- 查找第一个`a`元素

```
print(soup.a)

# 输出结果：
<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>
```

- 查找所有`a`元素

```
print(soup.find_all('a'))

# 输出结果：
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>, <a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
```

- 查找`id`为`link3`的元素

```
print(soup.find(id="link3"))

# 输出结果：
<a class="people" href="http://example.com/wangwu" id="link3">王五</a>
```

### 2. 安装 Beautiful Soup

```
$ pip install beautifulsoup4 -i https://pypi.tuna.tsinghua.edu.cn/simple/

Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple/
Collecting beautifulsoup4
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/9c/d8/909c4089dbe4ade9f9705f143c9f13f065049a9d5e7d34c828aefdd0a97c/beautifulsoup4-4.11.1-py3-none-any.whl (128 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 128.2/128.2 kB 1.3 MB/s eta 0:00:00
Collecting soupsieve>1.2
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/16/e3/4ad79882b92617e3a4a0df1960d6bce08edfb637737ac5c3f3ba29022e25/soupsieve-2.3.2.post1-py3-none-any.whl (37 kB)
Installing collected packages: soupsieve, beautifulsoup4
Successfully installed beautifulsoup4-4.11.1 soupsieve-2.3.2.post1
```

### 3. 安装解析器

```
pip install lxml
pip install html5lib
```

```
$ pip install lxml  -i https://pypi.tuna.tsinghua.edu.cn/simple/
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple/
Collecting lxml
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/b9/bb/00637cce419a958a8254ee4371b15446fd5cd41d8f53513aed52a1fbbe20/lxml-4.9.1-cp310-cp310-win_amd64.whl (3.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.6/3.6 MB 2.1 MB/s eta 0:00:00
Installing collected packages: lxml
Successfully installed lxml-4.9.1
```

### 4. 使用方法

```
# Python标准库

BeautifulSoup(markup,"html.parser")

# lxml HTML解析器

BeautifulSoup(markup,"lxml")

# lxml XML解析器

BeautifulSoup(markup,"lxml-xml") or BeautifulSoup(markup,"xml")

# html5lib

BeautifulSoup(markup,"html5lib")
```

### 5. 对象的种类

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:`Tag`,`NavigableString`,`BeautifulSoup`,`Comment`.

#### 5.1 Tag

```
from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="test">测试一下</b>',"html.parser")
tag = soup.b
print(tag)
print(type(tag))

# 输出结果：
<b class="test">测试一下</b>
<class 'bs4.element.Tag'>
```

Tag有很多方法和属性,后面会详细解释.现在主要说一下`name`和`attributes`两个属性

- **Name**

每个tag都有自己的名字,通过`.name`来获取:

```
from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="test">测试一下</b>',"html.parser")
tag = soup.b
print(tag.name)

# 输出结果
b
```

如果改变了tag的name,那将影响所有通过当前Beautiful Soup对象生成的HTML文档:

```
from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="test">测试一下</b>',"html.parser")
tag = soup.b
tag.name = "blockquote"
print(tag)

# 输出结果
<blockquote class="test">测试一下</blockquote>
```

- **Attributes**

一个tag可能有很多个属性. tag`<b class="test">`有一个 “class” 的属性,值为 “test” . tag的属性的操作方法与字典相同，也可以直接”点”取属性, 比如:`.attrs`:

```
# coding=utf-8

from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="test">测试一下</b>',"html.parser")
tag = soup.b
print(tag['class'])
print(tag.attrs)

# 输出结果
['test']
{'class': ['test']}
```

tag的属性可以被添加,删除或修改:

```
# coding=utf-8

from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="test">测试一下</b>',"html.parser")
tag = soup.b

tag['class'] = 'tester'
tag['id'] = 1
print(tag)

del tag['class']
del tag['id']
print(tag)

tag['class']
print(tag.get('class'))

# 输出结果
<b class="tester" id="1">测试一下</b>
<b>测试一下</b>
KeyError: 'class'
None
```

- 多值属性

一个`tag`可以有多个`class`，还有一些属性`rel`，`rev`，`accept-charset`，`headers`，`accesskey`，多值属性返回的类型是`list`:

```
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p class="test dev"></p>',"html.parser")
print(soup.p['class'])

soup = BeautifulSoup('<p class="test"></p>',"html.parser")
print(soup.p['class'])

# 输出结果
['test', 'dev']
['test']
```

一些属性只能有单个值，那么其以字符串返回：

```
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p id="test"></p>',"html.parser")
print(soup.p['id'])

# 输出结果
test
```

将tag转换成字符串时,多值属性会合并为一个值

```
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>',"html.parser")
print(soup.a['rel'])
soup.a['rel'] = ['index', 'contents']
print(soup.p)

# 输出结果
['index']
<p>Back to the <a rel="index contents">homepage</a></p>
```

如果转换的文档是XML格式,那么tag中不包含多值属性

```
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p class="test dev"></p>', 'lxml-xml')
print(soup.p['class'])

# 输出结果
test dev
```

#### 5.2 可遍历的字符串

字符串常被包含在tag内.Beautiful Soup用 NavigableString 类来包装tag中的字符串:

```
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p class="test">测试一下</p>', "html.parser")
tag = soup.p
print(tag.string)
print(type(tag.string))

# 输出结果
测试一下
<class 'bs4.element.NavigableString'>
```

通过 str() 方法可以直接将 NavigableString 对象转换成字符串:

```
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p class="test">测试一下</p>', "html.parser")
tag = soup.p
print(type(tag.string))
str_string = str(tag.string)
print(str_string)
print(type(str_string))

# 输出结果
<class 'bs4.element.NavigableString'>
测试一下
<class 'str'>
```

tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用 replace_with() 方法:

```
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p class="test">测试一下</p>', "html.parser")
tag = soup.p
tag.string.replace_with("洗洗睡吧")
print(tag)

# 输出结果
<p class="test">洗洗睡吧</p>
```

如果想在Beautiful Soup之外使用 NavigableString 对象，需要用str()方法将其转换成字符串。

#### 5.3 BeautifulSoup

`BeautifulSoup`对象表示的是一个文档的全部内容。大部分时候，可以把他当作`tag`对象。因为`BeautifulSoup`对象并不是真正的HTML或XML的tag，所以它没有`name`和`attribute`属性，但为了查看方便，给`BeautifulSoup`对象一个`[document]`的特殊属性。

```
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p class="test">测试一下</p>', "html.parser")
print(soup.name)

# 输出结果
[document]
```

#### 5.4 注释及特殊字符串

除`Tag`，`NavigableString`，`BeautifulSoup`外，还有一些特殊对象，是文档的注释部分:

```
from bs4 import BeautifulSoup

markup = "<b><!--你好，兄弟。这里有一个缺陷不要乱动？--></b>"
soup = BeautifulSoup(markup, "html.parser")
comment = soup.b.string
print(type(comment))

# 输出结果
<class 'bs4.element.Comment'>
```

Comment 对象是一个特殊类型的 NavigableString 对象:
```
print(comment)

# 输出结果
你好，兄弟。这里有一个缺陷不要乱动？
```

当它出现在HTML文档中时，`Comment`可以格式化输出：
```
print(soup.b.prettify())

# 输出结果
<b>
 <!--你好，兄弟。这里有一个缺陷不要乱动？-->
</b>
```

Beautiful Soup中定义的`CData`，`ProcessingInstruction`，`Declaration`，`Doctype`与`Comment`对象类似,这些类都是 `NavigableString`的子类,下面是用CDATA来替代注释的例子:

```
from bs4 import BeautifulSoup
from bs4 import CData

cdata = CData("A CDATA block")
markup = "<b><!--你好，兄弟。这里有一个缺陷不要乱动？--></b>"
soup = BeautifulSoup(markup, "html.parser")
comment = soup.b.string
comment.replace_with(cdata)
print(soup.b.prettify())

# 输出结果
<b>
 <![CDATA[A CDATA block]]>
</b>
```

### 6. 遍历方法

从文档的一段内容中查找另一段内容

举个例子：

```
html_doc = """
<html><head><title>这是一个例子</title></head>
<body>
<p class="title"><b>这是一个例子</b></p>

<p class="story">从前有三个人;他们的名字是
<a href="http://example.com/zhangsan" class="people" id="link1">张三</a>,
<a href="http://example.com/lisi" class="people" id="link2">李四</a> 和
<a href="http://example.com/wangwu" class="people" id="link3">王五</a>;
他们住在一个四合院。</p>

<p class="example">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

#### 6.1 子节点

一个`Tag`下的字符串或`Tag`，都是其子节点。注：字符串子节点不支持这些属性。

- tag的属性

获取tag的head：`soup.head`:

```
print(soup.head)

# 输出结果：
<head><title>这是一个例子</title></head>
```

获取tag的title：`soup.title`:

```
print(soup.title)

# 输出结果：
<title>这是一个例子</title>
```

获取<body>标签下第一个<b>标签：`soup.body.b`:

```
print(soup.body.b)

# 输出结果：
<b>这是一个例子</b>
```

获取tag下第一个`<a>`标签：`soup.a`:

```
print(soup.a)

# 输出结果：
<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>
```

获取tag下所有`<a>`标签：`soup.find_all('a')`:

```
print(soup.find_all('a'))

# 输出结果：
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>, <a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
```

- .contents 和 .children

tag的`.contents`属性可以将tag的子节点以列表方式输出：

```
head_tag = soup.head
print(head_tag)
print(head_tag.contents)

title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)

# 输出结果
<head><title>这是一个例子</title></head>
[<title>这是一个例子</title>]
<title>这是一个例子</title>
['这是一个例子']
```

BeautifulSoup对象一定包含子节点,也就是说`<html>`标签也是 BeautifulSoup 对象的子节点:

```
print(len(soup.contents))
print(soup.contents[0].name)

# 输出结果
1
html
```

字符串没有 .contents 属性,因为字符串没有子节点:

```
head_tag = soup.head
title_tag = head_tag.contents[0]
text = title_tag.contents[0]
print(text.contents)

# 输出结果
AttributeError: 'NavigableString' object has no attribute 'contents'
```

通过tag的 .children 生成器,可以对tag的子节点进行循环:

```
head_tag = soup.head
title_tag = head_tag.contents[0]
for child in title_tag.children:
    print(child)

# 输出结果
这是一个例子
```

- .descendants

.contents 和 .children 属性仅包含tag的直接子节点.例如,`<head>`标签只有一个直接子节点`<title>`,但是`<title>`标签也包含一个子节点:字符串 “这是一个例子”, 其也属于`<head>`标签的子孙节点. .descendants 属性可以对所有tag的子孙节点进行递归循环:

```
for child in head_tag.descendants:
    print(child)

# 输出结果
<title>这是一个例子</title>
这是一个例子
```

上面的例子中, `<head>`标签只有一个子节点,但是有2个子孙节点:`<head>`节点和`<head>`的子节点, BeautifulSoup 有一个直接子节点(<html>节点),也有很多子孙节点:

```
print(len(list(soup.children)))
print(len(list(soup.descendants)))

# 输出结果：
1
26
```

- .string

如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点:

```
head_tag = soup.head
title_tag = head_tag.contents[0]
print(title_tag.string)

# 输出结果：
这是一个例子
```

如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同:

```
head_tag = soup.head
print(head_tag.contents)
print(head_tag.string)

# 输出结果：
[<title>这是一个例子</title>]
这是一个例子
```

如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None :

```
print(soup.html.string)
# 输出结果：
None
```

- .strings 和 stripped_strings

如果tag中包含多个字符串,可以使用 .strings 来循环获取:

```
for string in soup.strings:
    print(repr(string))

# 输出结果
'这是一个例子'
'\n'
'\n'
'这是一个例子'
'\n'
'从前有三个人;他们的名字是\n'
'张三'
',\n'
'李四'
' 和\n'
'王五'
';\n他们住在一个四合院。'
'\n'
'...'
'\n'
```

输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容:

```
for string in soup.stripped_strings:
    print(repr(string))

# 输出结果
'这是一个例子'
'这是一个例子'
'从前有三个人;他们的名字是'
'张三'
','
'李四'
'和'
'王五'
';\n他们住在一个四合院。'
'...'
```

#### 6.2 父节点

每个tag或字符串都有父节点

- .parent

通过 .parent 属性来获取某个元素的父节点.在上面例子中,`<head>`标签是`<title>`标签的父节点:

```
title_tag = soup.title
print(title_tag)
print(title_tag.parent)

# 输出结果
<title>这是一个例子</title>
<head><title>这是一个例子</title></head>
```

title标签下的字符串也有父节点:`<title>`标签

```
title_tag = soup.title
print(title_tag.string.parent)

# 输出结果
<title>这是一个例子</title>
```

文档的顶层节点比如<html>的父节点是 BeautifulSoup 对象:

```
html_tag = soup.html
print(type(html_tag.parent))

# 输出结果
<class 'bs4.BeautifulSoup'>
```

BeautifulSoup 对象的 .parent 是None:

```
print(soup.parent)

# 输出结果
None
```

- .parents

通过元素的 .parents 属性可以递归得到元素的所有父辈节点
```
link = soup.a
print(link)
for parent in link.parents:
    print(parent.name)

# 输出结果
<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>
p
body
html
[document]
```

#### 6.3 兄弟节点

如下：

```
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'html.parser')
print(sibling_soup.prettify())

# 输出结果
<html>
 <body>
  <a>
   <b>
    text1
   </b>
   <c>
    text2
   </c>
  </a>
 </body>
</html>
```
同一个缩进级别的称为兄弟节点

- .next_sibling 和 .previous_sibling

使用 .next_sibling 和 .previous_sibling 属性来查询兄弟节点:

```
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>",'html.parser')
print(sibling_soup.b.next_sibling)
print(sibling_soup.c.previous_sibling)

# 输出结果
<c>text2</c> # b的下一个节点是c
<b>text1</b> # c的上一个节点是b
```

如果没有上一节点或下一节点，则显示`None`
```
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>",'html.parser')
print(sibling_soup.c.next_sibling)
print(sibling_soup.b.previous_sibling)

# 输出结果
None
None
```

tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白,如下：

```
link = soup.a
print(link)
print(link.next_sibling)

# 输出结果
<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>
,\n

```

`link`的下一个兄弟结点是`,\n`

- .next_siblings 和 .previous_siblings

通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出:

```
for sibling in soup.a.next_siblings:
    print(repr(sibling))

# 输出结果
',\n'
<a class="people" href="http://example.com/lisi" id="link2">李四</a>
' 和\n'
<a class="people" href="http://example.com/wangwu" id="link3">王五</a>
';\n他们住在一个四合院。'
```

```
for sibling in soup.find(id="link3").previous_siblings:
    print(repr(sibling))

# 输出结果
' 和\n'
<a class="people" href="http://example.com/lisi" id="link2">李四</a>
',\n'
<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>
'从前有三个人;他们的名字是\n'
```

#### 6.4 回退和前进

- .next_element 和 .previous_element

.next_element 和 .next_sibling 相似，但通常输出结果不一致
```
last_a_tag = soup.find("a", id="link3")
print(last_a_tag)
print(last_a_tag.next_sibling)
print(last_a_tag.next_element)

# 输出结果
<a class="people" href="http://example.com/wangwu" id="link3">王五</a>
;
他们住在一个四合院。
王五
```
对比一下，.next_sibling输出的是闭合区间的下一个，.next_element输出的是非闭合区间的下一个

.previous_element 属性刚好与 .next_element 相反,它指向当前被解析的对象的前一个解析对象:

```
last_a_tag = soup.find("a", id="link3")
print(last_a_tag)
print(last_a_tag.previous_sibling)
print(last_a_tag.previous_element)

# 输出结果
 和\n
 和\n
```

- .next_elements 和 .previous_elements

```
last_a_tag = soup.find("a", id="link3")
for element in last_a_tag.next_elements:
    print(repr(element))

# 输出结果
'王五'
';\n他们住在一个四合院。'
'\n'
<p class="example">...</p>
'...'
'\n'
```

### 7. 搜索方法

Beautiful Soup有很多搜索方法，这里主要说一下: `find()`和`find_all()`。

举个例子：

```
html_doc = """
<html><head><title>这是一个例子</title></head>
<body>
<p class="title"><b>这是一个例子</b></p>

<p class="story">从前有三个人;他们的名字是
<a href="http://example.com/zhangsan" class="people" id="link1">张三</a>,
<a href="http://example.com/lisi" class="people" id="link2">李四</a> 和
<a href="http://example.com/wangwu" class="people" id="link3">王五</a>;
他们住在一个四合院。</p>

<p class="example">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

#### 7.1 过滤器

过滤器主要有字符串、正则表达式、列表、True、方法等

- 字符串

在Beautiful Soup中传入一个字符串，查找与字符串完整匹配的内容，如下：

```
print(soup.find_all('b'))

# 输出结果
[<b>这是一个例子</b>]
```

- 正则表达式

在Beautiful Soup中传入正则表达式，则通过search()来匹配内容，如下：

```
import re

for tag in soup.find_all(re.compile("b")):
    print(tag.name)

# 输出结果
body
b
```

```
import re

for tag in soup.find_all(re.compile("t")):
    print(tag.name)

# 输出结果
html
title
```

- 列表

在Beautiful Soup中传入列表，则匹配列表中任一元素的内容，如下：

```
print(soup.find_all(["a", "b"]))

# 输出结果
[<b>这是一个例子</b>, <a class="people" href="http://example.com/zhangsan" id="link1">张三</a>, <a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
```

- True

True或以匹配任何值，如下：

```
for tag in soup.find_all(True):
    print(tag.name)

# 输出结果
html
head
title
body
p
b
p
a
a
a
p
```

- 方法

如果没有合适的过滤器，那就自定义一个方法，方法只接受一个参数，如下：

```
def not_zhangsan(href):
    return href and not re.compile("zhangsan").search(href)
```

使用这个方法可以得到链接中没有`zhangsan`的其他链接，如下：

```
print(soup.find_all(href=not_zhangsan))

# 输出结果
[<a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
```

#### 7.2 find_all()

`find_all()`格式如下：`find_all( name , attrs , recursive , string , **kwargs )`

`find_all`方法搜索当前tag的所有符合过滤器条件的子节点，如下：

- name参数

`name`参数可以查找所有名字为`name`的tag，如下：

```
print(soup.find_all("title"))

# 输出结果
[<title>这是一个例子</title>]
```

- keyword参数

查找指定参数包含的关键字的tag，如下：

查找id为link2的tag

```
print(soup.find_all(id="link2"))

# 输出结果
[<a class="people" href="http://example.com/lisi" id="link2">李四</a>]
```

查找href中包含zhangsan的tag, 如下：

```
import re
print(soup.find_all(href=re.compile("zhangsan")))

# 输出结果
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>]
```

查找有id属性的tag, 如下：

```
print(soup.find_all(id=True))

# 输出结果
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>, <a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
```

同时指定多个过滤属性，如下：
```
print(soup.find_all(href=re.compile("example.com"), id='link1'))

# 输出结果
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>]
```

有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性, 但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag::

```
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'html.parser')
print(data_soup.find_all(attrs={"data-foo": "value"}))

# 输出结果
[<div data-foo="value">foo!</div>]
```

- 按CSS搜索

通过`class_`参数搜索指定的CSS类名tag, 如下：

```
print(soup.find_all("a", class_="people"))

# 输出结果
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>, <a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
```

`class_`参数可接受各种类型的过滤器，如字符串、正则表达式、方法和True:

```
print(soup.find_all(class_=re.compile("itl")))
# 输出结果
[<p class="title"><b>这是一个例子</b></p>]

def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6
print(soup.find_all(class_=has_six_characters))
# 输出结果
[<p class="title"><b>这是一个例子</b></p>]
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>, <a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
```

tag的`class`可以是多个，每个都能用，也可以完全匹配，完全匹配时类名顺序不可变，如下：

```
css_soup = BeautifulSoup('<p class="dev test"></p>', 'html.parser')
print(css_soup.find_all("p", class_="dev"))
print(css_soup.find_all("p", class_="test"))
print(css_soup.find_all("p", class_="dev test"))

# 输出结果
[<p class="dev test"></p>]
[<p class="dev test"></p>]
[<p class="dev test"></p>]
```

还可以通过`attrs`来查找相关的内容，如下：

```
print(soup.find_all("a", attrs={"class": "people"}))

# 输出结果
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>, <a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
```

- string参数

通过 string 参数可以搜搜文档中的字符串内容，如下：

```
print(soup.find_all(string="张三"))
# 输出结果
['张三']

print(soup.find_all(string=["张三", "李四", "王五"]))
# 输出结果
['张三', '李四', '王五']

print(soup.find_all(string=re.compile("例子")))
# 输出结果
['这是一个例子', '这是一个例子']

def is_the_only_string_within_a_tag(s):
    return (s == s.parent.string)
print(soup.find_all(string=is_the_only_string_within_a_tag))
# 输出结果
['这是一个例子', '这是一个例子', '张三', '李四', '王五', '...']
```

string参数还可以与其它参数混合使用，如下：

```
print(soup.find_all("a", string="张三"))

# 输出结果
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>]
```

- limit参数

limit参数可限制搜索的量，与mysql中的limit有些相似，如下：

```
print(soup.find_all("a", limit=1))

# 输出结果
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>]
```

- recursive参数

`recursive=False`只搜索tag的直接子节点，如下：
```
print(soup.html.find_all("title"))
print(soup.html.find_all("title", recursive=False))

输出结果：
[<title>这是一个例子</title>]
[]
```

- `find_all()`的简写方法

下面的代码是等价的，如下：

```
soup.find_all("a")
soup("a")

soup.title.find_all(string=True)
soup.title(string=True)
```

#### 7.3 find()

find函数格式，如下：
```
find( name , attrs , recursive , string , **kwargs )
```

find()函数返回找到的第一个结果，等同于find_all()方法设置limit=1的情况，如下：

```
print(soup.find_all('title', limit=1))
print(soup.find('title'))

# 输出结果
[<title>这是一个例子</title>]
<title>这是一个例子</title>
```

不同的是，find_all()返回的是列表，find()返回的是字符串。

目标为空时，find_all()返回[]，find()返回None。

```
print(soup.find_all('test'))
print(soup.find('test'))

# 输出结果
[]
None
```

find()函数的简写：

```
soup.head.title 等同于soup.find("head").find("title")

```

#### 7.4 find_parents()和find_parent()

find_parents()格式如下：

```
find_parents( name , attrs , recursive , string , **kwargs )
```

find_parent()格式如下：

```
find_parent( name , attrs , recursive , string , **kwargs )
```

find_parents()用来搜索当前节点的父辈节点，find_parent() 用来搜索当前节点的父辈节点的第一个结果, 如下：

```
string = soup.find(string="张三")
print(string)
print(string.find_parents("a"))
print(string.find_parent("a"))
print(string.find_parents("p", id = "link1"))

# 输出结果
张三
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>]
<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>
[]
```

从上面的结果看出，`find_parents()`输出的是列表，`find_parent()`输出的是字符串。还有包含id值为link1的`<p>`标签找不到。

#### 7.5 find_next_sibling()和find_next_sibling()

find_next_sibling()格式如下：

```
find_next_siblings( name , attrs , recursive , string , **kwargs )
```

find_next_sibling()格式如下：

```
find_next_sibling( name , attrs , recursive , string , **kwargs )
```

`find_next_siblings()`方法返回所有符合条件的后面的兄弟节点, `find_next_sibling()`只返回符合条件的后面的第一个tag节点, 举例如下：

```
first_link = soup.a
print(first_link)
print(first_link.find_next_siblings("a"))
first_story_paragraph = soup.find("p", "story")
print(first_story_paragraph.find_next_sibling("p"))

# 输出结果
<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>
[<a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
<p class="example">...</p>
```

#### 7.6 find_previous_sibings()和find_previous_sibing()

find_previous_sibings()格式如下：

```
find_previous_siblings( name , attrs , recursive , string , **kwargs )
```

find_previous_sibing()格式如下：

```
find_previous_sibling( name , attrs , recursive , string , **kwargs )
```

`find_previous_siblings()`方法返回所有符合条件的前面的兄弟节点, `find_previous_sibling()`方法返回第一个符合条件的前面的兄弟节点, 举例如下：

```
last_link = soup.find("a", id="link3")
print(last_link)
print(last_link.find_previous_siblings("a"))
first_story_paragraph = soup.find("p", "story")
print(first_story_paragraph.find_previous_sibling("p"))

# 输出结果
<a class="people" href="http://example.com/wangwu" id="link3">王五</a>
[<a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/zhangsan" id="link1">张三</a>]
<p class="title"><b>这是一个例子</b></p>
```

#### 7.7 find_all_next()和find_next()

find_all_next()格式如下：

```
find_all_next( name , attrs , recursive , string , **kwargs )
```

find_next()格式如下：

```
find_next( name , attrs , recursive , string , **kwargs )
```

`find_all_next()`方法返回所有符合条件的节点, `find_next()`方法返回第一个符合条件的节点，举例如下：

```
first_link = soup.a
print(first_link)
print(first_link.find_all_next(string=True))
print(first_link.find_next("p"))

# 输出结果
<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>
['张三', ',\n', '李四', ' 和\n', '王五', ';\n他们住在一个四合院。', '\n', '...', '\n']
<p class="example">...</p>
```

#### 7.8 find_all_previous()和find_previous()

find_all_previous()格式如下：

```
find_all_previous( name , attrs , recursive , string , **kwargs )
```

find_previous()格式如下：

```
find_previous( name , attrs , recursive , string , **kwargs )
```

`find_all_previous()`方法返回所有符合条件的节点, `find_previous()`方法返回第一个符合条件的节点，举例如下：

```
first_link = soup.a
print(first_link)
print(first_link.find_all_previous("p"))
print(first_link.find_previous("title"))

# 输出结果
<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>
[<p class="story">从前有三个人;他们的名字是
<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>,
<a class="people" href="http://example.com/lisi" id="link2">李四</a> 和
<a class="people" href="http://example.com/wangwu" id="link3">王五</a>;
他们住在一个四合院。</p>, <p class="title"><b>这是一个例子</b></p>]
<title>这是一个例子</title>
```

#### 7.9 CSS选择器

在 Tag 或 BeautifulSoup 对象的 .select() 方法中传入字符串参数, 即可使用CSS选择器的语法找到tag，举例如下：

```
print(soup.select("title"))
print(soup.select("p:nth-of-type(3)"))

# 输出结果
[<title>这是一个例子</title>]
[<p class="example">...</p>]
```

找到兄弟节点标签:
```
print(soup.select("#link1 ~ .people"))
print(soup.select("#link1 + .people"))

# 输出结果
[<a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
[<a class="people" href="http://example.com/lisi" id="link2">李四</a>]
```

通过CSS的类名查找:

```
print(soup.select(".people"))
print(soup.select("[class~=people]"))

# 输出结果
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>, <a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>, <a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
```

通过tag的id查找:

```
print(soup.select("#link1"))
print(soup.select("a#link2"))

# 输出结果
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>]
[<a class="people" href="http://example.com/lisi" id="link2">李四</a>]
```

同时用多种CSS选择器查询元素:

```
print(soup.select("#link1,#link2"))

# 输出结果

```
通过是否存在某个属性来查找:

```
print(soup.select('a[href]'))

# 输出结果
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>, <a class="people" href="http://example.com/lisi" id="link2">李四</a>]
```

通过属性的值来查找:

```
print(soup.select('a[href="http://example.com/zhangsan"]'))
print(soup.select('a[href^="http://example.com/"]'))
print(soup.select('a[href$="lisi"]'))
print(soup.select('a[href*=".com/wa"]'))

# 输出结果
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>]
[<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>, <a class="people" href="http://example.com/lisi" id="link2">李四</a>, <a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
[<a class="people" href="http://example.com/lisi" id="link2">李四</a>]
[<a class="people" href="http://example.com/wangwu" id="link3">王五</a>]
```

返回查找到的元素的第一个

```
print(soup.select_one(".people"))

# 输出结果
<a class="people" href="http://example.com/zhangsan" id="link1">张三</a>
```

### 8. 修改方法

#### 8.1 修改tag的名称和属性

修改tag的名字，改变属性的值，添加或者删除属性

```
soup = BeautifulSoup('<b class="test">这是一个例子</b>', 'html.parser')
tag = soup.b

tag.name = "blockquote"
tag['class'] = 'dev'
tag['id'] = 1
print(tag)

del tag['class']
del tag['id']
print(tag)

# 输出结果
<blockquote class="dev" id="1">这是一个例子</blockquote>
<blockquote>这是一个例子</blockquote>
```

#### 8.2 修改 .string

给tag的 .string 属性赋值，替代原来的内容：

```
markup = '<a href="http://example.com/">这是一个链接</a>'
soup = BeautifulSoup(markup, 'html.parser')

tag = soup.a
print(tag)
tag.string = "新链接"
print(tag)

# 输出结果
<a href="http://example.com/">这是一个链接</a>
<a href="http://example.com/">新链接</a>
```

#### 8.3 append()

`append()`给tag添加内容，同python append()方法：

```
soup = BeautifulSoup("<a>测试</a>", 'html.parser')
soup.a.append("开发")

print(soup)
print(soup.a.contents)

# 输出结果
<a>测试开发</a>
['测试', '开发']
```

#### 8.4 NavigableString() 和 .new_tag()

添加一段文本内容或注释，用`NavigableString()`, 如下：

```
from bs4 import NavigableString
soup = BeautifulSoup("<b></b>", 'html.parser')
tag = soup.b
tag.append("你好")
new_string = NavigableString(" 我是谁")
tag.append(new_string)
print(tag)
print(tag.contents)

from bs4 import Comment
new_comment = soup.new_string("这是一个注释。", Comment)
tag.append(new_comment)
print(tag)
print(tag.contents)

# 输出结果
<b>你好 我是谁</b>
['你好', ' 我是谁']
<b>你好 我是谁<!--这是一个注释。--></b>
['你好', ' 我是谁', '这是一个注释。']
```

创建一个tag用`.new_tag()`, 如下：

```
soup = BeautifulSoup("<b></b>", 'html.parser')
tag = soup.b

new_tag = soup.new_tag("a", href="http://www.example.com")
print(new_tag)
tag.append(new_tag)
print(tag)

new_tag.string = "看这里"
print(tag)

# 输出结果
<a href="http://www.example.com"></a>
<b><a href="http://www.example.com"></a></b>
<b><a href="http://www.example.com">看这里</a></b>
```

#### 8.5 insert()

`insert()`将内容插入到指定位置，如下：

```
markup = '<a href="http://example.com/">这<i>是</i>一个例子</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
tag = soup.a

tag.insert(1, "不")
print(tag)
print(tag.contents)

# 输出结果
<a href="http://example.com/">这不<i>是</i>一个例子</a>
['这', '不', <i>是</i>, '一个例子']
```

#### 8.6 insert_before() 和 insert_after()

`insert_before()`在当前tag或文本节点前插入内容，`insert_after()`方法在当前tag或文本节点后插入内容，如下：

```
soup = BeautifulSoup("<b>吃苹果</b>", 'html.parser')
tag = soup.new_tag("i")
tag.string = "不要"
soup.b.string.insert_before(tag)
print(soup.b)
soup.b.i.insert_after(soup.new_string("不要"))
print(soup.b)

# 输出结果
<b><i>不要</i>吃苹果</b>
<b><i>不要</i>不要吃苹果</b>
```

#### 8.7 clear()

`clear()`方法移除当前tag的内容:

```
markup = '<a href="http://example.com/">这是一个例子</a>'
soup = BeautifulSoup(markup, 'html.parser')
tag = soup.a
print(tag)
tag.clear()
print(tag)

# 输出结果
<a href="http://example.com/">这是一个例子</a>
<a href="http://example.com/"></a>
```

#### 8.8 extract()

`extract()`方法将当前tag移除,并作为方法结果返回:

```
markup = '<a href="http://example.com/">这是一个<i>例子</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a
i_tag = soup.i.extract()
print(a_tag)
print(i_tag)
print(i_tag.parent)

# 输出结果
<a href="http://example.com/">这是一个</a>
<i>例子</i>
None
```

#### 8.9 decompose()

`decompose()`方法将当前节点移除并完全销毁:

```
markup = '<a href="http://example.com/">这是一个<i>例子</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a
i_tag = soup.i.decompose()
print(a_tag)
print(i_tag)

# 输出结果
<a href="http://example.com/">这是一个</a>
None
```
#### 8.10 replace_with()

`replace_with()`方法移除某段内容,并用新tag或文本节点替代它:

```
markup = '<a href="http://example.com/">这是一个<i>例子</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a
new_tag = soup.new_tag("b")
new_tag.string = "错误"
a_tag.i.replace_with(new_tag)
print(a_tag)

# 输出结果
<a href="http://example.com/">这是一个<b>错误</b></a>
```

#### 8.11 wrap()

`wrap()`方法可以对指定的tag元素进行包装,并返回包装后的结果:

```
soup = BeautifulSoup("<p>这是一个例子</p>", 'html.parser')
print(soup.p.string.wrap(soup.new_tag("b")))
print(soup.p.wrap(soup.new_tag("div")))

# 输出结果
<b>这是一个例子</b>
<div><p><b>这是一个例子</b></p></div>
```

#### 8.12 unwrap()

`wrap()`方法将移除tag内的所有tag标签:

```
markup = '<a href="http://example.com/">这是一个<i>例子</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a
i_tag = a_tag.i.unwrap()
print(a_tag)
print(i_tag)

# 输出结果
<a href="http://example.com/">这是一个例子</a>
<i></i>
```
### 9. 输出

#### 9.1 格式化输出

`prettify()`方法将Beautiful Soup格式化输出，如下：

```
markup = '<a href="http://example.com/">这是一个<i>例子</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
print(soup.prettify())

# 输出结果
<a href="http://example.com/">
 这是一个
 <i>
  例子
 </i>
</a>
```

#### 9.2 压缩输出

使用`str()`得到一个字符串，如下：

```
markup = '<a href="http://example.com/">这是一个<i>例子</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
print(str(soup))

# 输出结果
<a href="http://example.com/">这是一个<i>例子</i></a>
```

#### 9.3 输出格式

转化Beautiful Soup中的HTML特殊字符，如下：

```
soup = BeautifulSoup("&ldquo;Dammit!&rdquo; he said.",'html.parser')
print(str(soup))

# 输出结果
“Dammit!” he said.
```

#### 9.4 get_text()

得到tag中的文本内容，使用`get_text()`, 如下：

```
markup = '<a href="http://example.com/"> 这是一个<i>例子</i> </a>'
soup = BeautifulSoup(markup, 'html.parser')
print(soup.get_text())
print(soup.i.get_text())

# 输出结果
 这是一个例子 
例子
```

可以通过参数指定tag的文本内容的分隔符:

```
print(soup.get_text("|"))

# 输出结果
 这是一个|例子| 
```

还可以去除获得文本内容的前后空格:

```
print(soup.get_text("|", strip=True))

# 输出结果
这是一个|例子
```

使用`stripped_strings`生成器,以列表存储获得的文本:

```
print([text for text in soup.stripped_strings])

# 输出结果
['这是一个', '例子']
```