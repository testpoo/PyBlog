title: go入门
date: 2023-08-15
category: 技术
tag: go

[TOC]

### 1. 简介

Go由Google工程师Robert Griesemer，Rob Pike和Ken Thompson设计。它是一种静态类型的编译语言。 2012 年 3 月发布了第一个开源版本。

> Go 是一种开源编程语言，可以轻松构建简单、可靠和高效的软件”。— GoLang

在很多计算机语言中，有很多方式可以去解决一个给定的问题。

程序员花费大量的时间去思考最好的方式去解决它。

而Go功能简洁，只有一种正确的方式去解决问题。

这样可以节约程序员的时间，并且使大型代码库易于维护。

Go里面没有像映射(maps)和过滤器(filters)这样富有表现力的特征。

> “当你有增加表现力的功能时，它通常会增加成本”——罗伯·派克

### 2. 开始

> 本文以windows为例，所以只安装windows下的 `go`，下载地址为：`https://golang.google.cn/dl/go1.21.0.windows-amd64.msi`

Go 是由包组成的。 main 包告诉 Go 编译器，程序被编译为可执行文件，而不是共享库。它是应用程序的入口点。主包定义为：

```go
package main
```

我们先写一个简单的 `hello world` 示例，方法就是在 Go GOPATH中创建 `main.go` 文件。

### 3. 工作区

Go的工作区是由环境变量`GOPATH`决定的。  

你可以在工作区里写任意代码，Go会在`GOPATH`或者`GOROOT`目录下搜索包，这是在安装Go时默认设置的。`GOROOT`是Go的安装路径。

设置`GOPATH`为你想要的目录。现在，咱们设置它的目录为 `~/workspace`：

```shell
# 环境变量
export GOPATH=~/workspace
# 进入工作区目录
cd ~/workspace
```

以上是在linux下设置的，但本次分享是在Windows下进行的，所以我们设置Windows下的环境变量，设置的目录为 `D:\learn\gocode`

```shell
# 设置环境变量
go env GOPATH=D:\learn\gocode
# 恢复默认
go env -u GOPATH
```

在工作区目录里创建`mian.go`文件。

```go
package main

import (
 "fmt"
)

func main(){
  fmt.Println("Hello World!")
}
```

在上面的例子中，`fmt` 是Go中的内置包，主要用来格式化输入/输出。

在 Go 中我们使用 `import` 来导入一个包文件，`func main`是执行代码的入口，`Println` 是包fmt中的一个函数，它为我们打印 `“hello world”`。

让我们运行这个文件来看看。Go有两种运行方式。正如我们所知，Go 是一种编译语言，所以我们首先要在执行之前编译它。

```shell
go build main.go
```

这个命令会生成二进制可执行文件 main，然后我们再运行它。

```shell
main.exe
#Hello World!
```

还有另外一个简单的方法运行程序。`go run`可以抽象编译步骤，你可以简单的使用下面的命令执行程序。

```shell
go run main.go
# Hello World!
```

### 4. 变量

Go中的变量是显式声明的。Go 是一种静态类型语言。这意味着在变量在声明时会检查变量的类型。变量可以像下面这样声明：

```go
var a int
```

在本例中，该值默认设置为0。也可以直接指定变量的值，如下：

```go
var a = 1
```

在这里，变量被自动赋值为 `int` 型。我们也可以对变量进行一个简短的声明，如下:

```go
message := "hello world"
```

我们也可以在一行声明多个变量，如下：

```go
var b, c int = 2, 3
```

### 5. 数据类型

像其他一些计算机语言，Go 也支持各种不同的变量类型，如下：

#### 5.1 数字，字符串 和 布尔型

Go 支持的数字存储类型有很多，比如 `int`, `int8`, `int16`, `int32`, `int64`,`uint`, `uint8`, `uint16`, `uint32`, `uint64`, `uintptr` 等等。

字符串类型存储一个字节序列。使用关键字`string`来表示和声明。

布尔型使用`bool`声明。

Go 还支持复数类型的数据类型，可以使用`complex64`和`complex128`进行声明。

