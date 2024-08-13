title: nose简介
date: 2021-06-04
category: 测试
tag: nose, python

[TOC]

### 1. 简介

nose是python开发的测试框架。nose扩展了unittest，他让测试更加容易。

#### 1.1 编写用例更简单

nose可以收集继承于unittest.TestCase类中的测试例，当然，你也可以编写简单的测试函数，编写并不是继承于unittest.TestCase的测试类。nose也提供了许多帮助函数，用于编写定时测试例，用于异常的测试，和其他一些公共的使用情况。

#### 1.2 运行用例更简单

只要你按照一些简单的要求组织你的测试库和代码，nose就可以自动收集测试用例。并没有必要手动收集测试case到测试suites中。运行测试响应迅速，因为nose在加载第一个测试模块后立即开始运行测试

#### 1.3 初始化测试环境更简单

nose组件支持package，module，class和case级别，因此初始化操作很容易完成。

#### 1.4 做所想的事更简单

nose配备了一些[内置插件](https://nose.readthedocs.io/en/latest/plugins/builtin.html)，以帮助你捕获输出，反思错误，覆盖代码，文档测试，等等。它还配备了用于加载、运行测试，在测试例运行时，查看和报告测试。如果您不喜欢默认收集方案，或者它不适合你的项目，或者你需要不同于unittest标准的格式报告，或者需要收集有关测试的额外信息（如代码覆盖或数据分析），您可以编写插件来让nose做这些事。

### 2 安装

#### 2.1 通过setuptools安装

安装命令`easy_install nose`

```
WARNING: The easy_install command is deprecated and will be removed in a future version.
Searching for nose
Reading https://pypi.org/simple/nose/
Downloading https://files.pythonhosted.org/packages/15/d8/dd071918c040f50fa1cf80da16423af51ff8ce4a0f2399b7bf8de45ac3d9/nose-1.3.7-py3-none-any.whl#sha256=9ff7c6cc443f8c51994b34a667bbcf45afd6d945be7477b52e97516fd17c53ac
Best match: nose 1.3.7
Processing nose-1.3.7-py3-none-any.whl
Installing nose-1.3.7-py3-none-any.whl to c:\program files\python38\lib\site-packages
Adding nose 1.3.7 to easy-install.pth file
Installing nosetests-script.py script to c:\program files\python38\Scripts
Installing nosetests.exe script to c:\program files\python38\Scripts
Installing nosetests-3.4-script.py script to c:\program files\python38\Scripts
Installing nosetests-3.4.exe script to c:\program files\python38\Scripts

Installed c:\program files\python38\lib\site-packages\nose-1.3.7-py3.8.egg
Processing dependencies for nose
Finished processing dependencies for nose
```

#### 2.2 通过pip安装

安装命令`pip install nose`

```
PS C:\Users\dell> pip install nose

Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple

Collecting nose

 Downloading https://pypi.tuna.tsinghua.edu.cn/packages/15/d8/dd071918c040f50fa1cf80da16423af51ff8ce4a0f2399b7bf8de45ac3d9/nose-1.3.7-py3-none-any.whl (154 kB)

   |████████████████████████████████| 154 kB 1.7 MB/s

Installing collected packages: nose

Successfully installed nose-1.3.7
```

或者下载后通过`pip`安装

https://files.pythonhosted.org/packages/15/d8/dd071918c040f50fa1cf80da16423af51ff8ce4a0f2399b7bf8de45ac3d9/nose-1.3.7-py3-none-any.whl

安装命令`pip install nose-1.3.7-py3-none-any.whl `

```
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Processing e:\公司文档\分享内容\software\nose-1.3.7-py3-none-any.whl
Installing collected packages: nose
Successfully installed nose-1.3.7
```

#### 2.3 源码安装

下载源码 `https://files.pythonhosted.org/packages/58/a5/0dc93c3ec33f4e281849523a5a913fa1eea9a3068acfa754d44d88107a44/nose-1.3.7.tar.gz`

解压源码，进入目录 `cd nose-1.3.7`

安装命令`python setup.py install`

```
running install
running bdist_egg
running egg_info
writing nose.egg-info\PKG-INFO
writing dependency_links to nose.egg-info\dependency_links.txt
writing entry points to nose.egg-info\entry_points.txt
writing top-level names to nose.egg-info\top_level.txt
reading manifest file 'nose.egg-info\SOURCES.txt'
reading manifest template 'MANIFEST.in'
no previously-included directories found matching 'doc\.build'
writing manifest file 'nose.egg-info\SOURCES.txt'
installing library code to build\bdist.win-amd64\egg
running install_lib
running build_py
creating build
creating build\lib
creating build\lib\nose
copying nose\case.py -> build\lib\nose
copying nose\commands.py -> build\lib\nose
copying nose\config.py -> build\lib\nose
copying nose\core.py -> build\lib\nose
copying nose\exc.py -> build\lib\nose
copying nose\failure.py -> build\lib\nose
copying nose\importer.py -> build\lib\nose
copying nose\inspector.py -> build\lib\nose
copying nose\loader.py -> build\lib\nose
copying nose\proxy.py -> build\lib\nose
copying nose\pyversion.py -> build\lib\nose
copying nose\result.py -> build\lib\nose
copying nose\selector.py -> build\lib\nose
copying nose\suite.py -> build\lib\nose
copying nose\twistedtools.py -> build\lib\nose
copying nose\util.py -> build\lib\nose
copying nose\__init__.py -> build\lib\nose
copying nose\__main__.py -> build\lib\nose
creating build\lib\nose\ext
copying nose\ext\dtcompat.py -> build\lib\nose\ext
copying nose\ext\__init__.py -> build\lib\nose\ext
creating build\lib\nose\plugins
copying nose\plugins\allmodules.py -> build\lib\nose\plugins
copying nose\plugins\attrib.py -> build\lib\nose\plugins
copying nose\plugins\base.py -> build\lib\nose\plugins
copying nose\plugins\builtin.py -> build\lib\nose\plugins
copying nose\plugins\capture.py -> build\lib\nose\plugins
copying nose\plugins\collect.py -> build\lib\nose\plugins
copying nose\plugins\cover.py -> build\lib\nose\plugins
copying nose\plugins\debug.py -> build\lib\nose\plugins
copying nose\plugins\deprecated.py -> build\lib\nose\plugins
copying nose\plugins\doctests.py -> build\lib\nose\plugins
copying nose\plugins\errorclass.py -> build\lib\nose\plugins
copying nose\plugins\failuredetail.py -> build\lib\nose\plugins
copying nose\plugins\isolate.py -> build\lib\nose\plugins
copying nose\plugins\logcapture.py -> build\lib\nose\plugins
copying nose\plugins\manager.py -> build\lib\nose\plugins
copying nose\plugins\multiprocess.py -> build\lib\nose\plugins
copying nose\plugins\plugintest.py -> build\lib\nose\plugins
copying nose\plugins\prof.py -> build\lib\nose\plugins
copying nose\plugins\skip.py -> build\lib\nose\plugins
copying nose\plugins\testid.py -> build\lib\nose\plugins
copying nose\plugins\xunit.py -> build\lib\nose\plugins
copying nose\plugins\__init__.py -> build\lib\nose\plugins
creating build\lib\nose\sphinx
copying nose\sphinx\pluginopts.py -> build\lib\nose\sphinx
copying nose\sphinx\__init__.py -> build\lib\nose\sphinx
creating build\lib\nose\tools
copying nose\tools\nontrivial.py -> build\lib\nose\tools
copying nose\tools\trivial.py -> build\lib\nose\tools
copying nose\tools\__init__.py -> build\lib\nose\tools
copying nose\usage.txt -> build\lib\nose
C:\Program Files\Python38\lib\site-packages\setuptools\lib2to3_ex.py:39: SetuptoolsDeprecationWarning: 2to3 support is deprecated. If the project still requires Python 2 support, please migrate to a single-codebase solution or employ an independent conversion process.
  warnings.warn(
Fixing build\lib\nose\case.py build\lib\nose\commands.py build\lib\nose\config.py build\lib\nose\core.py build\lib\nose\exc.py build\lib\nose\failure.py build\lib\nose\importer.py build\lib\nose\inspector.py build\lib\nose\loader.py build\lib\nose\proxy.py build\lib\nose\pyversion.py build\lib\nose\result.py build\lib\nose\selector.py build\lib\nose\suite.py build\lib\nose\twistedtools.py build\lib\nose\util.py build\lib\nose\__init__.py build\lib\nose\__main__.py build\lib\nose\ext\dtcompat.py build\lib\nose\ext\__init__.py build\lib\nose\plugins\allmodules.py build\lib\nose\plugins\attrib.py build\lib\nose\plugins\base.py build\lib\nose\plugins\builtin.py build\lib\nose\plugins\capture.py build\lib\nose\plugins\collect.py build\lib\nose\plugins\cover.py build\lib\nose\plugins\debug.py build\lib\nose\plugins\deprecated.py build\lib\nose\plugins\doctests.py build\lib\nose\plugins\errorclass.py build\lib\nose\plugins\failuredetail.py build\lib\nose\plugins\isolate.py build\lib\nose\plugins\logcapture.py build\lib\nose\plugins\manager.py build\lib\nose\plugins\multiprocess.py build\lib\nose\plugins\plugintest.py build\lib\nose\plugins\prof.py build\lib\nose\plugins\skip.py build\lib\nose\plugins\testid.py build\lib\nose\plugins\xunit.py build\lib\nose\plugins\__init__.py build\lib\nose\sphinx\pluginopts.py build\lib\nose\sphinx\__init__.py build\lib\nose\tools\nontrivial.py build\lib\nose\tools\trivial.py build\lib\nose\tools\__init__.py
Skipping optional fixer: buffer
Skipping optional fixer: idioms
Skipping optional fixer: set_literal
Skipping optional fixer: ws_comma
Fixing build\lib\nose\case.py build\lib\nose\commands.py build\lib\nose\config.py build\lib\nose\core.py build\lib\nose\exc.py build\lib\nose\failure.py build\lib\nose\importer.py build\lib\nose\inspector.py build\lib\nose\loader.py build\lib\nose\proxy.py build\lib\nose\pyversion.py build\lib\nose\result.py build\lib\nose\selector.py build\lib\nose\suite.py build\lib\nose\twistedtools.py build\lib\nose\util.py build\lib\nose\__init__.py build\lib\nose\__main__.py build\lib\nose\ext\dtcompat.py build\lib\nose\ext\__init__.py build\lib\nose\plugins\allmodules.py build\lib\nose\plugins\attrib.py build\lib\nose\plugins\base.py build\lib\nose\plugins\builtin.py build\lib\nose\plugins\capture.py build\lib\nose\plugins\collect.py build\lib\nose\plugins\cover.py build\lib\nose\plugins\debug.py build\lib\nose\plugins\deprecated.py build\lib\nose\plugins\doctests.py build\lib\nose\plugins\errorclass.py build\lib\nose\plugins\failuredetail.py build\lib\nose\plugins\isolate.py build\lib\nose\plugins\logcapture.py build\lib\nose\plugins\manager.py build\lib\nose\plugins\multiprocess.py build\lib\nose\plugins\plugintest.py build\lib\nose\plugins\prof.py build\lib\nose\plugins\skip.py build\lib\nose\plugins\testid.py build\lib\nose\plugins\xunit.py build\lib\nose\plugins\__init__.py build\lib\nose\sphinx\pluginopts.py build\lib\nose\sphinx\__init__.py build\lib\nose\tools\nontrivial.py build\lib\nose\tools\trivial.py build\lib\nose\tools\__init__.py
Skipping optional fixer: buffer
Skipping optional fixer: idioms
Skipping optional fixer: set_literal
Skipping optional fixer: ws_comma
creating build\bdist.win-amd64
creating build\bdist.win-amd64\egg
creating build\bdist.win-amd64\egg\nose
copying build\lib\nose\case.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\commands.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\config.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\core.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\exc.py -> build\bdist.win-amd64\egg\nose
creating build\bdist.win-amd64\egg\nose\ext
copying build\lib\nose\ext\dtcompat.py -> build\bdist.win-amd64\egg\nose\ext
copying build\lib\nose\ext\__init__.py -> build\bdist.win-amd64\egg\nose\ext
copying build\lib\nose\failure.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\importer.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\inspector.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\loader.py -> build\bdist.win-amd64\egg\nose
creating build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\allmodules.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\attrib.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\base.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\builtin.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\capture.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\collect.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\cover.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\debug.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\deprecated.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\doctests.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\errorclass.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\failuredetail.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\isolate.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\logcapture.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\manager.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\multiprocess.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\plugintest.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\prof.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\skip.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\testid.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\xunit.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\plugins\__init__.py -> build\bdist.win-amd64\egg\nose\plugins
copying build\lib\nose\proxy.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\pyversion.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\result.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\selector.py -> build\bdist.win-amd64\egg\nose
creating build\bdist.win-amd64\egg\nose\sphinx
copying build\lib\nose\sphinx\pluginopts.py -> build\bdist.win-amd64\egg\nose\sphinx
copying build\lib\nose\sphinx\__init__.py -> build\bdist.win-amd64\egg\nose\sphinx
copying build\lib\nose\suite.py -> build\bdist.win-amd64\egg\nose
creating build\bdist.win-amd64\egg\nose\tools
copying build\lib\nose\tools\nontrivial.py -> build\bdist.win-amd64\egg\nose\tools
copying build\lib\nose\tools\trivial.py -> build\bdist.win-amd64\egg\nose\tools
copying build\lib\nose\tools\__init__.py -> build\bdist.win-amd64\egg\nose\tools
copying build\lib\nose\twistedtools.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\usage.txt -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\util.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\__init__.py -> build\bdist.win-amd64\egg\nose
copying build\lib\nose\__main__.py -> build\bdist.win-amd64\egg\nose
byte-compiling build\bdist.win-amd64\egg\nose\case.py to case.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\commands.py to commands.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\config.py to config.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\core.py to core.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\exc.py to exc.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\ext\dtcompat.py to dtcompat.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\ext\__init__.py to __init__.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\failure.py to failure.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\importer.py to importer.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\inspector.py to inspector.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\loader.py to loader.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\allmodules.py to allmodules.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\attrib.py to attrib.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\base.py to base.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\builtin.py to builtin.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\capture.py to capture.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\collect.py to collect.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\cover.py to cover.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\debug.py to debug.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\deprecated.py to deprecated.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\doctests.py to doctests.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\errorclass.py to errorclass.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\failuredetail.py to failuredetail.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\isolate.py to isolate.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\logcapture.py to logcapture.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\manager.py to manager.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\multiprocess.py to multiprocess.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\plugintest.py to plugintest.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\prof.py to prof.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\skip.py to skip.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\testid.py to testid.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\xunit.py to xunit.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\plugins\__init__.py to __init__.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\proxy.py to proxy.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\pyversion.py to pyversion.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\result.py to result.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\selector.py to selector.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\sphinx\pluginopts.py to pluginopts.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\sphinx\__init__.py to __init__.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\suite.py to suite.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\tools\nontrivial.py to nontrivial.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\tools\trivial.py to trivial.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\tools\__init__.py to __init__.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\twistedtools.py to twistedtools.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\util.py to util.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\__init__.py to __init__.cpython-38.pyc
byte-compiling build\bdist.win-amd64\egg\nose\__main__.py to __main__.cpython-38.pyc
installing package data to build\bdist.win-amd64\egg
running install_data
creating build\bdist.win-amd64\egg\man
creating build\bdist.win-amd64\egg\man\man1
copying nosetests.1 -> build\bdist.win-amd64\egg\man\man1
creating build\bdist.win-amd64\egg\EGG-INFO
copying nose.egg-info\PKG-INFO -> build\bdist.win-amd64\egg\EGG-INFO
copying nose.egg-info\SOURCES.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying nose.egg-info\dependency_links.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying nose.egg-info\entry_points.txt -> build\bdist.win-amd64\egg\EGG-INFO
copying nose.egg-info\not-zip-safe -> build\bdist.win-amd64\egg\EGG-INFO
copying nose.egg-info\top_level.txt -> build\bdist.win-amd64\egg\EGG-INFO
creating dist
creating 'dist\nose-1.3.7-py3.8.egg' and adding 'build\bdist.win-amd64\egg' to it
removing 'build\bdist.win-amd64\egg' (and everything under it)
Processing nose-1.3.7-py3.8.egg
creating c:\program files\python38\lib\site-packages\nose-1.3.7-py3.8.egg
Extracting nose-1.3.7-py3.8.egg to c:\program files\python38\lib\site-packages
Adding nose 1.3.7 to easy-install.pth file
Installing nosetests-script.py script to C:\Program Files\Python38\Scripts
Installing nosetests.exe script to C:\Program Files\Python38\Scripts
Installing nosetests-3.8-script.py script to C:\Program Files\Python38\Scripts
Installing nosetests-3.8.exe script to C:\Program Files\Python38\Scripts

Installed c:\program files\python38\lib\site-packages\nose-1.3.7-py3.8.egg
Processing dependencies for nose==1.3.7
Finished processing dependencies for nose==1.3.7
```

#### 2.4. 快速使用

nose使用相当简单，在windows系统下，只要在终端中进入脚本目录，输入`nosetests`即可

```
PS C:\Users\dell\Desktop\test\markdown> nosetests

----------------------------------------------------------------------
Ran 0 tests in 0.001s

OK
```

> 注意：nose支持python3，但nose下的部分第三方插件本不支持python3，所以使用的时候要注意，本文中提到的均为python3

### 3. nose命令

```
nosetests -h
Usage: nosetests [options]

Options:
  -h, --help            show this help message and exit
  -V, --version         Output nose version and exit
  -p, --plugins         Output list of available plugins and exit. Combine
                        with higher verbosity for greater detail
  -v, --verbose         Be more verbose. [NOSE_VERBOSE]
  --verbosity=VERBOSITY
                        Set verbosity; --verbosity=2 is the same as -v
  -q, --quiet           Be less verbose
  -c FILES, --config=FILES
                        Load configuration from config file(s). May be
                        specified multiple times; in that case, all config
                        files will be loaded and combined
  -w WHERE, --where=WHERE
                        Look for tests in this directory. May be specified
                        multiple times. The first directory passed will be
                        used as the working directory, in place of the current
                        working directory, which is the default. Others will
                        be added to the list of tests to execute. [NOSE_WHERE]
  --py3where=PY3WHERE   Look for tests in this directory under Python 3.x.
                        Functions the same as 'where', but only applies if
                        running under Python 3.x or above.  Note that, if
                        present under 3.x, this option completely replaces any
                        directories specified with 'where', so the 'where'
                        option becomes ineffective. [NOSE_PY3WHERE]
  -m REGEX, --match=REGEX, --testmatch=REGEX
                        Files, directories, function names, and class names
                        that match this regular expression are considered
                        tests.  Default: (?:^|[\b_\.\-])[Tt]est
                        [NOSE_TESTMATCH]
  --tests=NAMES         Run these tests (comma-separated list). This argument
                        is useful mainly from configuration files; on the
                        command line, just pass the tests to run as additional
                        arguments with no switch.
  -l DEBUG, --debug=DEBUG
                        Activate debug logging for one or more systems.
                        Available debug loggers: nose, nose.importer,
                        nose.inspector, nose.plugins, nose.result and
                        nose.selector. Separate multiple names with a comma.
  --debug-log=FILE      Log debug messages to this file (default: sys.stderr)
  --logging-config=FILE, --log-config=FILE
                        Load logging config from this file -- bypasses all
                        other logging config settings.
  -I REGEX, --ignore-files=REGEX
                        Completely ignore any file that matches this regular
                        expression. Takes precedence over any other settings
                        or plugins. Specifying this option will replace the
                        default setting. Specify this option multiple times to
                        add more regular expressions [NOSE_IGNORE_FILES]
  -e REGEX, --exclude=REGEX
                        Don't run tests that match regular expression
                        [NOSE_EXCLUDE]
  -i REGEX, --include=REGEX
                        This regular expression will be applied to files,
                        directories, function names, and class names for a
                        chance to include additional tests that do not match
                        TESTMATCH.  Specify this option multiple times to add
                        more regular expressions [NOSE_INCLUDE]
  -x, --stop            Stop running tests after the first error or failure
  -P, --no-path-adjustment
                        Don't make any changes to sys.path when loading tests
                        [NOSE_NOPATH]
  --exe                 Look for tests in python modules that are executable.
                        Normal behavior is to exclude executable modules,
                        since they may not be import-safe [NOSE_INCLUDE_EXE]
  --noexe               DO NOT look for tests in python modules that are
                        executable. (The default on the windows platform is to
                        do so.)
  --traverse-namespace  Traverse through all path entries of a namespace
                        package
  --first-package-wins, --first-pkg-wins, --1st-pkg-wins
                        nose's importer will normally evict a package from
                        sys.modules if it sees a package with the same name in
                        a different location. Set this option to disable that
                        behavior.
  --no-byte-compile     Prevent nose from byte-compiling the source into .pyc
                        files while nose is scanning for and running tests.
  -a ATTR, --attr=ATTR  Run only tests that have attributes specified by ATTR
                        [NOSE_ATTR]
  -A EXPR, --eval-attr=EXPR
                        Run only tests for whose attributes the Python
                        expression EXPR evaluates to True [NOSE_EVAL_ATTR]
  -s, --nocapture       Don't capture stdout (any stdout output will be
                        printed immediately) [NOSE_NOCAPTURE]
  --nologcapture        Disable logging capture plugin. Logging configuration
                        will be left intact. [NOSE_NOLOGCAPTURE]
  --logging-format=FORMAT
                        Specify custom format to print statements. Uses the
                        same format as used by standard logging handlers.
                        [NOSE_LOGFORMAT]
  --logging-datefmt=FORMAT
                        Specify custom date/time format to print statements.
                        Uses the same format as used by standard logging
                        handlers. [NOSE_LOGDATEFMT]
  --logging-filter=FILTER
                        Specify which statements to filter in/out. By default,
                        everything is captured. If the output is too verbose,
                        use this option to filter out needless output.
                        Example: filter=foo will capture statements issued
                        ONLY to  foo or foo.what.ever.sub but not foobar or
                        other logger. Specify multiple loggers with comma:
                        filter=foo,bar,baz. If any logger name is prefixed
                        with a minus, eg filter=-foo, it will be excluded
                        rather than included. Default: exclude logging
                        messages from nose itself (-nose). [NOSE_LOGFILTER]
  --logging-clear-handlers
                        Clear all other logging handlers
  --logging-level=LOGCAPTURE_LEVEL
                        Set the log level to capture
  --with-coverage       Enable plugin Coverage:  Activate a coverage report
                        using Ned Batchelder's coverage module.
                        [NOSE_WITH_COVERAGE]
  --cover-package=PACKAGE
                        Restrict coverage output to selected packages
                        [NOSE_COVER_PACKAGE]
  --cover-erase         Erase previously collected coverage statistics before
                        run
  --cover-tests         Include test modules in coverage report
                        [NOSE_COVER_TESTS]
  --cover-min-percentage=COVER_MIN_PERCENTAGE
                        Minimum percentage of coverage for tests to pass
                        [NOSE_COVER_MIN_PERCENTAGE]
  --cover-inclusive     Include all python files under working directory in
                        coverage report.  Useful for discovering holes in test
                        coverage if not all files are imported by the test
                        suite. [NOSE_COVER_INCLUSIVE]
  --cover-html          Produce HTML coverage information
  --cover-html-dir=DIR  Produce HTML coverage information in dir
  --cover-branches      Include branch coverage in coverage report
                        [NOSE_COVER_BRANCHES]
  --cover-xml           Produce XML coverage information
  --cover-xml-file=FILE
                        Produce XML coverage information in file
  --pdb                 Drop into debugger on failures or errors
  --pdb-failures        Drop into debugger on failures
  --pdb-errors          Drop into debugger on errors
  --no-deprecated       Disable special handling of DeprecatedTest exceptions.
  --with-doctest        Enable plugin Doctest:  Activate doctest plugin to
                        find and run doctests in non-test modules.
                        [NOSE_WITH_DOCTEST]
  --doctest-tests       Also look for doctests in test modules. Note that
                        classes, methods and functions should have either
                        doctests or non-doctest tests, not both.
                        [NOSE_DOCTEST_TESTS]
  --doctest-extension=EXT
                        Also look for doctests in files with this extension
                        [NOSE_DOCTEST_EXTENSION]
  --doctest-result-variable=VAR
                        Change the variable name set to the result of the last
                        interpreter command from the default '_'. Can be used
                        to avoid conflicts with the _() function used for text
                        translation. [NOSE_DOCTEST_RESULT_VAR]
  --doctest-fixtures=SUFFIX
                        Find fixtures for a doctest file in module with this
                        name appended to the base name of the doctest file
  --doctest-options=OPTIONS
                        Specify options to pass to doctest. Eg.
                        '+ELLIPSIS,+NORMALIZE_WHITESPACE'
  --with-isolation      Enable plugin IsolationPlugin:  Activate the isolation
                        plugin to isolate changes to external modules to a
                        single test module or package. The isolation plugin
                        resets the contents of sys.modules after each test
                        module or package runs to its state before the test.
                        PLEASE NOTE that this plugin should not be used with
                        the coverage plugin, or in any other case where module
                        reloading may produce undesirable side-effects.
                        [NOSE_WITH_ISOLATION]
  -d, --detailed-errors, --failure-detail
                        Add detail to error output by attempting to evaluate
                        failed asserts [NOSE_DETAILED_ERRORS]
  --no-skip             Disable special handling of SkipTest exceptions.
  --with-id             Enable plugin TestId:  Activate to add a test id (like
                        #1) to each test name output. Activate with --failed
                        to rerun failing tests only.  [NOSE_WITH_ID]
  --id-file=FILE        Store test ids found in test runs in this file.
                        Default is the file .noseids in the working directory.
  --failed              Run the tests that failed in the last test run.
  --processes=NUM       Spread test run among this many processes. Set a
                        number equal to the number of processors or cores in
                        your machine for best results. Pass a negative number
                        to have the number of processes automatically set to
                        the number of cores. Passing 0 means to disable
                        parallel testing. Default is 0 unless NOSE_PROCESSES
                        is set. [NOSE_PROCESSES]
  --process-timeout=SECONDS
                        Set timeout for return of results from each test
                        runner process. Default is 10. [NOSE_PROCESS_TIMEOUT]
  --process-restartworker
                        If set, will restart each worker process once their
                        tests are done, this helps control memory leaks from
                        killing the system. [NOSE_PROCESS_RESTARTWORKER]
  --with-xunit          Enable plugin Xunit: This plugin provides test results
                        in the standard XUnit XML format. [NOSE_WITH_XUNIT]
  --xunit-file=FILE     Path to xml file to store the xunit report in. Default
                        is nosetests.xml in the working directory
                        [NOSE_XUNIT_FILE]
  --xunit-testsuite-name=PACKAGE
                        Name of the testsuite in the xunit xml, generated by
                        plugin. Default test suite name is nosetests.
  --all-modules         Enable plugin AllModules: Collect tests from all
                        python modules.  [NOSE_ALL_MODULES]
  --collect-only        Enable collect-only:  Collect and output test names
                        only, don't run any tests.  [COLLECT_ONLY]
```

> 

### 4. 基本用法

使用notetests脚本

```
nosetests [options] [(optional) test files or directories]
```

除了使用命令行参数外，你还可以在测试目录下配置.noserc或者nose.cfg文件。该配置文件是标准的.ini配置文件。把你的配置写在[nosetests]部分，如下：

```
[nosetests]
verbosity=3
with-doctest=1
```

也有不能使用配置文件的情况（如运行nose时你不想让使用nose的全局配置文件）。为了忽略这个配置文件，我们可以设置一个环境变量`NOSE_IGNORE_CONFIG_FILES`。

除了使用notetests外，我们还可以使用其他方法运行nose，如下：

```
import nose
nose.main()
```

如果你不想使用unittest框架测试结束时这种显示方式，可以在脚本中使用以下方式：

```
import nose
result = nose.run()
```

#### 4.1 nose测试实践

- **函数形式的测试用例**

```
#coding:utf-8

def setUp():
    print("test_setUp")

def test_task_1():
    print("test_task_1")

def test_task_2():
    print("test_task_2")

def test_task_3():
    print("test_task_3")    

def tearDown():
    print("test_teardown")

test_task_1.teardown=test_task_3.teardown= tearDown
```

运行的结果如下：

```
PS C:\Users\dell\Desktop\test\nose> nosetests -v -s test_case.test_case_1
test_setUp
test_case_1.test_task_1 ... test_task_1
test_teardown
ok
test_case_1.test_task_2 ... test_task_2
ok
test_case_1.test_task_3 ... test_task_3
test_teardown
ok
test_teardown

----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

最后面加了一句`test_task_1.teardown=test_task_3.teardown= tearDown`，说明在运行完成后就执行tearDown操作，所以这里的执行顺序是：`setUp-->test_task_1-->teardown-->test_task_2-->test_task_3-->teardown-->teardown`

因次，在函数或者函数式的用例组织中，setUp和tearDown只会执行一次，分别是开始及结束。

- **类形式的测试用例**

```
# coding=utf-8

class TestClass():

    def setUpClass():
        print("TestClass.setUpClass")

    def setUp(self):
        print("TestClass.setup")

    def Testfunc1(self):
        print("TestClass.Testfunc1")

    def test_func1(self):
        print("TestClass.test_func1")

    def Testfunc2(self):
        print("TestClass.Testfunc2")

    def test_func2(self):
        print("TestClass.test_func2")

    def tearDown(self):
        print("TestClass_setup_teardown")

    def tearDownClass():
        print("TestClass.tearDownClass")
```

运行结果：

```
PS C:\Users\dell\Desktop\test\nose> nosetests -v -s test_case.test_case_2
TestClass.setUpClass
test_case_2.TestClass.Testfunc1 ... TestClass.setup
TestClass.Testfunc1
TestClass_setup_teardown
ok
test_case_2.TestClass.Testfunc2 ... TestClass.setup
TestClass.Testfunc2
TestClass_setup_teardown
ok
test_case_2.TestClass.test_func1 ... TestClass.setup
TestClass.test_func1
TestClass_setup_teardown
ok
test_case_2.TestClass.test_func2 ... TestClass.setup
TestClass.test_func2
TestClass_setup_teardown
ok
TestClass.tearDownClass

----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK
```

从运行结果中可以看出，每个用例都会分别执行`setUp`及`tearDown`，但是与unittest一样，在类中的测试用例顺序变更了，由字母排序了。而`setUpClass`和`tearDownClass`两个函数功能，只运行一次。

- 包形式运行
  
我们创建包的时候需要同时新建`__init__.py`，添加内容如下：

```
def setUp():
    print("全部开始")

def tearDown():
    print("全部结束")
```

然后再次执行包文件，结果如下：

```
PS C:\Users\dell\Desktop\test\nose> nosetests -v -s test_case.test_case_2
全部开始
TestClass.setUpClass
test_case.test_case_2.TestClass.Testfunc1 ... TestClass.setup
TestClass.Testfunc1
TestClass_setup_teardown
ok
test_case.test_case_2.TestClass.Testfunc2 ... TestClass.setup
TestClass.Testfunc2
TestClass_setup_teardown
ok
test_case.test_case_2.TestClass.test_func1 ... TestClass.setup
TestClass.test_func1
TestClass_setup_teardown
ok
test_case.test_case_2.TestClass.test_func2 ... TestClass.setup
TestClass.test_func2
TestClass_setup_teardown
ok
TestClass.tearDownClass
全部结束
  
----------------------------------------------------------------------
Ran 4 tests in 0.002s
  
OK
```
  
从结果中可以看出，在执行前执行了`__init__.py`中的setUp函数，在执行最后执行了teardown函数。

- with_setup修饰器
  
nose支持在每个用例前使用with_setup来自定义测试用例的setUp及tearDown功能，如下：
  
```
# coding=utf-8
  
from nose.tools import with_setup
  
def setup_func():
    print("set up test fixtures")
  
def teardown_func():
    print("tear down test fixtures")
  
@with_setup(setup_func, teardown_func)
def test_1():
    print("test_1")
  
def test_2():
    print("test_2")
  
test_2.setup = setup_func
test_2.teardown = teardown_func
```
  
运行结果：
  
```
PS C:\Users\dell\Desktop\test\nose> nosetests -v -s test_case.test_case_3
全部开始
test_case.test_case_3.test_1 ... set up test fixtures
test_1
tear down test fixtures
ok
test_case.test_case_3.test_2 ... set up test fixtures
test_2
tear down test fixtures
ok
全部结束
  
----------------------------------------------------------------------
Ran 2 tests in 0.002s
  
OK
```
  
除了`with_setup`的方法`@with_setup(setup_func, teardown_func)`，还可以这样写
  
```
test_2.setup = setup_func
test_2.teardown = teardown_func
```

- **多文件执行nose**
  
如下，有三个可执行的文件
  
```
test_case
|--__init__.py
|--test_case_1.py
|--test_case_2.py
|--test_case_3.py
```
  
运行结果：
  
```
PS C:\Users\dell\Desktop\test\nose> nosetests -w test_case test_case_2
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s
  
OK
```

#### 4.2 **nose运行方式**

`unittest` 所支持的用例发现和执行能力，`nose` 均支持。 `nose` 支持用例自动（递归）发现：

默认发现当前目录下所有包含 `test` 的测试用例，但不包括以 `_` 开头的用例，使用 `nosetests` 命令，通过 `-w` 参数指定要自动发现的目录， `-m` 参数指定用例文件、目录、函数、类的名称模式（正则匹配），`nosetests -w project_directory "test_.+"`。

`nose` 也支持执行指定用例：

- 指定测试模块
  
  `nosetests test_case.test_case_1`

- 指定测试类
  
  `nosetests test_case.test_case_2:TestClass`

- 指定测试方法
  
  `nosetests test_case.test_case_2:TestClass.Testfunc1`

- 指定测试文件路径
  
  `nosetests C:/Users/dell/Desktop/test/nose/test_case/test_case_1.py`

- 指定测试文件路径+测试类或测试函数（这是 `unittest` 所不支持的）
  
  `nosetests C:/Users/dell/Desktop/test/nose/test_case/test_case_2.py:TestClass`
  
  `nosetests C:/Users/dell/Desktop/test/nose/test_case/test_case_2.py:TestClass.Testfunc1`
  
  `nosetests C:/Users/dell/Desktop/test/nose/test_case/test_case_1.py:test_task_1`

### 5. 子测试/测试生成器

`nose` 除了支持 `unittest` 中的 `TestCase.subTest`，还支持一种更为强大的子测试编写方式，也就是 `测试生成器（Test generators）`，通过 `yield` 实现。

在下面的示例中，定义一个 `test_evens` 测试函数，里面生成了 5 个子测试 `check_even`：

```python
def test_evens():
    for i in range(0, 5):
        yield check_even, i, i*3

def check_even(n, nn):
    assert n % 2 == 0 or nn % 2 == 0
```

此外，相较于 `unittest.TestCase.subTest` 多个子测试只能执行一次测试前置和清理，`nose`的 `测试生成器` 可以支持每个子测试执行一次测试前置和清理，如：

```python
def test_generator():
    # ...
    yield func, arg, arg # ...

@with_setup(setup_func, teardown_func)
def func(arg):
    assert something_about(arg)
```

如下是一个例子：

```
# coding=utf-8

def setUp():
    print('testSetUp')

def tearDown():
    print('testTearDown')

def test_evens():
    for i in range(0, 5):
        yield check_even, i, i*3

def check_even(n, nn):
    assert n % 2 == 0 or nn % 2 == 0
```

运行结果：

```
PS C:\Users\dell\Desktop\test\nose> nosetests -v -s test_case.test_case_5
全部开始
testSetUp
test_case.test_case_5.test_evens(0, 0) ... ok
test_case.test_case_5.test_evens(1, 3) ... FAIL
test_case.test_case_5.test_evens(2, 6) ... ok
test_case.test_case_5.test_evens(3, 9) ... FAIL
test_case.test_case_5.test_evens(4, 12) ... ok
testTearDown
全部结束

======================================================================
FAIL: test_case.test_case_5.test_evens(1, 3)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\program files\python38\lib\site-packages\nose-1.3.7-py3.8.egg\nose\case.py", line 197, in runTest
    self.test(*self.arg)
  File "C:\Users\dell\Desktop\test\nose\test_case\test_case_5.py", line 14, in check_even
    assert n % 2 == 0 or nn % 2 == 0
AssertionError

======================================================================
FAIL: test_case.test_case_5.test_evens(3, 9)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\program files\python38\lib\site-packages\nose-1.3.7-py3.8.egg\nose\case.py", line 197, in runTest
    self.test(*self.arg)
  File "C:\Users\dell\Desktop\test\nose\test_case\test_case_5.py", line 14, in check_even
    assert n % 2 == 0 or nn % 2 == 0
AssertionError

----------------------------------------------------------------------
Ran 5 tests in 0.003s

FAILED (failures=2)
```

### **6. nose的测试工具集**

nose.tools模块提供了一系列的小工具，包括测试执行时间、异常输出及unittest框架中所有的assert功能。

 为了使写用例更加容易，nose.tools提供了部分便利的功能函数，下面写几个常用的，如下：

#### 6.1 nose.tools.ok_(expr, msg=None)

标准的assert，例子如下：

```
from nose.tools import ok_

def test_lean_2():
    print "test_case_2"
    ok_(4==3,msg="Error")
```

运行结果如下：

```
PS C:\Users\dell\Desktop\test\nose> nosetests -v test_case.test_case_4:test_task_1
test_case.test_case_4.test_task_1 ... FAIL

======================================================================
FAIL: test_case.test_case_4.test_task_1
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\program files\python38\lib\site-packages\nose-1.3.7-py3.8.egg\nose\case.py", line 197, in runTest
    self.test(*self.arg)
  File "C:\Users\dell\Desktop\test\nose\test_case\test_case_4.py", line 7, in test_task_1
    ok_(4==3,msg="Error")
AssertionError: Error
-------------------- >> begin captured stdout << ---------------------
test_task_1

--------------------- >> end captured stdout << ----------------------

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

断言结果`AssertionError: Error`

#### 6.2 nose.tools.eq_(a, b, msg=None)

将参数a与b快速对比

```
from nose.tools import eq_

def test_task_2():
    eq_(5, 6, msg="Wrong")
```

运行结果如下：

```
PS C:\Users\dell\Desktop\test\nose> nosetests -v test_case.test_case_4:test_task_2
test_case.test_case_4.test_task_2 ... FAIL

======================================================================
FAIL: test_case.test_case_4.test_task_2
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\program files\python38\lib\site-packages\nose-1.3.7-py3.8.egg\nose\case.py", line 197, in runTest
    self.test(*self.arg)
  File "C:\Users\dell\Desktop\test\nose\test_case\test_case_4.py", line 10, in test_task_2
    eq_(5, 6, msg="Wrong")
AssertionError: Wrong

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

断言结果`AssertionError: Wrong`

#### 6.3 nose.tools.assert_in(member, container, msg=None)

代码如下：

```
from nose.tools import assert_in
def test_task_3():
    assert_in("aaa",'bbb',msg="test  in failed")
```

运行结果如下：

```
PS C:\Users\dell\Desktop\test\nose> nosetests -v test_case.test_case_4:test_task_3
test_case.test_case_4.test_task_3 ... FAIL

======================================================================
FAIL: test_case.test_case_4.test_task_3
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\program files\python38\lib\site-packages\nose-1.3.7-py3.8.egg\nose\case.py", line 197, in runTest
    self.test(*self.arg)
  File "C:\Users\dell\Desktop\test\nose\test_case\test_case_4.py", line 13, in test_task_3
    assert_in("aaa",'bbb',msg="test in failed")
AssertionError: 'aaa' not found in 'bbb' : test in failed

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

断言结果`AssertionError: 'aaa' not found in 'bbb' : test in failed`

#### 6.4 nose.tools.set_trace()

单步调试工具，在多个模块，大程序时这个功能好用。内部使用的是pdb.set_trace。

代码如下：

```
from nose.tools import assert_in
from nose.tools import set_trace

def test_task_4():
    set_trace()
    assert_in("aaa",'bbb',msg="test in failed")
```

结果如下：

```
PS C:\Users\dell\Desktop\test\nose> nosetests -v test_case.test_case_4:test_task_4
test_case.test_case_4.test_task_4 ... > c:\users\dell\desktop\test\nose\test_case\test_case_4.py(17)test_task_4()
-> assert_in("aaa",'bbb',msg="test in failed")
(Pdb) n
AssertionError: 'aaa' not found in 'bbb' : test in failed
> c:\users\dell\desktop\test\nose\test_case\test_case_4.py(17)test_task_4()
-> assert_in("aaa",'bbb',msg="test in failed")
(Pdb) c
FAIL

======================================================================
FAIL: test_case.test_case_4.test_task_4
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\program files\python38\lib\site-packages\nose-1.3.7-py3.8.egg\nose\case.py", line 197, in runTest
    self.test(*self.arg)
  File "C:\Users\dell\Desktop\test\nose\test_case\test_case_4.py", line 17, in test_task_4
    assert_in("aaa",'bbb',msg="test in failed")
AssertionError: 'aaa' not found in 'bbb' : test in failed

----------------------------------------------------------------------
Ran 1 test in 4.615s

FAILED (failures=1)
```

断言结果`AssertionError: 'aaa' not found in 'bbb' : test in failed`

下面是该工具的命令集

```
Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb
```

#### 6.5 nose.tools.timed(limit)

测试必须在设定的时间内（以秒为单位）完成 ，否则测试失败；代码如下：

```
from nose.tools import timed
import time

@timed(1)    
def test_lean_5():
    time.sleep(2)
```

测试结果如下：

```
PS C:\Users\dell\Desktop\test\nose> nosetests -v test_case.test_case_4:test_task_5
test_case.test_case_4.test_task_5 ... FAIL

======================================================================
FAIL: test_case.test_case_4.test_task_5
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:\program files\python38\lib\site-packages\nose-1.3.7-py3.8.egg\nose\case.py", line 197, in runTest
    self.test(*self.arg)
  File "c:\program files\python38\lib\site-packages\nose-1.3.7-py3.8.egg\nose\tools\nontrivial.py", line 100, in newfunc
    raise TimeExpired("Time limit (%s) exceeded" % limit)
nose.tools.nontrivial.TimeExpired: Time limit (1) exceeded

----------------------------------------------------------------------
Ran 1 test in 2.008s

FAILED (failures=1)
```

#### 6.6 nose.tools.*

nose.tools中还有很多assert的函数工具，不一一介绍了，列出表如下，需要的时候可以使用。

|函数|描述|
|:--:|:--:|
|assert_equal(first,second,msg=None)|两个对像对比，使用"=="操作对比|
|assert_not_equal(first,second,msg=None)|不相等|
|assert_true(expr,msg=None)|判定表达式是否为真|
|assert_false(expr,msg=None)|判定表达式是否为假|
|assert_is(expr1,expr2,msg=None)|expr1isexpr2|
|assert_is_not(expr1,expr2,msg=None)||
|assert_is_none(obj,msg=None)|为空|
|assert_is_not_none(obj,msg=None)|不为空|
|assert_in(member,container,msg=None)|merberincontainer判断|
|assert_not_in(member,container,msg=None)|不包含判断|
|assert_is_instance(obj,cls,msg=None)||
|assert_not_is_instance(obj,cls,msg=None)||
|assert_raises_regexp(expected_exception,expected_regexp,callable_obj=None,*args,**kwargs)||
|assert_almost_equal(first,second,places=None,msg=None,delta=None)||
|assert_greater(a,b,msg=None)||
|assert_greater_equal(a,b,msg=None)||
|assert_less(a,b,msg=None)||
|assert_less_equal(a,b,msg=None)||
|assert_regexp_matches(text,expected_regexp,msg=None)||
|assert_not_regexp_matches(text,unexpected_regexp,msg=None)||
|assert_items_equal(expected_seq,actual_seq,msg=None)||
|assert_dict_contains_subset(expected,actual,msg=None)||
|assert_multi_line_equal(first,second,msg=None)||
|assert_sequence_equal(seq1,seq2,msg=None,seq_type=None)||
|assert_list_equal(list1,list2,msg=None)||
|assert_tuple_equal(tuple1,tuple2,msg=None)||
|assert_set_equal(set1,set2,msg=None)||
|assert_dict_equal(d1,d2,msg=None)||

### 7. 插件

`nose` 相较于 `unittest` 一个最大的优势就是插件体系，自带了很多有用的插件，也有丰富的第三方插件。这样就能做更多的事情。

其中，自带插件如下：

- [AllModules](https://nose.readthedocs.io/en/latest/plugins/allmodules.html)：在所有模块中收集用例。
- [Attrib](https://nose.readthedocs.io/en/latest/plugins/attrib.html)：给用例打标签，并可运行含指定标签的用例
- [Capture](https://nose.readthedocs.io/en/latest/plugins/capture.html)：捕获用例的标准输出
- [Collect](https://nose.readthedocs.io/en/latest/plugins/collect.html)：快速收集用例
- [Cover](https://nose.readthedocs.io/en/latest/plugins/cover.html)：统计代码覆盖率
- [Debug](https://nose.readthedocs.io/en/latest/plugins/debug.html)：用例失败时进入 pdb 调试
- [Deprecated](https://nose.readthedocs.io/en/latest/plugins/deprecated.html)：标记用例为弃用
- [Doctests](https://nose.readthedocs.io/en/latest/plugins/deprecated.html)：运行文档用例
- [Failure Detail](https://nose.readthedocs.io/en/latest/plugins/failuredetail.html)：断言失败时提供上下文信息
- [Isolate](https://nose.readthedocs.io/en/latest/plugins/isolate.html)：保护用例避免受一些副作用的影响
- [Logcapture](https://nose.readthedocs.io/en/latest/plugins/logcapture.html)：捕捉 logging 输出
- [Multiprocess](https://nose.readthedocs.io/en/latest/plugins/multiprocess.html)：并行执行用例
- [Prof](https://nose.readthedocs.io/en/latest/plugins/prof.html)：使用热点分析器进行分析
- [Skip](https://nose.readthedocs.io/en/latest/plugins/skip.html)：标记用例为跳过
- [Testid](https://nose.readthedocs.io/en/latest/plugins/testid.html)：为输出的每个用例名称添加测试 ID
- [Xunit](https://nose.readthedocs.io/en/latest/plugins/xunit.html)：以 xunit 格式输出测试结果

还有很多第三方库，如用来生成 HTML 格式测试报告的 [nose-htmloutput](https://github.com/ionelmc/nose-htmloutput) 等，这里不再赘述。

 `nose` 得益于丰富的插件生态，当 `nose` 本身不能够完全满足我们的测试需求时，可以通过安装插件，并在 `nosetests` 命令行指定该插件所提供的特定参数即可非常容易的使用插件。 相较于 `unittest`，就能省去很多自己开发额外测试逻辑的精力。
