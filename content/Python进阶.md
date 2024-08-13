title: Python进阶
date: 2021-11-30
category: 技术
tag: python

[TOC]

### `*args`和`**kwargs`

大部分人学习Python，很多时间都搞不清楚`*args`和`**kwargs`这两个变量。其实这两个变量并不是必须写`*args`和`**kwargs`。只要变量前面的`*`才是必须的。你也可以写成`*var`和`**vars`。写成`*args`和`**kwargs`只是一个通俗的命名约定。

#### `*args`

`*args`和`**kwargs`主要用于函数定义。你可以将不定数量的参数传递给一个函数。这里的不定的意思是：预先并不知道，函数使用者会传递多少个参数给你，所以在这个场景下使用这两个关键字。`*args`是用来发送一个非键值对的可变数量的参数列表给一个函数。例如：

```
def test_var_args(f_arg, *args):
    print("第一个普通的参数：", f_arg)
    for arg in args:
        print("另外一些通过*argv传递的参数:", arg)

test_var_args('苹果','香蕉','梨子','葡萄')
```

执行结果：

```
第一个普通的参数： 苹果
另外一些通过*argv传递的参数: 香蕉
另外一些通过*argv传递的参数: 梨子
另外一些通过*argv传递的参数: 葡萄
```

#### `**kwargs`的用法

`**kwargs`允许你将不定长度的键值对，作为参数传递给一个函数。如果你想要在一个函数里处理带名字的参数，你应该使用`**kwargs`。例如：

```
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

greet_me(name="苹果")
```

执行结果：

```
name == 苹果
```

现在可以看出怎样在一个函数里，处理一个键值对参数了。

#### 使用`*args`和`**kwargs`来调用函数

现在我们来看看怎样使用`*args`和`**kwargs`来调用一个函数。假设，有这样一个函数：

```
def test_args_kwargs(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3)
```

你可以使用`*args`和`**kwargs`来给这个函数传递参数，如下：

```
# 首先使用*args
args = ("二", 3, 5)
test_args_kwargs(*args)
```

执行结果：

```
arg1: 二
arg2: 3
arg3: 5
```

```
# 现在使⽤ **kwargs: 
kwargs = {"arg3": 3, "arg2": "二", "arg1": 5} 
test_args_kwargs(**kwargs) 
```

执行结果：

```
arg1: 5 
arg2: 二 
arg3: 3 
```

**标准参数与`*args`和`**kwargs`在使用时的顺序**

那么如果你想在函数⾥同时使⽤所有这三种参数， 顺序是这样的： 

```
some_func(fargs, *args, **kwargs)
```

### 调试Debugging

利用好调试，能大提高我们捕捉代码的bug。大部分人忽略了Python debugger（pdb）的重要性。在这里会讲一些重要的命令，其他的可以从官方文档中学习。地址如下：

https://docs.python.org/3/library/pdb.html 

#### 从命令运行

你可以在命令行使用Python debugger运行一个脚本，举个例子：

```
python -m pdb my_script.py
```

这会触发debugger在脚本第一行指令处停止执行。这个对比较短的脚本很有帮助。

#### 从脚本内部运行

可以在脚本内设置数点，这样就可以在某些特定点查看变量信息和各种执行时信息了。使用`pdb.set_trace()`方法来实现。举例说明：

```
import pdb 
def make_bread(): 
    pdb.set_trace() 
    return "I don't have time" 

print(make_bread())
```

运行上面的脚本，会立刻进入debugger模式。其操作命令如下：

- c：继续执行

- w：显示当前正在执行的代码行的上下文信息

- a：打印当前函数的参数列表

- s：执行当前代码行，并停在第一个能停的地方（相当于单步进入）

- n：继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）
  
  单步路过和单步进入的区别在于，单步进入会进入当前行调用的函数内部停在里面，而单步跳过会全速执行完成当前调用的函数，并停在当前函数的下一行。

### 生成器Generators

讲解生成器之前，我们先说一下迭代器。迭代器是一个让程序可以遍历一个容器（特别是列表）的对象。然而，一个迭代器在遍历并读取一个容器的数据元素时，并不会执行一个迭代。它有三个部分：

- 可迭代对象（Iterable）
- 迭代器（Iterator）
- 迭代（Iteration）

