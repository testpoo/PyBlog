title: FastApi简析
date: 2023-12-06
category: 技术
tag: FastApi, python

[TOC]

# 1. 简介

FastAPI 是一个用于构建 API 的现代、快速（高性能）的 web 框架，使用 Python 3.6+ 并基于标准的 Python 类型提示。

关键特性:

- **快速**：可与 **NodeJS** 和 **Go** 并肩的极高性能（归功于 Starlette 和 Pydantic）。最快的 Python web 框架之一。

- **高效编码**：提高功能开发速度约 200％ 至 300％。

- **更少 bug**：减少约 40％ 的人为（开发者）导致的错误。

- **智能**：极佳的编辑器支持。处处皆可自动补全，减少调试时间。

- **简单**：设计易于使用和学习，阅读文档的时间更短。

- **简短**：使代码重复最小化。通过不同的参数声明实现丰富功能，bug 更少。

- **健壮**：生产可用级别的代码。还有自动生成的交互式文档。

- **标准化**：基于（并完全兼容）API 的相关开放标准：[OpenAPI](https://github.com/OAI/OpenAPI-Specification) (以前被称为 Swagger) 和 [JSON Schema](https://json-schema.org/)。

# 2. FastAPI 特性

**FastAPI** 提供了以下内容：

## 2.1 基于开放标准

- 用于创建 API 的 [**OpenAPI**](https://github.com/OAI/OpenAPI-Specification) 包含了路径操作，请求参数，请求体，安全性等的声明。
- 使用 [**JSON Schema**](https://json-schema.org/) (因为 OpenAPI 本身就是基于 JSON Schema 的)自动生成数据模型文档。
- 经过了缜密的研究后围绕这些标准而设计，并非狗尾续貂。
- 这也允许了在很多语言中自动**生成客户端代码**。

## 2.2 自动生成文档

交互式 API 文档以及具探索性 web 界面。因为该框架是基于 OpenAPI，所以有很多可选项，FastAPI 默认自带两个交互式 API 文档。

- [**Swagger UI**](https://github.com/swagger-api/swagger-ui)，可交互式操作，能在浏览器中直接调用和测试你的 API 。

![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)

- 另外的 API 文档：[**ReDoc**](https://github.com/Rebilly/ReDoc)

![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)

## 2.3 更主流的 Python

全部都基于标准的 **Python 3.6 类型**声明（感谢 Pydantic ）。没有新的语法需要学习。只需要标准的 Python 。

如果你需要2分钟来学习如何使用 Python 类型（即使你不使用 FastAPI ），看看这个简短的教程：[Python Types](https://fastapi.tiangolo.com/zh/python-types/)。

编写带有类型标注的标准 Python：

```python
from datetime import date
from pydantic import BaseModel 
# Declare a variable as a str 
# and get editor support inside the function 
def main(user_id: str): 
    return user_id 
    # A Pydantic model 
class User(BaseModel): 
    id: int 
    name: str 
    joined: date
```

可以像这样来使用：

```python
my_user: User = User(id=3, name="John Doe", joined="2018-07-19") 
second_user_data = {
    "id": 4,
    "name": "Mary",
    "joined": "2018-11-30",
}
my_second_user: User = User(**second_user_data)
```

`second_user_data` 意思是:

直接将`second_user_data`字典的键和值直接作为key-value参数传递，等同于：`User(id=4, name="Mary", joined="2018-11-30")`

## 2.4 编辑器支持

整个框架都被设计得易于使用且直观，所有的决定都在开发之前就在多个编辑器上进行了测试，来确保最佳的开发体验。

在最近的 Python 开发者调查中，我们能看到 [被使用最多的功能是"自动补全"](https://www.jetbrains.com/research/python-developers-survey-2017/#tools-and-features)。

整个 **FastAPI** 框架就是基于这一点的。任何地方都可以进行自动补全。

你几乎不需要经常回来看文档。

在这里，你的编辑器可能会这样帮助你：

- [Visual Studio Code](https://code.visualstudio.com/) 中:

![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)

- [PyCharm](https://www.jetbrains.com/pycharm/) 中:

![editor support](https://fastapi.tiangolo.com/img/pycharm-completion.png)

你将能进行代码补全，这是在之前你可能曾认为不可能的事。例如，在来自请求 JSON 体（可能是嵌套的）中的键 `price`。

不会再输错键名，来回翻看文档，或者来回滚动寻找你最后使用的 `username` 或者 `user_name` 。

## 2.5 简洁

任何类型都有合理的**默认值**，任何和地方都有可选配置。所有的参数被微调，来满足你的需求，定义成你需要的 API。

但是默认情况下，一切都能**顺利工作**。

## 2.6 验证

- 校验大部分（甚至所有）的 Python **数据类型**，包括：
  
  - JSON 对象 (`dict`).
  - JSON 数组 (`list`) 定义成员类型。
  - 字符串 (`str`) 字段, 定义最小或最大长度。
  - 数字 (`int`, `float`) 有最大值和最小值， 等等。

- 校验外来类型， 比如:
  
  - URL.
  - Email.
  - UUID.
  - ...及其他.

所有的校验都由完善且强大的 **Pydantic** 处理。

## 2.7 安全性及身份验证

集成了安全性和身份认证。杜绝数据库或者数据模型的渗透风险。

OpenAPI 中定义的安全模式，包括：

- HTTP 基本认证。
- **OAuth2** (也使用 **JWT tokens**)。在 [OAuth2 with JWT](https://fastapi.tiangolo.com/zh/tutorial/security/oauth2-jwt/)查看教程。
- API 密钥，在:
  - 请求头。
  - 查询参数。
  - Cookies, 等等。

加上来自 Starlette（包括 **session cookie**）的所有安全特性。

所有的这些都是可复用的工具和组件，可以轻松与你的系统，数据仓库，关系型以及 NoSQL 数据库等等集成。

## 2.8 依赖注入

FastAPI 有一个使用非常简单，但是非常强大的**依赖注入**系统。

- 甚至依赖也可以有依赖，创建一个层级或者**“图”依赖**。
- 所有**自动化处理**都由框架完成。
- 所有的依赖关系都可以从请求中获取数据，并且**增加了路径操作**约束和自动文档生成。
- 即使在依赖项中被定义的*路径操作* 也会**自动验证**。
- 支持复杂的用户身份认证系统，**数据库连接**等等。
- **不依赖**数据库，前端等。 但是和它们集成很简单。

## 2.9 无限制"插件"

或者说，导入并使用你需要的代码，而不需要它们。

任何集成都被设计得被易于使用（用依赖关系），你可以用和*路径操作*相同的结构和语法，在两行代码中为你的应用创建一个“插件”。

## 2.10 测试

- 100% 测试覆盖。
- 代码库100% 类型注释。
- 用于生产应用。

# 3. Starlette 特性

**FastAPI** 和 [**Starlette**](https://www.starlette.io/) 完全兼容(并基于)。所以，你有的其他的 Starlette 代码也能正常工作。`FastAPI` 实际上是 `Starlette`的一个子类。所以，如果你已经知道或者使用 Starlette，大部分的功能会以相同的方式工作。

通过 **FastAPI** 你可以获得所有 **Starlette** 的特性 ( FastAPI 就像加强版的 Starlette )：

- 令人惊叹的性能。它是 [Python 可用的最快的框架之一，和 **NodeJS** 及 **Go** 相当](https://github.com/encode/starlette#performance)。
- **支持 WebSocket** 。
- **支持 GraphQL** 。
- 后台任务处理。
- Startup 和 shutdown 事件。
- 测试客户端基于 HTTPX。
- **CORS**, GZip, 静态文件, 流响应。
- 支持 **Session 和 Cookie** 。
- 100% 测试覆盖率。
- 代码库 100% 类型注释。

# 4. Pydantic 特性

**FastAPI** 和 [**Pydantic**](https://pydantic-docs.helpmanual.io/) 完全兼容(并基于)。所以，你有的其他的 Pydantic 代码也能正常工作。

兼容包括基于 Pydantic 的外部库， 例如用与数据库的 ORMs, ODMs。

这也意味着在很多情况下，你可以将从请求中获得的相同对象**直接传到数据库**，因为所有的验证都是自动的。

反之亦然，在很多情况下，你也可以将从数据库中获取的对象**直接传到客户端**。

通过 **FastAPI** 你可以获得所有 **Pydantic** (FastAPI 基于 Pydantic 做了所有的数据处理)：

- **更简单**：
  - 没有新的模式定义 micro-language 需要学习。
  - 如果你知道 Python types，你就知道如何使用 Pydantic。
- 和你 **IDE/linter/brain** 适配:
  - 因为 pydantic 数据结构仅仅是你定义的类的实例；自动补全，linting，mypy 以及你的直觉应该可以和你验证的数据一起正常工作。
- **更快**：
  - 在 [基准测试](https://pydantic-docs.helpmanual.io/benchmarks/) 中，Pydantic 比其他被测试的库都要快。
- 验证**复杂结构**:
  - 使用分层的 Pydantic 模型, Python `typing`的 `List` 和 `Dict` 等等。
  - 验证器使我们能够简单清楚的将复杂的数据模式定义、检查并记录为 JSON Schema。
  - 你可以拥有深度**嵌套的 JSON** 对象并对它们进行验证和注释。
- **可扩展**:
  - Pydantic 允许定义自定义数据类型或者你可以用验证器装饰器对被装饰的模型上的方法扩展验证。
- 100% 测试覆盖率。

# 5. Python 类型提示简介

**Python 3.6+ 版本**加入了对"类型提示"的支持。

这些**类型提示**是一种新的语法（在 Python 3.6 版本加入）用来声明一个变量的类型。

通过声明变量的类型，编辑器和一些工具能给你提供更好的支持。

这只是一个关于 Python 类型提示的**快速入门 / 复习**。它仅涵盖与 **FastAPI** 一起使用所需的最少部分，实际上只有很少一点。

整个 **FastAPI** 都基于这些类型提示构建，它们带来了许多优点和好处。

但即使你不会用到 **FastAPI**，了解一下类型提示也会让你从中受益。

如果你已经精通 Python，并且了解关于类型提示的一切知识，直接跳到下一章节吧。

## 5.1 动机

让我们从一个简单的例子开始：

```python
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name print(get_full_name("john", "doe"))
```

运行这段程序将输出：

`John Doe`

这个函数做了下面这些事情：

- 接收 `first_name` 和 `last_name` 参数。
- 通过 `title()` 将每个参数的第一个字母转换为大写形式。
- 中间用一个空格来拼接它们。

### 5.1.1 修改示例

这是一个非常简单的程序。

现在假设你将从头开始编写这段程序。

在某一时刻，你开始定义函数，并且准备好了参数。

现在你需要调用一个"将第一个字母转换为大写形式的方法"。

等等，那个方法是什么来着？`upper`？还是 `uppercase`？`first_uppercase`？`capitalize`？

然后你尝试向程序员老手的朋友——编辑器自动补全寻求帮助。

输入函数的第一个参数 `first_name`，输入点号（`.`）然后敲下 `Ctrl+Space` 来触发代码补全。

但遗憾的是并没有起什么作用：

![](https://fastapi.tiangolo.com/img/python-types/image01.png)

### 5.1.2 添加类型

让我们来修改上面例子的一行代码。

我们将把下面这段代码中的函数参数从：

    first_name, last_name

改成：

    first_name: str, last_name: str

就是这样。

这些就是"类型提示"：

```python
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name
    print(get_full_name("john", "doe"))
```

这和声明默认值是不同的，例如：

    first_name="john", last_name="doe"

这两者不一样。

我们用的是冒号（`:`），不是等号（`=`）。

而且添加类型提示一般不会改变原来的运行结果。

现在假设我们又一次正在创建这个函数，这次添加了类型提示。

在同样的地方，通过 `Ctrl+Space` 触发自动补全，你会发现：

![](https://fastapi.tiangolo.com/img/python-types/image02.png)

这样，你可以滚动查看选项，直到你找到看起来眼熟的那个：

![](https://fastapi.tiangolo.com/img/python-types/image03.png)

## 5.2 更多动机

下面是一个已经有类型提示的函数：

```python
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + age
    return name_with_age
```

因为编辑器已经知道了这些变量的类型，所以不仅能对代码进行补全，还能检查其中的错误：

![](https://fastapi.tiangolo.com/img/python-types/image04.png)

现在你知道了必须先修复这个问题，通过 `str(age)` 把 `age` 转换成字符串：

```python
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age
```

## 5.3 声明类型

你刚刚看到的就是声明类型提示的主要场景。用于函数的参数。

这也是你将在 **FastAPI** 中使用它们的主要场景。

### 5.3.1 简单类型

不只是 `str`，你能够声明所有的标准 Python 类型。

比如以下类型：

- `int`
- `float`
- `bool`
- `bytes`

```python
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e
```

### 5.3.2 嵌套类型

有些容器数据结构可以包含其他的值，比如 `dict`、`list`、`set` 和 `tuple`。它们内部的值也会拥有自己的类型。

你可以使用 Python 的 `typing` 标准库来声明这些类型以及子类型。

它专门用来支持这些类型提示。

#### 5.3.2.1 列表

例如，让我们来定义一个由 `str` 组成的 `list` 变量。

从 `typing` 模块导入 `List`（注意是大写的 `L`）：

```python
from typing import List

def process_items(items: List[str]):
    for item in items:
        print(item)
```

同样以冒号（`:`）来声明这个变量。

输入 `List` 作为类型。

由于列表是带有"子类型"的类型，所以我们把子类型放在方括号中：

```python
from typing import List

def process_items(items: List[str]):
    for item in items:
        print(item)
```

这表示："变量 `items` 是一个 `list`，并且这个列表里的每一个元素都是 `str`"。

这样，即使在处理列表中的元素时，你的编辑器也可以提供支持。

没有类型，几乎是不可能实现下面这样：

![](https://fastapi.tiangolo.com/img/python-types/image05.png)

注意，变量 `item` 是列表 `items` 中的元素之一。

而且，编辑器仍然知道它是一个 `str`，并为此提供了支持。

#### 5.3.2.2 元组和集合

声明 `tuple` 和 `set` 的方法也是一样的：

```python
from typing import Set, Tuple

def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s
```

这表示：

- 变量 `items_t` 是一个 `tuple`，其中的前两个元素都是 `int` 类型, 最后一个元素是 `str` 类型。
- 变量 `items_s` 是一个 `set`，其中的每个元素都是 `bytes` 类型。

#### 5.3.2.3 字典

定义 `dict` 时，需要传入两个子类型，用逗号进行分隔。

第一个子类型声明 `dict` 的所有键。

第二个子类型声明 `dict` 的所有值：

```python
from typing import Dict

def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)
```

这表示：

- 变量 `prices` 是一个 `dict`：
  - 这个 `dict` 的所有键为 `str` 类型（可以看作是字典内每个元素的名称）。
  - 这个 `dict` 的所有值为 `float` 类型（可以看作是字典内每个元素的价格）。

### 5.3.3 类作为类型

你也可以将类声明为变量的类型。

假设你有一个名为 `Person` 的类，拥有 name 属性：

```python
class Person:
    def __init__(self, name: str):
        self.name = name

    def get_person_name(one_person: Person):
        return one_person.name
```

接下来，你可以将一个变量声明为 `Person` 类型：

```python
class Person:
    def __init__(self, name: str):
        self.name = name

    def get_person_name(one_person: Person):
        return one_person.name
```

然后，你将再次获得所有的编辑器支持：

![](https://fastapi.tiangolo.com/img/python-types/image06.png)

## 5.4 Pydantic 模型

[Pydantic](https://pydantic-docs.helpmanual.io/) 是一个用来用来执行数据校验的 Python 库。

你可以将数据的"结构"声明为具有属性的类。

每个属性都拥有类型。

接着你用一些值来创建这个类的实例，这些值会被校验，并被转换为适当的类型（在需要的情况下），返回一个包含所有数据的对象。

然后，你将获得这个对象的所有编辑器支持。

下面的例子来自 Pydantic 官方文档：

```python
class Person:
    def __init__(self, name: str):
        self.name = name

    def get_person_name(one_person: Person):
        return one_person.name
```

想进一步了解 [Pydantic，请阅读其文档](https://pydantic-docs.helpmanual.io/).

整个 **FastAPI** 建立在 Pydantic 的基础之上。

实际上你将在 [教程 - 用户指南](https://fastapi.tiangolo.com/zh/tutorial/) 看到很多这种情况。

## 5.5 FastAPI 中的类型提示

**FastAPI** 利用这些类型提示来做下面几件事。

使用 **FastAPI** 时用类型提示声明参数可以获得：

- **编辑器支持**。
- **类型检查**。

并且 **FastAPI** 还会用这些类型声明来：

- **定义参数要求**：声明对请求路径参数、查询参数、请求头、请求体、依赖等的要求。
- **转换数据**：将来自请求的数据转换为需要的类型。
- **校验数据**： 对于每一个请求：
  - 当数据校验失败时自动生成**错误信息**返回给客户端。
- 使用 OpenAPI **记录** API：
  - 然后用于自动生成交互式文档的用户界面。

听上去有点抽象。不过不用担心。你将在 [教程 - 用户指南](https://fastapi.tiangolo.com/zh/tutorial/) 中看到所有的实战。

最重要的是，通过使用标准的 Python 类型，只需要在一个地方声明（而不是添加更多的类、装饰器等），**FastAPI** 会为你完成很多的工作。
