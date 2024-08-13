title: tkinter教程
date: 2022-11-14
category: 技术
tag: python,tkinter

[TOC]

### Tkinter简介

tkinter（Tk interface）是 Python 的标准 GUI 库，支持跨平台的 GUI 程序开发。tkinter 适合小型的 GUI 程序编写，也特别适合初学者学习 GUI 编程。


### Tkinter用法详解

一个最简单的 Tkinter 程序至少应包含以下四个部分：

- 导入 tkinter 模块
- 创建主窗口，也称 root 窗口（即根窗口）
- 添加人机交互控件，同时编写相应的事件函数
- 通过主循环（mainloop）来显示主窗口
  
以下是一个简单的例子： 

```
# coding=utf-8
 
import tkinter as tk
 
root_window =tk.Tk()
# 设置窗口title
root_window.title('我的第一个Tkinter程序')
# 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
root_window.geometry('450x300')
# 更改左上角窗口的的icon图标
root_window.iconbitmap('favicon.ico')
# 设置主窗口的背景颜色,颜色值可以是英文单词，或者颜色值的16进制数,除此之外还可以使用Tk内置的颜色常量
root_window["background"] = "#C9C9C9"
# 添加文本内,设置字体的前景色和背景色，和字体类型、大小
text=tk.Label(root_window,text="破污噗，欢迎您",bg="yellow",fg="red",font=('Times', 20, 'bold italic'))
# 将文本内容放置在主窗口内
text.pack()
# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
button=tk.Button(root_window,text="关闭",command=root_window.quit)
# 将按钮放置在主窗口内
button.pack(side="bottom")
#进入主循环，显示主窗口
root_window.mainloop()
```

### 常用控件和属性

#### 控件类型

下表列出了 Tkinter 中常用的控件：

|控件类型|控件名称|控件作用|
|--|--|--|
|Button|按钮|点击按钮时触发/执行一些事件（函数）|
|Canvas|画布|提供绘制图，比如直线、矩形、多边形等|
|Checkbutton|复选框|多项选择按钮，用于在程序中提供多项选择框|
|Entry|文本框输入框|用于接收单行文本输入|
|Frame|框架（容器）控件|定义一个窗体（根窗口也是一个窗体），用于承载其他控件，即作为其他控件的容器|
|Lable|标签控件|用于显示单行文本或者图片|
|LableFrame|容器控件|一个简单的容器控件，常用于复杂的窗口布局。|
|Listbox|列表框控件|以列表的形式显示文本|
|Menu|菜单控件|菜单组件（下拉菜单和弹出菜单）|
|Menubutton|菜单按钮控件|用于显示菜单项|
|Message|信息控件|用于显示多行不可编辑的文本，与 Label控件类似，增加了自动分行的功能|
|messageBox|消息框控件|定义与用户交互的消息对话框|
|OptionMenu|选项菜单|下拉菜单|
|PanedWindow|窗口布局管理组件|为组件提供一个框架，允许用户自己划分窗口空间|
|Radiobutton|单选框|单项选择按钮，只允许从多个选项中选择一项|
|Scale|进度条控件|定义一个线性“滑块”用来控制范围，可以设定起始值和结束值，并显示当前位置的精确值|
|Spinbox|高级输入框|Entry 控件的升级版，可以通过该组件的上、下箭头选择不同的值|
|Scrollbar|滚动条|默认垂直方向，鼠标拖动改变数值，可以和 Text、Listbox、Canvas等控件配合使用|
|Text|多行文本框|接收或输出多行文本内容|
|Toplevel|子窗口|在创建一个独立于主窗口之外的子窗口，位于主窗口的上一层，可作为其他控件的容器|

#### 控件基本属性

|属性名称|说明|
|--|--|
|anchor|定义控件或者文字信息在窗口内的位置|
|bg|bg 是 background 的缩写，用来定义控件的背景颜色，参数值可以颜色的十六进制数，或者颜色英文单词|
|bitmap|定义显示在控件内的位图文件|
|borderwidth|定于控件的边框宽度，单位是像素|
|command|该参数用于执行事件函数，比如单击按钮时执行特定的动作，可将执行用户自定义的函数|
|cursor|当鼠标指针移动到控件上时，定义鼠标指针的类型，字符换格式，参数值有 crosshair（十字光标）watch（待加载圆圈）plus（加号）arrow（箭头）等|
|font|若控件支持设置标题文字，就可以使用此属性来定义，它是一个数组格式的参数 (字体,大小，字体样式)|
|fg|fg 是 foreground 的缩写，用来定义控件的前景色，也就是字体的颜色|
|height|该参数值用来设置控件的高度，文本控件以字符的数目为高度（px），其他控件则以像素为单位|
|image|定义显示在控件内的图片文件|
|justify|定义多行文字的排列方式，此属性可以是 LEFT/CENTER/RIGHT|
|padx/pady|定义控件内的文字或者图片与控件边框之间的水平/垂直距离|
|relief|定义控件的边框样式，参数值为FLAT（平的）/RAISED（凸起的）/SUNKEN（凹陷的）/GROOVE（沟槽桩边缘）/RIDGE（脊状边缘）|
|text|定义控件的标题文字|
|state|控制控件是否处于可用状态，参数值默认为 NORMAL/DISABLED，默认为 NORMAL（正常的）|
|width|用于设置控件的宽度，使用方法与 height 相同| 

### 主窗口

#### 窗口常用方法

|函数|说明|
|--|--|
|window.title("my title")|接受一个字符串参数，为窗口起一个标题|
|window.resizable()|是否允许用户拉伸主窗口大小，默认为可更改，当设置为 resizable(0,0)或者resizable(False,False)时不可更改|
|window.geometry()|设定主窗口的大小以及位置，当参数值为 None 时表示获取窗口的大小和位置信息。|
|window.quit()|关闭当前窗口|
|window.update()|刷新当前窗口|
|window.mainloop()|设置窗口主循环，使窗口循环显示（一直显示，直到窗口被关闭）|
|window.iconbitmap()|设置窗口左上角的图标（图标是.ico文件类型）|
|window.config(background ="red")|设置窗口的背景色为红色，也可以接受 16 进制的颜色值|
|window.minsize(50,50)|设置窗口被允许调整的最小范围，即宽和高各50|
|window.maxsize(400,400)|设置窗口被允许调整的最大范围，即宽和高各400|
|window.attributes("-alpha",0.5)|用来设置窗口的一些属性，比如透明度（-alpha）、是否置顶（-topmost）即将主屏置于其他图标之上、是否全屏（-fullscreen）全屏显示等|
|window.state("normal")|用来设置窗口的显示状态，参数值 normal（正常显示），icon（最小化），zoomed（最大化），|
|window.withdraw()|用来隐藏主窗口，但不会销毁窗口。|
|window.iconify()|设置窗口最小化|
|window.deiconify()|将窗口从隐藏状态还原|
|window.winfo_screenwidth()|
|window.winfo_screenheight()|获取电脑屏幕的分辨率（尺寸）|
|window.winfo_width()|
|window.winfo_height() |获取窗口的大小，同样也适用于其他控件，但是使用前需要使用 window.update() 刷新屏幕，否则返回值为1|
|window.protocol("协议名",回调函数)|启用协议处理机制，常用协议有 WN_DELETE_WINDOW，当用户点击关闭窗口时，窗口不会关闭，而是触发回调函数。|

下面是一个简单地例子：
```
import tkinter as tk
 
window =tk.Tk()
#设置窗口title
window.title('破污噗')
#设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
window.geometry('450x300')
# 获取电脑屏幕的大小
print("电脑的分辨率是%dx%d"%(window.winfo_screenwidth(),window.winfo_screenheight()))
# 要求窗口的大小，必须先刷新一下屏幕
window.update()
print("窗口的分辨率是%dx%d"%(window.winfo_width(),window.winfo_height()))
# 如使用该函数则窗口不能被拉伸
# window.resizable(0,0)
# 改变背景颜色
window.config(background="#6fb765")
# 设置窗口处于顶层
window.attributes('-topmost',True)
# 设置窗口的透明度
window.attributes('-alpha',1)
# 设置窗口被允许最大调整的范围，与resizble()冲突
window.maxsize(600,600)
# 设置窗口被允许最小调整的范围，与resizble()冲突
window.minsize(50,50)
#更改左上角窗口的的icon图标,加载C语言中文网logo标
window.iconbitmap('favicon.ico')
#添加文本内容,并对字体添加相应的格式 font(字体,字号,"字体类型")
text=tk.Label(window,text="亲爱的读者,你好~",bg="yellow",fg="red",font=('Times', 15, 'bold italic underline'))
#将文本内容放置在主窗口内
text.pack()
# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
button=tk.Button(window,text="关闭",command=window.quit)
# 将按钮放置在主窗口内
button.pack(side="bottom")
#进入主循环，显示主窗口
window.mainloop()

程序输出结果：

电脑的分辨率是1536x864
窗口的分辨率是450x300
```

#### 设置窗的位置

通过窗口对象的 geometry() 方法即可改变主窗口的位置，其语法格式如下： 

`geometry('450x400+300+200')`

上述代码表示，设置主窗口的宽度为 450，高度为 400，同时窗口距离左边屏幕的距离为 300（以像素为单位），距离屏幕顶部的距离为 200，这里我们将带“+”的参数值称为“位置参数”，当然，您也可以将它们设置为负数，如下所示：

`geometry('+-1500+-2000')`

当设置了一个超过屏幕的负参数值时，主窗口会被移动至“屏幕之外”，此时就看不到主窗口了，这也是隐藏窗口的一种方法。

### Label标签控件

Label（标签）控件，主要用来显示窗口中的文本或者图像，并且不同的 Lable（标签）允许设置各自不同的背景图片。下面对 Label（标签）的常用属性做简单介绍：

