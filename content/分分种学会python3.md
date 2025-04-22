title:分分种学会python3
date:2020-05-14
category: 技术
tag:python

[TOC]

### python3.x

```
# 单行注释由一个井号开头。
""" 
   三个双引号（或单引号）之间可以写多行字符串，
   通常用来写注释。
"""
```

### 基本数据类型和操作符

```
# 数字就是数字
3 #=> 3
```

```
# 四则运算也是你所期望的那样
1 + 1 #=> 2
8 - 1 #=> 7
10 * 2 #=> 20
35 / 5 #=> 7.0
```

```
# 为了修正除法的问题，我们需要先学习浮点数。
2.0     # This is a float
2.0     # 这是一个浮点数
11.0 / 4.0 #=> 2.75 ahhh...much better
11.0 / 4.0 #=> 2.75 啊……这样就好多了
```

```
# 使用小括号来强制计算的优先顺序
(1 + 3) * 2 #=> 8
```

```
# 布尔值也是基本数据类型
True
False
```

```
# 使用 not 来取反
not True #=> False
not False #=> True
```

```
# 等式判断用 ==
1 == 1 #=> True
2 == 1 #=> False
```

```
# 不等式判断是用 !=
1 != 1 #=> False
2 != 1 #=> True
```

```
# 还有更多的比较运算
1 < 10 #=> True
1 > 10 #=> False
2 <= 2 #=> True
2 >= 2 #=> True
```

```
# 居然可以把比较运算串连起来！
1 < 2 < 3 #=> True
2 < 3 < 2 #=> False
```

```
# 使用 " 或 ' 来创建字符串
"This is a string."
'This is also a string.'
```

```
# 字符串也可以相加！
"Hello " + "world!" #=> "Hello world!"
```

```
# 一个字符串可以视为一个字符的列表
"This is a string"[0] #=> 'T'
```

```
# % 可以用来格式化字符串，就像这样：
"%s can be %s" % ("strings", "interpolated")
```

```
# 格式化字符串的新方法：format 方法。
"{0} can be {1}".format("strings", "formatted")
```

```
# 如果你不喜欢数数的话，可以使用关键字（变量）。
"{name} wants to eat {food}".format(name="Bob", food="lasagna")
```

```
# None 是一个对象
None #=> None
```

```
# 不要使用相等符号 `==` 来把对象和 None 进行比较，
# 而要用 `is`。
"etc" is None #=> False
None is None  #=> True

# 这个 `is` 操作符用于比较两个对象的标识。
# （译注：对象一旦建立，其标识就不会改变，可以认为它就是对象的内存地址。）
# 在处理基本数据类型时基本用不上，
# 但它在处理对象时很有用。
```

```
# None、0 以及空字符串和空列表都等于 False，
# 除此以外的所有值都等于 True。
0 == False  #=> True
"" == False #=> True
```

### 变量和集合

```
# 打印输出很简单
print("I'm Python. Nice to meet you!")
```

```
# 在赋值给变量之前不需要声明
some_var = 5   # 变量名的约定是使用下划线分隔的小写单词
some_var #=> 5
```

```
# 访问一个未赋值的变量会产生一个异常。
some_other_var  # 会抛出一个名称错误 NameError: name 'some_other_var' is not defined
```

```
# if 可以作为表达式来使用
"yahoo!" if 3 > 2 else 2 #=> "yahoo!"
```

```
# 列表用于存储序列
li = []
# 我们先尝试一个预先填充好的列表
other_li = [4, 5, 6]

# 使用 append 方法把元素添加到列表的尾部
li.append(1)   #li 现在是 [1]
li.append(2)   #li 现在是 [1, 2]
li.append(4)   #li 现在是 [1, 2, 4]
li.append(3)   #li 现在是 [1, 2, 4, 3]

# 使用 pop 来移除最后一个元素
li.pop()       #=> 3，然后 li 现在是 [1, 2, 4]
# 我们再把它放回去
li.append(3)   # li 现在又是 [1, 2, 4, 3] 了

# 像访问其它语言的数组那样访问列表
li[0] #=> 1
# 查询最后一个元素
li[-1] #=> 3

# 越界查询会产生一个索引错误
li[4] # 抛出一个索引错误 IndexError: list index out of range

# 你可以使用切片语法来查询列表的一个范围。
# （这个范围相当于数学中的左闭右开区间。）
li[1:3] #=> [2, 4]
# 省略开头
li[2:] #=> [4, 3]
# 省略结尾
li[:3] #=> [1, 2, 4]

# 使用 del 来删除列表中的任意元素
del li[2] # li 现在是 [1, 2, 3]

# 可以把列表相加
other_li = [4, 5, 6]
li + other_li #=> [1, 2, 3, 4, 5, 6] - 请留意 li 和 other_li 并不会被修改

# 使用 extend 来合并列表
li.extend(other_li) # 现在 li 是 [1, 2, 3, 4, 5, 6]

# 用 in 来检查是否存在于某个列表中
1 in li #=> True

# 用 len 来检测列表的长度
len(li) #=> 6
```