上面这些部分互相联系。我们先来讨论他们，然后再讨论生成器（generators）。

#### 可迭代对象（Iterable）

Python中任意的对象，只要它定义了可以返回一个迭代器`__iter__`方法，或者定义了可以支持下标索引的`__getitem__`方法，那么安就是一个可迭代器。简单说，可迭代对象就是能提供迭代器的任意对象。

#### 迭代器（Iterator）

任意对象，只要定义了`__next__`方法，它就是一个迭代器。

#### 迭代（Iteration）

迭代就是从某个地方（比如一个列表）取出一个元素的过程。当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代。

#### 生成器（Generators）

生成器也是一种迭代器，但是你只能对其迭代一次。这是因为他们并没有把所有的值存在内存中，而是在运行时生成值。你通过遍历来用不用它们，要么用一个”for“循环，要么将它们传递给任意可以进行迭代的函数和结构。大多数时个生成器是以函数来实现的。然而，他们并不返回一个值，而是yield一个值。如下：

```
def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)
```

执行结果：

```
0
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

这个例子并不是非常实用。生成器最佳应用场景是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。这样做会消耗大量的资源。

下面是一个计算斐波那契数列的生成器：

```
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibon(1000000):
    print(x)
```

用这种方式，我们可以不用担心它会使用大量资源。然而，之前如果我们这样实现的话：

```
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
```

这个会在计算很大的输入参数时，占用大量的资源。我们现在来测试一下生成器使用一次迭代，我们使用python的内置函数：`next()`，它可以获取一个序列的下一个元素。如下：

```
def generator_function():
    for i in range(3):
        yield i

gen = generator_function()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
```

执行结果:

```
0
1
2
Traceback (most recent call last):
  File "E:\公司文档\分享内容\markdown\python进阶\8.py", line 12, in <module>
    print(next(gen))
StopIteration
```

从结果中可以看出，在yield掉所有值后，next()触发了一个StopIteration的异常。这个说明所有的值都已经yield完了。for循环会自动捕捉这个异常并停止调用next()，所以for循环没有这个异常。

Python中有些内置数据也支持迭代，如下：

```
my_string = "tester" 
my_iter = iter(my_string) 
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
```

执行结果：

```
t
e
s
t
```

### Map，Filter和Reduce

#### Map

Map会将一个函数映射到一个输入列表的所有元素上。如下：

```
map(function_to_apply, list_of_inputs)
```

一般而言，要把列表中所有元素一个个地传递给一个函数，并收集输出。应做如下操作：

```
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
```

Map可以用一种简单得多的方式来实现。如下：

```
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x:x**2, items))
```

大多数时候，我们使用匿名函数（lambda）来配合map。其不仅可用于列表的输入，甚至可以用于列表的函数。如下：

```
def multiply(x):
    return (x*x)

def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x:x(i), funcs))
    print(value)
