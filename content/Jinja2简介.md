title: Jinja2简介
date: 2024-02-29
category: python
tag: Jinja2

[TOC]

### 1. 简介

Jinja 是一个快速、表现力强、可扩展的模板引擎。模板中的特殊占位符允许编写类似 Python 语法的代码。然后将数据传递给模板，以渲染最终文档。



特点：

*   模板继承；

*   可在模板中定义和导入宏；

*   HTML 模板可使用自动换码功能，防止来自不受信任用户输入的 XSS；

*   沙箱环境可安全地呈现不受信任的模板；

*   支持异步，可生成无需额外语法即可自动处理同步和异步函数的模板；

*   通过 `Babel` 支持 I18N；

*   模板会及时编译为优化的 Python 代码并缓存，也可以提前编译；

*   精确展示模板中的异常行，使调试更容易；

*   可扩展过滤器、测试、函数甚至语法。

### 2. 安装

建议使用最新版本的 Python。Jinja 支持 Python 3.7 及更新版本。建议使用虚拟环境，以便将项目依赖关系与其他项目和系统隔离。

使用 pip 安装最新版本的 Jinja：

```Shell
$ pip install Jinja2
```

#### 2.1 依赖项

**安装 Jinja 时会自动安装这些依赖项。**

`MarkupSafe` 会在渲染模板时转义不信任的输入，以避免注入攻击。

#### 2.2 可选依赖项

**安装 Jinja 时不会自动安装。**

`Babel` 在模板中提供翻译支持。

#### 2.3 基本API使用

最基本的方式就是通过 `Template` 创建一个模板并渲染它。

```Shell
>>> from jinja2 import Template
>>> template = Template('Hello {{ name }}!')
>>> template.render(name='test poo')
'Hello test poo!'
```

### 3 API

#### 3.1 基础知识

Jinja 使用一个名为 "模板环境 "的中心对象。该类的实例用于存储配置和全局对象，并用于从文件系统或其他位置加载模板。即使您使用模板类的构造函数从字符串创建模板，也会自动创建一个环境。



配置 `Jinja` 为应用程序加载模板的最简单方法是使用 `PackageLoader`。

```Python
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("yourapp")
    autoescape=select_autoescape()
)
```

这将创建一个带有加载器的模板环境，加载器会在 yourapp Python 软件包内的模板文件夹中查找模板。它还会启用 HTML 文件的自动换码功能。该加载器只要求 yourapp 是可导入的，它会为你找出文件夹的绝对路径。



不同的加载器可用于以其他方式或从其他位置加载模板。它们都列在下面的加载器部分。如果你想从更适合你的项目的来源加载模板，也可以自己编写。



要从该环境加载模板，请使用 get\_template() 方法，它会返回已加载的模板。

```Python
template = env.get_template("mytemplate.html") 
```

调用 `render()` 方法用一些变量渲染模板。

    print(template.render(the="variables", go="here"))

使用模板加载器而不是向 Template 或 Environment.from\_string() 传递字符串有很多好处。除了更容易使用外，它还能实现模板继承。

#### 3.2 高级API

高级应用程序接口（High Level API）是您将在应用程序中使用的应用程序接口，用于加载和呈现 Jinja 模板。而低级应用程序接口（Low Level API）只有在你想深入研究 Jinja或开发扩展时才有用。



详见：<https://jinja.palletsprojects.com/en/3.1.x/api/#high-level-api>

### 4 模板

**简介**

Jinja 模板是一个简单的文本文件。Jinja 可以生成任何基于文本的格式（HTML、XML、CSV、LaTeX 等）。Jinja 模板不需要特定的扩展名：.html、.xml 或任何其他扩展名都可以。

一个模板包含变量和/或表达式，当模板被渲染时，这些变量和/或表达式将被替换为值；还包含标签，用于控制模板的逻辑。