```
# 元组很像列表，但它是“不可变”的。
tup = (1, 2, 3)
tup[0] #=> 1
tup[0] = 3  # 抛出一个类型错误 SyntaxError: can't assign to function call

# 操作列表的方式通常也能用在元组身上
len(tup) #=> 3
tup + (4, 5, 6) #=> (1, 2, 3, 4, 5, 6)
tup[:2] #=> (1, 2)
2 in tup #=> True

# 你可以把元组（或列表）中的元素解包赋值给多个变量
a, b, c = (1, 2, 3)    # 现在 a 是 1，b 是 2，c 是 3
# 如果你省去了小括号，那么元组会被自动创建
d, e, f = 4, 5, 6
# 再来看看交换两个值是多么简单。
e, d = d, e    # 现在 d 是 5 而 e 是 4
```

```
# 字典用于存储映射关系
empty_dict = {}
# 这是一个预先填充的字典
filled_dict = {"one": 1, "two": 2, "three": 3}

# 使用 [] 来查询键值
filled_dict["one"] #=> 1

# 将字典的所有键名获取为一个列表
filled_dict.keys() #=> ["three", "two", "one"]
# 请注意：无法保证字典键名的顺序如何排列。
# 你得到的结果可能跟上面的示例不一致。

# 将字典的所有键值获取为一个列表
filled_dict.values() #=> [3, 2, 1]
# 请注意：顺序的问题和上面一样。

# 使用 in 来检查一个字典是否包含某个键名
"one" in filled_dict #=> True
1 in filled_dict #=> False

# 查询一个不存在的键名会产生一个键名错误
filled_dict["four"] # 键名错误 KeyError: 'four'

# 所以要使用 get 方法来避免键名错误
filled_dict.get("one") #=> 1
filled_dict.get("four") #=> None
# get 方法支持传入一个默认值参数，将在取不到值时返回。
filled_dict.get("one", 4) #=> 1
filled_dict.get("four", 4) #=> 4

# Setdefault 方法可以安全地把新的名值对添加到字典里
filled_dict.setdefault("five", 5) #filled_dict["five"] 被设置为 5
filled_dict.setdefault("five", 6) #filled_dict["five"] 仍然为 5
```

```
# set 用于保存集合
empty_set = set()
# 使用一堆值来初始化一个集合
some_set = set([1,2,2,3,4]) # some_set 现在是 set([1, 2, 3, 4])

# {} 可以用来声明一个集合
filled_set = {1, 2, 2, 3, 4} # => {1, 2, 3, 4}
# 集合是种无序不重复的元素集，因此重复的 2 被滤除了。
# {} 不会创建一个空集合，只会创建一个空字典。

# 把更多的元素添加进一个集合
filled_set.add(5) # filled_set 现在是 {1, 2, 3, 4, 5}

# 使用 & 来获取交集
other_set = {3, 4, 5, 6}
filled_set & other_set #=> {3, 4, 5}

# 使用 | 来获取并集
filled_set | other_set #=> {1, 2, 3, 4, 5, 6}

# 使用 - 来获取补集
{1,2,3,4} - {2,3,5} #=> {1, 4}

# 使用 in 来检查是否存在于某个集合中
2 in filled_set #=> True
10 in filled_set #=> False
```

### 控制流

```
# 我们先创建一个变量
some_var = 5

# 这里有一个条件语句。缩进在 Python 中可是很重要的哦！
# 程序会打印出 "some_var is smaller than 10"
if some_var > 10:
   print("some_var is totally bigger than 10.")
elif some_var < 10:   # 这里的 elif 子句是可选的
   print("some_var is smaller than 10.")
else:          # 这一句也是可选的
   print("some_var is indeed 10.")
```

```
# for 循环可以遍历列表
# 如果要打印出：
dog is a mammal
cat is a mammal
mouse is a mammal

for animal in ["dog", "cat", "mouse"]:
   # 别忘了你可以使用 % 来格式化字符串
   print("%s is a mammal" % animal)
   # （译注：意为“%s 是哺乳动物”。）
```

```
# range(数字) 会返回一个数字列表，这个列表将包含从零到给定的数字。
如果要打印出：
0
1
2
3

for i in range(4):
   print(i)
```