|属性名称|说明|
|--|--|
|anchor|控制文本（或图像）在 Label 中显示的位置（方位），通过方位的英文字符串缩写（n、ne、e、se、s、sw、w、nw、center）实现定位，默认为居中（center）|
|bg|用来设置背景色|
|bd|即 borderwidth 用来指定 Label 控件的边框宽度，单位为像素，默认为 2 个像素|
|bitmap|指定显示在 Label 控件上的位图，若指定了 image 参数，则该参数会被忽略|
|compound|控制 Lable 中文本和图像的混合模式，若选项设置为 CENTER，则文本显示在图像上，如果将选项设置为 BOTTOM、LEFT、RIGHT、TOP，则图像显示在文本旁边。|
|cursor|指定当鼠标在 Label 上掠过的时候，鼠标的的显示样式，参数值为 arrow、circle、cross、plus|
|disableforeground|指定当 Label 设置为不可用状态的时候前景色的颜色|
|font|指定 Lable 中文本的 (字体,大小,样式）元组参数格式，一个 Lable 只能设置一种字体|
|fg|设置 Label 的前景色|
|height/width|设置 Lable 的高度/宽度，如果 Lable 显示的是文本，那么单位是文本单元，如果 Label 显示的是图像，那么单位就是像素，如果不设置，Label 会自动根据内容来计算出标签的高度|
|highlightbackground|当 Label 没有获得焦点的时候高亮边框的颜色，系统的默认是标准背景色|
|highlightcolor|指定当 Lable 获得焦点的话时候高亮边框的颜色，系统默认为0，不带高亮边框|
|image|指定 Label 显示的图片，一般是 PhotoImage、BitmapImage 的对象|
|justify|表示多行文本的对齐方式，参数值为 left、right、center，注意文本的位置取决于 anchor 选项|
|padx/pady|padx 指定 Label 水平方向上的间距（即内容和边框间），pady 指定 Lable 水平方向上的间距（内容和边框间的距离）|
|relief|指定边框样式，默认值是 "flat"，其他参数值有 "groove"、"raised"、"ridge"、"solid"或者"sunken"|
|state|该参数用来指定 Lable 的状态，默认值为"normal"（正常状态），其他可选参数值有"active"和"disabled"|
|takefocus|默认值为False，如果是 True，表示该标签接受输入焦点|
|text|用来指定 Lable 显示的文本，注意文本内可以包含换行符|
|underline|给指定的字符添加下划线，默认值为 -1 表示不添加，当设置为 1 时，表示给第二个文本字符添加下划线。|
|wraplength|将 Label 显示的文本分行，该参数指定了分行后每一行的长度，默认值为 0|

下面是一个简单的例子：

```
import tkinter as tk
win = tk.Tk()
win.title("破污噗")
win.geometry('400x200')
win.iconbitmap('favicon.ico')
# 若内容是文字则以字符为单位，图像则以像素为单位
label = tk.Label(win, text="网址：www.baidu.com",font=('宋体',20, 'bold italic'),bg="#7CCD7C",
                 # 设置标签内容区大小
                 width=30,height=5,
                 # 设置填充区距离、边框宽度和其样式（凹陷式）
                 padx=10, pady=15, borderwidth=10, relief="sunken")
label.pack()
win.mainloop()
```

#### 标签添加背景图

下面是一个简单的例子： 

```
import tkinter as  tk
 
win = tk.Tk()
win.title("破污噗")
win.iconbitmap('favicon.ico')
 
#显示图片
photo = tk.PhotoImage(file = 'pic.png')
# 将图片放在主窗口的右边
lab =tk.Label(win,image=photo).pack(side="right")
 
# 显示文字，设置文本格式
text = "小姐姐,\n"\
       "今天天气不错,\n "\
       "出来吃个饭吧~"
lab_text =tk.Label(win,text=text,fg ='#7CCD7C',font=('微软雅黑',15,'italic'),justify='left',padx=10).pack(side='left')
win.mainloop()
```

### Message控件

Message 控件与 Label 控件的功能类似，它主要用来显示多行不可编辑的文本信息，与 Label 的不同之处在于该控件增加了自动分行的功能。下面对它做简单的介绍，示例如下：

```
from tkinter import *
#创建主窗口
win = Tk()
win.config(bg='#8DB6CD')
win.title("破污噗")
win.geometry('400x300')
win.iconbitmap('favicon.ico')
txt = "小姐姐，今天天气不错，出来吃个饭吧~"
msg = Message (win, text=txt,width =60,font=('微软雅黑',10,'bold'))
msg .pack(side=LEFT)
#开始程序循环
win .mainloop ()
```

### Button按钮控件 

Button 控件通过用户点击按钮的行为来执行回调函数，是 Button 控件的主要功用。它可以包含文本、图像、位图，并通过command参数回调函数。

#### Button 控件的常用属性

|属性|说明|
|--|--|
|anchor|控制文本所在的位置，默认为中心位置（CENTER）|
|activebackground|当鼠标放在按钮上时候，按钮的背景颜色|
|activeforeground|当鼠标放在按钮上时候，按钮的前景色|
|bd|按钮边框的大小，默认为 2 个像素|
|bg|按钮的背景色|
|command|用来执行按钮关联的回调函数。当按钮被点击时，执行该函数|
|fg|按钮的前景色|
|font|按钮文本的字体样样式|
|height|按钮的高度|
|highlightcolor|按钮控件高亮处要显示的颜色|
|image|按钮上要显示的图片|
|justify|按钮显示多行文本时，用来指定文本的对齐方式，参数值有 LEFT/RIGHT/CENTER|
|padx/pady|padx 指定 x 轴（水平方向）的间距大小，pady 则表示 y轴（垂直方向）的间距大小|
|ipadx/ipady|ipadx 指标签文字与标签容器之间的横向距离；ipady 则表示标签文字与标签容器之间的纵向距离|
|state|设置按钮的可用状态，可选参数有NORMAL/ACTIVE/DISABLED，默认为 NORMAL|
|text|按钮控件要显示的文本|

下面是一个简单的例子：

```
import tkinter as tk
from tkinter import messagebox
 
window = tk.Tk()
# 设置窗口的标题
window.title('破污噗')
# 设置并调整窗口的大小、位置
window.geometry('400x300+300+200')
# 当按钮被点击的时候执行click_button()函数
def click_button():
    # 使用消息对话框控件，showinfo()表示温馨提示
    messagebox.showinfo(title='温馨提示', message='恭喜你发现了宝藏文章！')
 
# 点击按钮时执行的函数
button = tk.Button(window,text='点击前往',bg='#7CCD7C',width=20, height=5,command=click_button).pack()
# 显示窗口
window.mainloop()
```

下面为 Button 控件添加一张背景图片，实现代码如下所示： 

```
import tkinter as tk
from tkinter import messagebox
 
window = tk.Tk()
# 设置窗口的标题
window.title('破污噗')
# 设置并调整窗口的大小、位置
window.geometry('400x300+300+200')
# 当按钮被点击的时候执行click_button()函数
def click_button():
    # 使用消息对话框控件，showinfo()表示温馨提示
    messagebox.showinfo(title='温馨提示', message='恭喜你发现了宝藏文章！')
# 创建图片对象
im = tk.PhotoImage(file='agree.png')
# 点击按钮时执行的函数
button = tk.Button(window,image=im,command=click_button).pack()
# 显示窗口
window.mainloop()
```

#### 扩展：按钮的布局

按钮在主窗口中的布局，通常使用 grid() 函数来完成，该函数以网格状的形式（即行和列）来管理窗口的布局。grid() 布局管理器提供了一个sticky参数，通过该参数可以设置按钮的方位，该参数默认将控件设置居中，其他参数值有 N/S/W/E（上/下/左/右），而且可以组合在一起使用，比如 NW/WE/SE/SW/NE 等，这与anchor参数控制文本的显示位置，有着异曲同工之妙。

```
下面看一组简单的示例：

import tkinter as tk
from tkinter import messagebox
 
win = tk.Tk()
win.title("破污噗")
win.iconbitmap('favicon.ico')
win.geometry('400x200+100+100')
win.resizable(0,0)
# 将俩个标签分别布置在第一行、第二行
tk.Label(win, text="账号：").grid(row=0)
tk.Label(win, text="密码：").grid(row=1)
# 创建输入框控件
e1 = tk.Entry(win)
# 以 * 的形式显示密码
e2 = tk.Entry(win,show='*')
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)
 
# 编写一个简单的回调函数
def login():
    messagebox.showinfo(title='登录成功',message='欢迎来到tkinter的世界~')
 
# 使用 grid()的函数来布局，并控制按钮的显示位置
tk.Button(win, text="登录", width=10, command=login).grid(row=3, column=0, sticky="w", padx=10, pady=5)
tk.Button(win, text="退出", width=10, command=win.quit).grid(row=3, column=1, sticky="e", padx=10, pady=5)
 
win.mainloop()
```

### Entry输入控件
Entry 控件的作用就是允许用户输入内容。基本语法格式如下：

#### 基本属性
Entry 控件除了具备一些共有属性之外，还有一些自身的特殊属性，如下表所示：

|属性名称|说明|
|--|--|
|exportselection|默认情况下，如果在输入框中选中文本会复制到粘贴板，如果要忽略这个功能，可以设置为 exportselection=0|
|selectbackground|选中文字时的背景颜色|
|selectforeground|选中文字时的前景色|
|show|指定文本框内容以何种样式的字符显示，比如密码可以将值设为 show="*"|
|textvariable|输入框内值，也称动态字符串，使用 StringVar() 对象来设置，而 text 为静态字符串对象|
|xscrollcommand|设置输入框内容滚动条，当输入的内容大于输入框的宽度时使用户|

#### 动态数据类型

上述表格中提及了 StringVar() 方法，和其同类的方法还有 BooleanVar()、DoubleVar()、IntVar() 方法，不难看出他们分别代表一种数据类型，即字符串、布尔值、浮点型、整型，这些方法并不属于 Python 内置方法，而是 Tkinter 特有的方法。在界面编程的过程中，有时我们需要“动态跟踪”一些变量值的变化，从而保证值的变换及时的反映到显示界面上，但是 Python 内置的数据类型是无法这一目的的，因此使用了 Tcl 内置的对象，我们把这些方法创建的数据类型称为“动态类型”，比如 StringVar() 创建的字符串，称为“动态字符串”。

#### 常用方法

|方法|说明|
|--|--|
|delete()|根据索引值删除输入框内的值|
|get()|获取输入框内的是|
|set()|设置输入框内的值|
|insert()|在指定的位置插入字符串|
|index()|返回指定的索引值|
|select_clear()|取消选中状态|
|select_adujst()|确保输入框中选中的范围包含 index 参数所指定的字符，选中指定索引和光标所在位置之前的字符|
|select_from (index)|设置一个新的选中范围，通过索引值 index 来设置|
|select_present()|返回输入框是否有处于选中状态的文本，如果有则返回 true，否则返回 false。|
|select_to()|选中指定索引与光标之间的所有值|
|select_range()|选中指定索引与光标之间的所有值，参数值为 start,end，要求 start 必须小于 end。|

注意：在 Entry 控件中，我们可以通过以下方式来指定字符的所在位置：

- 数字索引：表示从 0 开始的索引数字；
- "ANCHOE"：在存在字符的情况下，它对应第一个被选中的字符；
- "END"：对应已存在文本中的最后一个位置；
- "insert(index,'字符')：将字符插入到 index 指定的索引位置。

示例如下：
```
import tkinter as tk
 
win = tk.Tk()
# 设置主窗口
win.geometry('250x100')
win.title("破污噗")
win.iconbitmap('favicon.ico')
win.resizable(0,0)
# 创建输入框控件
entry1 = tk.Entry(win)
# 放置输入框，并设置位置
entry1.pack(padx=20, pady=20)
 
entry1.delete(0, "end")
# 插入默认文本
entry1.insert(0,'百度网址：www.baidu.com')
# 得到输入框字符串
print(entry1.get())
# 删除所有字符
# entry1.delete(0, tk.END)
win.mainloop()
```

#### Entry控件验证功能

Entry 控件也提供了对输入内容的验证功能，比如要求输入英文字母，你却输入了数字，这就属于非法输入，Entry 控件通过以下参数实现对内容的校验：

|参数|说明|
|--|--|
|validate|指定验证方式，字符串参数，参数值有 focus、focusin、focusout、key、all、none。 |
|validatecommand|指定用户自定义的验证函数，该函数只能返回 True 或者 Fasle|
|invalidcommand|当 validatecommand 指定的验证函数返回 False 时，可以使用该参数值再指定一个验证函数。|

下面对 validate 的参数值做简单的介绍：

|参数值|说明|
|--|--|
|focus|当 Entry 组件获得或失去焦点的时候验证|
|focusin|当 Entry 组件获得焦点的时候验证|
|focuson|当 Entry 组件失去焦点的时候验证|
|key|当输入框被编辑的时候验证|
|all|当出现上边任何一种情况的时候验证|
|none| 默认不启用验证功能，需要注意的是这里是字符串的 'none'|

下面看一组具体的运行示例：
```
import tkinter as tk
from tkinter import messagebox
 
win = tk.Tk()
# 设置主窗口
win.geometry('250x200+250+200')
win.title("破污噗")
win.iconbitmap('favicon.ico')
win.resizable(0,0)
 
# 创建验证函数
def check():
    if entry1.get() == "破污噗":
        messagebox.showinfo(title='温馨提示',message="输入正确")
        return True
    else:
        messagebox.showwarning(title='温馨提示',message="输入不正确")
        entry1.delete(0,tk.END)  # 删除输入框中的值
        return False
# 新建文本标签
labe1 = tk.Label(win,text="账号：")
labe2 = tk.Label(win,text="密码：")
labe1.grid(row=0)
labe2.grid(row=1)
# 创建动字符串
Dy_String = tk.StringVar()
# 使用验证参数 validata,参数值为 focusout 当失去焦点的时候，验证输入框内容是否正确
entry1 = tk.Entry(win,textvariable =Dy_String,validate ="focusout",validatecommand=check)
entry2 = tk.Entry(win)
 
# 对控件进行布局管理，放在文本标签的后面
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
 
win.mainloop()
```

### Spinbox 高级输入框

Spinbox 是 Entry 控件的升级版，它是 Tkinter 8.4 版本后新增的控件，该控件不仅允许用户直接输入内容，还支持用户使用微调选择器（即上下按钮调节器）来输入内容。在一般情况下，Spinbox 控件用于在固定的范围内选取一个值的时候使用。下面看一组简单的应用示例：

```
import tkinter as tk
 
root = tk.Tk()
root.title("破污噗")
root.geometry('300x200+300+300')
root.iconbitmap('favicon.ico')
# 如果是数字使用 from_和to参数，范围 0-20,并且与2步长递增或递减
w = tk.Spinbox(root,from_=0,to=20, increment=2,width = 15,bg='#9BCD9B')
w.pack()
# 显示窗口
root.mainloop()
```

#### 若不是数字，而是字符串形式的选项值，则采用values参数以元组的形式进行传参，如下所示：
```
import tkinter as tk
 
root = tk.Tk()
root.title("破污噗")
root.geometry('300x200+300+300')
root.iconbitmap('favicon.ico')
# 使用values传递即可
w = tk.Spinbox(root,values=['python','c++','java'])
w.pack()
# 显示窗口
root.mainloop()
```

### Text 文本控件

Text 控件用于显示和编辑多行文本。可以包含纯文本或者格式化文本，同时支持嵌入图片、显示超链接以及带有 CSS 格式的 HTML 等。

#### 基本属性

除了基本的共有属性之外，Text 控件还具备以下属性：

|属性|说明|
|--|--|
|autoseparators|默认为 True，表示执行撤销操作时是否自动插入一个“分隔符”（其作用是用于分隔操作记录）|
|exportselection|默认值为 True，表示被选中的文本是否可以被复制到剪切板，若是 False 则表示不允许。|
|insertbackground|设置插入光标的颜色，默认为 BLACK|
|insertborderwidth|设置插入光标的边框宽度，默认值为 0|
|insertofftime|该选项控制光标的闪烁频频率（灭的状态）|
|insertontime|该选项控制光标的闪烁频频率（亮的状态）|
|selectbackground|指定被选中文本的背景颜色，默认由系统决定|
|selectborderwidth|指定被选中文本的背景颜色，默认值是0|
|selectforeground|指定被选中文本的字体颜色，默认值由系统指定|
|setgrid|默认值是 False，指定一个布尔类型的值，确定是否启用网格控制|
|spacing1|指定 Text 控件文本块中每一行与上方的空白间隔，注意忽略自动换行，且默认值为 0。|
|spacing2|指定 Text 控件文本块中自动换行的各行间的空白间隔，忽略换行符，默认值为0|
|spacing3|指定 Text 组件文本中每一行与下方的空白间隔，忽略自动换行，默认值是 0|
|tabs|定制 Tag 所描述的文本块中 Tab 按键的功能，默认被定义为 8 个字符宽度，比如 tabs=('1c', '2c', '8c') 表示前 3 个 Tab 宽度分别为 1厘米，2厘米，8厘米。|
|undo|该参数默认为 False，表示关闭 Text 控件的“撤销”功能，若为 True 则表示开启|
|wrap|该参数用来设置当一行文本的长度超过 width 选项设置的宽度时，是否自动换行，参数值 none（不自动换行）、char（按字符自动换行）、word（按单词自动换行）|
|xscrollcommand|该参数与 Scrollbar 相关联，表示沿水平方向上下滑动|
|yscrollcommand|该参数与 Scrollbar 相关联，表示沿垂直方向左右滑动|

#### 基本方法

|方法|说明|
|--|--|
|bbox(index)|返回指定索引的字符的边界框，返回值是一个 4 元组，格式为(x,y,width,height)|
|edit_modified()|该方法用于查询和设置 modified 标志（该标标志用于追踪 Text 组件的内容是否发生变化）|
|edit_redo()|“恢复”上一次的“撤销”操作，如果设置 undo 选项为 False，则该方法无效。|
|edit_separator()|插入一个“分隔符”到存放操作记录的栈中，用于表示已经完成一次完整的操作，如果设置 undo 选项为 False，则该方法无效。|
|get(index1, index2)|返回特定位置的字符，或者一个范围内的文字。|
|image_cget(index, option)|返回 index 参数指定的嵌入 image 对象的 option 选项的值，如果给定的位置没有嵌入 image 对象，则抛出 TclError 异常|
|image_create()|在 index 参数指定的位置嵌入一个 image 对象，该 image 对象必须是 Tkinter 的 PhotoImage 或 BitmapImage 实例。|
|insert(index, text)|在 index 参数指定的位置插入字符串，第一个参数也可以设置为 INSERT，表示在光标处插入，END 表示在末尾处插入。|
|delete(startindex [, endindex])|删除特定位置的字符，或者一个范围内的文字。|
|see(index)|如果指定索引位置的文字是可见的，则返回 True，否则返回 False。|

下面来一个小案例：

```
from tkinter import *
 
win = Tk()
win.title("破污噗")
win.iconbitmap('favicon.ico')
win.geometry('400x300')
# 创建一个文本控件
# width 一行可见的字符数；height 显示的行数
text = Text(win, width=50, height=20, undo=True, autoseparators=False)
text.grid()
# INSERT 光标处插入；END 末尾处插入
text.insert(INSERT, '恭喜你，发现了宝藏文章！')
# 定义撤销和恢复方法，调用edit_undo()和 edit_redo()方法
def backout():
    text.edit_undo()
def regain():
    text.edit_redo()
# 定义撤销和恢复按钮
Button(win,text = '撤销',command = backout).grid(row=3, column=0, sticky="w", padx=10, pady=5)
Button(win,text = '恢复',command = regain).grid(row=3, column=0, sticky="e", padx=10, pady=5)
win.mainloop()
```

### 列表框(ListBox)和组合框(Combobox)

列表框（Listbox）和复选框（Combobox）是 Tkinter 中两个控件，由于其非常相似，所有将它们放在一起进行介绍。 

#### Listbox控件

Listbox，列表框中的选项可以是多个条目，也可以是单个唯一条目，但常用于多个条目。下面对列表框控件（Listbox）的常用方法做简单的介绍：

|方法|说明|
|--|--|
|activate(index)|将给定索引号对应的选项激活，即文本下方画一条下划线|
|bbox(index)|返回给定索引号对应的选项的边框，返回值是一个以像素为单位的 4 元祖表示边框：(xoffset, yoffset, width, height)， xoffset 和 yoffset 表示距离左上角的偏移位置|
|curselection()|返回一个元组，包含被选中的选项序号（从 0 开始）|
|delete(first, last=None)| 删除参数 first 到 last 范围内（包含 first 和 last）的所有选项|
|get(first, last=None)|返回一个元组，包含参数 first 到 last 范围内（包含 first 和 last）的所有选项的文本|
|index(index)|返回与 index 参数相应选项的序号|
|itemcget(index, option)|获得 index 参数指定的项目对应的选项（由 option 参数指定）|
|itemconfig(index, **options)|设置 index 参数指定的项目对应的选项（由可变参数 **option 指定）|
|nearest(y)|返回与给定参数 y 在垂直坐标上最接近的项目的序号|
|selection_set(first, last=None)|设置参数 first 到 last 范围内（包含 first 和 last）选项为选中状态，使用 selection_includes(序号) 可以判断选项是否被选中。 |
|size()|返回 Listbox 组件中选项的数量|
|xview(*args)|该方法用于在水平方向上滚动 Listbox 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现。 如果第一个参数是 "moveto"，则第二个参数表示滚动到指定的位置：0.0 表示最左端，1.0 表示最右端；如果第一个参数是 "scroll"，则第二个参数表示滚动的数量，第三个参数表示滚动的单位（可以是 "units" 或 "pages"），例如：xview("scroll", 2, "pages")表示向右滚动二行。|
|yview(*args)|该方法用于在垂直方向上滚动 Listbox 组件的内容，一般通过绑定 Scollbar 组件的 command 选项来实现|

除了共有属性之外，列表框控件也有一些其他属性，如下表所示：

|属性|说明|
|--|--|
|listvariable|1. 指向一个 StringVar 类型的变量，该变量存放 Listbox 中所有的项目|
|1. 在 StringVar 类型的变量中，用空格分隔每个项目，例如 var.set("c c++ java python")|
|selectbackground|1. 指定当某个项目被选中的时候背景颜色，默认值由系统指定|
|selectborderwidth|1. 指定当某个项目被选中的时候边框的宽度|
|2. 默认是由 selectbackground 指定的颜色填充，没有边框|
|3. 如果设置了此选项，Listbox 的每一项会相应变大，被选中项为 "raised" 样式|
|selectforeground|1. 指定当某个项目被选中的时候文本颜色，默认值由系统指定|
|selectmode|1. 决定选择的模式，tk 提供了四种不同的选择模式，分别是："single"（单选）、"browse"（也是单选，但拖动鼠标或通过方向键可以直接改变选项）、"multiple"（多选）和 "extended"（也是多选，但需要同时按住 Shift 键或 Ctrl 键或拖拽鼠标实现），默认是 "browse"|
|setgrid|指定一个布尔类型的值，决定是否启用网格控制，默认值是 False|
|takefocus|指定该组件是否接受输入焦点（用户可以通过 tab 键将焦点转移上来），默认值是 True|
|xscrollcommand|为 Listbox 组件添加一条水平滚动条，将此选项与 Scrollbar 组件相关联即可|
|yscrollcommand|为 Listbox 组件添加一条垂直滚动条，将此选项与 Scrollbar 组件相关联即可|

下面是一个简单的例子：

```
# 创建一个列表控件，并增加相应的选项
from tkinter import *
# 创建主窗口
win = Tk()
win.title("破污噗")
win.geometry('400x200')
win.iconbitmap('favicon.ico')
# 创建列表选项
listbox1 =Listbox(win)
listbox1.pack()
# i表示索引值，item 表示值，根据索引值的位置依次插入
for i,item in enumerate(["C","C++","C#","Python","Java"]):
    listbox1.insert(i,item)
# 显示窗口
win.mainloop()
```

#### 增加滚动条和删除功能

下面为上述示例增加一个滚动条和选项的删除功能，如下所示：

```
from tkinter import *
# 创建主窗口
win = Tk()
win.title("破污噗")
win.geometry('400x180')
win.iconbitmap('favicon.ico')
# 创建滚动条
s = Scrollbar(win)
# 设置垂直滚动条显示的位置，使得滚动条，靠右侧；通过 fill 沿着 Y 轴填充
s.pack(side = RIGHT,fill = Y)
 
# 将 selectmode 设置为多选模式，并为Listbox控件添加滚动条
listbox1 = Listbox(win,selectmode = MULTIPLE,height =5, yscrollcommand = s.set)
# i 表示索引值，item 表示值，根据索引值的位置依次插入
for i,item in enumerate(range(1,50)):
    listbox1.insert(i,item)
listbox1.pack()
# 设置滚动条，使用 yview使其在垂直方向上滚动 Listbox 组件的内容，通过绑定 Scollbar 组件的 command 参数实现
s.config(command = listbox1.yview)
 
# 使用匿名函数,创建删除函数，点击删除按钮，会删除选项
bt = Button(win,text='删除',command = lambda x = listbox1:x.delete(ACTIVE))
# 将按钮放置在底部
bt.pack(side = BOTTOM)
# 显示窗口
win.mainloop()
```

#### StringVar() 添加列表选项

下面演示如何通过  StringVar() 方法动态地获取列表框中的选项，示例代码如下：

```
import tkinter as tk
from tkinter import messagebox
 
window = tk.Tk()
 
window.title("破污噗")
window.geometry('400x180')
window.iconbitmap('favicon.ico')
 
# 创建变量，用var1用来接收鼠标点击的具体选项内容
var1 = tk.StringVar()
l = tk.Label(window, bg='#B0B0B0', font=('微软雅黑', 15), width=20, textvariable=var1)
l.pack()
 
# 创建一个按钮的点击事件
def click_button():
    # 使用 curselection来选中文本
    try:
        val = lb.get(lb.curselection())
    # 设置label值
        var1.set(val)
    except Exception as e:
        e = '发现一个错误'
        messagebox.showwarning(e,'没有选择任何条目')
 
# 创建一个按钮并放置，点击按钮调用print_selection函数
b1 = tk.Button(window, text='获取当前选项', command=click_button)
b1.pack()
 
 
# 创建Listbox并为其添加内容
var2 = tk.StringVar()
var2.set(("C语言辅导班", "Python答疑辅导", "Java答疑辅导", "C++辅导"))
# 创建Listbox，通过 listvariable来传递变量
lb = tk.Listbox(window, listvariable=var2)
# 新建一个序列，然后将值循环添加到Listbox控件中
items = ["C", "Java", "Python", "C#", "Golang", "Runby"]
for i in items:
    lb.insert('end', i)  # 从最后一个位置开始加入值
lb.insert(0, '编程学习')  # 在第一个位置插入一段字符串
lb.delete(4)  # 删除第2个位置处的索引
lb.pack()
 
#主窗显示
window.mainloop()
```

#### Combobox控件

Combobox 控件，就是下拉菜单控件。包含在tkinter.ttk子模块中，想使用 Combobox 控件，需要导入包`from tkinter import ttk`。

Combobox 控件在形式虽然与列表控件存在不同，但它们的本质是相同，因此属性和方法是通用的。对于 Combobox 控件而言，它常用的方法有两个，分别是 get() 和 current()，前者表示获取当前选中选项的内容，后者表示获取选中选项的索引值。下面通过一组简单的示例进一步了解 Combobox 控件，示例代码如下：

```
import tkinter
from tkinter import ttk # 导入ttk模块，下拉菜单控件位于ttk子模块中
 
# 创建窗口
win = tkinter.Tk()
win.title("破污噗")
win.iconbitmap('favicon.ico')
win.geometry('400x250')
win.resizable(0,0)
# 创建下拉菜单
cbox = ttk.Combobox(win)
# 使用 grid() 来控制控件的位置
cbox.grid(row = 1, sticky="NW")
# 设置下拉菜单中的值
cbox['value'] = ('C','C#','Go','Python','Java')
 
#通过 current() 设置下拉菜单选项的默认值
cbox.current(3)
 
# 编写回调函数，绑定执行事件,向文本插入选中文本
def func(event):
    text.insert('insert',cbox.get()+"\n")
# 绑定下拉菜单事件
cbox.bind("<<ComboboxSelected>>",func)
# 新建文本框
text = tkinter.Text(win)
# 布局
text.grid(pady = 5)
win.mainloop()
```

### 单选框(Radiobutton)和多选框按钮(Checkbutton)

#### Radiobutton单选框按钮控件

单选框按钮控件（Radiobutton），允许用户选择具体的选项值，仅允许用户选择单一的选项值。Radiobutton 控件通常都是成组出现的，所有控件都使用相同的变量。Radiobutton 可以包含文本或图像，每一个按钮都可以与一个 Python 函数相关联。当按钮被按下时，对应的函数会被执行。这里需要注意的是，单选按钮控件仅能显示单一字体的文本，但文本可以跨越多行，除此之外，您还可以为个别的字符添加下划线。

Radiobutton 除常用的共有属性之外，还具有一些其他属性，如下表所示：

|属性|说明|
|--|--|
|activebackground|设置当 Radiobutton 处于活动状态（通过 state 选项设置状态）的背景色，默认值由系统指定|
|activeforeground|设置当 Radiobutton 处于活动状态（通过 state 选项设置状态）的前景色，默认值由系统指定|
|compound|1. 默认值为 None，控制 Radiobutton 中文本和图像的混合模式，默认情况下，如果有指定位图或图片，则不显示文本<br />2. 如果该选项设置为 "center"，文本显示在图像上（文本重叠图像）<br />3. 设置为 "bottom"，"left"，"right" 或 "top"，那么图像显示在文本的旁边，比如如"bottom"，则显示图像在文本的下方。|
|disabledforeground|指定当 Radiobutton 不可用的时的前景色颜色，默认由系统指定|
|indicatoron|1. 该参数表示选项前面的小圆圈是否被绘制，默认为 True，即绘制；<br />2. 如果设置为 False，则会改变单选按钮的样式，当点击时按钮会变成 "sunken"（凹陷），再次点击变为 "raised"（凸起）|
|selectcolor|设置当 Radiobutton 为选中状态的时候显示的图片；如果没有指定 image 选项，该选项被忽略|
|takefocus|如果是 True，该组件接受输入焦点，默认为 False|
|variable|表示与 Radiobutton 控件关联的变量，注意同一组中的所有按钮的 variable 选项应该都指向同一个变量，通过将该变量与 value 选项值对比，可以判断用户选中了哪个按钮。|

Radiobutton 控件的常用方法如下所示：

|方法|说明|
|--|--|
|deselect()|取消该按钮的选中状态|
|flash()|刷新 Radiobutton 控件，该方法将重绘 Radiobutton控件若干次（即在"active" 和 "normal" 状态间切换）|
|invoke()|1. 调用 Radiobutton 中 command 参数指定的函数，并返回函数的返回值|
|2. 如果 Radiobutton 控件的 state(状态) 是 "disabled" （不可用）或没有指定 command 选项，则该方法无效|
|select()|将 Radiobutton 控件设置为选中状态|

Radiobutton 控件用来解决多选一的问题，它通常是成组出现的，下面看一组简答的示例：

```
import tkinter as tk
 
window = tk.Tk()
window.title("破污噗")
window.geometry('400x180')
window.iconbitmap('favicon.ico')
# IntVar() 用于处理整数类型的变量
v = tk.IntVar()
# 根据单选按钮的 value 值来选择相应的选项
v.set(0)
# 使用 variable 参数来关联 IntVar() 的变量 v
tk.Radiobutton(window, text="JAVA", fg='blue',font=('微软雅黑','12','bold'),variable=v, value=0).pack(anchor = 'w')
tk.Radiobutton(window, text="Python", variable=v, value=1).pack(anchor = 'w')
tk.Radiobutton(window, text="C++", variable=v, value=2).pack(anchor = 'w')
tk.Radiobutton(window, text="Go", variable=v, value=3).pack(anchor = 'w')
# 显示窗口
window.mainloop()
```

上述代码是比较直接的写法，虽然编码过程简单，但是从代码重构的角度来讲，它是比较冗余的，因此我们推荐下面这种写法，如下所示：

```
import tkinter as tk
 
window = tk.Tk()
window.title("破污噗")
window.geometry('400x180')
window.iconbitmap('favicon.ico')
 
site = [('美团外卖',1),
        ('饿了么外卖',2),
        ('美团闪购',3),
        ('艾奇外卖',4)]
 
# IntVar() 用于处理整数类型的变量
v = tk.IntVar()
# 重构后的写法，也非常简单易懂
for name, num in site:
    radio_button = tk.Radiobutton(window,text = name, variable = v,value =num)
    radio_button.pack(anchor ='w')
# 显示窗口
window.mainloop()
```

对上述代码稍作修改，当点击某一按钮时，获取选项的内容，代码如下：
```
import tkinter as tk
 
def select():
    dict = {1:'Python',2:'java',3:'c++',4:'Go'}
    strings = '您选择了' + dict.get(v.get()) + '，祝您学习愉快'
    lable.config(text = strings)
 
 
window = tk.Tk()
window.title("破污噗")
window.geometry('400x180')
window.iconbitmap('favicon.ico')
lable = tk.Label(window,font=('微软雅黑', '15','bold'),fg='#43CD80')
lable.pack(side ='bottom')
site = [('Python',1),
        ('java',2),
        ('c++',3),
        ('Go',4)]
 
# IntVar() 用于处理整数类型的变量
v = tk.IntVar()
for name, num in site:
    radio_button = tk.Radiobutton(window,text = name, variable = v,value =num,command = select,indicatoron = False)
    radio_button.pack(anchor ='w')
# 显示窗口
window.mainloop()
```

#### Checkbutton复选框控件

Checkbutton 控件是一种供用户选择相应条目的按钮控件，Checkbutton 允许用户同时选择多项，各个选项之间属于并列的关系。下面对它们做简单地介绍：

|属性|说明|
|--|--|
|text|显示的文本，使用 "\n" 来对文本进行换行。|
|variable|1. 和复选框按钮关联的变量，该变量值会随着用户选择行为来改变（选或不选），即在 onvalue 和 offvalue 设置值之间切换，这些操作由系统自动完成|
|1. 在默认情况下，variable 选项设置为 1 表示选中状态，反之则为 0，表示不选中。|
|onvalue|通过设置 onvalue 的值来自定义选中状态的值。|
|offvalue|通过设置 offvalue 的值来自定义未选中状态的值。|
|indicatoron|默认为 True，表示是否绘制用来选择的选项的小方块，当设置为 False 时，会改变原有按钮的样式，与单选按钮相同|
|selectcolor|选择框的颜色（即小方块的颜色），默认由系统指定|
|selectimage|设置当 Checkbutton 为选中状态的时候显示的图片，若如果没有指定 image 选项，该选项被忽略|
|textvariable|Checkbutton 显示 Tkinter 变量（通常是一个 StringVar 变量）的内容，如果变量被修改，Checkbutton 的文本会自动更新|
|wraplength|表示复选框文本应该被分成多少行，该选项指定每行的长度，单位是屏幕单元，默认值为 0|

下面看一组简单的示例，创建一组复选框控件，代码如下： 

```
from tkinter import *
win = Tk()
win.title("破污噗")
win.geometry('500x200')
win.resizable(0,0)
lb = Label(text='编程语言答疑辅导班',font=('微软雅黑', 18,'bold'),fg='#CD7054')
lb.pack()
win.iconbitmap('favicon.ico')
# 新建整型变量
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
# 设置三个复选框控件，使用variable参数来接收变量
check1 = Checkbutton(win, text="Python",font=('微软雅黑', 15,'bold'),variable = CheckVar1,onvalue=1,offvalue=0)
check2 = Checkbutton(win, text="C语言",font=('微软雅黑', 15,'bold'),variable = CheckVar2,onvalue=1,offvalue=0)
check3 = Checkbutton(win, text="Java",font=('微软雅黑', 15,'bold'),variable = CheckVar3,onvalue=1,offvalue=0)
# 选择第一个为默认选项
# check1.select ()
check1.pack(side = LEFT)
check2.pack(side = LEFT)
check3.pack(side = LEFT)
# 定义执行函数
def study():
    # 没有选择任何项目的情况下
    if (CheckVar1.get() == 0 and CheckVar2.get() == 0 and CheckVar3.get() == 0):
        s = '您还没选择任语言'
    else:
        s1 = "Python" if CheckVar1.get() == 1 else ""
        s2 = "C语言" if CheckVar2.get() == 1 else ""
        s3 = "Java" if CheckVar3.get() == 1 else ""
        s = "您选择了%s %s %s" % (s1, s2, s3)
     #设置标签lb2的字体
    lb2.config(text=s)
 
btn = Button(win,text="选好了",bg='#BEBEBE',command=study)
btn.pack(side = LEFT)
# 该标签，用来显示选择的文本
lb2 = Label(win,text='',bg ='#9BCD9B',font=('微软雅黑', 8,'bold'),width = 8,height=2)
lb2.pack(side = BOTTOM, fill = X)
 
# 显示窗口
win.mainloop()
```

复选框控件提供以下常用方法，如下表所示：

|方法|属性|
|--|--|
|desellect()|取消 Checkbutton 组件的选中状态，也就是设置 variable 为 offvalue|
|flash()|刷新 Checkbutton 组件，对其进行重绘操作，即将前景色与背景色互换从而产生闪烁的效果。|
|invoke()|1. 调用 Checkbutton 中 command 选项指定的函数或方法，并返回函数的返回值<br />2. 如果 Checkbutton 的state(状态)"disabled"是 （不可用）或没有指定 command 选项，则该方法无效|
|select()|将 Checkbutton 组件设置为选中状态，也就是设置 variable 为 onvalue|
|toggle()|改变复选框的状态，如果复选框现在状态是 on，就改成 off，反之亦然|

下面看一组简答的示例，如下所示：
```
from tkinter import *
win = Tk()
win.title("破污噗")
win.geometry('500x200')
win.resizable(0,0)
lb = Label(text='编程语言答疑辅导班',font=('微软雅黑', 18,'bold'),fg='#CD7054')
lb.pack()
win.iconbitmap('favicon.ico')
# 设置三个复选框控件，
check1 = Checkbutton(win, text="Python",font=('微软雅黑', 15,'bold'),onvalue=1,offvalue=0)
check2 = Checkbutton(win, text="C语言",font=('微软雅黑', 15,'bold'),onvalue=1,offvalue=0)
check3 = Checkbutton(win, text="Java",font=('微软雅黑', 15,'bold'),onvalue=1,offvalue=0)
# 将第一个 复选框按钮的 variable值，设置为 onvalue =1 ，表示选中状态
check1.select ()
# 取消了第一个复选框的选中状态
# check1.toggle()
check1.pack (side = LEFT)
check2.pack (side = LEFT)
check3.pack (side = LEFT)
# 显示窗口
win.mainloop()
```

### Scale控件

Scale 控件，即滑块控件或标尺控件，该控件可以创建一个类似于标尺式的滑动条对象，用户通过操作它可以直接设置相应的数值（刻度值)。