```

执行结果：

```
[0, 0]
[1, 2]
[4, 4]
[9, 6]
[16, 8]
```

#### Filter

filter过滤列表中的元素，并返回一个由所有符合要求的元素所构成的列表。如下:

```
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x:x<0, number_list))
print(less_than_zero)
```

执行结果：

```
[-5, -4, -3, -2, -1]
```

filter类似for循环，但它是一个内置函数，并且更快。

#### Reduce

当需要对一个列表进行一些计算并返回结果时，Reduce是个非常有用的函数。如下：

```
from functools import reduce
product = reduce((lambda x, y:x *y), [1, 2, 3, 4])
```

执行结果：

```
24
```

### set（集合）数据结构

#### set

set（集合）是一个非常有用的数据结构。它与列表（list）的行为类似，区别在于set不能包含重复的值。这在去重和检查列表中是否包含重复元素很有用。如下：

```
some_list = ['a','b','c','b','d','m','n','n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])

print(duplicates)
```

执行结果：

```
{'n', 'b'}
```

#### 交集

对比两个集合的交集，如下：

```
valid = set(['yellow','red','blue','green','black'])
input_set = set(['red','brown'])
print(input_set.intersection(valid))
```

执行结果:

```
{'red'}
```

注：intersection() 方法用于返回两个或更多集合中都包含的元素，即交集。

#### 差集

用差集找出无效的数据，如下：

```
valid = set(['yellow','red','blue','green','black'])
input_set = set(['red','brown'])
print(input_set.difference(valid))
```

执行结果:

```
{'brown'}
```

注：difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。

### 三元运算符

三元运算符通常被称为条件表达式，这些表达式基于真(true)/假(not)的条件判断。如下：

```
condition_is_true if condiiton else condition_is_false
```

举个例子：

```
is_fat = True
state = "fat" if is_fat else "not fat"
```

它还有一种不常用的用法，使用了元组，如下：

```
(if_test_if_false, if_test_is_true)[test]
```

举个例子：

```
fat = True
fitness = ("skinny", "fat")[fat]
print("All is", fitness)
```

执行结果：

```
All is fat
```

一般不建议使用元组条件表达式的缘故是在元组中会把两个条件都执行，而if else的条件表达式不会。例如：

```
condition = True
print(2 if condition else 1/0)
```

执行如果：

```
2
```

```
condition = True
print((2, 1/0)[condition])
```

执行结果：

```
ZeroDivisionError: division by zero
```

### 装饰器

装饰器是修改其他函数的功能的函数。

#### 第一个装饰器

如下：

```
def a_new_decorator(a_func):

    def wrapTheFunction():
        print("在执行a_func函数之前我正在干一些无趣的事情")
        a_func()
        print("在执行a_func函数之后我正在干一些无趣的事情")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("我需要一些装饰来掩饰我的伤口")
```

执行1及结果：

```
a_function_requiring_decoration()
# 执行结果：
我需要一些装饰来掩饰我的伤口
```

执行2及结果：

```
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

a_function_requiring_decoration()
# 执行结果：
在执行a_func函数之前我正在干一些无趣的事情
我需要一些装饰来掩饰我的伤口
在执行a_func函数之后我正在干一些无趣的事情
```

以上就是python中装饰器的作用。它封装一个函数，并且用一些方式来修改它的行为。下面我们使用@来运行之前的代码：

```
def a_new_decorator(a_func):

    def wrapTheFunction():
        print("在执行a_func函数之前我正在干一些无趣的事情")
        a_func()
        print("在执行a_func函数之后我正在干一些无趣的事情")

    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    # 装饰
    print("我需要一些装饰来掩饰我的伤口")

a_function_requiring_decoration()
```

执行结果：

```
在执行a_func函数之前我正在干一些无趣的事情
我需要一些装饰来掩饰我的伤口
在执行a_func函数之后我正在干一些无趣的事情
```

附：`@a_new_decorator`是`a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)`的缩略方式

现在我们对装饰器有了一个基本的了解。如果我们运行下面的代码会有一个问题：

```
print(a_function_requiring_decoration.__name__)
```

执行结果：

```
wrapTheFunction
```

这个并不是我们想要的，Python提供了一个函数来解决这个问题，那就是functools.wraps。如下：

```
from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("在执行a_func函数之前我正在干一些无趣的事情")
        a_func()
        print("在执行a_func函数之后我正在干一些无趣的事情")

    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    # 装饰
    print("我需要一些装饰来掩饰我的伤口")

print(a_function_requiring_decoration.__name__)
```

执行结果：

```
a_function_requiring_decoration
```

**装饰器规范**

```
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated
@decorator_name
def func():
    return("Function is running")
```

执行1及结果：

```
can_run = True
print(func())
# 执行结果
Function is running
```

执行2及结果：

```
can_run = False
print(func())
# 执行结果
Function is not running
```

注：@wraps接受一个函数来进行装饰，并加入复制函数名称、注释文档、参数列表等功能。

#### 使用场景

**授权(Authorization)**

装饰器有助于检查是否被授权去使用一个web应用的端点。它被大量用于Flask和Django框架中。如下：

```
from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated
```

**日志(Logging)**

日志是装饰器运用的另一个亮点。如下：

```
from functools import wraps
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + "被调用")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
    return x + x

result = addition_func(4)
```

执行结果：

```
addition_func被调用
```

#### 带参数的装饰器

**在函数中嵌入装饰器**

在刚才的日志铺子中创建一个包裹函数，可以用来指定一个用于输出的日志文件。如下：

```
from functools import wraps