```go
var a bool = true
var b int = 1
var c string ="hello world"
var d float32 = 1.222
var x complex128 = cmplx.Sqrt(-5+12i)
```

#### 5.2 数组(Arrays), 切片(Slice) 和 映射(Maps)

数组是具有相同数据类型的元素的序列。数组在声明时定义了固定长度，因此不能随意扩展超。如下：

```go
var s [5]int
```

数组也可以是多维的，声明方式如下：

```go
var multiD [2][3]int
```

Go 中的数组有一定限制，比如不能修改数组长度、不能添加元素、不能获取子数组。这时候，更适合使用切片(slices)这一类型。

切片(slices)用于存储一组元素，允许随时扩展其长度。切片(slices)的声明类似数组，只是去掉了长度声明。

```go
var b []int
```

这行代码会创建一个 0容量、0长度的切片。也可以使用以下代码设置切片的容量和长度。

```go
numbers := make([]int,5,10)
```

这里，切片的初始长度是5，容量是10。

切片是数组的抽象。切片使用数组作为底层结构。切片包含三个组成部分:容量、长度和指向底层数组的指针。

切片的容量可以通过`append`或`copy`函数来增加。`append` 函数将值添加到数组的末尾，并在需要时增加容量。

```go
numbers = append(numbers, 1, 2, 3, 4)
```

另一个增加切片容量的方法是`copy`函数。只需创建另一个容量更大的片，并将原始片复制到新创建的片：

```go
// 创建一个新的大容量的切片
number2 := make([]int, 15)
// 把原来的切片复制到新切片
copy(number2, numbers)
```

我们可以创建一个切片的子切片吗？这个可以用如下简单的代码来完成：

```go
// 初始化一个长度为4并有值的切片
number2 = []int{1,2,3,4}
fmt.Println(number2) // -> [1 2 3 4]
// 创建一个子切片
slice1 := number2[2:]
fmt.Println(slice1) // -> [3 4]
slice2 := number2[:3]
fmt.Println(slice2) // -> [1 2 3]
slice3 := number2[1:4]
fmt.Println(slice3) // -> [2 3 4]
```

Maps也是Go的一个数据类型，用于记录键值间的映射关系。我们可以用下面的命令定义一个 `map` :

```go
var m map[string]int
```

这里 `m`是一个新的 `map`变量，它有字符型的主键和整型的值，我们可以很容易的给 `map` 加主键和值：

### 6. 类型转换

可以使用类型转换将一种数据类型转换为另一种数据类型。我们来看一个简单的类型转换:

```go
a := 1.1
b := int(a)
fmt.Println(b)
//-> 1
```

并非所有的数据类型都能转换成其他类型。确保数据类型与转换类型相互兼容。

### 7. 条件语句

#### 7.1 if else

对于条件语句，我们可以使用if-else语句，如下例所示。确保花括号与条件在同一行。

```go
if num := 9; num < 0 {
 fmt.Println(num, "is negative")
} else if num < 10 {
 fmt.Println(num, "has 1 digit")
} else {
 fmt.Println(num, "has multiple digits")
}
```

#### 7.2 switch case

switch-case用于组织多个条件语句，下面的例子展示了一个简单的switch case语句:

```go
i := 2
switch i {
case 1:
 fmt.Println("one")
case 2:
 fmt.Println("two")
default:
 fmt.Println("none")
}
```

####7.3 循环

Go的循环只有一个关键字。`for` 循环命令可以帮助实现不同类型的循环:

```go
i := 0
sum := 0
for i < 10 {
 sum += 1
  i++
}
fmt.Println(sum)
```

以上代码类似于C语言中的`while`循环。相同的语句可以用在普通的 `for` 循环：

```go
sum := 0
for i := 0; i < 10; i++ {
  sum += i
}
fmt.Println(sum)
```

Go中的死循环

```go
for {
}
```

### 8. 指针

Go 提供了指针。指针是保存值的地址的地方。指针由 `*` 定义。指针是根据数据类型来定义的。如下：

```go
var ap *int
```

这里`ap`是指向整型的指针。`&` 操作符用于获取变量的地址。