#### Scale 控件常用基本属性

|参数|说明|
|--|--|
|activebackground|指定当鼠标在上方飘过的时候滑块的背景颜色|
|bigincrement|1. 设置“大”增长量<br />2. 该选项设置增长量的大小<br />3. 默认值是 0，增长量为范围的 1/10|
|borderwidth|1. 指定边框宽度<br />2. 默认值是 2|
|command|1. 指定一个函数，每当滑块发生改变的时候都会自动调用该函数<br />2. 该函数有一个唯一的参数，就是最新的滑块位置<br />3. 如果滑块快速地移动，函数可能无法获得每一个位置，但一定会获得滑块停下时的最终位置|
|digits|1. 设置最多显示多少位数字<br />2. 补充注释：例如设置 from 选项为 0，to 选项为 20，digits 选项设置为 5，那么滑块的范围就是在 0.000 ~ 20.000 直接滑动<br />3. 默认值是 0（不开启）|
|font|1. 指定滑块左侧的 Label 和刻度的文字字体<br />2. 默认值由系统指定|
|from_|1. 设置滑块最顶（左）端的位置<br />2. 默认值是 0|
|highlightcolor|1. 指定当 Scale 获得焦点的时候高亮边框的颜色<br />2. 默认值由系统指定|
|label|1. 你可以在垂直的 Scale 组件的顶端右侧（水平的话是左端上方）显示一个文本标签<br />2. 默认值是不显示标签|
|length|1. Scale 组件的长度，默认值是 100 像素|
|orient|1. 设置 Scale 控件是水平放置（HORIZONTAL）还是垂直放置（VERTICAL）<br />2. 默认值是 VERTICAL（垂直放置）|
|repeatdelay|1. 该选项指定鼠标左键点击滚动条凹槽的响应时间<br />2. 默认值是 300（毫秒）|
|repeatinterval|1. 该选项指定鼠标左键紧按滚动条凹槽时的响应间隔<br />2. 默认值是 100（毫秒）|
|resolution|1. 指定 Scale 组件的分辨率（每点击一下移动的步长）示例： 比如 resolution 选项设置为 0.1 的话，那么每点击一下鼠标就是在 0.0 ~ 20.0 之间以 0.1 的步长移动<br />2. 该参数的默认值是 1|
|showvalue|1. 设置是否显示滑块旁边的数字<br />2. 默认值为 True|
|sliderlength|1. 设置滑块的长度<br />2. 默认值是 30 像素|
|state|1. 默认情况下 Scale 组件支持鼠标事件和键盘事件，可以通过设置该选项为 DISABLED 来禁用此功能<br />2. 默认值是 NORMAL|
|takefocus|1. 指定使用 Tab 键是否可以将焦点移动到该 Scale 组件上<br />2. 默认是开启的，可以通过将该选项设置为 False 避免焦点落在此组件上|
|tickinterval|1. 设置显示的刻度，如果设置一个值，那么就会按照该值的倍数显示刻度<br />2. 默认值是不显示刻度|
|to|1. 设置滑块最底（右）端的位置<br />2. 默认值是 100|
|troughcolor|1. 设置凹槽的颜色<br />2. 默认值由系统指定|
|variable|1. 指定一个与 Scale 组件相关联的 Tkinter 变量，该变量存放滑块最新的位置<br />2. 当滑块移动的时候，该变量的值也会发生相应的变化|
|width|1. 指定 Scale 组件的宽度<br />2. 默认值是 15 像素|

