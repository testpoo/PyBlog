title: Markdown笔记
date: 2020-04-03
category: 技术
tag: markdown

[TOC]

### 1. Markdown 标题

**使用 = 和 - 标记一级和二级标题**

= 和 - 标记语法格式如下：

```
我展示的是一级标题
=================

我展示的是二级标题
-----------------
```

显示效果如下图：

# 我展示的是一级标题

## 我展示的是二级标题

使用 # 号标记

使用 # 号可表示 1-6 级标题，一级标题对应一个 # 号，二级标题对应两个 # 号，以此类推。

```
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```

显示效果如下图：

# 一级标题

## 二级标题

### 三级标题

#### 四级标题

##### 五级标题

###### 六级标题

### 2. Markdown 段落

Markdown 段落没有特殊的格式，直接编写文字就好，段落的换行是使用两个以上空格加上回车。

当然也可以在段落后面使用一个空行来表示重新开始一个段落。

#### 字体

Markdown 可以使用以下几种字体：

```
*斜体文本*
_斜体文本_
**粗体文本**
__粗体文本__
***粗斜体文本***
___粗斜体文本___
```

显示效果如下所示：

*斜体文本*

_斜体文本_

**粗体文本**

__粗体文本__

***粗斜体文本***

___粗斜体文本___

#### 分隔线

你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线：

```
***

* * *

*****

- - -

----------
```

显示效果如下所示：

***

* * *

*****

- - -

----------

#### 下划线

下划线可以通过 HTML 的`<u>`标签来实现：

```
<u>带下划线文本</u>
```

显示效果如下所示：

<u>带下划线文本</u>

#### 脚注

脚注是对文本的补充说明。

Markdown 脚注的格式如下:

[^要注明的文本] 以下实例演示了脚注的用法：

```
创建脚注格式类似这样 [^TESTPOO]。

[^TESTPOO]: Markdown笔记 -- 做个记录方便查找！！！
```

演示效果如下：

创建脚注格式类似这样 [^TESTPOO]。

[^TESTPOO]: Markdown笔记 -- 做个记录方便查找！！！

### 3. Markdown 列表

Markdown 支持有序列表和无序列表。

无序列表使用星号(*)、加号(+)或是减号(-)作为列表标记：

```
* 第一项
* 第二项
* 第三项

+ 第一项
+ 第二项
+ 第三项

- 第一项
- 第二项
- 第三项
```

显示结果如下：

* 第一项

* 第二项

* 第三项
+ 第一项

+ 第二项

+ 第三项
- 第一项

- 第二项

- 第三项

有序列表使用数字并加上.号来表示，如：

```
1. 第一项
2. 第二项
3. 第三项
```

显示结果如下：

1. 第一项
2. 第二项
3. 第三项

#### 列表嵌套

列表嵌套只需在子列表中的选项添加四个空格即可：

```
1. 第一项：
    - 第一项嵌套的第一个元素
    - 第一项嵌套的第二个元素
2. 第二项：
    - 第二项嵌套的第一个元素
    - 第二项嵌套的第二个元素
```

显示结果如下：

1. 第一项：
   - 第一项嵌套的第一个元素
   - 第一项嵌套的第二个元素
2. 第二项：
   - 第二项嵌套的第一个元素
   - 第二项嵌套的第二个元素

### 4. Markdown 区块

Markdown 区块引用是在段落开头使用 > 符号 ，然后后面紧跟一个空格符号：

```
> 区块引用
> Markdown笔记
> 做个记录方便查找
```

显示结果如下：

> 区块引用
> Markdown笔记
> 做个记录方便查找

另外区块是可以嵌套的，一个 > 符号是最外层，两个 > 符号是第一层嵌套，以此类推：

```
> 最外层
> > 第一层嵌套
> > > 第二层嵌套
```

显示结果如下：

> 最外层
> 
> > 第一层嵌套
> > 
> > > 第二层嵌套

#### 区块中使用列表

区块中使用列表实例如下：

```
> 区块中使用列表
> 1. 第一项
> 2. 第二项
> + 第一项
> + 第二项
> + 第三项
```

显示结果如下：

> 区块中使用列表
> 
> 1. 第一项
> 2. 第二项
> + 第一项
> + 第二项
> + 第三项

#### 列表中使用区块

如果要在列表项目内放进区块，那么就需要在 > 前添加四个空格的缩进。

区块中使用列表实例如下：

```
* 第一项
    > Markdown笔记
    > 做个记录方便查找
* 第二项
```

显示结果如下：

* 第一项
  
  > Markdown笔记
  > 做个记录方便查找
* 第二项

### 5. Markdown 代码