def logit(logfile="out.log"):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            lgo_string = func.__name__ + "被调用"
            print(lgo_string)
            with open(logfile, 'a') as opened_file:
                opened_file.write(lgo_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator
```

执行1及结果：

```
@logit()
def myfunc1():
    pass

myfunc1()
# 执行结果
myfunc1被调用
#当前目录下会生成文件out.log,而且“myfunc1被调用”被写入。
```

执行2及结果：

```
@logit(logfile="func2.log")
def myfunc2():
    pass

myfunc2()
# 执行结果
myfunc2被调用
#当前目录下会生成文件func2.log,而且“myfunc2被调用”被写入。
```

**装饰器类**

类也可以用来构建装饰器。如下：

```
from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + "被调用"
            print(log_string)
            with open(self.logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        # 只用于日志
        pass
```

执行及结果：

```
@logit()
def myfunc1():
    pass

myfunc1()
# 执行结果
myfunc1被调用
#当前目录下会生成文件out.log,而且“myfunc1被调用”被写入。
```

为了保存日志的同时，给相关人员发送邮件，可以给logit创建一个子类，来添加邮件功能。如下：

```
class email_logit(logit):
    def __init__(self, email="test@test.cn", *args, **kwargs):
        self.email = email
        super(logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 邮件功能实现略
        pass
```

现在`@email_logit`在打日志的基础上，还有发邮件的功能。

### Global和Return

return和global的作用，如下：

```
def add(value1, value2):
    return value1 +  value2

result = add(3, 5)
print(result)
```

执行结果：

```
8
```

return<函数把值赋给了调用它的变量。

```
def add(value1,value2):
    global result
    result = value1 + value2

add(3,5)
print(result)
```

执行结果：

```
8
```

global的作用是在函数以外的区域都能访问这个变量。举个例子：

```
def add(value1, value2):
    result = value1 + value2

add(2, 4)
print(result)
```

执行结果：

```
Traceback (most recent call last):
  File "E:\公司文档\分享内容\markdown\python进阶\29.py", line 7, in <module>
    print(result)
NameError: name 'result' is not defined
```

函数内的result只是局部变量，不要被用于函数外部。申明global后可正常执行，但应尽量避免使用global，它会引入多余的变量到全局作用域。

#### 多个return值

返回多个值，不建议使用global关键字，使用元组(tuple)，列表(list)，字典(dict)是可行的，但并不是最好的，按照惯例如下：

```
def profile():
    name = "Tester"
    age = 30
    return name, age

print("name:",profile()[0])
print("age:",profile()[1])
```

执行结果：

```
name: Tester
age: 30
```

### 对象变动（Mutation)

Python中有可变与不可变的数据类型。可变意味着“可以被改动”，而不变的意思就是“常量”。举例如下：

```
poo = ['hi']
print(poo)

bar = poo
bar += ['bye']
print(poo)
```

执行结果：

```
['hi']
['hi', 'bye']
```

这不是一个问题。这个是对象可变性。每当你将一个变量赋值为另一个可变类型的变量时，对这个数据的任意改动会同时反映到这两个变量上去。新变量不过是老变量的一个别名。

```
def add_to(num, target=[]):
    target.append(num)
    return target

print(add_to(1))
print(add_to(2))
print(add_to(3))
```

执行结果：

```
[1]
[1, 2]
[1, 2, 3]
```

在Python中当函数被定义时，默认参数只运算一次，而不是每次用时都会重新运算。所以不要定义可变类型的默认参数，除非这个默认参数是你真的需要的。为了达到效果，你可以这样做：

```
def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

print(add_to(1))
print(add_to(2))
print(add_to(3))
```

执行结果：

```
[1]
[2]
[3]
```

### `__slots__`魔法

在Python中，每个类都有实例属性。默认情况下Python用一个字典来保存一个对象的实例属性。不过，这个字典浪费了很多内存。Python不能在对象创建时直接分配一个固定量的来保存所有属性。因此创建许多象，会消耗很多内存。不过可以用`__slots__`来告诉Python不要使用字典，而且只给一个固定集合的属性分配空间。举个列子：

- 不使用`__slots__`

```
class MyClass(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.set_up()
    # ...
```

- 使用`__slots__`

```
class MyClass(object):
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.set_up()
    # ...
```

第二段代码会减少40~50%的内存占用，可以通过[ipython_memory_usage](https://github.com/ianozsvald/ipython_memory_usage)来查看效果，这里安装失败了，暂不对比。

### 虚拟环境

#### virtualenv

virtualenv是一个可以创建独立（隔离）的Python环境的工具。它可以为每一个程序创建一个独立的环境，只为自己安装依赖的模块，而不用全局安装所有依赖的模块。

安装virtualenv

```
pip install virtualenv
```

常用的命令：

```
# 在myproject文件夹下创建一个隔离的virtualenv环境
virtualenv myproject
# 激活这个隔离的环境
source bin/activate
# 退出当前virtualenv
deactivate  # 恢复使用系统全局Python模块
```

如果你想让你的virtualenv使用全局模块，可以用`--system-site-packages`参数创建virtualenv，如下：

```
virtualenv --system-site-packages myproject
```

### 容器Collections

Python附带一个模块collections，它包含许多容器数据类型，如`defaultdict`，`counter`,`deque`,`namedtuple`,`enum.Enum`。

#### defaultdict

defaultdict，与dict类型不同，不需要检查key是否存在，举例如下：

```
from collections import defaultdict

colours = (
    ('张三', '黄色'),
    ('李四', '蓝色'),
    ('王五', '绿色'),
    ('李四', '黑色'),
    ('张三', '红色'),
    ('赵六', '紫色'),
    )

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)
```

执行结果：

```
defaultdict(<class 'list'>, {'张三': ['黄色', '红色'], '李四': ['蓝色', '黑色'], '王五': ['绿色'], '赵六': ['紫色']})
```

当在一个字典中对一个键进行嵌套赋值时，如果这个键不存在，会触发keyError异常。defaultdict允许绕过这个问题。举例如下：

```
some_dict = {}
some_dict['colours']['favourite'] = "yellow"
```

执行结果：

```
Traceback (most recent call last):
  File "E:\公司文档\分享内容\markdown\python进阶\35.py", line 2, in <module>
    some_dict['colours']['favourite'] = "yellow"
KeyError: 'colours'
```

解决方案：

```
import collections
import json

tree = lambda:collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"

print(json.dumps(some_dict))
```

执行结果：

```
{"colours": {"favourite": "yellow"}}
```

#### Counter

Counter是一个计数器，它可以帮助我们针对某项数据进行计数。如下：

```
from collections import Counter

colours = (
    ('张三', '黄色'),
    ('李四', '蓝色'),
    ('王五', '绿色'),
    ('李四', '黑色'),
    ('张三', '红色'),
    ('赵六', '紫色'),
    )

favs = Counter(name for name, colour in colours)
print(favs)
```

执行结果：

```
Counter({'张三': 2, '李四': 2, '王五': 1, '赵六': 1})
```

#### deque

deque提供了一个双端队列，你可以从头/尾两端添加或删除元素。如下：

```
from collections import deque

d = deque()
# 用法和list差不多
d.append('1')
d.append('2')
d.append('3')

print(len(d))
print(d[0])
print(d[-1])
```

执行结果：

```
3
1
3
```

从两端删除数据：

```
from collections import deque

d = deque(range(5))
print(len(d))
print(d.popleft())
print(d.pop())
print(d)
```

执行结果：

```
5
0
4
deque([1, 2, 3])
```

可以限制deque的大小，当超过这个限制时，会把左边的数据挤出去。如下：

```
from collections import deque

d = deque(maxlen=2)

d.append('1')
d.append('2')
d.append('3')

print(d)
```

执行结果：

```
deque(['2', '3'], maxlen=2)
```

从两端扩展数据：

```
from collections import deque

d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)
```

执行结果：

```
deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
```

#### namedtuple

namedtuple把元组变成一个简单任务的容器，不用像元组那样使用整数索引来访问一个namedtuple数据，而是像字典一样访问namedtuple，namedtuple也是不可娈的。如下：

```
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)
print(perry.name)
```

执行结果：

```
Animal(name='perry', age=31, type='cat')
perry
```

命名元组是不可娈的。如下：

```
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
perry.age = 42
```

执行结果：

```
Traceback (most recent call last):
  File "E:\公司文档\分享内容\markdown\python进阶\44.py", line 7, in <module>
    perry.age = 42
AttributeError: can't set attribute
```

命名元组可以兼容普通元组，就是说你也可以用整数索引来访问namedtuple。如下：

```
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry[0])
```

执行结果：

```
perry
```

命名元组可以转换为字典。如下：

```
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry._asdict())
```

执行结果：

```
{'name': 'perry', 'age': 31, 'type': 'cat'}
```

#### enum.Enum

让我们回顾⼀下上⼀个'Animal'命名元组的例⼦。它有⼀个type字段，问题是，type是⼀个字符串。那么问题来了，万⼀程序员输⼊了Cat，因为他按到了Shift键，或者输⼊了'CAT'，甚⾄'kitten'？枚举可以帮助我们避免这个问题，通过不使⽤字符串。如下：

```
from collections import namedtuple
from enum import Enum

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # ……

    kitten = 1
    puppy = 2

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)