#### Scale 常用方法

|方法|说明|
|--|--|
|coords(value=None)|1. 获得当前滑块位置相对于 Scale 控件左上角位置的相对坐标，<br />2. 如果设置了 value 值，则返回当滑块位于该位置时与左上角的相对坐标|
|get()|获得当前滑块的位置（即当前数值），返回值可以为整型或者浮点型|
|identify(x, y)|返回一个字符串表示指定位置下的 Scale 控件|
|set(value)|设置 Scale 控件的值，即滑块的位置，默认为初始位置|

下面看一组简单的实例应用：创建一个 Scale 控件
```
from tkinter import *
# 创建主窗口
win =Tk()
win.title("控制管理界面")
win.iconbitmap('favicon.ico')
win.geometry('400x250')
# 添加一个 Scale 控件，默认垂直方向，步长设置为 5，长度为200，滑动块的大小为 50，最后使用label参数文本
s=Scale(win, from_ =100, to =0,resolution =5,length =200,sliderlength= 20,label ='音量控制' )
s.pack()
# 设置滑块的位置
s.set(value=15)
# 显示窗口
mainloop()
```

> 下面看一个稍微复杂点的应用示例，代码如下：

```
import tkinter as tk
 
window = tk.Tk()
window.title("购物车界面")
window.iconbitmap('favicon.ico')
window.geometry('450x200+450+250')
window.resizable(0,0)
# 创建一个文本标签
label = tk.Label(window, bg='#9FB6CD',width=18, text='')
label.grid(row =2)
# 创建执行函数
def select_price(value):
    label.config(text='您购买的数量是 ' + value)
# 创建 Scale控件
scale = tk.Scale(window,
             label='选择您要购买的数量',
             from_=1,
             to= 100,
             orient=tk.HORIZONTAL,   # 设置Scale控件平方向显示
             length=400,
             tickinterval=9,       # 设置刻度滑动条的间隔
             command=select_price)  # 调用执行函数，是数值显示在 Label控件中
scale.grid(row =1)
 
# 显示窗口
window.mainloop()
```

### Canvas画布控件

Canvas 控件具有两个功能，首先它可以用来绘制各种图形，比如弧形、线条、椭圆形、多边形和矩形等，其次 Canvas 控件还可以用来展示图片（包括位图），我们将这些绘制在画布控件上的图形，称之为“画布对象”。每一个画布对象都有一个“唯一身份ID”，这是 Tkinter 自动为其创建的，从而方便控制和操作这些画布对象。通过 Canvas 控件创建一个简单的图形编辑器，让用户可以达到自定义图形的目的，就像使用画笔在画布上绘画一样，可以绘制各式各样的形状，从而有更好的人机交互体验。

#### Canvas控件基本属性

|属性|方法|
|--|--|
|background(bg)|指定 Canvas 控件的背景颜色|
|borderwidth(bd)|指定 Canvas 控件的边框宽度|
|closeenough|1. 指定一个距离，当鼠标与画布对象的距离小于该值时，认为鼠标位于画布对象上<br />2. 该选项是一个浮点类型的值|
|confine|1. 指定 Canvas 控件是否允许滚动超出 scrollregion 选项设置的滚动范围，默认值为 True|
|selectbackground|指定当画布对象（即在 Canvas 画布上绘制的图形）被选中时的背景色，|
|selectborderwidth|指定当画布对象被选中时的边框宽度（选中边框）|
|selectforeground|指定当画布对象被选中时的前景色|
|state|设置 Canvas 的状态："normal" 或 "disabled"，默认值是 "normal"，注意，该值不会影响画布对象的状态|
|takefocus|指定使用 Tab 键可以将焦点移动到输入框中，默认为开启，将该选项设置为 False 避免焦点在此输入框中|
|width|指定 Canvas 的宽度，单位为像素|
|xscrollcommand|与 scrollbar（滚动条）控件相关联（沿着 x 轴水平方向）|
|xscrollincrement|1. 该选项指定 Canvas 水平滚动的“步长”<br />2. 例如 '3c' 表示 3 厘米，还可以选择的单位有 'i'（英寸），'m'（毫米）和 'p'（DPI，大约是 '1i' 等于 '72p'）<br />3. 默认为 0，表示可以水平滚动到任意位置|
|yscrollcommand|与 scrollbar 控件（滚动条）相关联（沿着 y 轴垂直方向）|
|yscrollincrement|1. 该选项指定 Canvas 垂直滚动的“步长”<br />2. 例如 '3c' 表示 3 厘米，还可以选择的单位有 'i'（英寸），'m'（毫米）和 'p'（DPI，大约是 '1i' 等于 '72p'）<br />3. 默认值是 0，表示可以垂直方向滚动到任意位置|

#### Canvas控件绘图常用方法

Cansvas 控件提供了一系列绘制几何图形的常用方法，下面对这些方法做简单介绍:

|方法|说明|
|--|--|
|create_line(x0, y0, x1, y1, ... , xn, yn, options)|1. 根据给定的坐标创建一条或者多条线段；<br />2. 参数 x0,y0,x1,y1,...,xn,yn 定义线条的坐标；<br />3. 参数 options 表示其他可选参数|
|create_oval(x0, y0, x1, y1, options)|1. 绘制一个圆形或椭圆形；<br />2. 参数 x0 与 y0 定义绘图区域的左上角坐标；参数 x1 与 y1 定义绘图区域的右下角坐标；<br />3. 参数 options 表示其他可选参数|
|create_polygon(x0, y0, x1, y1, ... , xn, yn, options)|1. 绘制一个至少三个点的多边形；<br />2. 参数 x0、y0、x1、y1、...、xn、yn 定义多边形的坐标；<br />3. 参数 options 表示其他可选参数|
|create_rectangle(x0, y0, x1, y1, options)|1. 绘制一个矩形；<br />2. 参数 x0 与 y0 定义矩形的左上角坐标；参数 x 与 y1 定义矩形的右下角坐标；<br />3. 参数 options 表示其他可选参数|
|create_text(x0, y0, text, options)|1. 绘制一个文字字符串。其中<br />2. 参数 x0 与 y0 定义文字字符串的左上角坐标，参数 text 定义文字字符串的文字；<br />3. 参数 options 表示其他可选参数|
|create_image(x, y, image)|1. 创建一个图片;<br />2. 参数 x 与 y 定义图片的左上角坐标；<br />3. 参数 image 定义图片的来源，必须是 tkinter 模块的 BitmapImage 类或 PhotoImage 类的实例变量。|
|create_bitmap(x, y, bitmap)|1. 创建一个位图；<br />2. 参数 x 与 y 定义位图的左上角坐标；<br />3. 参数 bitmap 定义位图的来源，参数值可以是 gray12、gray25、gray50、gray75、hourglass、error、questhead、info、warning 或 question，或者也可以直接使用 XBM（X Bitmap）类型的文件，此时需要在 XBM 文件名称前添加一个 @ 符号，例如 bitmap=@hello.xbm|
|create_arc(coord, start, extent, fill)|1. 绘制一个弧形；<br />2. 参数 coord 定义画弧形区块的左上角与右下角坐标；<br />3. 参数 start 定义画弧形区块的起始角度（逆时针方向）；<br />4. 参数 extent 定义画弧形区块的结束角度（逆时针方向）；<br />5. 参数 fill 定义填充弧形区块的颜色。|

注意：上述方法都会返回一个画布对象的唯一 ID。关于 options 参数，下面会通过一个示例对经常使用的参数做相关介绍。（但由于可选参数较多，并且每个方法中的参数作用大同小异，因此对它们不再逐一列举）

从上述表格不难看出，Canvas 控件采用了坐标系的方式来确定画布中的每一点。一般情况下，默认主窗口的左上角为坐标原点，这种坐标系被称作为“窗口坐标系”，但也会存在另外一种情况，即画布的大小可能大于主窗口，当发生这种情况的时，可以采用带滚动条的 Canvas 控件，此时会以画布的左上角为坐标原点，我们将这种坐标系称为“画布坐标系”。

#### 绘制直线