```go
a := 12
ap = &a
```

指针所指向的值可以使用 `*` 操作符访问:

```go
fmt.Println(*ap)
// => 12
```

在将结构体作为参数传递或为已定义的类型声明方法时，通常首选指针。

- 当传递值时，值实际上被复制，这意味着更多的内存。
- 传递指针后，方法/函数可以直接修改指针所指向的值。

比如：

```go
func increment(i *int) {
  *i++
}
func main() {
  i := 10
  increment(&i)
  fmt.Println(i)
}
//=> 11
```

注意：不要忘记在需要的时候写上package main和import fmt或其他包

### 9. 函数

`main`包中定义的`main`函数是go程序执行的入口，我们还可以定义和使用更多其他函数。先来看个例子吧：

```go
func add(a int, b int) int {
 c := a + b
 return c
}
func main() {
 fmt.Println(add(2, 1))
}
//=> 3
```

如上所示，一个 Go 函数是用 `func` 关键字和函数名定义的。函数接受的参数需要根据它的数据类型来定义，最后是返回的数据类型。

函数的返回值也可以在函数中提前定义：

```go
func add(a int, b int) (c int) {
  c = a + b
  return
}
func main() {
  fmt.Println(add(2, 1))
}
//=> 3
```

这里 `c` 被定义为返回变量。因此，定义的变量 `c` 将自动返回，而不需要在最后的返回语句中定义。

您也可以从单个函数返回多个返回值，返回值之间用逗号分隔。

```go
func add(a int, b int) (int, string) {
  c := a + b
  return c, "successfully added"
}
func main() {
  sum, message := add(2, 1)
  fmt.Println(message)
  fmt.Println(sum)
}
```

### 10. 方法、结构体和接口

Go 并不是一种完全面向对象的语言，但是通过结构、接口和方法，让它有了很多面向对象的支持和效果。

#### 10.1 结构体(Struct)

结构体包含不同类型的字段，可用来对数据进行分组。例如，如果我们要对Person类型的数据进行分组，那么可以定义一个人的各种属性，包括姓名，年龄，性别等。

结构体是不同字段的类型化集合。结构体用于将数据进行分组。例如，如果我们想对Person类型的数据进行分组，我们定义一个人的属性，该属性包括姓名、年龄、性别。结构体可以使用以下语法定义:

```go
type person struct {
  name string
  age int
  gender string
}
```

Person类型定义后，现在我们来创建一个 Person对象:

```go
//方法 1: 指定参数和值
p := person{name: "Bob", age: 42, gender: "Male"}
//方法 2: 仅指定值
person{"Bob", 42, "Male"}
```

我们可以容易的使用`.`来获取一个对象的参数。

```go
p.name
//=> Bob
p.age
//=> 42
p.gender
//=> Male
```

你也可以通过结构体的指针对象来获取参数。

```go
pp := &person{name: "Bob", age: 42, gender: "Male"}
pp.name
//=> Bob
```

#### 10.2 方法(Methods)

方法是一种带有接收器的特殊函数。一个接收器可以是一个值或指针。我们可以创建一个叫 `describe` 的方法作为刚刚创建的Person类型的接收器，如下：

```go
package main
import "fmt"

// 定义结构体
type person struct {
  name   string
  age    int
  gender string
}

// 定义方法
func (p *person) describe() {
  fmt.Printf("%v is %v years old.", p.name, p.age)
}
func (p *person) setAge(age int) {
  p.age = age
}

func (p person) setName(name string) {
  p.name = name
}

func main() {
  pp := &person{name: "Bob", age: 42, gender: "Male"}
  pp.describe()
  // => Bob is 42 years old
  pp.setAge(45)
  fmt.Println(pp.age)
  //=> 45
  pp.setName("Hari")
  fmt.Println(pp.name)
  //=> Bob
}
```

正如我们在上面的例子中看到的那样，现在可以使用点操作符pp.describe来调用该方法。注意，接收器是一个指针。有了指针，我们传递了一个值的引用，所以如果我们在方法中做了任何改变，它将反映在接收器pp中。它也不会创建对象的新副本，这节省了内存。