print(charlie.type == tom.type)
print(charlie.type)
```

执行结果：

```
True
Species.cat
```

这样就没有那么容易错误了，但应该只使用定义了的枚举类型。有三种方法访问枚举类型，如以下方法都可以获取`cat`的值：

```
Species(1)
Species['cat']
Species.cat
```

### 枚举Enumerate

枚举是python的内置函数。它的作用举例来说明，如下：

**枚举允许遍历数据并自动计数。**

```
some_list = ['苹果', '香蕉', '葡萄', '梨子']
for counter, value in enumerate(some_list):
    print(counter, value)
```

执行结果：

```
0 苹果
1 香蕉
2 葡萄
3 梨子
```

**枚举还可以接受一些可选参数。**

```
some_list = ['苹果', '香蕉', '葡萄', '梨子']
for counter, value in enumerate(some_list,2):   # 计数从2开始
    print(counter, value)
```

执行结果：

```
2 苹果
3 香蕉
4 葡萄
5 梨子
```

**枚举可以用来创建包含索引的元组列表。**

```
some_list = ['苹果', '香蕉', '葡萄', '梨子']
counter_list = list(enumerate(some_list))
print(counter_list)
```

执行结果：

```
[(0, '苹果'), (1, '香蕉'), (2, '葡萄'), (3, '梨子')]
```

### 对象自省

自省，上指在运行时来判断一个对象的类型的能力。

#### dir

dir是用于自省的最重要的函数之一。它返回一个列表，列出一个对象所拥有的属性和方法。如下：

```
my_list = [1, 2, 3]
print(dir(my_list))
```

执行结果：

```
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