下面示例展示了如何在画布（Canvas控件）上绘制一条虚线和实线，代码如下：
```
from tkinter import *
root = Tk()
# 设置窗口的背景颜色以区别画布
root.config(bg='#87CEEB')
root.title("破污噗")
root.geometry('450x350')
root.iconbitmap('favicon.ico')
# 设置画布的背景颜色为白色
cv=Canvas(root,bg="white",width =300, height = 250)
# 将控件放置在主窗口中
cv.pack()
# 设置坐标点,此处可以元组的形式来设置坐标点
point=[(10,20),(20,30),(30,40),(40,100),(80,120),(150,90)]
# 创建画布，添加线条
# fill 参数指定填充的颜色，如果为空字符串，则表示透明
# dash 参数表示用来绘制虚线轮廓，元组参数，分别代表虚线中线段的长度和线段之间的间隔
# arrow 设线段的箭头样式，默认不带箭头，参数值 first 表示添加箭头带线段开始位置，last表示到末尾占位置，both表示两端均添加
# smooth 布尔值参数，表示是否以曲线的样式划线，默认为 False
# width 控制线宽
line1=cv.create_line(point,fill="purple",dash=(1,1),arrow=LAST,width=5)
line2=cv.create_line(point,fill="red",arrow=BOTH,smooth=TRUE,width=5)
# 移动其中一条线段，只需要更改其坐标就可以,使用 coords()方法移动曲线
cv.coords(line2,50,30,25,35,35,40,50,120,60,170,10,180)
# 显示窗口
root.mainloop()
```

上述示例中涉及了一部分参数，比如 fill、dash、arrow 等，下表对 create_line() 函数的相关参数做了简单介绍：

|属性|说明|
|--|--|
|activedash|当画布对象状态为 "active" 的时候，绘制虚线|
|activefill|当画布对象状态为 "active" 的时候，填充颜色|
|activestipple|当画布对象状态为 "active" 的时候，指定填充的位图|
|activewidth|当画布对象状态为 "active" 的时候，指定边框的宽度|
|arrow|1. 默认线段是不带箭头的，通过设置该选项添加箭头到线段中<br />2. "first" 表示添加箭头到线段开始的位置<br />3. "last" 表示添加箭头到线段结束的位置<br />4. "both" 表示两端均添加箭头|
|arrowshape|1. 用一个三元组来指定箭头的形状，默认值是 (8, 10, 3)，元组中的数值分别代表箭头中三条边的长度|
|capstyle|1. 指定线段两端的样式，默认值是 "butt"<br />2. 该选项的值可以是："butt"（线段的两段平切于起点和终点）、"projecting"（线段的两段在起点和终点的位置将 width 选项设置的长度分别延长一半）、"round"（线段的两段在起点和终点的位置将 width设置的长度分别延长一半，并以圆角进行绘制）|
|dash|绘制虚线，该选项值是一个整数元组，元组中的元素分别代表短线的长度和间隔，比如 (3, 5) 代表 3 个像素的短线和 5 个像素的间隔|
|dashoffset|指定虚线开始的偏移位置，比如 dash=(5, 1, 2, 1)，dashoffset=3，则从 2 开始画虚线|
|disableddash|当画布对象状态为 "disabled" 的时候，绘制虚线|
|disabledfill|当画布对象状态为 "disabled" 的时候，填充颜色|
|disabledstipple|当画布对象状态为 "disabled" 的时候，指定填充的位图|
|disabledwidth|当画布对象状态为 "disabled" 的时候，指定边框的宽度|
|fill|1. 指定填充的颜色，空字符串表示透明|
|joinstyle|1. 指定当绘制两个相邻线段之间时接口的样式，默认为 "round"<br />2. 该选项的值可以是：|
|"round"（以连接点为圆心，1/2 width 选项设置的长度为半径来绘制圆角）|
|"bevel"（在连接点处将两线段的夹角做平切操作）|
|"miter"（沿着两线段的夹角延伸至一个点）|
|offset|指定当点画模式时填充位图的偏移|
|smooth|默认值为 False，若设置为 True，表示将以曲线的样式代替所绘线段|
|splinesteps|当绘制曲线的时，该选项指定由多少条折线来构成曲线，默认值是 12，这里需要注意，只有当 smooth 选项为 True 时该选项才会生效。|
|state|指定该画布对象的状态，默认值为 "normal"，参数值有 "normal"，"disabled"（不可用）和 "hidden"（隐藏）三种状态。|
|stipple|指定一个位图进行填充，默认值为空字符串，表示实心|
|tags|为创建的画布对象添加标签|
|width|指定边框的宽度|

对于扇形、矩形、三角形、圆形等，这些封闭式图形，它们由轮廓线和填充颜色两部分组成。在绘制这些图形时相关函数的可选参数与上述表格也存在略微差异，下面以绘制扇形的 create_arc() 函数为例做简单的介绍：

|属性|方法|
|--|--|
|activedash|当画布对象状态为 "active" 的时候，绘制虚线|
|activefill|当画布对象状态为 "active" 的时候，填充颜色|
|activeoutline|当画布对象状态为 "active" 的时候，绘制轮廓线|
|activeoutlinestipple|当画布对象状态为 "active" 的时候，指定填充轮廓的位图|
|activestipple|当画布对象状态为 "active" 的时候，指定填充的位图|
|activewidth|当画布对象状态为 "active" 的时候，指定边框的宽度|
|dash|指定绘制虚线轮廓，与绘制线段的含义相同|
|dashoffset|指定虚线轮廓开始的偏移位置|
|disableddash|当画布对象状态为 "disabled" 的时候，绘制虚线|
|disabledfill|当画布对象状态为 "disabled" 的时候，填充颜色|
|disabledoutline|当画布对象状态为 "disabled" 的时候，绘制轮廓线|
|disabledoutlinestipple|当画布对象状态为 "disabled" 的时候，指定填充轮廓的位图|
|disabledstipple|当画布对象状态为 "disabled" 的时候，指定填充的位图|
|disabledwidth|当画布对象状态为 "disabled" 的时候，指定边框的宽度|
|extent|指定跨度（从 start 选项指定的位置开始到结束位置的角度）默认值是 90.0|
|fill|与上述表格的含义相同，表示指定的填充颜色，若为空字符串则为透明色|
|offset|指定当点画模式时填充位置的偏移，参数值为 "x,y"坐标偏移和位置偏移两种方式，比如 "ne"/"e" 等|
|outline|指定轮廓的颜色|
|outlineoffset|指定当点画模式绘制轮廓时位图的偏移|
|outlinestipple|当 outline 选项被设置时，该选项用于指定一个位图来填充边框，默认值是空字符串，表示黑色|
|start|指定起始位置的偏移角度|
|style| 默认创建的是扇形，指定该方法创建的是扇形（"pieslice"）、弓形（"chord"）还是弧形（"arc"）|
|tags|为创建的画布对象添加标签|
|width|指定边框的宽度|

下面让我们来一组绘制几何图形的简单示例：
```
from tkinter import *
root = Tk()
# 设置主窗口区的背景颜色以区别画布区的颜色
root.config(bg='#8DB6CD')
root.title("破污噗")
root.geometry('500x400')
root.iconbitmap('favicon.ico')
 
# 将画布设置为白色
canvas = Canvas(root,width = 400,height = 400,bg='white')
# 设置基准坐标
x0,y0,x1,y1 = 10,10,80,80
# 绘制扇形,起始角度为 0 度，结束角度为 270, 扇形区域填充色为淡蓝色，轮廓线为蓝色，线宽为 2px
arc = canvas.create_arc(x0, y0, x1, y1,start = 0, extent = 270, fill = '#B0E0E6',outline ='blue',width = 2)
# 绘制圆形
oval = canvas.create_oval(x0+150, y0, x1+150, y1,fill ='#CD950C',outline = 'blue',width=2)
# 绘制矩形,并将轮廓线设置为透明色，即不显示最外围的轮廓线，默认为黑色
rect = canvas.create_rectangle(x0,y0+100,x1,y1+100,fill='red',outline = '')
# 绘制一个三角形，填充色为绿色
trigon = canvas.create_polygon(80,80,150,80,200,200, outline="", fill="green",)
 
# 当然也可以绘制一个任意多边形，只要你的坐标正确就可以
# 绘制一个多边形，首先定义一系列的多边形上的坐标点
poly_points=[(0,280),(140,200),(140,240),(270,240),(270,320),(140,320),(140,360)]
polygon = canvas.create_polygon(poly_points,fill="#BF3EFF")
 
# 放置画布在主窗口
canvas.pack()
# 显示窗口
root.mainloop()
```

注意：create_rectangle() 方法的前两个参数决定了矩形的左上角坐标，后两个参数决定了矩形的右下角坐标；另外 create_oval() 方法并不是只能绘制圆形，还能绘制椭圆形，这取决于传入的参数。 

### Menu菜单控件

Menu 控件（菜单控件）它以可视化的方式将一系列的“功能选项卡”进行分组，并在每个分组下又“隐藏”了许多其他的“选项卡”。当打开菜单时，这些选项卡就会“显式”的呈现出来，方便用户进行选择。

通过使用菜单控件（Menu）可以充分地节省有限的窗口区域，让我们的界面更加简洁优雅，避免臃肿、混乱。 Tkinter Menu 控件提供了三种类型的菜单，分别是：topleve（主目录菜单）、pull-down（下拉式菜单）、pop-up（弹出式菜单，或称快捷式菜单）。
下表列出创建菜单时用到的相关方法，如下所示：

|方法|说明|
|--|--|
|add_cascade(**options)|添加一个父菜单，将一个指定的子菜单，通过 menu 参数与父菜单连接，从而创建一个下拉菜单。|
|add_checkbutton(**options)|添加一个多选按钮的菜单项|
|add_command(**options)| 添加一个普通的命令菜单项|
|add_radiobutton(**options)|添加一个单选按钮的菜单项|
|add_separator(**options)| 添加一条分割线|
|add(add(itemType, options))|添加菜单项，此处 itemType 参数可以是以下几种："command"、"cascade"，"checkbutton"、"radiobutton"、"separator" 五种，并使用 options 选项来设置菜单其他属性。|

除了上述方法之外，Menu 控件也提供了一些其他方法来操作菜单项，比如删除菜单项、获取菜单项、设置指定的菜单项等，如下表所示：

|方法|说明|
|--|--|
|delete(index1, index2=None)|1. 删除 index1 ~ index2（包含）的所有菜单项|
|1. 如果忽略 index2 参数，则删除 index1 指向的菜单项|
|entrycget(index, option)|获得指定菜单项的某选项的值|
|entryconfig(index, **options)|设置指定菜单项的选项|
|index(index)|返回与 index 参数相应的选项的序号|
|insert(index, itemType, **options)|插入指定类型的菜单项到 index 参数指定的位置，类型可以是|
|是："command"，"cascade"，"checkbutton"，"radiobutton"|
|或 "separator" 中的一个，或者也可以使用 insert_类型() 形式来，|
|比如 insert_cascade(index, **options)..等|
|invoke(index)|调用 index 指定的菜单项相关联的方法|
|post(x, y)|在指定的位置显示弹出菜单|
|type(index)|获得 index 参数指定菜单项的类型|
|unpost()|移除弹出菜单|
|yposition(index)|返回 index 参数指定的菜单项的垂直偏移位置|

下面对 Menu 控件的 options 参数做简单地介绍，如下所示：

|属性|说明|
|--|--|
|accelerator|1. 设置菜单项的快捷键，快捷键会显示在菜单项目的右边，比如 accelerator = "Ctrl+O" 表示打开；|
|2. 注意，此选项并不会自动将快捷键与菜单项连接在一起，必须通过按键绑定来实现|
|command|选择菜单项时执行的 callback 函数|
|label|定义菜单项内的文字|
|menu|此属性与 add_cascade() 方法一起使用，用来新增菜单项的子菜单项|
|selectcolor|指定当菜单项显示为单选按钮或多选按钮时选择中标志的颜色|
|state|定义菜单项的状态，可以是 normal、active 或 disabled|
|onvalue/offvalue|1. 默认情况下，variable 选项设置为 1 表示选中状态，反之设置为 0，设置 offvalue/onvalue 的值可以自定义未选中状态的值|
|2. |
|tearoff|1. 如果此选项为 True，在菜单项的上面就会显示一个可选择的分隔线；|
|2. 注意：分隔线会将此菜单项分离出来成为一个新的窗口|
|underline|设置菜单项中哪一个字符要有下画线|
|value|1. 设置按钮菜单项的值|
|2. 在同一组中的所有按钮应该拥有各不相同的值|
|3. 通过将该值与 variable 选项的值对比，即可判断用户选中了哪个按钮|
|variable|当菜单项是单选按钮或多选按钮时，与之关联的变量|

#### 创建主目录菜单

主目录菜单也称之为“顶级菜单”，下拉菜单等其他子菜单的都需要建立在“顶级菜单”的基础之上，下面示例创建了一个类似于“记事本”界面的程序，代码如下：

```
from tkinter import *
import tkinter . messagebox
#创建主窗口
win = Tk()
win.config(bg='#87CEEB')
win.title("破污噗")
win.geometry('450x350+300+200')
win.iconbitmap('favicon.ico')
 
# 绑定一个执行函数，当点击菜单项的时候会显示一个消息对话框
def menuCommand() :
    tkinter.messagebox.showinfo("主菜单栏","你正在使用主菜单栏")
# 创建一个主目录菜单，也被称为顶级菜单
main_menu = Menu(win)
#新增命令菜单项，使用 add_command() 实现
main_menu.add_command(label="文件",command=menuCommand)
main_menu.add_command(label="编辑",command=menuCommand)
main_menu.add_command(label="格式",command=menuCommand)
main_menu.add_command(label="查看",command=menuCommand)
main_menu.add_command(label="帮助",command=menuCommand)
#显示菜单
win.config(menu=main_menu)
win.mainloop()
```

#### 创建下拉菜单

下拉菜单时主菜单的重要组成部分，也是用户选择相关命令的重要交互界面，下拉菜单的创建方式也非常简单，不过需要我们注意，下拉菜单是建立的主菜单（即顶级菜单）的基础之上的，并非主窗口之上，这一点千万不要搞混，否则创建下拉菜单会失败。

下面继续仿照“记事本”的相关功能来创建下拉菜单，示例如下：

```
from tkinter import *
import tkinter .messagebox
#创建主窗口
win = Tk()
win.config(bg='#87CEEB')
win.title("破污噗")
win.geometry('450x350+300+200')
win.iconbitmap('favicon.ico')
 
#创建一个执行函数，点击下拉菜单中命令时执行
def menuCommand() :
    tkinter .messagebox .showinfo("下拉菜单", "您正在使用下拉菜单功能")
 
#创建主目录菜单（顶级菜单）
mainmenu = Menu (win)
 
#在顶级菜单上新增"文件"菜单的子菜单，同时不添加分割线
filemenu = Menu (mainmenu, tearoff=False)
 
#新增"文件"菜单的菜单项，并使用 accelerator 设置菜单项的快捷键
filemenu.add_command (label="新建",command=menuCommand,accelerator="Ctrl+N")
filemenu.add_command (label="打开",command=menuCommand, accelerator="Ctrl+O")
filemenu.add_command (label="保存",command=menuCommand, accelerator="Ctrl+S")
# 添加一条分割线
filemenu.add_separator ()
filemenu.add_command (label="退出",command=win. quit)
#在主目录菜单上新增"文件"选项，并通过menu参数与下拉菜单绑定
mainmenu.add_cascade (label="文件",menu=filemenu)
 
# 将主菜单设置在窗口上
win.config (menu=mainmenu)
# 绑定键盘事件，按下键盘上的相应的键时都会触发执行函数
win.bind("<Control-n>",menuCommand)
win. bind("<Control-N>", menuCommand)
win.bind("<Control-o>",menuCommand)
win. bind("<Control-O>", menuCommand)
win. bind("<Control-s>", menuCommand)
win.bind("<Control-S>",menuCommand)
# 显示主窗口
win.mainloop()
```