注意，在上面的例子中，`age` 的值被改变了，而 `name` 的值没有改变，因为 `setName`是接收者类型，而 `setAge` 是指针类型。

#### 10.3 接口

在 Go 中，接口是方法的集合。接口可以对一个类型的属性进行分组，我们以动物为例，比如：

```go
type animal interface {
  description() string
}
```

这里`animal`是一个接口。现在让我们来创建两种不同类型的动物来实现`animal`接口。

```go
package main

import (
  "fmt"
)

type animal interface {
  description() string
}

type cat struct {
  Type  string
  Sound string
}

type snake struct {
  Type      string
  Poisonous bool
}

func (s snake) description() string {
  return fmt.Sprintf("Poisonous: %v", s.Poisonous)
}

func (c cat) description() string {
  return fmt.Sprintf("Sound: %v", c.Sound)
}

func main() {
  var a animal
  a = snake{Poisonous: true}
  fmt.Println(a.description())
  a = cat{Sound: "Meow!!!"}
  fmt.Println(a.description())
}

//=> Poisonous: true
//=> Sound: Meow!!!
```

在main函数中，我们创建了 一个类型为 `animal`的变量 `a`，然后把蛇和猫分配给类型 `animal` ，并且打印`a.description`。因此我们用两种类型(猫和蛇)以不同的方式实现了方法，最后我们得到了关于动物类型的描述。

### 11. 包

在 Go 中，所有的代码都写在包里面。`main`包是程序执行的入口，Go 自带了很多内置包，最有名的就是刚刚用过的`fmt`包。

> “Go packages in the main mechanism for programming in the large that go provides and they make possible to divvy up a large project into smaller pieces.”  
> — Robert Griesemer

翻译不出来，感觉大意就是 Go 包是 Go 的特色，可以把大型项目分成很多个小包，好维护。

#### 11.1 安装一个包go

```go
go get <package-url-github>
// 举个例子
go get github.com/satori/go.uuid
```

包默认安装在`GOPATH`环境变量设置的工作区中。可以使用`cd $GOPATH/pkg`命令进入目录，查看已安装的包。windows下是`cd %GOPATH%\pkg`，目前这个`GOPATH`还是在win下不好用。

#### 11.2 自定义包

首先在 `$GOPATH\src`目录下创建一个`custom_package`文件夹

```shell
mkdir custom_package
cd custom_package
```

要创建自定义包，我们首先要创建一个包含所需包名的文件夹，那我们就创建刚刚提到的`person`包，即在`custom_package`目录下创建一个`person`文件夹，如下：

```shell
mkdir person
cd person
```

然后在 `person` 文件夹下创建一个 `person.go`文件

```go
package person
func Description(name string) string {
  return "The person name is: " + name
}
func secretName(name string) string {
  return "Do not share"
}
```

现在我们需要安装这个包，以便引入并使用它。现在我们来安装它，如下：

```go
> go install person
```

然后我们回到`main`目录下，创建一个`20.go`文件。

```go
package main
import(
  "custom_package/person"
  "fmt"
)
func main(){ 
  p := person.Description("Milap")
  fmt.Println(p)
}
// => The person name is: Milap
```

现在，我们可以导入我们创建的包 `person` 并使用 `Description` 函数了。注意，我们在包中创建的函数 `secretName` 将不可访问。在 Go 中，不是大写字母开头的方法名是私有的。

#### 11.3 包的文档

下载 `godoc`

```shell
go env -w GO111MODULE=on
go env -w GOPROXY=https://goproxy.cn,direct
go get golang.org/x/tools/cmd/godoc

go: downloading golang.org/x/tools v0.12.0
go: downloading golang.org/x/sys v0.11.0
go: downloading github.com/yuin/goldmark v1.4.13
go: downloading golang.org/x/mod v0.12.0
go: downloading github.com/yuin/goldmark v1.5.5
go: trying upgrade to github.com/yuin/goldmark@v1.5.5
go: added github.com/yuin/goldmark v1.5.5
go: added golang.org/x/mod v0.12.0
go: added golang.org/x/sys v0.11.0
go: added golang.org/x/tools v0.12.0
```