上面的自省给了这个列表对象所有的方法的名字，如果你不清楚其所具有的方法，可以使用dir()来查询。

#### type和id

**type函数返回一个对象的类型。如下：**

```
print(type(''))
print(type([]))
print(type({}))
print(type(dict))
print(type(3))
```

执行结果：

```
<class 'str'>
<class 'list'>
<class 'dict'>
<class 'type'>
<class 'int'>
```

**id()函数返回任意不同各类对象的唯一id。如下：**

```
name = "tester"
print(id(name))
```

执行结果：

```
1546700355120
```

#### inspect模块

inspect模块也提供了许多有用的函数，来获取活跃对象的信息。比如，你可以查看一个对象的成员，只需运行：

```
import inspect
print(inspect.getmembers(str))
```

执行结果：

```
[('__add__', <slot wrapper '__add__' of 'str' objects>), ('__class__', <class 'type'>), ('__contains__', <slot wrapper '__contains__' of 'str' objects>), ('__delattr__', <slot wrapper '__delattr__' of 'object' objects>), ('__dir__', <method '__dir__' of 'object' objects>), ('__doc__', "str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'."), ('__eq__', <slot wrapper '__eq__' of 'str' objects>), ('__format__', <method '__format__' of 'str' objects>), ('__ge__', <slot wrapper '__ge__' of 'str' objects>), ('__getattribute__', <slot wrapper '__getattribute__' of 'str' objects>), ('__getitem__', <slot wrapper '__getitem__' of 'str' objects>), ('__getnewargs__', <method '__getnewargs__' of 'str' objects>), ('__gt__', <slot wrapper '__gt__' of 'str' objects>), ('__hash__', <slot wrapper '__hash__' of 'str' objects>), ('__init__', <slot wrapper '__init__' of 'object' objects>), ('__init_subclass__', <built-in method __init_subclass__ of type object at 0x00007FF9D967AC60>), ('__iter__', <slot wrapper '__iter__' of 'str' objects>), ('__le__', <slot wrapper '__le__' of 'str' objects>), ('__len__', <slot wrapper '__len__' of 'str' objects>), ('__lt__', <slot wrapper '__lt__' of 'str' objects>), ('__mod__', <slot wrapper '__mod__' of 'str' objects>), ('__mul__', <slot wrapper '__mul__' of 'str' objects>), ('__ne__', <slot wrapper '__ne__' of 'str' objects>), ('__new__', <built-in method __new__ of type object at 0x00007FF9D967AC60>), ('__reduce__', <method '__reduce__' of 'object' objects>), ('__reduce_ex__', <method '__reduce_ex__' of 'object' objects>), ('__repr__', <slot wrapper '__repr__' of 'str' objects>), ('__rmod__', <slot wrapper '__rmod__' of 'str' objects>), ('__rmul__', <slot wrapper '__rmul__' of 'str' objects>), ('__setattr__', <slot wrapper '__setattr__' of 'object' objects>), ('__sizeof__', <method '__sizeof__' of 'str' objects>), ('__str__', <slot wrapper '__str__' of 'str' objects>), ('__subclasshook__', <built-in method __subclasshook__ of type object at 0x00007FF9D967AC60>), ('capitalize', <method 'capitalize' of 'str' objects>), ('casefold', <method 'casefold' of 'str' objects>), ('center', <method 'center' of 'str' objects>), ('count', <method 'count' of 'str' objects>), ('encode', <method 'encode' of 'str' objects>), ('endswith', <method 'endswith' of 'str' objects>), ('expandtabs', <method 'expandtabs' of 'str' objects>), ('find', <method 'find' of 'str' objects>), ('format', <method 'format' of 'str' objects>), ('format_map', <method 'format_map' of 'str' objects>), ('index', <method 'index' of 'str' objects>), ('isalnum', <method 'isalnum' of 'str' objects>), ('isalpha', <method 'isalpha' of 'str' objects>), ('isascii', <method 'isascii' of 'str' objects>), ('isdecimal', <method 'isdecimal' of 'str' objects>), ('isdigit', <method 'isdigit' of 'str' objects>), ('isidentifier', <method 'isidentifier' of 'str' objects>), ('islower', <method 'islower' of 'str' objects>), ('isnumeric', <method 'isnumeric' of 'str' objects>), ('isprintable', <method 'isprintable' of 'str' objects>), ('isspace', <method 'isspace' of 'str' objects>), ('istitle', <method 'istitle' of 'str' objects>), ('isupper', <method 'isupper' of 'str' objects>), ('join', <method 'join' of 'str' objects>), ('ljust', <method 'ljust' of 'str' objects>), ('lower', <method 'lower' of 'str' objects>), ('lstrip', <method 'lstrip' of 'str' objects>), ('maketrans', <built-in method maketrans of type object at 0x00007FF9D967AC60>), ('partition', <method 'partition' of 'str' objects>), ('removeprefix', <method 'removeprefix' of 'str' objects>), ('removesuffix', <method 'removesuffix' of 'str' objects>), ('replace', <method 'replace' of 'str' objects>), ('rfind', <method 'rfind' of 'str' objects>), ('rindex', <method 'rindex' of 'str' objects>), ('rjust', <method 'rjust' of 'str' objects>), ('rpartition', <method 'rpartition' of 'str' objects>), ('rsplit', <method 'rsplit' of 'str' objects>), ('rstrip', <method 'rstrip' of 'str' objects>), ('split', <method 'split' of 'str' objects>), ('splitlines', <method 'splitlines' of 'str' objects>), ('startswith', <method 'startswith' of 'str' objects>), ('strip', <method 'strip' of 'str' objects>), ('swapcase', <method 'swapcase' of 'str' objects>), ('title', <method 'title' of 'str' objects>), ('translate', <method 'translate' of 'str' objects>), ('upper', <method 'upper' of 'str' objects>), ('zfill', <method 'zfill' of 'str' objects>)]
```