#### 创建弹出菜单栏

弹出式菜单栏，也称为快捷式菜单栏，比如通过点击鼠标右键弹出一个菜单栏，其中包含一些常用的选项卡，如复制、粘贴等.

Tkinter Menu 控件同样可以是实现上述功能，而且并不复杂，示例如下：

```
import tkinter as tk
 
root = tk.Tk()
root.config(bg='#8DB6CD')
root.title("破污噗")
root.geometry('400x300')
root.iconbitmap('favicon.ico')
def func():
    print('您通过弹出菜单执行了命令')
 
# 创建一个弹出菜单
menu = tk.Menu(root, tearoff=False)
menu.add_command(label="新建", command=func)
menu.add_command(label="复制", command=func)
menu.add_command(label="粘贴", command=func)
menu.add_command(label="剪切", command=func)
# 定义事件函数
def command(event):
    # 使用 post()在指定的位置显示弹出菜单
    menu.post(event.x_root, event.y_root)
   
# 绑定鼠标右键，这是鼠标绑定事件
# <Button-3>表示点击鼠标的右键，1 表示左键，2表示点击中间的滑轮
root.bind("<Button-3>", command)
root.mainloop()
```

### Scrollbar滚动条控件

Scrollbar 控件常用于创建一个水平或者垂直的滚动条，通常情况下，Scrollbar 控件可以与 Listbox、Text、Canvas 以及 Entry 等控件一起使。

滚动条控件是 GUI  程序中经常使用的一种控件类型，它主要用来控制控件区域的可见范围，比如当 Text 控件的文本内容非常多时，为了方便用户阅读，可以给 Text 控件增加滚动条，用户只需拖动滚动条就能完成内容的阅读。
Scrollbar 控件的常用属性，如下表所示：

|属性|说明|
|--|--|
|activebackground|指定当鼠标在上方飘过的时候滑块和箭头的背景颜色，默认由系统决定|
|activerelief|指定当鼠标在滑块上方飘过时滑块的样式，默认值是 "raised"，其他可选值有 "flat"，"sunken"，"groove"，"ridge"|
|background(bg)|指定背景颜色，默认值由系统指定|
|borderwidth(bd)|指定边框宽度，默认值是 0|
|command|当滚动条更新时回调的函数，通常指定对应组件的 xview() 或 yview() 方法|
|cursor|指定当鼠标在上方飘过的时的鼠标样式，默认值由系统指定|
|elementborderwidth|1. 指定滚动条和箭头的边框宽度|
|2. 默认值是 -1（表示使用 borderwidth 选项的值）|
|jump|1. 指定当用户拖拽滚动条时的行为|
|2. 默认值为 False，滚动条的任何一丝变动都会即刻调用 command 指定的回调函数|
|3. 设置为 True 则当用户松开鼠标才调用|
|orient|指定绘制 "horizontal"（垂直滚动条）还是 "vertical"（水平滚动条），默认值是 VERTICAL|
|repeatdelay|该选项指定鼠标左键点击滚动条凹槽的响应时间，默认值是 300（毫秒）|
|repeatinterval|该选项指定鼠标左键紧按滚动条凹槽时的响应间隔，默认值是 100（毫秒）|
|takefocus|指定使用 Tab 键可以将焦点移到该 Scrollbar 组件上，默认为开启，可以将该选项设置为 False 避免焦点在此组件上|
|troughcolor|指定凹槽的颜色，默认由系统指定|
|width|指定滚动条的宽度,默认值是 16px|

下面是介绍了 Scrollbar 控件常用的函数：

|属性|说明|
|--|--|
|activate(element) |1. 显示 element 参数指定的元素的背景颜色和样式;<br />2. element 参数可以设置为："arrow1"（箭头1），"arrow2"（箭头2）或 "slider"（滑块）|
|delta(deltax, deltay)|1. 给定一个鼠标移动的范围 deltax 和 deltay，然后该方法返回一个浮点类型的值（范围 -1.0 ~ 1.0）<br />2. 注意：deltax 表示水平移动量，deltay 表示垂直移动量|
|fraction(x, y)|给定一个像素坐标 (x, y)，该方法返回最接近给定坐标的滚动条位置。|
|get()| 返回当前滑块的位置 (a, b)，其中 a 值表示当前滑块的顶端或左端的位置，b 值表示当前滑块的底端或右端的位置。|
|identify(x, y)|1. 返回一个字符串表示指定位置下（如果有的话）的滚动条部件，<br />2. 返回值可以是："arrow1"（箭头1），"arrow2"（箭头2）、"slider"（滑块）或 ""（空）|
|set(*args)|1. 设置当前滚动条的位置<br />2. 该方法有两个参数即 (first, last)，其中 first 表示当前滑块的顶端或左端的位置，last 表示当前滑块的底端或右端的位置（范围 0.0 ~ 1.0）|

下面看一组简单的示例：

```
from tkinter import *
root = Tk()
root.title("破污噗")
root.geometry('450x180+300+200')
root.iconbitmap('favicon.ico')
# 创建一个滚动条控件，默认为垂直方向
sbar1= Scrollbar(root)
# 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
sbar1.pack(side=RIGHT, fill=Y)
# 创建水平滚动条，默认为水平方向,当拖动窗口时会沿着X轴方向填充
sbar2 = Scrollbar(root, orient=HORIZONTAL)
sbar2.pack(side=BOTTOM, fill=X)
 
# 创建列表框控件,并添加两个滚动条（分别在垂直和水平方向），使用 set() 进行设置
mylist = Listbox(root,xscrollcommand = sbar2.set,yscrollcommand = sbar1.set)
for i in range(30):
    mylist.insert(END,'第'+ str(i+1)+'次:'+'百度网址为：www.baidu.com'+ '\n' )
# 当窗口改变大小时会在X与Y方向填满窗口
mylist.pack(side=LEFT,fill = BOTH)
# 使用 command 关联控件的 yview、xview方法
sbar1.config(command = mylist.yview)
sbar2.config(command = mylist.xview)
#  显示主窗口
root.mainloop()
```

通过滑动滚动条可以浏览列表框中的内容，垂直方向的滚动条沿着上下浏览，水平方向的滚动条则沿着左右方向浏览。

### Event事件处理

事件处理，是 GUI 程序中不可或缺的重要组成部分，相比来说，控件只是组成一台机器的零部件， 而事件处理则是驱动这台机器“正常”运转的关键所在，它能够将零部件之间“优雅”的贯穿起来，因此“事件处理”可谓是 GUI 程序的“灵魂”，同时它也是实现人机交互的关键。在一款 GUI 程序中，我们将用户对软件的操作统称为“事件”，比如鼠标点击按钮、键盘输入文本以及窗口管理器触发的重绘事件等，这些事件有一个共同的特点，即都是由用户直接或者间接触发的。

#### 事件绑定方法

Tkinter 提供的事件处理机制允许我们为“控件”绑定相应的事件和事件处理函数（即 callback函数），从而实现控件与用户的交互，其语法格式如下：

`widget.bind("<event>",func)`

上述语法中，widget 代表控件的实例对象，之后，采用 bind() 方法进行事件绑定，该函数有两个参数：

`<event>`：一个字符串参数，表示事件的类型，并使用“尖括号”的形式进行包裹；
func：表示事件的处理函数（callback，即回调函数），当触发事件时，Tk 会携带事件对象（Event）去调用 func 方法。

注意：`bind()` 方法可以完成事件与处理函数绑定，而使用 unbind() 方法可以将事件与处理函数解绑。

#### 常用事件类型

事件类型（也称事件码）是 Tkinter 模块规定的，主要包括鼠标、键盘、光标等相关事件，Tkinter 为其规定了相应的语法格式：

`<modifier-type-detail>`

上述语法由三部分组成，说明如下：

- <>：事件类型必须包含在“尖括号”内；
- modifier：可选项，事件类型的修饰符，通常用于描述组合键、双击<Double-Button-1>、大写锁定键<Lock>以及<Alt-Shift>等；
- type：是必不可少的一项，表示事件的具体类型；
- detail：可选项，通常用于描述具体的哪个按键，比如 <Button-1> 表示鼠标左键；

这里有必要对经常使用的 modifier 修饰符做简单的介绍，修饰符可以修改事件的激活条件，比如双击鼠标或者需要同时按下某个键才触发事件，常用的修饰符如下：

|修饰符|说明|
|--|--|
|Control|事件发生时需按下 Control 键|
|Alt|事件发生时需按下 Alt 键|
|Shift|事件发生时需按下 Shift 键|
|Lock|事件发生时需处于大写锁定状态|
|Double|事件连续发生两次，比如双击鼠标|
|Triple|事件连续发生三次|
|Quadruple|事件连续发生四次|

下述表格中介绍了 Tkinter 中经常使用的事件类型，如下所示：

|事件码|说明|
|--|--|
|<ButtonPress-1>|单击鼠标左键，简写为<Button-1>，后面的数字可以是1/2/3，分别代表左键、中间滑轮、右键|
|<ButtonRelease-1>|释放鼠标左键，后面数字可以是1/2/3，分别代表释放左键、滑轮、右键|
|<B1-Motion>|按住鼠标左键移动，<B2-Motion>和<B3-Motion>分别表示按住鼠标滑轮移动、右键移动|
|<MouseWheel>|转动鼠标滑轮|
|<Double-Button-1>|双击鼠标左键|
|<Enter>|鼠标光标进入控件实例|
|<Leave>|鼠标光标离开控件实例|
|<Key>|按下键盘上的任意键|
|<KeyPress-字母>/<KeyPress-数字>|按下键盘上的某一个字母或者数字键|
|<KeyRelease>|释放键盘上的按键|
|<Return>|回车键，其他同类型键有<Shift>/<Tab>/<Control>/<Alt>|
|<Space>|空格键|
|<UP>/<Down>/<Left>/<Right>|方向键|
|<F1>...<F12>|常用的功能键|
|<Control-Alt>|组合键，再比如<Control-Shift-KeyPress-T>，表示用户同时点击 Ctrl + Shift + T|
|<FocusIn>|当控件获取焦点时候触发，比如鼠标点击输入控件输入内容，可以调用 focus_set() 方法使控件获得焦点|
|<FocusOut>|当控件失去焦点时激活，比如当鼠标离开输入框的时候|
|<Configure >|控件的发生改变的时候触发事件，比如调整了控件的大小等|
|<Deactivate>|当控件的状态从“激活”变为“未激活”时触发事件|
|<Destroy>|当控件被销毁的时候触发执行事件的函数|
|<Expose>|当窗口或组件的某部分不再被覆盖的时候触发事件|
|<Visibility>|当应用程序至少有一部分在屏幕中是可见状态时触发事件|

#### Event事件对象

当事件触发后，Tkinter 会自动将事件对象交给回调函数进行下步的处理，Event 对象包含了以下常用属性：

|属性|说明|
|--|--|
|widget|发生事件的是哪一个控件|
|x,y|相对于窗口的左上角而言，当前鼠标的坐标位置|
|x_root,y_root|相对于屏幕的左上角而言，当前鼠标的坐标位置|
|char|用来显示所按键相对应的字符|
|keysym|按键名，比如 Control_L 表示左边的 Ctrl 按键|
|keycode|按键码，一个按键的数字编号，比如 Delete 按键码是107|
|num|1/2/3中的一个，表示点击了鼠标的哪个按键，按键分为左、中、右|
|width,height|控件的修改后的尺寸，对应着 <Configure>事件|
|type|事件类型|

下面看一组关于“键盘事件”的使用示例：

```
from tkinter import *
# 定义事件函数，必须用event参数
def show_key(event):
    # 查看触发事件的按钮
    s=event.keysym
    # 将其显示在按钮控件上
    lb.config(text=s)
 
root=Tk()
root.config(bg='#87CEEB')
root.title("破污噗")
root.geometry('450x350+300+200')
root.iconbitmap('favicon.ico')
# 添加一个按钮控件
lb=Label(root,text='请按键',fg='blue',font=('微软雅黑',15))
# 给按钮控件绑定事件，按下任意键，然后调用事件处理函数。注意，此处需要在英文状态下进行输入
lb.bind('<Key>',show_key)
# 设置按钮获取焦点
lb.focus_set()
lb.pack()
# 显示窗口
root.mainloop()
```

注意：在上述示例中，只有当 Label 控件获取焦点后才能接收键盘事件，因此在给控件绑定事件和回调函数后，需要使用 focus_set() 方法来获取焦点。

下面再看一组关于“鼠标事件”的相关示例：

```
# 定义事件函数
from tkinter import *
 
def handleMotion(event):
    lb1['text'] = '你移动了光标的所在位置'
    lb2['text'] = '目前光标位置：x ='+ str(event.x)+';y='+str(event.y)
    print('光标当前位置',event.x,event.y)
 
# 创建主窗口
win = Tk()
win.config(bg='#87CEEB')
win.title("破污噗")
win.geometry('450x350+300+200')
win.iconbitmap('favicon.ico')
# 创建一个窗体容器frame
frame = Frame (win, relief=RAISED, borderwidth=2, width=300,height=200)
frame.bind('<Motion>',handleMotion)
lb1 = Label(frame,text='没有任何事件触发')
# 使用place进行位置布局，下一节会介绍
lb1.place (x=20,y=20)
lb2 = Label(frame,text='')
lb2.place (x=16,y=60)
frame.pack(side=TOP)
# 显示窗口
win.mainloop()
```

### 布局管理器（pack，grid，place）

Tkinter 提供了三种常用的布局管理器，分别是 pack()、grid() 以及 place()，如下表所示：

|方法|说明|
|--|--|
|pack()|按照控件的添加顺序其进行排列，遗憾的是此方法灵活性较差|
|grid()|以行和列（网格）形式对控件进行排列，此种方法使用起来较为灵活|
|place()|可以指定组件大小以及摆放位置，三个方法中最为灵活的布局方法|

#### pack()

pack() 是一种较为简单的布局方法，在不使用任何参数的情况下，它会将控件以添加时的先后顺序，自上而下，一行一行的进行排列，并且默认居中显示。pack() 方法的常用参数如下所示：

|属性|说明|
|--|--|
|anchor|组件在窗口中的对齐方式，有 9 个方位参数值，比如"n"/"w"/"s"/"e"/"ne"，以及 "center" 等（这里的 e w s n分别代表，东西南北）|
|expand|是否可扩展窗口，参数值为 True（扩展）或者 False（不扩展），默认为 False，若设置为 True，则控件的位置始终位于窗口的中央位置|
|fill|参数值为 X/Y/BOTH/NONE，表示允许控件在水平/垂直/同时在两个方向上进行拉伸，比如当 fill = X 时，控件会占满水平方向上的所有剩余的空间。|
|ipadx,ipady|需要与 fill 参数值共同使用，表示组件与内容和组件边框的距离（内边距），比如文本内容和组件边框的距离，单位为像素(p)，或者厘米(c)、英寸(i)|
|padx,pady|用于控制组件之间的上下、左右的距离（外边距），单位为像素(p)，或者厘米(c)、英寸(i)|
|side|组件放置在窗口的哪个位置上，参数值 'top','bottom','left','right'。注意，单词小写时需要使用字符串格式，若为大写单词则不必使用字符串格式|

下面看一组简单的使用示例：