Go 内置了对包文档。运行以下命令生成文档:

```go
go doc person Description

// 结果
package person // import "custom_package/person"

func Description(name string) string
```

这将为包 `person` 中的 `Description` 函数生成文档。要查看文档，使用以下命令运行web服务器:

```shell
godoc -http=":8080"
```

打开这个链接 [http://localhost:8080/pkg](http://localhost:8080/pkg)，就能看到文档了。

### 12. Go中的一些内置包

#### 12.1 fmt

`fmt`包实现了格式化输入输出的功能。我们已经使用过这个包进行标准输出了。

#### 12.2 json

Go 中另外一个很有用的包是`json`，它用来编码/解码`Json`数据。我们来看一些邓编码/解码的例子：

```go
// 编码
package main

import (
  "fmt"
  "encoding/json"
)

func main(){
  mapA := map[string]int{"apple": 5, "lettuce": 7}
  mapB, _ := json.Marshal(mapA)
  fmt.Println(string(mapB))
}
// 解码
package main

import (
  "fmt"
  "encoding/json"
)

type response struct {
  PageNumber int `json:"page"`
  Fruits []string `json:"fruits"`
}

func main(){
  str := `{"page": 1, "fruits": ["apple", "peach"]}`
  res := response{}
  json.Unmarshal([]byte(str), &res)
  fmt.Println(res.PageNumber)
}
//=> 1
```

当使用`Unmarshal`解码json字节时，第一个参数是json字节，第二个参数是我们期望的解码后的结构体指针。注意：`json:"page"`负责把`page`映射到结构体中的`PageNumber`键上。

### 13. 错误处理

错误是程序不希望出现的和意想不到的结果。假设我们正在对外部服务进行API调用。此API调用可能成功，也可能失败。当出现错误类型时，可以识别出程序中的错误。我们来看看这个例子:

```go
resp, err := http.Get("http://example.com/")
```

在这里，对错误对象的API调用可能通过，也可能失败。我们可以检查错误是否为nil或者存在错误，并正确地处理响应：

```go
package main

import (
  "fmt"
  "net/http"
)

func main(){
  resp, err := http.Get("http://example.com/")
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(resp)
}
```

#### 13.1 返回自定义错误

在写函数时，我们可能会遇到需要报错的情景，这时可以返回一个自定义的`error`对象。

当我们编写自己的函数时，有时会出现错误。这些错误可以自定义一个 `error` 对象返回：

```go
func Increment(n int) (int, error) {
  if n < 0 {
    // return error object
    return 0, errors.New("math: cannot process negative number")
  }
  return (n + 1), nil
}
func main() {
  num := 5

  if inc, err := Increment(num); err != nil {
    fmt.Printf("Failed Number: %v, error message: %v", num, err)
  }else {
    fmt.Printf("Incremented Number: %v", inc)
  }
}
```

Go 内置的大多数包，或者我们使用的外部包，都有错误处理机制。所以我们调用的任何函数都可能有错误。这些错误永远不会被忽略，并且总是在调用时总能被很好地处理，就像我们在上面的例子中所做的那样。

#### 13.2 Panic

Panic是指在程序执行过程中突然遇到的无法处理的问题。在Go中，panic不是处理程序异常的理想方式。建议使用error对象。当出现panic时，程序会停止运行，但会运行`defer`语句代码。

```go
//Go
package main

import "fmt"

func main() {
    f()
    fmt.Println("Returned normally from f.")
}

func f() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered in f", r)
        }
    }()
    fmt.Println("Calling g.")
    g(0)
    fmt.Println("Returned normally from g.")
}

func g(i int) {
    if i > 3 {
        fmt.Println("Panicking!")
        panic(fmt.Sprintf("%v", i))
    }
    defer fmt.Println("Defer in g", i)
    fmt.Println("Printing in g", i)
    g(i + 1)
}
```

#### 13.3 Defer

`Defer` 总是在函数结束时执行。

在上面的例子中，我们使用panic()来执行panic。如你所注见，有一个总是需要在函数结束执行后执行的defer语句。当我们需要在函数末尾执行某些操作时，例如关闭文件，就可以使用Defer。

### 14. 并发

Go 在设计时就考虑了并发性。 Go 中的并发可以通过轻量级线程`Go routines`来实现。

#### 14.1 Go routine

`Go routine`是可以与另一个函数并行或并发运行的函数。创建一个`Go routine`非常简单。只需在函数前面添加关键字Go，就可以使其并行执行。`Go routine`非常轻量级，因此我们可以创建数千个`routine`。让我们来看一个简单的例子:

```go
package main
import (
  "fmt"
  "time"
)
func main() {
  go c()
  fmt.Println("I am main")
  time.Sleep(time.Second * 2)
}
func c() {
  time.Sleep(time.Second * 2)
  fmt.Println("I am concurrent")
}
//=> I am main
//=> I am concurrent
```

正如你在上面的例子中看到的，函数c是一个与Go主线程并行执行的 `Go routine`。有时我们希望在多个线程之间共享资源。Go不喜欢与另一个线程共享一个线程的变量，因为这会增加死锁和资源等待的机会。还有另一种方法可以在 `Go routine` 之间共享资源：那就是 `go channels`。

#### 14.2 Channels

我们可以使用通道在两个 `Go routine` 之间传递数据。在创建通道时，有必要指定通道接收的数据类型。让我们创建一个字符串类型的通道，如下所示:

```go
c := make(chan string)
```

有了这个通道，我们可以发送字符串类型的数据。我们可以在这个通道中发送和接收数据:

```go
package main

import "fmt"

func main(){
  c := make(chan string)
  go func(){ c <- "hello" }()
  msg := <-c
  fmt.Println(msg)
}
//=>"hello"
```

接收方`channel`会一直等待，直到发送方将数据发数据到`channel`。

#### 14.3 单向channel

在某些情况下，我们希望 `Go routine` 通过通道接收数据但不发送数据，反之亦然。为此，我们还可以创建一个单向通道。让我们来看一个简单的例子:

```go
package main

import (
 "fmt"
)

func main() {
 ch := make(chan string)

 go sc(ch)
 fmt.Println(<-ch)
}

func sc(ch chan<- string) {
 ch <- "hello"
}
```

在上面的例子中，sc是一个 `Go routine` 例程，它只能向通道发送消息，但不能接收消息。

#### 14.4 使用`select`语句在`Go routine`中处理多个`channel`

一个函数可能正在等待多个通道。这时，我们可以使用`select`语句。让我们看一个更清楚的例子：

```go
package main

import (
 "fmt"
 "time"
)

func main() {
 c1 := make(chan string)
 c2 := make(chan string)
 go speed1(c1)
 go speed2(c2)
 fmt.Println("Th first to arrive is:")
 select {
 case s1 := <-c1:
  fmt.Println(s1)
 case s2 := <-c2:
  fmt.Println(s2)
 }
}

func speed1(ch chan string) {
 time.Sleep(2 * time.Second)
 ch <- "speed 1"
}

func speed2(ch chan string) {
 time.Sleep(1 * time.Second)
 ch <- "speed 2"
}
```

在上面的示例中，主进程正在等待两个通道c1和c2。对于主函数打印的select case语句，消息从第一个接收到的通道发送。

#### 14.5 Buffered channel

您可以在go中创建缓冲通道。对于缓冲通道，如果缓冲区已满，则发送到该通道的消息将被阻塞。让我们来看看这个例子：

```go
package main

import "fmt"

func main(){
  ch := make(chan string, 2)
  ch <- "hello"
  ch <- "world"
  ch <- "!" // extra message in buffer
  fmt.Println(<-ch)
}

// => fatal error: all goroutines are asleep - deadlock!
```

正如我们在上面看到的，一个通道不能接受超过2个消息。

### 15. 为什么 `Golang` 能够成功呢？

> Simplicity… — Rob-pike  
> 
> 因为简单...

好了，我们今天学习了Go的一些主要组件和特性。希望大家能有一些收获吧~！