如果是段落上的一个函数或片段的代码可以用反引号把它包起来（`），例如：

```
`print()` 函数
```

显示结果如下：

`print()` 函数

#### 代码区块

代码区块使用 4 个空格或者一个制表符（Tab 键）。

实例如下：

```
    ```
    print('这是Tab')

    print('这是四个空格')
    ```
```

显示结果如下：

```
    print('这是Tab')

    print('这是四个空格')
```

你也可以用 ``` 包裹一段代码，并指定一种语言（也可以不指定）：

```
    ```python
print('This is a test!')
    ```
```

显示结果如下：

```python
print('This is a test!')
```

### 6. Markdown 链接

链接使用方法如下：

```
[链接名称](链接地址)
```

或者

```
<链接地址>
```

例如：

```
这是一个链接 [Markdown笔记](https://testpoo.github.io/)
```

显示结果如下：

这是一个链接 [Markdown笔记](https://testpoo.github.io/)

直接使用链接地址：

```
<https://testpoo.github.io/>
```

显示结果如下：

<https://testpoo.github.io/>

#### 高级链接

我们可以通过变量来设置一个链接，变量赋值在文档末尾进行：

```
这个链接用 1 作为网址变量 [Baidu][1]
这个链接用 testpoo 作为网址变量 [Testpoo][testpoo]
然后在文档的结尾为变量赋值（网址）

  [1]: http://www.baidu.com/
  [testpoo]: https://testpoo.github.io/
```

显示结果如下：

这个链接用 1 作为网址变量 [Baidu][1]

这个链接用 testpoo 作为网址变量 [Testpoo][testpoo]

然后在文档的结尾为变量赋值（网址）

  [1]: http://www.baidu.com/
  [testpoo]: https://testpoo.github.io/

### 7. Markdown 图片

Markdown 图片语法格式如下：

```
![alt 属性文本](图片地址)

![alt 属性文本](图片地址 "可选标题")
```

- 开头一个感叹号 !

- 接着一个方括号，里面放上图片的替代文字

- 接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上选择性的 'title' 属性的文字。

使用实例：

```
![TESTPOO 图标](https://testpoo.github.io/themes/img/favicon.ico)

![TESTPOO 图标](https://testpoo.github.io/themes/img/favicon.ico "TESTPOO")
```

显示结果如下：

![TESTPOO 图标](https://testpoo.github.io/themes/img/favicon.ico)

![TESTPOO 图标](https://testpoo.github.io/themes/img/favicon.ico "TESTPOO")

当然，你也可以像网址那样对图片网址使用变量:

```
这个链接用 1 作为网址变量 [TESTPOO][1].
然后在文档的结尾为变量赋值（网址）

[1]: https://testpoo.github.io/themes/img/favicon.ico
```

显示结果如下：

[1]: https://testpoo.github.io/themes/img/favicon.ico

这个链接用 1 作为网址变量 TESTPOO. 然后在文档的结尾为变量赋值（网址）

Markdown 还没有办法指定图片的高度与宽度，如果你需要的话，你可以使用普通的  标签。

```
<img src="https://testpoo.github.io/themes/img/favicon.ico" width="50%">
```

显示结果如下：

<img src="https://testpoo.github.io/themes/img/favicon.ico" width="50%">

### 8. Markdown 表格

Markdown 制作表格使用 | 来分隔不同的单元格，使用 - 来分隔表头和其他行。

语法格式如下：

```
|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |
```

以上代码显示结果如下：

| 表头  | 表头  |
| --- | --- |
| 单元格 | 单元格 |
| 单元格 | 单元格 |

对齐方式

我们可以设置表格的对齐方式：

- -: 设置内容和标题栏居右对齐。
- :- 设置内容和标题栏居左对齐。
- :-: 设置内容和标题栏居中对齐。

实例如下：

```
| 左对齐 | 右对齐 | 居中对齐 |
| :-----| ----: | :----: |
| 单元格 | 单元格 | 单元格 |
| 单元格 | 单元格 | 单元格 |
```

以上代码显示结果如下：

| 左对齐 | 右对齐 | 居中对齐 |
|:--- | ---:|:----:|
| 单元格 | 单元格 | 单元格  |
| 单元格 | 单元格 | 单元格  |

### 9. Markdown 高级技巧

支持的 HTML 元素不在 Markdown 涵盖范围之内的标签，都可以直接在文档里面用 HTML 撰写。

#### 转义

Markdown 使用了很多特殊符号来表示特定的意义，如果需要显示特定的符号则需要使用转义字符，Markdown 使用反斜杠转义特殊字符：

```
**文本加粗** 
\*\* 正常显示星号 \*\*
```

输出结果为：

**文本加粗** 
\*\* 正常显示星号 \*\*

Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：

```
\   反斜线
`   反引号
*   星号
_   下划线
{}  花括号
[]  方括号
()  小括号
#   井字号
+   加号
-   减号
.   英文句点
!   感叹号
```