下面是一个模板示例：

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ a_variable }}

    {# a comment #}
</body>
</html>
```

上面的示例显示了默认配置设置。应用程序开发人员可以将语法配置从 `{% foo %}` 更改为 `<% foo %>` 或类似内容。

有几种分隔符。Jinja 的默认分隔符配置如下：

*   {% ... %} 用于语句

*   {{ ... }} 用于要打印到模板输出的表达式

*   {# ... #} 表示不包含在模板输出中的注释

行语句和注释也可以使用，但它们没有默认的前缀字符。要使用它们，请在创建环境时设置 `line_statement_prefix` 和 `line_comment_prefix`。

详见：<https://jinja.palletsprojects.com/en/3.1.x/templates/>

### 5 集成

#### 5.1 Flask

Flask 框架默认使用 Jinja 模板。Flask 会设置一个 Jinja 环境和模板加载器，并提供从视图函数轻松呈现模板的功能。

#### 5.2 Django

Django 支持使用 Jinja 作为模板引擎，请参见 <https://docs.djangoproject.com/en/stable/topics/templates/#support-for-template-engines。>



可集成的还有 [Babel](https://jinja.palletsprojects.com/en/3.1.x/integration/#babel) 和 [Pylons](https://jinja.palletsprojects.com/en/3.1.x/integration/#pylons)

### 6 实例

*   **渲染模板**

在这个模板中，`{{ title }}`、`{{ heading }}` 和 `{{ name }}` 是变量，将在渲染时被替换。

```Python
from jinja2 import Template

# 模板字符串
template_string = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>嗨, {{ name }}!</p>
</body>
</html>
"""

# 创建模板对象
template = Template(template_string)

# 渲染模板
print(template.render(title="测试一下", heading="欢迎一下", name="初学者")) 
```

**运行结果：**

    <!DOCTYPE html>
    <html>
    <head>
        <title>测试一下</title>
    </head>
    <body>
        <h1>欢迎一下</h1>
        <p>嗨, 初学者!</p>
    </body>
    </html>

*   **控制结构**

Jinja2支持常见的控制结构，例如条件判断和循环。下面是一个使用循环的例子：

    <ul>
    {% for item in item_list %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul> 

在Python代码中，提供一个列表来渲染这个模板：

    print(template.render(item_list=["苹果", "香蕉", "橘子"])) 

*   **模板继承**

模板继承是Jinja2的一个强大功能。你可以创建一个基础模板，然后在其他模板中继承和扩展它。例如：

**基础模板（base.html）:**

    <!DOCTYPE html>
    <html>
    <head>
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        {% block body %}
        {% endblock %}
    </body>
    </html> 

**子模板（child.html）:**

    {% extends "base.html" %}

    {% block title %}子页面标题{% endblock %}

    {% block body %}
        <p>这是子页面的内容。</p>
    {% endblock %} 

*   **过滤器**

Jinja2还提供了多种过滤器，用于转换变量。例如，使用 `capitalize` 过滤器将字符串的首字母大写：

    <p>{{ "hello world" | capitalize }}</p> 

过滤器是可以自己定义的，详见：<https://jinja.palletsprojects.com/en/3.1.x/api/#custom-filters>

*   **集成 flask**

**安装 flask**

    pip install flask

**项目结构**

    flaskr/
    │
    ├── templates/
    │   └── index.html
    │
    └── flaskr.py

**创建Jinja2模板**

在 `templates` 目录下创建一个 `index.html` 文件，作为我们的 `Jinja2` 模板。这个模板将简单地展示一个传入的变量。

```HTML
<!DOCTYPE html>
<html>
<head>
    <title>Flask with Jinja2</title>
</head>
<body>
    <h1>Welcome to Flask with Jinja2</h1>
    <p>Hello, {{ name }}!</p>
</body>
</html>
```

**Flask集成Jinja2**

在 `flaskr.py` 文件中，我们将创建一个FastAPI应用，并配置Jinja2环境。然后，我们将创建一个路由来渲染上面的模板。

```Python
from flask import Flask, render_template

# 创建我们的小程序 :)
app = Flask(__name__)

# 登陆页面
@app.route('/', methods=['GET', 'POST'])
def test():
    return render_template('index.html',name="test poo!")

if __name__ == '__main__':
    app.run()
```

**运行应用**

    python flaskr.py

打开浏览器，访问 `http://localhost:5000`，你将看到由 `Jinja2` 模板渲染的页面，其中包含了从 `Flask` 路由传递的变量。
