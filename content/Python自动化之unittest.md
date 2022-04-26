title: Python自动化之unittest
date: 2021-04-21
category: python
tag: unittest

[TOC]

本次主要给大家介绍关于Python自动化框架unittest。

### 1. unittest 基本用法
unittest 框架是 Python 自带的一个作为单元测试的测试框，相当于 Java中的 JUnit，随着自动化技术的成熟，unittest 成为了测试框架第一选择，可以完整的结合 Selenium、Requests 来实现 Ul 和接口的自动化。
#### 基本应用：
1. 环境搭建，Python 中已经自带了 unittest 框架，无须额外安装
2. 四大组件：
- test fixture：setUp(前置条件）、tearDown（后置条件），用于初始化测试用例及清理和释放资源
- test case：测试用例，通过集成 unttest.TestCase，来实现用例的继承，在 unittest 中，测试用例都是通过test_来识别的，测试用例命名 test_XXX
- test suite：测试套件，也称之为测试用例集
- test runner：运行器，一般通过 runner 来调用 suite 去执行测试
unittest 运行机制：通过在 main 函数中，调用 unittest.main(verbosity=2) 运行所有内容

#### 1.1 unittest 初体验

先通过实例对unittest来个直观了解吧

1.py
```
# coding=utf-8

import unittest

# 通过继承 unittest.TestCase 来实现用例
class forTest(unittest.TestCase):
    # 类的初始化
    @classmethod
    def setUpClass(cls):
        print('class')
    # 类的释放
    @classmethod
    def tearDownClass(cls):
        print('tclass')
        
    # 测试用例初始化
    def setUp(self):
        print("setUp")
    # 测试用例释放
    def tearDown(self):
        print("teadDown")
    
    # 测试用例
    def test_a(self):
        print("a")
    # 测试用例
    def test_b(self):
        print("b")
    
    # 函数
    def add(self, a, b):
        return a + b
    # 测试用例
    def test_c(self):
        c = self.add(1, 3)
        print('c =', c)
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
```

对上面的程序进行讲解：

1. 类的初始化与释放

- `def setUpClass(cls)`表示类的初始化，在执行测试用例之前执行，只执行一次，函数参数为cls 表示这是一个类方法

- `def tearDownClass(cls)`表示类的释放，在执行测试用例之后执行，只执行一次

2. 测试用例的初始化与释放
   
- `def setUp(self)`用于测试用例的初始化，在每个测试用例之前都会执行，有多少个测试用例，就会执行多少次

- `def tearDown(self)`用于测试用例释放，在每个测试用例执行之后执行，有多少个测试用例，就会执行多少次

注意：方法 setUpClass，tearDownClass，setUp，tearDown 的方法名是固定的，不能改动，不然框架无法识别

3. 测试用例的定义

- 测试用例的命名规则为 test_xxx，这样测试用例就会自动执行

- 注意：只有测试用例才会被执行，不以test_xxx 命名的函数是方法，方法是不能被执行的
4. 执行测试用例

- 通过在 main 函数中，调用 unitest.main() 运行所有内容

5. verbosity：表示测试结果的信息复杂度

- verbosity默认为1，可以设置为0和2。

- 0 (静默模式): 只能获得总的测试用例数和总的结果。
  
- 1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个“F”，每个跳过的案例前面有个“S”，每个预期失败真失败的案例前面有个“X”，每个预期失败却成功的案例前面有个“U”

- 2 (详细模式):测试结果会显示每个测试用例的所有相关的信息 并且 你在命令行里加入不同的参数可以起到一样的效果

运行结果分析：

- 类的初始化方法 setUpClass(cls) 在所有的测试用例之前执行，类的释放函数 tearDownClass(cls) 在所有的测试用例之后执行

- 测试用例的初始化在每个测试用例之前都会执行，测试用例的释放在每个测试用例之后都会执行

- test_a(self) 和 test_b(self) 是测试用例，运行时被自动执行，add(self, a, b) 是函数，不会被自动执行，test_c(self) 是测试用例，调用了 add 函数，这样就可以执行 add 函数了。

运行结果如下：
```
class
test_a (__main__.forTest) ... setUp
a
teadDown
ok
test_b (__main__.forTest) ... setUp
b
teadDown
ok
test_c (__main__.forTest) ... setUp
c = 4
teadDown
ok
tclass
----------------------------------------------------------------------
Ran 3 tests in 0.002s
OK
```
相信有了上面的例子，已经对unittest 有了一个初步的印象。

#### 1.2 unittest 自动化实现实战

有了类的初始化与释放，测试用例的初始化与释放，我们可以将多个测试用例中相同的代码提取出来，减少自动化测试冗余，这样便于维护。
下面看这样一个例子，我们打开谷歌浏览器，输入百度网址并进行搜索，搜索后关闭浏览器

2.py
```
#coding=utf-8
import unittest
from selenium import webdriver
import time

class forTest(unittest.TestCase):
    # 测试用例初始化
    # 打开谷歌浏览器，并进入百度
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
    # 测试用例释放
    # 等待 3s，关闭浏览器
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
 
    # 输入'苹果'，并点击搜索
    def test_1(self):
        self.driver.find_element_by_id('kw').send_keys('苹果')
        self.driver.find_element_by_id('su').click()
 
    # 输入'香蕉'，并点击搜索
    def test_2(self):
        self.driver.find_element_by_id('kw').send_keys('香蕉')
        self.driver.find_element_by_id('su').click()
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
```
上面的案例中，我们将打开谷歌浏览器，进入百度，放在 setUp 中，完成每个测试用例之前的初始化，浏览器的关闭放在tearDown 中，完成测试用例的释放

执行结果：
```
test_1 (__main__.forTest) ... 
ok
test_2 (__main__.forTest) ... 
ok
----------------------------------------------------------------------
Ran 2 tests in 38.884s
OK
```

### 2 unittest 结合 DDT(data-driver tests) 自动化

#### 2.1 ddt 中的 data 与 unpack

在实际测试中，单个测试是需要用多种不同的条件（测试数据）对其进行测试的。

需要额外安装ddt库

ddt 中最基本的应用；在 class 前定义 @ddt，用于表示要使用 ddt 了，再基于实际的应用。选择对应的装饰器来使用即可，说白了，就是一个装饰器

- data 用于设定参数
- unpack 用于解析参数

直接看例子比较直观

3.py
```
# coding=utf-8
import unittest
from ddt import ddt
from ddt import data    # 导入data

# 类之前定义装饰器，表示在类中要使用ddt了
@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('\n{:=^20}'.format("测试开始"))
    def tearDown(self):
        print("{:=^20}".format('测试结束'))
    # data用于设定参数
    @data('苹果', '香蕉', '葡萄', '石榴')
    def test_1(self, txt):
        print(txt)
if __name__ == '__main__':
    unittest.main(verbosity=2)
```
运行结果：
```
test_1_1_苹果 (__main__.MyTestCase) ... 
========测试开始========
苹果
========测试结束========
ok
test_1_2_香蕉 (__main__.MyTestCase) ... 
========测试开始========
香蕉
========测试结束========
ok
test_1_3_葡萄 (__main__.MyTestCase) ...
========测试开始========
葡萄
========测试结束========
ok
test_1_4_石榴 (__main__.MyTestCase) ...
========测试开始========
石榴
========测试结束========
ok
----------------------------------------------------------------------
Ran 4 tests in 0.004s
OK
```
可以看到测试用例 def test_1(self, txt) 被执行了四次，data 用于设定参数，将参数依次放入测试用例中进行测试。

我们改变一下设定的参数，将 data 设定的参数改为 (('苹果', '香蕉'), ('葡萄', '石榴'))，再进行测试，如下所示

4.py
```
#coding=utf-8
import unittest
from ddt import ddt
from ddt import data

# 类之前定义装饰器，表示在类中要使用ddt了
@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('\n{:=^20}'.format("测试开始"))
    def tearDown(self):
        print("{:=^20}".format('测试结束'))
 
    # data 用于设定参数，将包 ('苹果', '香蕉') 作为一个整体赋值给 txt
    @data(('苹果', '香蕉'), ('葡萄', '石榴'))
    def test_1(self, txt):
        print(txt)
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
```
运行结果如下：
```
test_1_1___苹果____香蕉__ (__main__.MyTestCase) ... 
========测试开始========
('苹果', '香蕉')
========测试结束========
ok
test_1_2___葡萄____石榴__ (__main__.MyTestCase) ... 
========测试开始========
('葡萄', '石榴')
========测试结束========
ok
----------------------------------------------------------------------
Ran 2 tests in 0.001s
OK
```
可以看到，传入参数 (('苹果', '香蕉'), ('葡萄', '石榴')) 时，将包 ('苹果', '香蕉') 和 ('葡萄', '石榴') 作为一个整体，传递给测试用例了，如果我们希望将包里面的数据解开，传递给测试用例不同的参数，就需要用到 unpack 进行解包。

加入解包后的代码如下所示：

5.py
```
#coding=utf-8
import unittest
from ddt import ddt
from ddt import data
from ddt import unpack # 导入unpack

# 类之前定义装饰器，表示在类中要使用ddt了
@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('\n{:=^20}'.format("测试开始"))
    def tearDown(self):
        print("{:=^20}".format('测试结束'))
    @data(('苹果', '香蕉'), ('葡萄', '石榴'))
    # 解包，将 ('苹果', '香蕉') 解包，'苹果' 赋值给 txt1，'香蕉'赋值给 txt2
    @unpack
    def test_3(self, txt1, txt2):
        print(txt1)
        print(txt2)
if __name__ == '__main__':
    unittest.main(verbosity=2)
```
运行结果如下：
```
test_3_1___苹果____香蕉__ (__main__.MyTestCase) ... 
========测试开始========
苹果
香蕉
========测试结束========
ok
test_3_2___葡萄____石榴__ (__main__.MyTestCase) ... 
========测试开始========
葡萄
石榴
========测试结束========
ok
----------------------------------------------------------------------
Ran 2 tests in 0.002s
OK
```
上面的例子中，我们将输入的参数直接固定了，其实也可以通过文件读取，读取结果决定

6.py
```
#coding=utf-8
import unittest
from ddt import ddt
from ddt import data
from ddt import unpack

def readFile():
    params = []
    file = open('6.ddt.txt', 'r', encoding = 'utf-8')
    for line in file.readlines():
        params.append(line.strip('\n').split(','))
return params

# 类之前定义装饰器，表示在类中要使用ddt了
@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('{:=^20}'.format("测试开始"))
    def tearDown(self) -> None:
        print("{:=^20}".format('测试结束'))

    # 从文件中读取
    @data(*readFile())
    @unpack
    def test_1(self, txt1, txt2):
        print(txt1)
        print(txt2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
```
6.ddt.txt 文件中的内如下：
```
苹果,香蕉
葡萄,石榴
```
运行结果：

函数 readFile 从文件中读取数据，unpack 进行解包
```
test_1_1___苹果____香蕉__ (__main__.MyTestCase) ... 
========测试开始========
苹果
香蕉
========测试结束========
ok
test_1_2___葡萄____石榴__ (__main__.MyTestCase) ... 
========测试开始========
葡萄
石榴
========测试结束========
ok
----------------------------------------------------------------------
Ran 2 tests in 0.003s
OK
```
#### 2.2 ddt 数据驱动

打开浏览器进入百度查询的例子中我们发现除了输入的参数不同，test_1(self) 和 test_2(self) 完全相同，这里我们就要通过 data 设定参数实现在一个测试用例中输入不同的参数

7.py
```
#coding=utf-8
import unittest
from selenium import webdriver
import time
from ddt import ddt
from ddt import data
    
# 在 class 前定义 @ddt，用于表示要使用 ddt 了
@ddt
class forTestTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
        
    # data 用于设定参数
    @data('苹果', '香蕉', '石榴')
    def test_1(self, txt):
        self.driver.find_element_by_id('kw').send_keys(txt)
        self.driver.find_element_by_id('su').click()
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
```
运行结果，谷歌浏览器被打开三次，进入百度，分别输入 '苹果'，'香蕉'，'石榴'，每次浏览器关闭之后，才打开下一次，再进行搜索

执行结果：
```
test_1_1_苹果 (__main__.forTestTest) ... 
ok
test_1_2_香蕉 (__main__.forTestTest) ... 
ok
test_1_3_石榴 (__main__.forTestTest) ... 
ok
----------------------------------------------------------------------
Ran 3 tests in 33.639s
OK
```
上面的例子中，我们将输入的参数直接固定了，其实也可以通过文件读取，决定进入哪一个url 和输入的参数

8.py
```
#coding=utf-8
import unittest
from selenium import webdriver
import time
from ddt import ddt
from ddt import data
from ddt import unpack
    
def readFile():
    params = []
    file = open('8.ddt.txt', 'r', encoding = 'utf-8')
    for line in file.readlines():
        params.append(line.strip('\n').split(','))
    return params
    
@ddt
class forTestTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
                    
    # data 用于设定参数，表示参数由 readFile() 函数的返回值决定
    # unpack 用于解析参数，例如将['http://www.baidu.com', '苹果'] 分别 赋值给 url 和 txt
    @data(*readFile())
    @unpack
    def test_1(self, url, txt):
        self.driver.get(url)
        self.driver.find_element_by_id('kw').send_keys(txt)
        self.driver.find_element_by_id('su').click()
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
```
8.ddt.txt 文件中的内容如下：
```
http://www.baidu.com,苹果
http://www.baidu.com,香蕉
http://www.baidu.com,石榴
```
分析：

- readFile() 函数打开文件，读取文件的每一行，按逗号 ‘,' 划分关键字，
- unpack 用于解析参数，ddt 对于数据的解析方式为，解析一个，传参一个，所以函数中 url 和 txt 的参数顺序不能调换。

运行结果，谷歌浏览器被打开两次，进入百度，分别输入 '苹果', '香蕉', '石榴'，每次浏览器关闭之后，才打开下一次，再进行搜索

执行结果：
```
test_1_1___http___www_baidu_com____苹果__ (__main__.forTestTest) ... 
ok
test_1_2___http___www_baidu_com____香蕉__ (__main__.forTestTest) ... 
ok
test_1_3___http___www_baidu_com____石榴__ (__main__.forTestTest) ... 
ok
----------------------------------------------------------------------
Ran 3 tests in 42.588s
OK
```

### 3 unittest 断言用法

在 unittest中，TestCase 已经提供有封装好的断言方法进行断言校验。

断言：用于校验实际结果与预期结果是否匹型，在断言的内容选择上，是有要求的。

断言强调的是对于整个测试流程的结果进行判断，所以断言的内容是极为核心的。

上面的代码

9.py
```
#coding=utf-8
import unittest
from ddt import ddt
from ddt import data
from ddt import unpack

def readFile():
    params = []
    file = open('9.ddt.txt', 'r', encoding = 'utf-8')
    for line in file.readlines():
        params.append(line.strip('\n').split(','))
return params

# 类之前定义装饰器，表示在类中要使用ddt了
@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print('\n{:=^20}'.format("测试开始"))
    def tearDown(self) -> None:
        print("{:=^20}".format('测试结束'))
    
    @data(*readFile())
    @unpack
    def test_yam(self, name, age):
        # 获取参数name
        print(name)
        # 这里做断言，当断言不相等的时候返回 msg
        self.assertEqual(name, '张三', msg = 'NotEqual')
        # 获取为 text 的 value
        print(age)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)
```
文件内容：
```
张三,23
李四,25
王五,27
```
执行结果：
```
test_yam_1___张三____23__ (__main__.MyTestCase) ... 
========测试开始========
张三
23
========测试结束========
ok
test_yam_2___李四____25__ (__main__.MyTestCase) ... 
========测试开始========
李四
========测试结束========
FAIL
test_yam_3___王五____27__ (__main__.MyTestCase) ...
========测试开始========
王五
========测试结束========
FAIL

======================================================================
FAIL: test_yam_2___李四____25__ (__main__.MyTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Program Files\Python38\lib\site-packages\ddt.py", line 182, in wrapper
    return func(self, *args, **kwargs)
  File "c:/Users/dell/Desktop/test/9.py", line 28, in test_yam
    self.assertEqual(name, '张三', msg = 'NotEqual')
AssertionError: '李四' != '张三'
- 李四
+ 张三
 : NotEqual

======================================================================
FAIL: test_yam_3___王五____27__ (__main__.MyTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Program Files\Python38\lib\site-packages\ddt.py", line 182, in wrapper
    return func(self, *args, **kwargs)
  File "c:/Users/dell/Desktop/test/9.py", line 28, in test_yam
    self.assertEqual(name, '张三', msg = 'NotEqual')
AssertionError: '王五' != '张三'
- 王五
+ 张三
 : NotEqual

----------------------------------------------------------------------
Ran 3 tests in 0.003s

FAILED (failures=2)
```

可以看到第一个例子执行正确，后面的例子，执行结果和预期不一致，返回 NotEqual，从最终结果看，执行了三条用例，失败两条。

unittest 框架的 TestCase 类提供以下方法用于测试结果的判断

|方法|检查|
|:--:|:--:|
|assertEqual(a, b)|a ==b|
|assertNotEqual(a, b)|a !=b|
|assertTrue(x)|bool(x) is True|
|assertFalse(x)|Bool(x) is False|
|assertIs(a, b)|a is b|
|assertIsNot(a, b)|a is not b|
|assertIsNone(x)|x is None|
|assertIsNotNone(x)|x is not None|
|assertIn(a, b)|a in b|
|assertNotIn(a, b)|a not in b|
|assertIsInstance(a, b)|isinstance(a,b)|
|assertNotIsInstance(a, b)|not isinstance(a,b)|

### 4 unittest.skip()用法

假设我们有很多测试用例，有些我们需要执行，有些我们不想执行，不想执行的测试用例如何才能不执行呢，这就需要用到 skip。

Skip用法：

- 在 Case 中，对于不需要运行的用例或者特定条件下不执行的用例，可以应用 skip() 来实现有条件执行，或者绝对性跳过，用于对指定用例进行不执行操作
- skip通过装饰器进行使用
- 还是通过案例进行讲解，下面有 6 个测试用例，2-5测试用例被屏蔽了，使用的方法不同，
- `@unittest.skip(“xxx”)`是无条件跳过，xxx为跳过的理由
- `unittest.skipIf(1 < 2, ‘xxx')`，条件为 True 时跳过
- `@unittest.skipUnless(1 > 2, ‘xxx')`，条件为 False 时跳过，和 skipIf 更好相反
- `@unittest.expectedFailure`，如果用例执行失败，则不计入失败的case数中

直接看例子更加直观

10.py
```
#coding=utf-8
import unittest
    
class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_1(self):
        print('1')
    
    # 无条件跳过该条用例
    @unittest.skip("不想运行")
    def test_2(self):
        print('2')
    
    # 有条件跳过操作，条件为True跳过
    @unittest.skipIf(1 < 2, '1 < 2 为True，条件成立，跳过执行')
    def test_3(self):
        print('3')
    
    # 有条件执行跳过，条件为False跳过
    @unittest.skipUnless(1 > 2, 'Unless的理由，条件为False，跳过执行')
    def test_4(self):
        print('4')
    
    # 标记该测试预期为失败 ，如果该测试方法运行失败，则该测试不算做失败
    @unittest.expectedFailure
    def test_5(self):
        print('5')
        self.assertEqual(4, 3, msg = 'Equal')
    
    @unittest.expectedFailure
    def test_6(self):
        print('6')
        self.assertNotEqual(4, 3, msg = 'NotEqual')
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
```
执行结果如下，可以看到，test_2，test_3，test_4 跳过，test_5执行失败，但不算做失败
```
test_1 (__main__.MyTestCase) ... 1
ok
test_2 (__main__.MyTestCase) ... skipped '不想运行'
test_3 (__main__.MyTestCase) ... skipped '1 < 2 为True，条件成立，跳过执行'   
test_4 (__main__.MyTestCase) ... skipped 'Unless的理由，条件为False，跳过执行'
test_5 (__main__.MyTestCase) ... 5
expected failure
test_6 (__main__.MyTestCase) ... 6
unexpected success
----------------------------------------------------------------------
Ran 6 tests in 0.005s
FAILED (skipped=3, expected failures=1, unexpected successes=1)
```

### 5 unittest测试套件及runner应用

测试套件 suite 作用：

- 用于给测试用例进行排序
- 管理测试用例

通过例子讲解最容易理解，看一个最简单的例子，下面的代码中有五个测试用例，程序运行的结果和测试用例在代码中位置是没有关系的，结果永远打印 1 2 3 4 5，这是因为测试用例的执行顺序默认是按照字典顺序执行的，如何才能控制测试用例的执行顺序呢，这就需要使用测试套件了。

testCase.py
```
import unittest
class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
        
    def test_2(self):
        print("2")
        
    def test_1(self):
        print("1")
    
    def test_4(self):
        print("4")
    
    def test_3(self):
        print("3") 
    
    def test_5(self):
        print("5")
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
```
运行结果：
```
test_1 (__main__.MyTestCase) ... 1
ok
test_2 (__main__.MyTestCase) ... 2
ok
test_3 (__main__.MyTestCase) ... 3
ok
test_4 (__main__.MyTestCase) ... 4
ok
test_5 (__main__.MyTestCase) ... 5
ok
----------------------------------------------------------------------
Ran 5 tests in 0.002s
OK
```

再建一个py 文件11.py
```
#coding=utf-8
import unittest
from testCase import *
    
# 创建一个测试套件 list
suite = unittest.TestSuite()
# 方法一，添加测试用例（子元素）到测试套件（集合）
suite.addTest(MyTestCase('test_3'))
suite.addTest(MyTestCase("test_1"))
suite.addTest(MyTestCase("test_5"))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
```
我们首先创建一个测试套件，然后向测试套件中添加测试用例，最后创建 TextTestRunner 对象，调用 run 函数运行测试用例。这样我们不仅可以控制测试用例的执行顺序，还可以控制运行哪个测试用例。

结果如下：
```
test_3 (testCase.MyTestCase) ... 3
ok
test_1 (testCase.MyTestCase) ... 1
ok
test_5 (testCase.MyTestCase) ... 5
ok
----------------------------------------------------------------------
Ran 3 tests in 0.001s
OK
```
上面的方法每次添加测试用例都需要调用 addTest 函数，能不能一次添加多个测试用例

12.py
```
#coding=utf-8
import unittest
from testCase import *

# 创建一个测试套件 list
suite = unittest.TestSuite()

# 方法二，批量添加测试用例
cases = [MyTestCase('test_3'), MyTestCase('test_1'), MyTestCase('test_5')]
suite.addTests(cases)

# 套件通过TextTestRunner对象运行，功能相当于unittest.main(verbosity=2)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
```
如果测试用例非常多，或者有多个文件中的测试用例都需要测试，这样添加也不是很方便，我们好可以按照文件路径，将该路径下需要测试的文件添加进测试套件中

13.py
```
#coding=utf-8
import unittest
from testCase import *

# 创建一个测试套件 list
suite = unittest.TestSuite()

# 方法三，批量运行多个unittest类
test_dir = './'
# start_dir 参数指定文件路径，pattern 执行规则，'s*.py' 表示以 "s" 开头，".py" 的都加入测试套件中
discover = unittest.defaultTestLoader.discover(start_dir = test_dir, pattern = 't*.py')

runner = unittest.TextTestRunner(verbosity=2)
runner.run(discover) # 通过 run 函数运行测试用例
```
还可以执行类的名字，执行该类下面所有的测试用例，使用 loadTestsFromName 函数或者 loadTestsFromTestCase 都可以，案例如下：

14.py
```
#coding=utf-8
import unittest
from testCase import *

# 创建一个测试套件 list
suite = unittest.TestSuite()

# 方法四，给出文件名和类名，就能测试所有的测试用例
suite.addTests(unittest.TestLoader().loadTestsFromName('testCase.MyTestCase'))

# 套件通过TextTestRunner对象运行，功能相当于unittest.main(verbosity=2)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
```
15.py
```
#coding=utf-8
import unittest
from testCase import *

# 创建一个测试套件 list
suite = unittest.TestSuite()

# 方法五，给出类名，就能测试所有的测试用例
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTestCase))
# 套件通过TextTestRunner对象运行，功能相当于unittest.main(verbosity=2)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
```

### 6 unittest+HTMLTestRunner 自动化实现

通过 HTMLTestRunner 我们可以将测试结果生成 html 文件，通过网页端进行查看。步骤如下：

#### 6.1 导入环境

下载 `HTMLTestRunner.py` 文件，下载地址：<http://tungwaiyip.info/software/HTMLTestRunner_0_8_2/HTMLTestRunner.py>

下载后，把`HTMLTestRunner.py` 文件复制到 Python 安装路径下的 lib 文件夹中。在python3中用`HTMLTestRunner.py`会报错，原因是`HTMLTestRunner`仅支持python2，不支持python3，需要做小小的改动。

修改内容：

- 第94行，将`import StringIO`修改成`import io`
- 第539行，将`self.outputBuffer = StringIO.StringIO()`修改成`self.outputBuffer = io.StringIO()`
- 第642行，将`if not rmap.has_key(cls)`:修改成`if not cls in rmap:`
- 注释掉763行、766行、767行，768行前提4格；注释掉769行、772行、773行，774行前提4格；
- 第631行，将`print >> sys.stderr, ‘\nTime Elapsed: %s' % (self.stopTime-self.startTime)`修改成`print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime))`

#### 6.2 导包

`from HTMLTestRunner import HTMLTestRunner`

下面就通过案例进行演示

testCase.py 文件
```
import unittest
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    def tearDown(self) -> None:
        pass
    
    def test_2(self):
        print("2")
    
    def test_1(self):
        print("1")
    
    def test_4(self):
        print("4")
    
    def test_3(self):
        print("3")
    
    def test_5(self):
        print("5")
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
```
16.py
```
#coding=utf-8
import unittest
from suite_case import MyTestCase
from HTMLTestRunner import HTMLTestRunner
import os

suite = unittest.TestSuite()

report_path = './report/'
report_file = report_path + 'report.html'
# 路径不存在就创建一个文件夹
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
pass

report_name = '测试报告名称'
report_title = '测试报告标题'
report_desc = '测试报告描述'
    
with open(report_file, 'wb') as report:
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTestCase))
    # 套件结合 TextTestRunner 对象进行运行，相当于 unittest.mian()
    # 如果结合 HTMLTestRunner 使用，则需要调用 HTMLTestRunner 中的运行器
    runner = HTMLTestRunner(stream = report, title = report_title, description = report_desc)
    runner.run(suite)
```
运行 就会成成 report.html 文件，浏览器打开该文件，如下所示：

测试报告标题

start Time: 2020-11-15 20:35:50

Duration: 0:00:01

Status: Pass 5

测试报告描述

Show [Summary]() [Failed]() [All]()

|Test Group/Test Case|Count|Pass|Fail|Error|View|
|:--:|:--:|:--:|:--:|:--:|:--:|
|testCase.MyTestCase|5|5|0|0|[Detail]()|
|Total|5|5|0|0||

这样就生成一个比较直观的测试报告

### 7.总结

到此关于Python自动化之unittest框架的介绍就完了。