```
from tkinter import  *
win = Tk()
win.title("破污噗")
win.geometry('450x300+300+300')
win.iconbitmap('favicon.ico')
 
lb_red = Label(win,text="红色",bg="Red",fg='#ffffff',relief=GROOVE)
# 默认以top方式放置
lb_red.pack()
lb_blue = Label(win,text="蓝色",bg="blue",fg='#ffffff',relief=GROOVE)
# 沿着水平方向填充，使用 pady 控制蓝色标签与其他标签的上下距离为 5 个像素
lb_blue.pack(fill=X,pady='5px')
lb_green = Label(win,text="绿色",bg="green",fg='#ffffff',relief=RAISED)
# 将 黄色标签所在区域都填充为黄色，当使用 fill 参数时，必须设置 expand = 1，否则不能生效
lb_green.pack(side=LEFT,expand=1,fill = BOTH)
win.mainloop()
```

#### grid()

grid() 函数是一种基于网格式的布局管理方法，相当于把窗口看成了一张由行和列组成的表格。当使用该 grid 函数进行布局的时，表格内的每个单元格都可以放置一个控件。，从而实现对界面的布局管理。

注意：这里的所说的“表格”是虚拟出来，目的是便于大家理解，其实窗体并不会因为使用了 gird() 函数，而增加一个表格。

grid() 函数的常用参数如下所示：

|属性|说明|
|--|--|
|column|控件位于表格中的第几列，窗体最左边的为起始列，默认为第 0 列|
|columnsapn|控件实例所跨的列数，默认为 1 列，通过该参数可以合并一行中多个领近单元格。|
|ipadx,ipady|用于控制内边距，在单元格内部，左右、上下方向上填充指定大小的空间。|
|padx,pady|用于控制外边距，在单元格外部，左右、上下方向上填充指定大小的空间。|
|row|控件位于表格中的第几行，窗体最上面为起始行，默认为第 0 行|
|rowspan|控件实例所跨的行数，默认为 1 行，通过该参数可以合并一列中多个领近单元格。|
|sticky|该属性用来设置控件位于单元格那个方位上，参数值和 anchor 相同，若不设置该参数则控件在单元格内居中|

grid() 方法相比 pack() 方法来说要更加灵活，以网格的方式对组件进行布局管理，让整个布局显得非常简洁、优雅。如果说非要从三个布局管理器中选择一个使用的话，那么我推荐大家使用 grid() 方法。

这里有一点需要大家要特别注意，在一个程序中不能同时使用 pack() 和 grid() 方法，这两个方法只能二选一，否则程序会运行错误。

下面看一组有关 grid() 函数的简单的示例：

```
from tkinter import *
#主窗口
win = Tk()
win.config(bg='#87CEEB')
win.title("破污噗")
win.geometry('500x350+300+300')
win.iconbitmap('favicon.ico')
 
#在窗口内创建按钮，以表格的形式依次排列
for i in range (10):
    for j in range (10):
        Button (win, text=" (" + str(i) + ","+ str(j)+ ")",bg='#D1EEEE') .grid(row=i,column=j)
 
# 在第5行第11列添加一个Label标签
Label(win,text="张小白",fg='blue',font=('楷体',12,'bold')).grid(row =4,column=11)
#开始窗口的事件循环
win. mainloop()
```

当使用 grid 函数布局的时，其实就是为各个控件指定行号、列号的过程，我们不需要为每个单元格指定大小，因为 grid 会为每个单元格自动设置一个适合的尺寸。

下面通过 grid() 布局管理器制作一个简易的登录界面，代码如下所示：

```
import tkinter as tk
from tkinter import messagebox
 
root = tk.Tk()
root.title("破污噗")
 
root.iconbitmap('favicon.ico')
root.resizable(0,0)
tk.Label(root, text="用户名").grid(row=0, sticky="w")
tk.Label(root, text="密码").grid(row=1, sticky="w")
tk.Entry(root).grid(row=0, column=1)
tk.Entry(root, show="*").grid(row=1, column=1)
# 加载图片LOGO,注意这里是gif格式的图片
photo = tk.PhotoImage(file="agree.png")
tk.Label(root, image=photo).grid(row=0, column=2, rowspan=2, padx='4px', pady='5px')
# 编写一个简单的回调函数
def login():
    messagebox.showinfo('恭喜你发现了宝藏文章!')
 
# 使用grid()函数来布局，并控制按钮的显示位置
tk.Button(root, text="登录", width=10, command=login).grid(row=3, column=0, columnspan=2,sticky="w", padx=10, pady=5)
tk.Button(root, text="退出", width=10, command=root.quit).grid(row=3, column=1, columnspan=2,sticky="e", padx=10, pady=5)
# 开启事件主循环
root.mainloop()
```

#### place()

与前两种布局方法相比，采用 place() 方法进行布局管理要更加精细化，通过 place() 布局管理器可以直接指定控件在窗体内的绝对位置，或者相对于其他控件定位的相对位置。

下面对 place 布局管理器的常用属性做相关介绍：

|属性|说明|
|--|--|
|anchor|定义控件在窗体内的方位，参数值N/NE/E/SE/S/SW/W/NW 或 CENTER，默认值是 NW|
|bordermode|定义控件的坐标是否要考虑边界的宽度，参数值为 OUTSIDE（排除边界） 或 INSIDE（包含边界），默认值 INSIDE。|
|x、y|定义控件在根窗体中水平和垂直方向上的起始绝对位置|
|relx、rely|1. 定义控件相对于根窗口（或其他控件）在水平和垂直方向上的相对位置（即位移比例），取值范围再 0.0~1.0 之间|
|2. 可设置 in_ 参数项，相对于某个其他控件的位置|
|height、width|控件自身的高度和宽度（单位为像素）|
|relheight、relwidth|控件高度和宽度相对于根窗体高度和宽度的比例，取值也在 0.0~1.0 之间|

通过上述描述我们知道，relx和rely参数指定的是控件相对于父组件的位置，而relwidth和relheight参数则是指定控件相对于父组件的尺寸大小。

注意：这里父组件指的是当前可操作控件的上层组件，比如在没有使用容器控件（frame）的窗体中，控件的父组件就是主窗口本身。

上述表格中关于距离位置的参数容易产生“疑惑”，下面通过一组简单的示例来进一步说明：

```
from tkinter import *
#主窗口
win = Tk()
win.title("破污噗")
win.iconbitmap('favicon.ico')
#创建一个frame窗体对象，用来包裹标签
frame = Frame(win, relief=SUNKEN, borderwidth=2, width=450, height=250)
# 在水平、垂直方向上填充窗体
frame.pack(side=TOP, fill=BOTH, expand=1)
 
# 创建 "位置1"
Label1 = Label(frame, text="位置1",bg='blue',fg='white')
# 使用 place,设置第一个标签位于距离窗体左上角的位置（40,40）和其大小（width，height）
# 注意这里（x,y）位置坐标指的是标签左上角的位置（以NW左上角进行绝对定位，默认为NW）
Label1.place(x=40,y=40, width=60, height=30)
 
# 设置标签2
Label2 = Label(frame, text="位置2",bg='purple',fg='white')
# 以右上角进行绝对值定位，anchor=NE，第二个标签的位置在距离窗体左上角的(180，80)
Label2.place(x=180,y=80, anchor=NE, width=60, height=30)
 
# 设置标签3
Label3 = Label (frame, text="位置3",bg='green',fg='white')
# 设置水平起始位置相对于窗体水平距离的0.6倍，垂直的绝对距离为80，大小为60，30
Label3.place(relx=0.6,y=80, width=60, height=30)
 
# 设置标签4
Label4 = Label (frame, text="位置4",bg='gray',fg='white')
# 设置水平起始位置相对于窗体水平距离的0.01倍，垂直的绝对距离为80，并设置高度为窗体高度比例的0.5倍，宽度为80
Label4.place(relx=0.01,y=80,relheight=0.4,width=80)
#开始事件循环
win. mainloop()
```

注意：在一个父组件中 place()方法可以与 grid() 方法混合使用，要与 pack() 进行区别。

### 布局管理控件

这里介绍了三种常用的容器控件以及它们的使用方法，分别是 Frame、LabelFrame、PanedWindow 

#### Frame控件

Frame 本质上也是一个矩形窗体，同其他控件一样也需要位于主窗口内。我们可以在主窗口内放置多个 Frame 控件，并且每个 Frame 中还可以嵌套一个或者多个Frame，从而将主窗口界面划分成多个区域。

Frame 控件的常用属性如下表所示：

|属性|说明|
|--|--|
|bg|设置 Frame 的背景颜色|
|bd|指定 Frame 的边框宽度|
|colormap|指定  Frame 组件及其子组件的颜色映射|
|container|布尔值参数，若参数值为 True，则窗体将被用作容器使用，一些其他程序也可以被嵌入。|
|cursor|指定鼠标在 Frame 上飘过的鼠标样式，默认由系统指定|
|height/width|设置 Frame 的高度和宽度|
|highlightbackground|指定当 Frame 没有获得焦点的时候高亮边框的颜色，通常由系统指定为标准颜色|
|highlightcolor|指定当 Frame 获得焦点的时候高亮边框的颜色|
|highlightthickness|指定高亮边框的宽度，默认值是 0|
|padx/pady|距离主窗口在水平/垂直方向上的外边距|
|relief|指定边框的样式，参数值 "sunken"，"raised"，"groove" 或 "ridge"，"flat"，默认为 "falt'|
|takefocus|布尔值参数，默认为 False，指定该组件是否接受输入焦点（即用户通过 Tab 键将焦点转移上来）|

下面看一组简单的示例，通过 Frame 将主窗口分成左右两个部分，如下所示：

```
import tkinter as tk
 
win = tk.Tk()
win.title("破污噗")
win.geometry('400x350+200+200')
win.iconbitmap('favicon.ico')
 
# 在主窗口上添加一个frame控件
frame1 = tk.Frame(win)
frame1.pack()
 
# 在frame_1上添加另外两个frame， 一个在靠左，一个靠右
# 左侧的frame
frame_left = tk.Frame(frame1)
tk.Label(frame_left,text='左侧标签1',bg='green',width=10,height=5).grid(row =0,column=0)
tk.Label(frame_left,text='左侧标签2',bg='blue',width=10,height=5).grid(row = 1 ,column =1)
frame_left.pack(side=tk.LEFT)
 
frame_right = tk.Frame(frame1)
tk.Label(frame_right,text='右侧标签1',bg='gray',width=10,height=5).grid(row = 0 ,column =1)
tk.Label(frame_right,text='右侧标签2',bg='pink',width=10,height=5).grid(row = 1 ,column =0)
tk.Label(frame_right,text='右侧标签3',bg='purple',width=10,height=5).grid(row= 1,column=1)
frame_right.pack(side=tk.RIGHT)
win.mainloop()
```

上述示例利用 Frame 控件将主窗口分成了左右两个子区域，同时在各自区域中添加了 Label 标签，而且区域之间互不干扰。采用这种分区、分块的布局方式，可以使得 GUI 程序更加规范、简洁化。

#### LabelFrame控件

LabelFrame 控件也是一种容器类型的控件，它属于是 Frame 控件的变体，因此它们的属性选项大体相同。
在默认情况下，LabelFrame 会在其包裹的子组件周围绘制一个边框和一个标题。当我们想要将一些相关的组件分为一组时，就可以使用 LabelFrame 组件，比如把一系列 Radiobutton（单选按钮）放在一起来供用户选择。
同 Frame 控件一样，LabelFrame 的主要作用也是对控件进行分组处理，下面看一个具体的实例：

#### PanedWindow控件

PanedWindow（窗格界面）也可以理解成一个特殊的 Frame 控件，它是 Tkinter 8.4 版本后新增的空间管理组件，其主要目的是为其他组件提供一个容器或者框架，从而实现以分块的形式对图形界面进行布局。

与 Frame 控件不同， PanedWindow 允许用户自主地调整界面划分以及每块区域的大小。因此，当您需要让用户自己调节每块区域的大小时，就可以采用 PanedWindow 作为组件载体来进行界面的布局。

不仅如此 PanedWindow 组件还提供了“手柄” 功能（设置参数 showhandle=True 来启用），通过拖动“手柄”图标也可以改变每块区域的大小。

其中 master 表示父组件，即包裹该组件的上层组件。其常用属性如下表所示：

|属性|说明|
|--|--|
|handlepad|1. 调节“手柄”的位置|
|2. 比如当 orient ='vertical' 设置垂直时，handlepad 表示“分割线”上的手柄与左端的距离，默认为 8 像素|
|handlesize|设置“手柄”的尺寸（由于“手柄”必须是一个正方形，所以是设置正方形的边长）默认为 8 像素|
|opaqueresize|1. 该选项定义了用户调整窗格尺寸的操作，如果该选项的值为 True（默认），窗格的尺寸随用户鼠标的拖拽而改变|
|2.  如果该选项的值为 False，那么窗格的尺寸，在用户释放鼠标时才会更新到新的位置上|
|orient|指定窗格的分布方式，默认为水平方向分布（"horizontal"），或者还可以设置为垂直纵向分布（"vertical"）|
|relif|指定边框的样式，默认为 "flat"，还可以设置为  "sunken"，"raised"，"groove" 或 "ridge"|
|sashpad|设置每一条分割线到窗格间的间距|
|sashrelief|设置分割线的样式，默认值是："flat"，还可以设置 "sunken"，"raised"，"groove" 或 "ridge"|
|sashwidth|设置分割线的宽度|
|showhandle|设置是否显示调节窗格的手柄，默认为 False|
|height/width|设置 PanedWindow 的高度、宽度，若不设置，则其大小由其子组件的尺寸决定|

PanedWindow 的常用方法如下表所示：

|方法|说明|
|--|--|
|add(child)|添加一个新的子组件到窗格中语法格式 add(child,**option)，参数值 after、before、sticky|
|forget(child)|删除一个子组件|
|panecget(child, option)|获得子组件指定选项的值|
|paneconfig(child, **options)|设置子组件的各种选项|
|panes()|将父组件中包含的子组件以列表的形式返回|
|sash_coord(index)|返回一个二元组表示指定分割线的起点坐标|
|sash_place(index, x, y)|将指定的分割线移动到一个新的位置|

下面示例设计一个简单的界面布局，然后将图形界面分割成四部分：创建一个水平方向的 PanedWindow，并向其中添加两个 Label 组件，之后创建一个垂直的方向的 PanedWindow，并向其中中添加两个 Label 标签。示例代码如下：

```
import tkinter as tk
win = tk.Tk()
win.title("破污噗")
win.geometry('400x400+200+200')
win.iconbitmap('favicon.ico')
# 创建一个水平方向的 panedwindow，并添加到主窗口中，默认为水平方向
p_window1 = tk.PanedWindow(win)
p_window1.pack(fill=tk.BOTH, expand=1)
# 在窗口区的左侧添加两个水平方向的 Label
left1 =tk. Label(p_window1, text='百度', bg='#7CCD7C', width=10,font=('微软雅黑',15))
p_window1.add(left1)
left2 =tk.Label(p_window1, text='网址：www.baidu.com', bg='#9AC0CD', width=10,font=('微软雅黑',15))
p_window1.add(left2)
 
# 创建一个垂直方向的panedwindow,并添加一个手柄，设置分割线样式
p_window2 = tk.PanedWindow(orient=tk.VERTICAL,showhandle=True,sashrelief='sunken')
# 添加到 p_window1中
p_window1.add(p_window2)
# 在 p_window2 中添加两个垂直方向的标签
top_label =tk. Label(p_window2, text='教程', bg='#7171C6', height=8,font=('宋体',15))
p_window2.add(top_label)
bottom_label =tk. Label(p_window2, text='辅导班', bg='#8968CD',font=('宋体',15))
p_window2.add(bottom_label)
 
win.mainloop()
```
 