### 推导式Comprehension

推导式是可以从一个数据序列构建另一个新的数据序列的结构体。共有三种推导：

- 列表（list）推导式
- 字典（dict）推导式
- 集合（set）推导式

#### 列表推导式

列表推导式是在一个中括号里包含一个表达式，然后是一个for语句，然后是0个或多个for或者if语句。

**规范**

```
variable = [out_exp for out_exp in input_list if out_exp == 2]
```

举例如下：

```
multiples = [i for i in range(30) if i%3 == 0]
print(multiples)
```

执行结果：

```
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
```

这个对快速生成列表很有用。列表推导式在使用for循环生成一个新列表时，非常好用，如下：

```
squared = []
for x in range(10):
    squared.append(x**2)
```

这个用推导式就可以简化为：

```
squared = [x**2 for x in range(10)]
```

执行结果：

```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#### 字典推导式

字典推导式和列表推导式用法是类似的。如下：

将字典中一个字母但不同大小写的值合并起来：

```
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mcase_frequency = {
    k.lower():mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

print(mcase_frequency)
```

执行结果：

```
{'a': 17, 'b': 34, 'z': 3}
```

#### 集合推导式

它和列表推导式也是类似的。唯一区别在于它作用大括号{}。举个例子：

```
squared = {x**2 for x in [1, 1, 2]}
```

执行结果：

```
{1, 4}
```

### 异常

最基本的就是`try/except`从句。可能触发异常的代码会放到try语句块里，而处理异常的代码会在except语句块中。举个例子：

```
try:
    file = open('test.txe', 'rb')
except IOError as e:
    print("一个读写错误发生:{}".format(e.args[-1]))
```

执行结果：

```
一个读写错误发生:No such file or directory
```

#### 处理多个异常

有三种方法可以用来处理多个异常。

1. 需要把所有可能发生的异常放到一个元组里面。如下：
   
   ```
   try:
       file = open('test.txe', 'rb')
   except (IOError, EOFError) as e:
       print("一个读写错误发生:{}".format(e.args[-1]))
   ```

2. 对每个单独的异常在单独的except语句块中处理。如下：
   
   ```
   try:
       file = open('test.txe', 'rb')
   except EOFError as e:
       print("一个EOF错误发生。")
       raise e
   except IOError as e:
       print("一个读写错误发生。")
       raise e
   ```

3. 直接捕获所有异常
   
   ```
   try:
       file = open('test.txe', 'rb')
   except Exception:
       # 打印一些想要的异常日志
       raise
   ```
   
   当你不知道程序会抛什么异常的时候，第三种方法比较好用。

#### finally从句

除了try和eccept从句，还有第三个从句，就是finally从句。finally从句中的代码不管异常是否触发都会执行。如下：

```
try:
    file = open('test.txe', 'rb')
except (IOError, EOFError) as e:
    print("一个读写错误发生:{}".format(e.args[-1]))
finally:
    print("不管是否触发异常都会执行。")
```

执行结果：

```
一个读写错误发生:No such file or directory
不管是否触发异常都会执行。
```

#### try/else从句

如果想在没有触发异常的时候执行一些代码，可以用else从句来达到目的。如下：

```
try:
    print("我确信没有异常发生。")
except Exception:
    print("exception.")
else:
    # 这里的代码只会在try语句没有触发异常时运行
    # 但这里的异常将不会被捕获
    print("这里的代码只会在try语句没有触发异常时运行,异常将不会被捕获。")
finally:
    print("这里将一直被执行。")
```

执行结果：

```
我确信没有异常发生。
这里的代码只会在try语句没有触发异常时运行,异常将不会被捕获。
这里将一直被执行。
```

else从句只会在没有异常的情况下执行，而且它会在finally语句之前执行。

### lambda表达式

lambada表达式是一行函数，也被称为匿名表达式。

**原型**

```
lambda 参数:操作(参数)
```

如下：

```
add = lambda x, y:x + y
print(add(3, 5))
```

执行结果：

```
8
```

lambda表达式，可以在一些特殊的情况下使用：

- 列表排序
  
  ```
  a = [(1, 2), (4, 1), (9, 10), (13, -3)]
  a.sort(key=lambda x:x[1])
  ```
  
  执行结果：
  
  ```
  [(13, -3), (4, 1), (1, 2), (9, 10)]
  ```

- 列表并行排序
  
  ```
  list1 = [1,2,3]
  list2 = [4,5,6]
  data = list(zip(list1, list2))
  data.sort()
  list1, list2 = map(lambda t:list(t), zip(*data))
  
  print(list1)
  print(list2)
  ```
  
  执行结果：
  
  ```
  [1, 2, 3]
  [4, 5, 6]
  ```