```
while 循环会一直继续，直到条件不再满足。
如果要打印出：
0
1
2
3

x = 0
while x < 4:
   print(x)
   x += 1  # 这是 x = x + 1 的简写方式
```

```
# 使用 try/except 代码块来处理异常

try:
   # 使用 raise 来抛出一个错误
   # 抛出一个索引错误：“这是一个索引错误”。
except IndexError as e:
   pass    # pass 只是一个空操作。通常你应该在这里做一些恢复工作。
```

### 函数

```
# 使用 def 来创建新函数
def add(x, y):
   print("x is %s and y is %s" % (x, y))
   # （译注：意为"x 是 %s 而且 y 是 %s"。）
   return x + y    # 使用 return 语句来返回值

# 调用函数并传入参数
add(5, 6) #=> 意为“x 是 5 而且 y 是 6”，并返回 11

# 调用函数的另一种方式是传入关键字参数
add(y=6, x=5)  # 关键字参数可以以任意顺序传入

# 你可以定义一个函数，并让它接受可变数量的定位参数。
def varargs(*args):
   return args

varargs(1, 2, 3) #=> (1,2,3)

# 你也可以定义一个函数，并让它接受可变数量的关键字参数。
def keyword_args(**kwargs):
   return kwargs

# 我们试着调用它，看看会发生什么：
keyword_args(big="foot", loch="ness") #=> {"big": "foot", "loch": "ness"}

# 你还可以同时使用这两类参数，只要你愿意：
def all_the_args(*args, **kwargs):
   print(args)
   print(kwargs)

all_the_args(1, 2, a=3, b=4) prints:
   (1, 2)
   {"a": 3, "b": 4}

# 在调用函数时，定位参数和关键字参数还可以反过来用。
# 使用 * 来展开元组，使用 ** 来展开关键字参数。
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args) # 相当于 all_the_args(1, 2, 3, 4)
all_the_args(**kwargs) # 相当于 all_the_args(a=3, b=4)
all_the_args(*args, **kwargs) # 相当于 all_the_args(1, 2, 3, 4, a=3, b=4)

# 函数在 Python 中是一等公民
def create_adder(x):
   def adder(y):
       return x + y
   return adder

add_10 = create_adder(10)
add_10(3) #=> 13

# 还有匿名函数
(lambda x: x > 2)(3) #=> True

# 还有一些内建的高阶函数
list(map(add_10, [1,2,3])) #=> [11, 12, 13]l
list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])) #=> [6, 7]

# 我们可以使用列表推导式来模拟 map 和 filter
[add_10(i) for i in [1, 2, 3]]  #=> [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5] #=> [6, 7]
```

### 类

```
# 我们可以从对象中继承，来得到一个类。
class Human(object):

   # 下面是一个类属性。它将被这个类的所有实例共享。
   species = "H. sapiens"

   # 基本的初始化函数（构造函数）
   def __init__(self, name):
       # 把参数赋值为实例的 name 属性
       self.name = name

   # 下面是一个实例方法。所有方法都以 self 作为第一个参数。
   def say(self, msg):
      return "%s: %s" % (self.name, msg)

   # 类方法会被所有实例共享。
   # 类方法在调用时，会将类本身作为第一个函数传入。
   @classmethod
   def get_species(cls):
       return cls.species

   # 静态方法在调用时，不会传入类或实例的引用。
   @staticmethod
   def grunt():
       return "*grunt*"

# 实例化一个类
i = Human(name="Ian")
print（i.say("hi")） # 打印出 "Ian: hi"

j = Human("Joel")
print(j.say("hello"))  # 打印出 "Joel: hello"

# 调用我们的类方法
i.get_species() #=> "H. sapiens"

# 修改共享属性
Human.species = "H. neanderthalensis"
i.get_species() #=> "H. neanderthalensis"
j.get_species() #=> "H. neanderthalensis"

# 调用静态方法
Human.grunt() #=> "*grunt*"
```

### 模块

```
# 你可以导入模块
import math
print(math.sqrt(16)) #=> 4

# 也可以从一个模块中获取指定的函数
from math import ceil, floor
print(ceil(3.7))  #=> 4.0
print(floor(3.7)) #=> 3.0

# 你可以从一个模块中导入所有函数
# 警告：不建议使用这种方式
from math import *

# 你可以缩短模块的名称
import math as m
math.sqrt(16) == m.sqrt(16) #=> True

# Python 模块就是普通的 Python 文件。
# 你可以编写你自己的模块，然后导入它们。
# 模块的名称与文件名相同。

# 你可以查出一个模块里有哪些函数和属性，定义一个模块
import math
dir(math)
```