注意：从上述示例中可以看出 PanedWindw 会为每一个 Label 控件创建一个独立的窗格， 当我们将鼠标悬停在两个控件接壤处的白色边框上时，就会出现可以上下或者左右拉伸的指示光标，用户按照可以按照自己的意愿来调整每块区域的大小。

### 对话框控件

在前面，我们花费了大量的时间讲解了 Tkinter 中常用基本控件，通过对这些控件的学习，我们对  GUI 开发有了基本的认识与掌握，一个完整的 GUI 程序就是由这些组件以合理、美观的布局方式构成的。
除了基本的控件之外，Tkinter 还提供了三种对话框控件：

- 文件选择对话框：filedailog
- 颜色选择对话框：colorchooser
- 消息对话框：messagebox

这些对话框的使用能够在一定程度上增强用户的交互体验，下面对这些对话框控件进行详细地介绍。

- 文件选择对话框

文件对话框在 GUI 程序中经常的使用到，比如上传文档需要从本地选择一个文件，包括文件的打开和保存功能都需要一个文件对话框来实现。Tkinter 提供文件对话框被封装在tkinter.filedailog模块中，该模块提供了有关文件对话框的常用函数，经常使用的有以下几个：

|方法|说明|
|--|--|
|Open()|打开个某个文件|
|SaveAs()|打开一个保存文件的对话框|
|askopenfilename()|打开某个文件，并以包函文件名的路径作为返回值|
|askopenfilenames()|同时打开多个文件，并以元组形式返回多个文件名|
|askopenfile()|打开文件，并返回文件流对象|
|askopenfiles()|打开多个文件，并以列表形式返回多个文件流对象|
|asksaveasfilename()|选择以什么文件名保存文件，并返回文件名|
|asksaveasfile()|选择以什么类型保存文件，并返回文件流对象|
|askdirectory|选择目录，并返回目录名|

上述方法的常用参数值如下所示：

|参数|说明|
|--|--|
|defaultextension|指定文件的后缀名，当保存文件时自动添加文件名，如果自动添加了文件的后缀名，则该选项值不会生效|
|filetypes|指定筛选文件类型的下拉菜单选项，该选项值是由 2 元祖构成的列表，其中每个二元祖由两部分组成 (类型名,后缀)，比如 filetypes = [("PNG","*.png"), ("JPG", "*.jpg"), ("GIF","*.gif"),("文本文件","*.txt")...] |
|initialdir|指定打开/保存文件的默认路径，默认路径是当前文件夹|
|parent| 如果不指定该选项，那么对话框默认显示在根窗口上，通过设置该参数可以使得对话框显示在子窗口上|
|title|指定文件对话框的标题|

下面看一组具体的实例应用：

```
from tkinter import *
import tkinter.filedialog  # 注意次数要将文件对话框导入
 
# 定义一个处理文件的相关函数
def askfile():
    # 从本地选择一个文件，并返回文件的目录
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text= filename)
    else:
         lb.config(text='您没有选择任何文件')
 
root = Tk()
root.config(bg='#87CEEB')
root.title("破污噗")
root.geometry('400x200+300+300')
root.iconbitmap('favicon.ico')
btn=Button(root,text='选择文件',relief=RAISED,command=askfile)
btn.grid(row=0,column=0)
lb = Label(root,text='',bg='#87CEEB')
lb.grid(row=0,column=1,padx=5)
# 显示窗口
root.mainloop()
```

下面再看一组“保存文件”的示例代码如下：

```
import tkinter as tk
from tkinter import filedialog
from PIL import Image
 
def open_img():
    try:
        global img
        filepath = filedialog.askopenfilename() # 打开文件，返回该文件的完整路径
        filename.set(filepath)
        img = Image.open(filename.get())
    except Exception as e:
        print("您没有选择任何文件",e)
 
 
def save_png():
    try:
 
        filetypes = [("PNG","*.png"), ("JPG", "*.jpg"), ("GIF","*.gif"),("txt files","*.txt"),('All files','*')]
        # 返回一个 pathname 文件路径字符串，如果取消或者关闭则返回空字符，返回文件如何操作是后续代码的事情，
        # 该函数知识返回选择文件的文件名字，不具备保存文件的能力
        filenewpath= filedialog.asksaveasfilename(title='保存文件',
                                                filetypes=filetypes,
                                                defaultextension='.png',
                                                initialdir='C:/Users/Administrator/Desktop' )
        path_var.set(filenewpath)
        # 保存文件
        img.save(str(path_var.get()))
    except Exception as e:
        print(e)
 
window = tk.Tk()
window.title("破污噗")
window.geometry('400x200+300+300')
window.iconbitmap('favicon.ico')
 
filename = tk.StringVar()
path_var = tk.StringVar()
# 定义读取文件的组件
entry = tk.Entry(window, textvariable=filename)
entry.grid(row=1, column=0, padx=5, pady=5)
tk.Button(window, text='选择文件', command=open_img).grid(row=1, column=1, padx=5, pady=5)
 
# 定义保存文件的组件
entry1 = tk.Entry(window, textvariable=path_var)
entry1.grid(row=2, column=0, padx=5, pady=5)
tk.Button(window, text='保存文件', command=save_png).grid(row=2, column=1, padx=5, pady=5)
window.mainloop()
```

- 颜色选择对话框

颜色选择对话框（colorchooser），提供了一个非常友善的颜色面板，它允许用户选择自己所需要的颜色。 当用户在面板上选择一个颜色并按下“确定”按钮后，它会返回一个二元祖，其第 1 个元素是选择的 RGB 颜色值，第 2 个元素是对应的 16 进制颜色值。

颜色选择对话款主要应用在画笔、涂鸦等功能上，通过它可以绘制出五彩缤纷的颜色，该对话框的使用非常简单，主要有以下两个常用方法：

|方法|说明|
|--|--|
|askcolor()|打开一个颜色对话框，并将用户选择的颜色值以元组的形式返回（没选择返回None），格式为((R, G, B), "#rrggbb")|
|Chooser()|打开一个颜色对话框，并用户选择颜色确定后，返回一个二元组，格式为（(R, G, B), "#rrggbb"）|

常用的颜色对话框的参数值如下表所示：

|属性|说明|
|--|--|
|default|要显示的初始的颜色，默认颜色是浅灰色（light gray）|
|title|指定颜色选择器标题栏的文本，默认标题为“颜色”|
|parent|1. 如果不指定该选项，那么对话框默认显示在根窗口上<br />2. 如果想要将对话框显示在子窗口上，那么可以设置 parent = 子窗口对象|

下面看一组简单的使用示例：

```
import tkinter as tk
from tkinter import colorchooser
root = tk.Tk()
root.title("颜色选择")
root.geometry('400x200+300+300')
root.iconbitmap('favicon.ico')
 
def callback():
    # 打开颜色对话款
    colorvalue = tk.colorchooser.askcolor()
    # 在颜色面板点击确定后，会在窗口显示二元组颜色值
    lb.config(text='颜色值:'+ str(colorvalue))
 
lb=tk.Label(root,text='',font=('宋体',10))
# 将label标签放置在主窗口
lb.pack()
tk.Button(root, text="点击选择颜色", command=callback, width=10, bg='#9AC0CD').pack()
# 显示界面
root.mainloop()
```

- 消息对话框

关于消息对话款（messagebox），在前面介绍其他控件时已经使用过，在这里仅对它做简单介绍。
消息对话框主要起到信息提示、警告、说明、询问等作用，通常配合“事件函数”一起使用，比如执行某个操作出现了错误，然后弹出错误消息提示框。通过使用消息对话框可以提升用户的交互体验，也使得 GUI 程序更加人性化。消息对话框主要包含了以下常用方法：

|方法|说明|
|--|--|
|askokcancel(title=None, message=None)|打开一个“确定／取消”的对话框|
|askquestion(title=None, message=None)|打开一个“是／否”的对话框。|
|askretrycancel(title=None, message=None)|打开一个“重试／取消”的对话框|
|askyesno(title=None, message=None)|打开一个“是／否”的对话框|
|showerror(title=None, message=None)|打开一个错误提示对话框|
|showinfo(title=None, message=None)|打开一个信息提示对话框|
|showwarning(title=None, message=None)|打开一个警告提示对话框|

上述方法拥有相同的选项参数，如下表所示：

|属性|说明|
|--|--|
|default|1. 设置默认的按钮（也就是按下回车响应的那个按钮）<br />2. 默认是第一个按钮（像“确定”，“是”或“重试”）<br />3. 可以设置的值根据对话框函数的不同，可以选择 CANCEL，IGNORE，OK，NO，RETRY 或 YES|
|icon|1. 指定对话框显示的图标<br />2. 可以指定的值有：ERROR，INFO，QUESTION 或 WARNING<br />3. 注意：不能指定自己的图标|
|parent|1. 如果不指定该选项，那么对话框默认显示在根窗口上<br />2. 如果想要将对话框显示在子窗口上，那么可以设置 parent= 子窗口对象|

上述方法的返回值一般会是一个布尔值，或者是“YES”，“NO”，“OK”等，这些方法使用较为简单，此处不进行逐一列举。

### Notebook

Notebook 是一个Widget 容器控件，这个控件的特点就是有许多选项卡，当选择不同选项卡时可以看到不同的子控件内容，也可以当做子窗口内容，Notebook 是属于tkinter.ttk模块的控件

构造方法如下：

`Notebook(父对象, options)`

参数：

- 第一个参数：父对象，表示这个选项卡将建立在哪一个窗口内
- 第二个参数：options，参数如下

|参数|含义|
|--|--|
|height|如果设置数值则使用设置高度|
|默认是使用最大可能高度|
|padding|设置Notebook外围的额外空间，可以设置4个数值代表left、top、tight、bottom四周的空间|
|width|如果设置数值则使用设置宽度<br />默认是使用最大可能宽度|

整个建立Notebook框架的步骤：

- Notebook()建立Notebook对象，假设对象名称是notebook
- 使用notebook对象调用add()方法
  - add(子对象, text='xxx')
  - xxx是要添加的选项卡名称
- 上述代码可以将子对象插入notebook，同时产生’xxx’选项卡名称

如果用正规语法表示add()方法，它的语法格式如下

`add(子对象, options)`

options参数如下：

|参数|含义|
|--|--|
|compound|可以设置当选项卡内同时含图像和文字时，彼此之间的位置关系|
|image|选项卡以图像方式呈现|
|padding|设置Notebook和面板Pane的额外空间|
|state|可能值是normal、disabled、hidden<br />如果是disabled表示无法被选取使用<br />如果是hidden表示被隐藏|
|sticky|指出子窗口面板的配置方式，n/s/e/w分别表示North、South、East、West|
|text|选项卡中的字符串内容|
|underline|指出第几个字母含下划线<br />从0开始计算的索引|

Notebook 基本应用

例子：
```
import tkinter
import tkinter.ttk
root = tkinter.Tk()
root.geometry('300x180')

notebook = tkinter.ttk.Notebook(root)

frameOne = tkinter.Frame()
frameTwo = tkinter.Frame()

notebook.add(frameOne, text='选项卡1')
notebook.add(frameTwo, text='选项卡2')
notebook.pack(padx=10, pady=5, fill=tkinter.BOTH, expand=True)

root.mainloop()
```

绑定选项卡与子控件内容

例子：
```
import tkinter
import tkinter.ttk
root = tkinter.Tk()
root.geometry('150x120')

def show():
    labelOther.config(text='Tkinter')
    labelOther.config(bg='lightgreen')

notebook = tkinter.ttk.Notebook(root)

frameOne = tkinter.Frame()
frameTwo = tkinter.Frame()

# 添加内容
label = tkinter.Label(frameOne, text='Python', bg='lightblue', fg='red')
label.pack(padx=10, pady=5)

button = tkinter.Button(frameTwo, text='请点击', command=show)
button.pack(padx=10, pady=5)

labelOther = tkinter.Label(frameTwo, fg='red')
labelOther.pack(padx=10, pady=5)

notebook.add(frameOne, text='选项卡1')
notebook.add(frameTwo, text='选项卡2')
notebook.pack(padx=10, pady=5, fill=tkinter.BOTH, expand=True)

root.mainloop()
```

### 构建桌面软件模板

```
#!/usr/bin/env python3
# coding=utf-8

from tkinter import *
from tkinter import ttk
import os

__author__ = {'name' : 'TestPoo', 'created' : '2022-05-05', 'modify' : '2022-11-14'}

#**实现界面功能****
class Application_ui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('万年历')
        self.master["bg"]='#fff'
        self.createWidgets()
        self.position()


    def position(self):
        top.resizable(False,False)
        curWidth = 900
        curHeight = 600
        scnWidth,scnHeight = top.maxsize()
        tmpplace = '%dx%d+%d+%d'%(curWidth,curHeight,(scnWidth-curWidth)/2,(scnHeight-curHeight)/2)
        top.geometry(tmpplace)
        top.iconphoto(False, PhotoImage(file=os.getcwd() + '/calendar.png'))

    def createWidgets(self):
        top = self.winfo_toplevel()

#**实现具体的事件处理回调函数****
class Application(Application_ui):
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
```

### 附录

```
# 去年tkinter边框，包括标题栏
top.overrideredirect(True)

# linux下去掉标题栏，变身dock
top.attributes('-type', 'dock')

# 最上层显示
top.attributes("-topmost", True)

# 获取焦点
top.focus_force()

# 获取窗口宽度
curWidth = top.winfo_width()

# 获取窗口高度
curHeight = top.winfo_height()

# 获取屏幕宽度和高度
scnWidth,scnHeight = top.maxsize()

# 窗口居中
tmpplace = '%dx%d+%d+%d'%(curWidth,curHeight,(scnWidth-curWidth)/2,(scnHeight-curHeight)/2)

# 失去焦点时，关闭窗口
top.bind('<FocusOut>', self.lossfocus)
def lossfocus(self, event=None):
    if event.widget == top:
        top.destroy()

# ttk样式
self.style = ttk.Style()
self.style.theme_use('default')
self.style.configure("TButton",foreground="#000",background="#fff",borderwidth=0,font=('',config['fontSize']),justify='center',relief=FLAT)

# 原始样式
self.nextYear = Button(top,text="▶",command = self.next_year,fg="#303133",bg="#fff",bd=0,font=('Helvetica',12))

# tk屏幕大小
width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()

# 重启当前程序
path = sys.executable
os.execl(path, "python", * sys.argv)

# DPI缩放
#导入库
import ctypes
from tkinter import *
from tkinter.ttk import *

#创建窗口，root可替换成自己定义的窗口
root=Tk()
#调用api设置成由应用程序缩放
ctypes.windll.shcore.SetProcessDpiAwareness(1)
#调用api获得当前的缩放因子
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
#设置缩放因子
root.tk.call('tk', 'scaling', ScaleFactor/75)
```
