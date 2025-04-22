title: go测试库apitest简介
date: 2023-08-23
category: 测试
tag: go, apitest

[TOC]

### 1. 开始

#### 1.1. 概述

apitest是一个简单且可扩展的 Go 语言测试库。你可以使用 `apitest` 来简化 REST 服务、HTTP handlers(事件处理器) 和HTTP客户端的测试。

#### 1.2. 特征

- 可模拟外部http调用

- 在测试完成时可呈现序列图

- 可扩展——支持各种注入点

- GraphQL（一种用于 API 的查询语言）支持

- 自定义断言函数和模拟匹配器

- JSON路径断言，css选择器断言等等

#### 1.3. 安装

```shell
go get -u github.com/steinfletcher/apitest
# 使用时导入
import "github.com/steinfletcher/apitest"
# 就咱们现在这种网络状态，第一种方法基本不能用，目前只能手动下载，然后手动放到GOPATH/src/github.com/下。
```

apitest遵循语义版本控制，使用 Github 版本管理发布。

#### 1.4. 一个测试例子的解析

例子主要包括三个部分

配置：定义将要测试的HTTP请求处理程序和所有其他特定的测试配置，例如模拟、调试模式和报告

请求：定义测试输入，这通常是一个http请求需要的

预期：定义被测应用程序应该如何响应。这通常是一个http响应需要的

```go
package main

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestGetMessage(t *testing.T) {
    handler := func(w http.ResponseWriter, r *http.Request) {
        msg := `{"message": "hello"}`
        _, _ = w.Write([]byte(msg))
        w.WriteHeader(http.StatusOK)
    }

    apitest.New(). // 配置
            HandlerFunc(handler).  // 不通过网络进行 HTTP 调用
            Get("/message"). // 请求，必须写
            Expect(t).       // Expect(t).Body 匹配 HTTP 响应体
            Body(`{"message": "hello"}`).
            Status(http.StatusOK).  // 断言http状态 http.StatusOK = 200
            End()  // 测试结束
}
```

使用 `go test` 执行测试，`go test -v` 打印测试函数的所有细节，如下：

```shell
$ go test 1_hello_test.go
ok      command-line-arguments  0.217s

=============================================

$ go test -v 1_hello_test.go
=== RUN   TestGetMessage

----------> inbound http request
GET /message HTTP/1.1
Host: sut



<---------- final response
HTTP/1.1 200 OK
Connection: close
Content-Type: text/plain; charset=utf-8

{"message": "hello"}
Duration: 0s

--- PASS: TestGetMessage (0.00s)
PASS
ok      command-line-arguments  0.220s5s
```

源文件和测试文件放在同一目录下，测试文件以 `_test` 结尾，这个是固定格式，使用 `go build` 进行编译时，`_test` 文件不会编译。每个测试函数需要以 `Test` 为前缀，每个性能测试函数需要以 `Benchmark` 为前缀。

### 2. 配置

`APITest` 配置类型公开了一些方法来注册测试钩子、启用调试日志记录、并定义被测处理程序。

#### 2.1. Debug

启用调试日志记录并把所有请求和响应交互的http连接情况写入控制台。

```go
apitest.New().
  Debug().
  Handler(myHandler)
```

这样会记录整个模拟交互过程，这对于定位失败测试用例背后的原因非常有用。在下面的示例中，由于模拟的 URL 不正确，导致不匹配。控制台会将每个模拟不匹配的原因记录下来。

```shell
----------> inbound http request
GET /user HTTP/1.1
Host: application

failed to match mocks. Errors: received request did not match any mocks

Mock 1 mismatches:
• received path /user/12345 did not match mock path /preferences/12345

Mock 2 mismatches:
• received path /user/12345 did not match mock path /user/123456

----------> request to mock
GET /user/12345 HTTP/1.1
Host: localhost:8080
User-Agent: Go-http-client/1.1
Accept-Encoding: gzip
...
```

#### 2.2. HTTP Handler

应该使用 Handler 或 HandlerFunc 测试定义的 `handler`，其中 myHandler 是 一个Go的 `http.handler`。

```go
apitest.New().Handler(myHandler)
```

设置 Handler 时，apitest 不会通过网络进行 HTTP 调用。相反，提供的 HTTP Handler 的 `serveHTTP` 方法在与测试代码相同的进程中调用。用户定义的请求和响应将通过 Go 的 `httptest` 包转换成 `http.Request` 和 `http.Response` 类型。这里的目标是测试内部应用程序而非网络。这种方法使测试既快速又简单。如果你想要用真正的 http 客户端发起一个请求去运行应用程序，则需要通过网络执行。

Handler 例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestHandler(t *testing.T) {
    handler := http.NewServeMux()
    handler.HandleFunc("/data", func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(http.StatusOK)
    })

    apitest.New().
        Handler(handler).
        Get("/data").
        Expect(t).
        Status(http.StatusOK).
        End()
}
```

HandlerFunc 例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestHandlerFunc(t *testing.T) {
    handlerFunc := func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(http.StatusOK)
    }

    apitest.New().
        HandlerFunc(handlerFunc).
        Post("/login").
        Expect(t).
        Status(http.StatusOK).
        End()
}
```

#### 2.3. Hooks

**Intercept**

在请求调用前，`Intercept` 和 `Observe`类似。允许请求发起者将请求对象发送到被测系统之前对其进行更改。在此示例中，我们使用自定义方案设置请求参数。

```go
package main

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestIntercept(t *testing.T) {
    handler := func(w http.ResponseWriter, r *http.Request) {
        if r.URL.RawQuery != "a[]=xxx&a[]=yyy" {
            t.Fatal("unexpected query")
        }
        w.WriteHeader(http.StatusOK)
    }

    apitest.New().
        HandlerFunc(handler).
        Intercept(func(req *http.Request) {
            req.URL.RawQuery = "a[]=xxx&a[]=yyy"
        }).
        Get("/").
        Expect(t).
        Status(http.StatusOK).
        End()
}
```

**Observe**

`Observe` 可用于在测试完成时检查请求、响应和 APITest 实例。此方法在 apitest 内部使用，以捕获跨模拟服务器的所有交互，从而呈现测试结果。

```go
package main

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestObserve(t *testing.T) {
    var observeCalled bool

    apitest.New().
        Observe(func(res *http.Response, req *http.Request, apiTest *apitest.APITest) {
            observeCalled = true
            if http.StatusOK != res.StatusCode {
                t.Fatal("unexpected status code")
            }
        }).
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.WriteHeader(http.StatusOK)
        }).
        Get("/hello").
        Expect(t).
        Status(http.StatusOK).
        End()

    if !observeCalled {
        t.Fatal("Observe not called")
    }
}
```

#### 2.4. Networking

如果要针对正在运行的应用程序发起 HTTP 请求，则需要网络。并传递带有 cookie 的 http 请求，类似浏览器的会话行为，其中 cookie 要在多个 apitest 请求中留从。此方法可用于执行端到端的测试。

```go
package main

import (
    "fmt"
    "net/http"
    "net/http/cookiejar"
    "testing"
    "time"

    "github.com/steinfletcher/apitest"
)

// TestEnableNetworking creates a server with two endpoints, /login sets a token via a cookie and /authenticated_resource
// validates the token. A cookie jar is used to verify session persistence across multiple apitest instances
func TestEnableNetworking(t *testing.T) {
    srv := &http.Server{Addr: "localhost:9876"}
    finish := make(chan struct{})
    tokenValue := "ABCDEF"

    http.HandleFunc("/login", func(w http.ResponseWriter, r *http.Request) {
        http.SetCookie(w, &http.Cookie{Name: "Token", Value: tokenValue})
        w.WriteHeader(203)
    })

    http.HandleFunc("/authenticated_resource", func(w http.ResponseWriter, r *http.Request) {
        token, err := r.Cookie("Token")
        if err == http.ErrNoCookie {
            w.WriteHeader(400)
            return
        }
        if err != nil {
            w.WriteHeader(500)
            return
        }

        if token.Value != tokenValue {
            t.Fatalf("token did not equal %s", tokenValue)
        }
        w.WriteHeader(204)
    })

    go func() {
        if err := srv.ListenAndServe(); err != nil {
            panic(err)
        }
    }()

    go func() {
        defer func() {
            if r := recover(); r != nil {
                fmt.Println("Recovered in f", r)
            }
        }()

        cookieJar, _ := cookiejar.New(nil)
        cli := &http.Client{
            Timeout: time.Second * 1,
            Jar:     cookieJar,
        }

        apitest.New().
            EnableNetworking(cli).
            Get("http://localhost:9876/login").
            Expect(t).
            Status(203).
            End()

        apitest.New().
            EnableNetworking(cli).
            Get("http://localhost:9876/authenticated_resource").
            Expect(t).
            Status(204).
            End()

        finish <- struct{}{}
    }()

    <-finish
}
```

### 3. 请求

要配置对被测系统的初始请求，您可以指定请求参数，例如 http 方法、url、标头和 cookie。

```go
apitest.New().
    Handler(handler).
    Method(http.MethodGet).
    URL("/user/12345")
```

这非常冗长，因此为常见的 http 动作定义了一些快捷方式，这些动作对方法和 URL 进行了封闭。该示例可以更简洁地表示为：

```go
apitest.Handler(handler).
    Get("/user/12345")
```

你还可以用标准的 Go http.Request 来定义请求。

```go
req := httptest.NewRequest(http.MethodGet, "/user/1234", nil)
apitest.Handler(handler).
    Request(req)
```

#### 3.1. Basic Auth

提供了一个向请求添加基本身份验证的方法。

`BasicAuth("username", "password")`

例子

```go
package main

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestRequests_BasicAuth(t *testing.T) {
    handler := func(w http.ResponseWriter, r *http.Request) {
        username, password, ok := r.BasicAuth()
        if !ok {
            w.WriteHeader(http.StatusBadRequest)
            return
        }

        if username != "username" || password != "password" {
            w.WriteHeader(http.StatusBadRequest)
            return
        }

        w.WriteHeader(http.StatusOK)
    }

    apitest.New().
        HandlerFunc(handler).
        Get("/hello").
        BasicAuth("username", "password").
        Expect(t).
        Status(http.StatusOK).
        End()
}
```

#### 3.2. Body

有两个方法去设置请求体--`Bady` 和 `JSON` 。使用 `Body` 将数据复制到原始请求中并包装在 `io.Reader`。

```go
Post("/message").Body("hello")
```

`JSON` 执行相同的操作并将提供的数据复制到正文，但 `JSON` 方法还将内容类型设置为 `application/json`。

```go
Post("/chat").JSON(`{"message": "hi"}`)
```

如果要定义其他内容类型，请使用 `Body(data)` 设置包体，使用 `header` 设置标头。

```go
Post("/path").
Body("<html>content</html>").
Header("Content-Type", "text/html")
```

JSON 包体例子

```go
package main

import (
    "io/ioutil"
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestRequests_JSONBody(t *testing.T) {
    handler := func(w http.ResponseWriter, r *http.Request) {
        data, _ := ioutil.ReadAll(r.Body)
        if string(data) != `{"a": 12345}` {
            w.WriteHeader(http.StatusInternalServerError)
            return
        }
        if r.Header.Get("Content-Type") != "application/json" {
            w.WriteHeader(http.StatusBadRequest)
            return
        }
        w.WriteHeader(http.StatusOK)
    }

    apitest.New().
        HandlerFunc(handler).
        Post("/hello").
        JSON(`{"a": 12345}`).
        Expect(t).
        Status(http.StatusOK).
        End()
}
```

文本包体例子

```go
package main

import (
    "io/ioutil"
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestRequests_TextBody(t *testing.T) {
    handler := func(w http.ResponseWriter, r *http.Request) {
        data, _ := ioutil.ReadAll(r.Body)
        if string(data) != `hello` {
            w.WriteHeader(http.StatusInternalServerError)
            return
        }
        w.WriteHeader(http.StatusOK)
    }

    apitest.New().
        HandlerFunc(handler).
        Put("/hello").
        Body(`hello`).
        Expect(t).
        Status(http.StatusOK).
        End()
}
```

#### 3.3. Cookies

有多种方法可以指定 http 的请求 cookie。这些方法可以一起使用。

**简短形式**

```go
Cookie("name", "value")
```

**结构**

Cookies 是一个被用于获取已定义的不同数量的 cookie 的结构体。

```go
Cookies(apitest.NewCookie("name").
    Value("value").
    Path("/user").
    Domain("example.com"))
```

该结构的底层字段都是指针类型。这样，断言库就可以忽略结构体中未定义的字段。

#### 3.4. Form

在请求中创建 URL 表单有多种方法。以下几种方法可以一起使用。

**多个值的Form**

FormData 是一个可变函数，可用于为同一键获取不同数量的值。

```go
FormData("name", "value1", "value2")
```

**简短的Form**

```go
FormData("name", "value")
```

#### 3.5. GraphQL

以下帮助程序可简化 GraphQL 请求的构建。

```go
Post("/graphql").
GraphQLQuery(`query { todos { text } }`).

Post("/graphql").
GraphQLRequest(apitest.GraphQLRequestBody{
    Query: "query someTest($arg: String!) { test(who: $arg) }",
    Variables: map[string]interface{}{
        "arg": "myArg",
    },
    OperationName: "myOperation",
}).
```

例子

```go
package main

import (
    "encoding/json"
    "io/ioutil"
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
    "github.com/stretchr/testify/assert"
)

func TestRequests_GraphQLQuery(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            bodyBytes, err := ioutil.ReadAll(r.Body)
            if err != nil {
                t.Fatal(err)
            }

            var req apitest.GraphQLRequestBody
            if err := json.Unmarshal(bodyBytes, &req); err != nil {
                t.Fatal(err)
            }

            assert.Equal(t, apitest.GraphQLRequestBody{
                Query: `query { todos { text } }`,
            }, req)

            w.WriteHeader(http.StatusOK)
        }).
        Post("/query").
        GraphQLQuery(`query { todos { text } }`).
        Expect(t).
        Status(http.StatusOK).
        End()
}

func TestRequests_GraphQLRequest(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            bodyBytes, err := ioutil.ReadAll(r.Body)
            if err != nil {
                t.Fatal(err)
            }

            var req apitest.GraphQLRequestBody
            if err := json.Unmarshal(bodyBytes, &req); err != nil {
                t.Fatal(err)
            }

            expected := apitest.GraphQLRequestBody{
                Query:         `query { todos { text } }`,
                OperationName: "myOperation",
                Variables: map[string]interface{}{
                    "a": float64(1),
                    "b": "2",
                },
            }

            assert.Equal(t, expected, req)

            w.WriteHeader(http.StatusOK)
        }).
        Post("/query").
        GraphQLRequest(apitest.GraphQLRequestBody{
            Query: "query { todos { text } }",
            Variables: map[string]interface{}{
                "a": 1,
                "b": "2",
            },
            OperationName: "myOperation",
        }).
        Expect(t).
        Status(http.StatusOK).
        End()
}
```

上面的例子需要下载一些依赖项，如下：

```shell
go get github.com/stretchr/testify
go get github.com/davecgh/go-spew
go get github.com/pmezard/go-difflib
go get gopkg.in/yaml.v3
```

#### 3.6. Headers

有多种方法可以指定 http 请求头。以下方法可以一起使用。

**Map**

```go
Headers(map[string]string{"name1": "value1", "name2": "value2"})
```

**Params**

```go
Header("name", "value")
```

#### 3.7. Intercept

`Intercept` 会在请求前调用，允许实现者在请求对象发送到被测系统前对其进行更改。在本例中，我们使用自定义方案设置请求参数。

```go
package main

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestIntercept(t *testing.T) {
    handler := func(w http.ResponseWriter, r *http.Request) {
        if r.URL.RawQuery != "a[]=xxx&a[]=yyy" {
            t.Fatal("unexpected query")
        }
        w.WriteHeader(http.StatusOK)
    }

    apitest.New().
        HandlerFunc(handler).
        Intercept(func(req *http.Request) {
            req.URL.RawQuery = "a[]=xxx&a[]=yyy"
        }).
        Get("/").
        Expect(t).
        Status(http.StatusOK).
        End()
}
```

#### 3.8. Query Params

有多种指定查询参数的方法。这些方法可以一起使用。

例子

```go
package main

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestRequests_Query(t *testing.T) {
    expectedQueryString := "a=1&a=2&a=9&a=22&b=2"
    handler := func(w http.ResponseWriter, r *http.Request) {
        if expectedQueryString != r.URL.RawQuery {
            w.WriteHeader(http.StatusBadRequest)
            return
        }
        w.WriteHeader(http.StatusOK)
    }

    apitest.New().
        HandlerFunc(handler).
        Get("/foo").
        Query("a", "9").
        Query("a", "22").
        QueryCollection(map[string][]string{"a": {"1", "2"}}).
        QueryParams(map[string]string{"b": "2"}).
        Expect(t).
        Status(http.StatusOK).
        End()
}
```

**Collection**

```go
QueryCollection(map[string][]string{"a": {"1", "2"}})
```

参数的值设置为 `a=1&a=2` 。

**Custom**

如果所提供的方法不合适，你可以定义自定义一个请求拦截器。

```go
apitest.New().
    Handler(handler).
    Intercept(func(req *http.Request) {
        req.URL.RawQuery = "a[]=xxx&a[]=yyy"
    }).
    Get("/path")
```

**Map**

```go
QueryParams(map[string]string{"param1": "value1", "param2": "value2"})
```

**Params**

```go
Query("param", "value")
```

### 4. 异常

我们提供了多种机制来验证响应。如果这些机制都不能满足您的需要，您可以提供自定义的 Assert 函数。定义请求后，必须调用 Expect(t) 去定义期望的结果。

#### 4.1. Body

通过在 `Body` 方法中输入字符串去匹配 HTTP 响应体。

```go
Expect(t).Body(`{"param": "value"}`)
```

断言库会检查内容是否为 JSON，如果是，则使用 testify 的 assert.JSONEq 方法执行断言。如果内容不是 JSON，则使用 testify 的 assert.Equal 方法。

```go
package body

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestAssertBody(t *testing.T) {
    apitest.New().
        HandlerFunc(handler).
        Get("/greeting").
        Expect(t).
        Body(`{"message": "hello"}`).
        End()
}

func handler(w http.ResponseWriter, r *http.Request) {
    w.WriteHeader(http.StatusOK)
    w.Header().Set("Content-Type", "application/json")
    _, _ = w.Write([]byte(`{"message": "hello"}`))
}
```

#### 4.2. Cookies

断言响应 cookie 的最简单方法是将 cookie 名称和值作为参数提供给 Cookie 方法。

```go
Cookie("name", "value")
```

例子

```go
package main

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestAssertCookies(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            http.SetCookie(w, &http.Cookie{Name: "name", Value: "value"})
            w.WriteHeader(http.StatusOK)
        }).
        Get("/data").
        Expect(t).
        Cookie("name", "value").
        End()
}
```

**Cookie Not Present**

这是与 CookiePresent 相反的行为，用于判断断言响应中不存在具有给定名称的 cookie。

```go
CookieNotPresent("Session-Token")
```

例子

```go
package main

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestAssertCookies_NotPresent(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            http.SetCookie(w, &http.Cookie{Name: "name", Value: "value"})
            w.WriteHeader(http.StatusOK)
        }).
        Get("/data").
        Expect(t).
        CookieNotPresent("token").
        End()
}
```

**Cookie Present**

有时，应用程序会生成一个具有动态值的 cookie。如果不需要断言值，可使用 CookiePresent 方法，它只会断言 cookie 已被设置为给定的键。

```go
CookiePresent("Session-Token")
```

apitest 会在内部保存 cookie，因此您可以多次调用此方法，对多个 cookie 进行断言。

例子

```go
package main

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestAssertCookies_Present(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            http.SetCookie(w, &http.Cookie{Name: "name", Value: "value"})
            w.WriteHeader(http.StatusOK)
        }).
        Get("/data").
        Expect(t).
        CookiePresent("name").
        End()
}
```

**Struct**

Cookies 是一个被用于获取已定义的不同数量的 cookie 的结构体。

```go
Cookies(apitest.NewCookie("name").
    Value("value").
    Path("/user").
    Domain("example.com"))
```

该结构的底层字段都是指针类型。这样，断言库就可以忽略结构体中未定义的字段。

例子

```go
package main

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestAssertCookies_Struct(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            http.SetCookie(w, &http.Cookie{Name: "name1", Value: "value1", Path: "/path1", Secure: true})
            http.SetCookie(w, &http.Cookie{Name: "name2", Value: "value2", Path: "/path2", Secure: false})
            w.WriteHeader(http.StatusOK)
        }).
        Get("/data").
        Expect(t).
        Cookies(
            apitest.NewCookie("name1").Value("value1").Secure(true).Path("/path1"),
            apitest.NewCookie("name2").Value("value2").Secure(false).Path("/path2"),
        ).
        End()
}
```

#### 4.3. 自定义

通过执行签名 `fn func(*http.Response, *http.Request) error`，提供自定义断言函数。

```go
Assert(func(res *http.Response, _ *http.Request) error {
    if res.StatusCode >= 200 && res.StatusCode < 400 {
        return nil
    }
    return errors.New("unexpected status code")
}).
```

自定义断言函数可以是链式的。

```go
package body

import (
    "errors"
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestAssert_Custom(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.WriteHeader(http.StatusCreated)
        }).
        Get("/data").
        Expect(t).
        Assert(isSuccess).
        End()
}

func isSuccess(res *http.Response, _ *http.Request) error {
    if res.StatusCode >= 200 && res.StatusCode < 400 {
        return nil
    }
    return errors.New("unexpected status code")
}
```

#### 4.4. Headers

有两种方法可以指定 HTTP 响应头。以下方法可以连锁使用。

**Map**

```go
Headers(map[string]string{"name1": "value1", "name2": "value2"})
```

头信息在 apitest 内部以规范形式存储。例如，"accept-encoding "的规范键是 "Accept-Encoding"。如果内容是 JSON，则使用 testify 的 assert.JSONEq 方法执行断言。如果内容不是 JSON，则使用 testify 的 assert.Equal 方法。

```go
package body

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestAssertHeaders_Map(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.Header().Set("name1", "value1")
            w.Header().Set("name2", "value2")
            w.WriteHeader(http.StatusOK)
        }).
        Get("/data").
        Expect(t).
        Headers(map[string]string{"name1": "value1", "name2": "value2"}).
        End()
}
```

**Params**

```go
Header("name", "value")
```

例子

```go
package body

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestAssertHeaders_Params(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.Header().Set("name", "value")
            w.WriteHeader(http.StatusOK)
        }).
        Get("/data").
        Expect(t).
        Header("name", "value").
        End()
}
```

#### 4.5. JSON Path

您可以使用 JSONPath 来断言响应中的部分内容。当你只对响应中的特定字段感兴趣时，这就很有用了。首先要安装一个单独的模块来提供这些断言，如下：

`get -u github.com/steinfletcher/apitest-jsonpath`

例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
    "github.com/steinfletcher/apitest-jsonpath"
)

func TestJSONPath(t *testing.T) {
    handler := http.NewServeMux()
    handler.HandleFunc("/data", func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(http.StatusOK)
        w.Header().Set("Content-Type", "application/json")
        _, _ = w.Write([]byte(`{
          "aValue": "0",
          "anObject": {"a": "1", "b":  12345},
          "matches": {
            "anObject": {
              "aString": "tom<3Beer",
              "aNumber": 7.212,
              "aBool": true
            },
            "aString": "tom<3Beer",
            "aNumber": 7,
            "aNumberSlice": [7, 8, 9],
            "aStringSlice": ["7", "8", "9"],
            "anObjectSlice": [{"key":  "c", "value": "ABC"}]
          }
        }`))
    })

    apitest.New().
        Handler(handler).
        Get("/data").
        Expect(t).
        Assert(jsonpath.Equal("aValue", "0")).
        Assert(jsonpath.NotEqual("aValue", "1")).
        Assert(jsonpath.Present("aValue")).
        Assert(jsonpath.NotPresent("x")).
        Assert(jsonpath.Equal(`$.anObject`, map[string]interface{}{"a": "1", "b": float64(12345)})).
        Assert(jsonpath.Contains(`$.matches.anObjectSlice[? @.key=="c"].value`, "ABC")).
        Assert(
            jsonpath.Root("matches").
                Matches(`aString`, `^[mot]{3}<3[AB][re]{3}$`).
                Matches(`aNumber`, `^\d$`).
                Matches(`anObject.aNumber`, `^\d\.\d{3}$`).
                Matches(`aNumberSlice[1]`, `^[80]$`).
                Matches(`anObject.aBool`, `^true$`).
                End(),
        ).
        Assert(
            jsonpath.Chain().
                NotPresent("password").
                NotEqual("aValue", "12").
                End(),
        ).
        End()
}
```

上面的项目需要用到如下依赖，如下：

```shell
go get github.com/steinfletcher/apitest-jsonpath
go get github.com/PaesslerAG/jsonpath
go get github.com/PaesslerAG/gval
go get github.com/shopspring/decimal
```

**Chain**

同时提供多种解决方案

```go
Assert(
    jsonpath.Chain().
        Equal("a", "1").
        NotEqual("b", "2").
        Present("c").
        End(),
).
```

例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
    "github.com/steinfletcher/apitest-jsonpath"
)

func TestJSONPath_Chain(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.WriteHeader(http.StatusOK)
            w.Header().Set("Content-Type", "application/json")
            _, _ = w.Write([]byte(`{"a": "1", "b": "3", "c": "4"}`))
        }).
        Get("/data").
        Expect(t).
        Assert(jsonpath.Chain().
            Equal("a", "1").
            NotEqual("b", "2").
            Present("c").
            End()).
        End()
}
```

**Contains**

当选择器返回使用 `Contains` 的数组类型时，假设响应中的 JSON 主体为 {"id"： 12345, "items"： [{"available": true, "color": "red"}, {"available": false, "color": "blue"}]}, 我们可以选择所有在结果中可用于断言的颜色值。

```go
Assert(jsonpath.Contains("$.items[?@.available==true].color", "red"))
```

例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
    "github.com/steinfletcher/apitest-jsonpath"
)

func TestJSONPath_Contains(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.WriteHeader(http.StatusOK)
            w.Header().Set("Content-Type", "application/json")
            _, _ = w.Write([]byte(`{
              "items": [
                {
                  "available": true,
                  "color": "red"
                },
                {
                  "available": false,
                  "color": "blue"
                }
              ]
            }`))
        }).
        Get("/data").
        Expect(t).
        Assert(jsonpath.Contains("$.items[?@.available==true].color", "red")).
        End()
}
```

**Equal**

当选择器返回单个值时，使用 Equal。假设响应中的 JSON 主体为 {"id"： "12345"}

```go
Assert(jsonpath.Equal("$.id", "12345"))
```

例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
    "github.com/steinfletcher/apitest-jsonpath"
)

func TestJSONPath_Equal(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.WriteHeader(http.StatusOK)
            w.Header().Set("Content-Type", "application/json")
            _, _ = w.Write([]byte(`{"message": "hello"}`))
        }).
        Get("/data").
        Expect(t).
        Assert(jsonpath.Equal("message", "hello")).
        End()
}
```

**Greater Than**

使用 "大于 "对返回值执行最小长度限制。

```go
Assert(jsonpath.GreaterThan("$.items", 2))
```

例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
    "github.com/steinfletcher/apitest-jsonpath"
)

func TestJSONPath_GreaterThan_LessThan(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.WriteHeader(http.StatusOK)
            w.Header().Set("Content-Type", "application/json")
            _, _ = w.Write([]byte(`{"items": [3, 4]}`))
        }).
        Get("/data").
        Expect(t).
        Assert(jsonpath.GreaterThan("items", 1)).
        Assert(jsonpath.LessThan("items", 3)).
        End()
}
```

**JWT Matchers**

`JWTHeaderEqual` 和 `JWTPayloadEqual` 可用于断言响应中的 JWT 内容（不会验证 JWT）。

```go
func Test(t *testing.T) {
    apitest.New().
        HandlerFunc(myHandler).
        Post("/login").
        Expect(t).
        Assert(jsonpath.JWTPayloadEqual(fromAuthHeader, `$.sub`, "1234567890")).
        Assert(jsonpath.JWTHeaderEqual(fromAuthHeader, `$.alg`, "HS256")).
        End()
}

func fromAuthHeader(res *http.Response) (string, error) {
    return res.Header.Get("Authorization"), nil
}
```

例子

```go
func Test(t *testing.T) {
    apitest.New().
        HandlerFunc(myHandler).
        Post("/login").
        Expect(t).
        Assert(jsonpath.JWTPayloadEqual(fromAuthHeader, `$.sub`, "1234567890")).
        Assert(jsonpath.JWTHeaderEqual(fromAuthHeader, `$.alg`, "HS256")).
        End()
}

func fromAuthHeader(res *http.Response) (string, error) {
    return res.Header.Get("Authorization"), nil
}
```

**Len**

使用 `Len` 检查返回值的长度。如果响应是 {"items"： [1, 2, 3]}，我们可以这样断言项的长度

```go
Assert(jsonpath.Len("$.items", 3))
```

例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
    "github.com/steinfletcher/apitest-jsonpath"
)

func TestJSONPath_Len(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            _, _ = w.Write([]byte(`{"items": [1, 2, 3]}`))
            w.WriteHeader(http.StatusOK)
        }).
        Get("/hello").
        Expect(t).
        Assert(jsonpath.Len(`$.items`, 3)).
        End()
}
```

**Less Than**

使用 `LessThan` 对返回值执行最大长度限制。

```go
Assert(jsonpath.LessThan("$.items", 2))
```

例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
    "github.com/steinfletcher/apitest-jsonpath"
)

func TestJSONPath_GreaterThan_LessThan(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.WriteHeader(http.StatusOK)
            w.Header().Set("Content-Type", "application/json")
            _, _ = w.Write([]byte(`{"items": [3, 4]}`))
        }).
        Get("/data").
        Expect(t).
        Assert(jsonpath.GreaterThan("items", 1)).
        Assert(jsonpath.LessThan("items", 3)).
        End()
}
```

**Matches**

使用 `Matches` 检查字符串、数字或布尔类型的单个路径元素是否与正则表达式匹配。

```go
Assert(jsonpath.Matches("$.a", "^[abc]{1,3}$"))
```

例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
    "github.com/steinfletcher/apitest-jsonpath"
)

func TestJSONPath_Matches(t *testing.T) {
    handler := http.NewServeMux()
    handler.HandleFunc("/data", func(w http.ResponseWriter, r *http.Request) {
        w.WriteHeader(http.StatusOK)
        w.Header().Set("Content-Type", "application/json")
        _, _ = w.Write([]byte(`{
          "matches": {
            "anObject": {
              "aString": "tom<3Beer",
              "aNumber": 7.212,
              "aBool": true
            },
            "aString": "tom<3Beer",
            "aNumber": 7,
            "aNumberSlice": [7, 8, 9],
            "aStringSlice": ["7", "8", "9"],
            "anObjectSlice": [{"key":  "c", "value": "ABC"}]
          }
        }`))
    })

    apitest.New().
        Handler(handler).
        Get("/data").
        Expect(t).
        Assert(
            jsonpath.Root("matches").
                Matches(`aString`, `^[mot]{3}<3[AB][re]{3}$`).
                Matches(`aNumber`, `^\d$`).
                Matches(`anObject.aNumber`, `^\d\.\d{3}$`).
                Matches(`aNumberSlice[1]`, `^[80]$`).
                Matches(`anObject.aBool`, `^true$`).
                End(),
        ).
        End()
}
```

**Not Equal**

`NotEqual` 检查 json 路径表达式值是否不等于给定值

```go
Assert(jsonpath.NotEqual("$.id", "56789"))
```

例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
    "github.com/steinfletcher/apitest-jsonpath"
)

func TestJSONPath_NotEqual(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.WriteHeader(http.StatusOK)
            w.Header().Set("Content-Type", "application/json")
            _, _ = w.Write([]byte(`{"message": "hello"}`))
        }).
        Get("/data").
        Expect(t).
        Assert(jsonpath.NotEqual("message", "hello1")).
        End()
}
```

**Not Present**

使用 `NotPresent` 来检查响应中是否缺少某个字段，而不对其值进行评估。

```go
Assert(jsonpath.NotPresent("password"))
```

例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
    "github.com/steinfletcher/apitest-jsonpath"
)

func TestJSONPath_NotPresent(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.WriteHeader(http.StatusOK)
            w.Header().Set("Content-Type", "application/json")
            _, _ = w.Write([]byte(`{"name": "jan"}`))
        }).
        Get("/user").
        Expect(t).
        Assert(jsonpath.NotPresent("password")).
        End()
}
```

**Present**

检查响应中是否存在字段，但不评估其值。

```go
Assert(jsonpath.Present("token"))
```

例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
    "github.com/steinfletcher/apitest-jsonpath"
)

func TestJSONPath_Present(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.WriteHeader(http.StatusOK)
            w.Header().Set("Content-Type", "application/json")
            _, _ = w.Write([]byte(`{"token": "f9a5eb123c01de"}`))
        }).
        Post("/login").
        Expect(t).
        Assert(jsonpath.Present("token")).
        End()
}
```

**Root**

`Root` 用于避免在body中出现重复路径。如下：

```go
Assert(jsonpath.Equal("$.a.b.c.d", "a")).
Assert(jsonpath.Equal("$.a.b.c.e", "b")).
Assert(jsonpath.Equal("$.a.b.c.f", "c")).
```

也可以这样定义 `Root` 路径

```go
Assert(
    jsonpath.Root("a.b.c").
        Equal("d", "a").
        Equal("e", "b").
        Equal("f", "c").
        End(),
)
```

#### 4.6. Status code

使用 `status` 方法匹配 http 状态代码。

```go
Expect(t).Status(http.StatusOK)
```

例子

```go
package jsonpath

import (
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestAssertions_StatusCode(t *testing.T) {
    apitest.New().
        HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.WriteHeader(http.StatusOK)
        }).
        Get("/ping").
        Expect(t).
        Status(http.StatusOK).
        End()
}
```

### 5. MOCKS

**我们为什么要用 `mocks`？**

应用程序与外部应用程序接口集成的情况非常普遍。在开发阶段运行测试时，最好有一个较短的反馈回路，而且测试必须是可重复和可再现的。与真正的外部应用程序接口集成会增加一些未知因素，这些因素往往会因为无法控制的原因而导致测试失败。

模拟外部调用可提高开发生命周期测试阶段的稳定性，帮助您更有信心地快速发布功能。这并不能取代集成测试。要不要进行mocks没有硬性规定，因项目而异。

**Mocks如何工作**

apitest 中的 mock 在很大程度上受到了 gock 的启发。模拟包劫持了默认的 HTTP 传输，并实现了一个自定义的 RoundTrip 方法。如果发出的 HTTP 请求与定义的模拟集合相匹配，模拟中定义的结果将返回给调用者。

#### 5.1. 定义Mocks

调用 `apitest.NewMock()` 工厂方法可定义 mock。

```go
var mock = apitest.NewMock().
    Get("http://external.com/user/12345").
    RespondWith().
    Body(`{"name": "jon"}`).
    Status(http.StatusOK).
    End()
```

在上例中，当 HTTP 客户向 http://example.com/user/12345 发送 GET 请求时，{"name"： "jon"} 会在响应体中以 HTTP 状态代码 200 返回。

然后就可以在 apitest 配置部分添加 mock，如下所示：

```go
apitest.New().
    Mocks(mock).
    Handler(httpHandler).
    Get("/user").
    Expect(t).
    Status(http.StatusOK).
    End()
```

例子

```go
package defining_mocks

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestMocks(t *testing.T) {
    getUserMock := apitest.NewMock().
        Get("/user-api").
        RespondWith().
        Body(`{"name": "jon", "id": "1234"}`).
        Status(http.StatusOK).
        End()

    getPreferencesMock := apitest.NewMock().
        Get("/preferences-api").
        RespondWith().
        Body(`{"is_contactable": false}`).
        Status(http.StatusOK).
        End()

    apitest.New().
        Mocks(getUserMock, getPreferencesMock).
        Handler(myHandler()).
        Get("/user").
        Expect(t).
        Status(http.StatusOK).
        Body(`{"name": "jon", "is_contactable": false}`).
        End()
}

func myHandler() *http.ServeMux {
    handler := http.NewServeMux()
    handler.HandleFunc("/user", func(w http.ResponseWriter, r *http.Request) {
        var user user
        if err := httpGet("/user-api", &user); err != nil {
            w.WriteHeader(http.StatusInternalServerError)
            return
        }

        var contactPreferences contactPreferences
        if err := httpGet("/preferences-api", &contactPreferences); err != nil {
            w.WriteHeader(http.StatusInternalServerError)
            return
        }

        response := userResponse{
            Name:          user.Name,
            IsContactable: contactPreferences.IsContactable,
        }

        bytes, _ := json.Marshal(response)
        _, err := w.Write(bytes)
        if err != nil {
            w.WriteHeader(http.StatusInternalServerError)
            return
        }

        w.WriteHeader(http.StatusOK)
    })
    return handler
}

type user struct {
    Name string `json:"name"`
    ID   string `json:"id"`
}

type contactPreferences struct {
    IsContactable bool `json:"is_contactable"`
}

type userResponse struct {
    Name          string `json:"name"`
    IsContactable bool   `json:"is_contactable"`
}

func httpGet(path string, response interface{}) error {
    res, err := http.DefaultClient.Get(fmt.Sprintf("http://localhost:8080%s", path))
    if err != nil {
        return err
    }

    bytes, err := ioutil.ReadAll(res.Body)
    if err != nil {
        return err
    }

    err = json.Unmarshal(bytes, response)
    if err != nil {
        return err
    }

    return nil
}
```

#### 5.2. Matchers

您可以为header、cookie、url 查询参数和body添加匹配器。

**Body**

Body 允许您为请求报文添加匹配器。

```go
var getUserMock = apitest.NewMock().
    Post("http://example.com/user/12345").
    Body(`{"username": "John"}`).
    RespondWith().
    Status(http.StatusOK).
    End()
```

如果要处理 URL 编码的表单正文，可以使用 `FormData` 来匹配键和值。正则表达式也可以作为值。

```go
FormData("name", "Simon").
FormData("name", "Jo([a-z]+)n").
```

您还可以要求表单体键存在（FormDataPresent）或不存在（FormDataNotPresent）。

```go
FormDataPresent("name").
FormDataNotPresent("pets").
```

JSONPath 扩展提供了一个自定义匹配器，支持在请求正文中进行匹配。这对部分匹配正文非常有用。

```go
apitest.NewMock().
    Post("/user-external").
    AddMatcher(mocks.Equal("$.name", "jan")).
    RespondWith().
```

例子

```go
package matchers

import (
    "bytes"
    jsonpath "github.com/steinfletcher/apitest-jsonpath/mocks"
    "io/ioutil"
    "net/http"
    "testing"

    "github.com/steinfletcher/apitest"
)

func TestMocks(t *testing.T) {
    createUserMock := apitest.NewMock().
        Post("/user-external").
        AddMatcher(jsonpath.Equal("$.name", "jan")).
        RespondWith().
        Status(http.StatusCreated).
        End()

    apitest.New().
        Mocks(createUserMock).
        Handler(myHandler()).
        Post("/user").
        JSON(map[string]string{"name": "jan"}).
        Expect(t).
        Status(http.StatusCreated).
        End()
}

func myHandler() *http.ServeMux {
    handler := http.NewServeMux()
    handler.HandleFunc("/user", func(w http.ResponseWriter, r *http.Request) {
        reqBody, err := ioutil.ReadAll(r.Body)
        if err != nil {
            panic(err)
        }

        _, err = http.DefaultClient.Post("http://localhost:8080/user-external", "application/json", bytes.NewReader(reqBody))
        if err != nil {
            panic(err)
        }

        w.WriteHeader(http.StatusCreated)
    })
    return handler
}
```

**Cookies**

`Cookie` 允许您为 cookie 名称和值添加匹配器。

```go
var getUserMock = apitest.NewMock().
    Get("http://example.com/user/12345").
    Cookie("sessionid", "1321").
    RespondWith().
    Body(`{"name": "jon"}`).
    Status(http.StatusOK).
    End()
```

您还可以要求 cookie 名称存在（`CookiePresent`）或不存在（`CookieNotPresent`）。

```go
var getUserMock = apitest.NewMock().
    Get("http://example.com/user/12345").
    CookiePresent("trackingid").
    CookieNotPresent("analytics").
    RespondWith().
    Body(`{"name": "jon"}`).
    Status(http.StatusOK).
    End()
```

**Custom matchers**

您可以使用 `AddMatcher` 编写自己的自定义匹配器。匹配器函数定义为 `func(*http.Request, *MockRequest) error`.

```go
var getUserMock = apitest.NewMock().
    Post("http://example.com/user/12345").
    AddMatcher(func(req *http.Request, mockReq *MockRequest) error {
        if req.Method == http.MethodPost {
            return nil
        }
        return errors.New("invalid http method")
    }).
    RespondWith().
    Status(http.StatusOK).
    End()
```

**Header**

`Header` 允许为头信息键和值添加匹配器。正则表达式也可以作为值

```go
var getUserMock = apitest.NewMock().
    Get("http://example.com/user/12345").
    Header("foo", "bar").
    Header("token", "b([a-z]+)z").
    Headers(map[string]string{"name": "John"})
    RespondWith().
    Body(`{"name": "jon"}`).
    Status(http.StatusOK).
    End()
```

您也可以要求头必须存在（`HeaderPresent`）或不存在（`HeaderNotPresent`）。

```go
var getUserMock = apitest.NewMock().
    Get("http://example.com/user/12345").
    HeaderPresent("authtoken").
    HeaderNotPresent("requestid").
    RespondWith().
    Body(`{"name": "jon"}`).
    Status(http.StatusOK).
    End()
```

**Query parameters**

通过 `Query`，您可以为 url 查询参数的键和值添加匹配器。正则表达式也可以作为值。

```go
var getUserMock = apitest.NewMock().
    Get("http://example.com/user/12345").
    Query("page", "1").
    Query("name", "Jo([a-z]+)n").
    QueryParams(map[string]string{"orderBy": "ASC"}).
    RespondWith().
    Body(`{"name": "jon"}`).
    Status(http.StatusOK).
    End()
```

您还可以要求查询参数存在（`QueryPresent`）或不存在（`QueryNotPresent`）。

```go
var getUserMock = apitest.NewMock().
    Get("http://example.com/user/12345").
    QueryPresent("page").
    QueryNotPresent("name").
    RespondWith().
    Body(`{"name": "jon"}`).
    Status(http.StatusOK).
    End()
```

#### 5.3. Standalone

通过使用 mock 生成器上的 `EndStandalone` 终止方法，可以在 API 测试之外使用 mock。这对于在 API 测试之外测试 http 客户端非常有用。

```go
func TestMocks_Standalone(t *testing.T) {
    cli := http.Client{Timeout: 5}
    defer NewMock().
        Post("http://localhost:8080/path").
        Body(`{"a", 12345}`).
        RespondWith().
        Status(http.StatusCreated).
        EndStandalone()()

    resp, err := cli.Post("http://localhost:8080/path",
        "application/json",
        strings.NewReader(`{"a", 12345}`))

    assert.NoError(t, err)
    assert.Equal(t, http.StatusCreated, resp.StatusCode)
}
```

`EndStandalone` 会返回一个函数，在测试运行后调用该函数可将 http 传输重置为默认配置。

如果想在一个测试中注册多个独立模拟，请使用 `apitest.NewStandaloneMocks()` 工厂方法。

```go
resetTransport := apitest.NewStandaloneMocks(
    apitest.NewMock().
        Post("http://localhost:8080/path").
        Body(`{"a": 12345}`).
        RespondWith().
        Status(http.StatusCreated).
        End(),
    apitest.NewMock().
        Get("http://localhost:8080/path").
        RespondWith().
        Body(`{"a": 12345}`).
        Status(http.StatusOK).
        End(),
).End()
defer resetTransport()
```

### 6. INTEGRATIONS

`apitest` 有许多注入点，因此很容易与其他第三方工具和测试库集成。

#### 6.1. Ginkgo

`apitest` 通过接口接受 `*testing.T`。这样就可以与其他测试库（如 Ginkgo）集成。您可以通过 [GinkgoT()](https://onsi.github.io/ginkgo/#using-other-matcher-libraries) 生成一个模仿 `*testing.T` 的对象，并直接与 Ginkgo 通信。请参阅完整示例 [此处](https://github.com/steinfletcher/apitest/tree/master/examples/ginkgo)。

```go
var _ = Describe("Ginkgo/Server", func() {

    var (
        t      GinkgoTInterface
        router *mux.Router
    )

    BeforeEach(func() {
        t = GinkgoT()
        router = server.NewApp().Router
    })

    Context("Successful CookieMatching", func() {
        It("cookies should be set correctly", func() {
            apitest.New().
                Handler(router).
                Get("/user/1234").
                Expect(t).
                Cookies(apitest.NewCookie("TomsFavouriteDrink").
                    Value("Beer").
                    Path("/")).
                Status(http.StatusOK).
                End()
        })
    })
})
```

### 7. REPORTS

apitest 包含一种报告机制，可以生成序列图，说明入站请求、最终响应、与模拟的任何交互，甚至数据库查询。您甚至可以实现自己的 "ReportFormatter "来消费报告数据，从而生成自己的报告。

报告支持的主要组成部分是：

1. **Event** 有两种类型的事件：HTTP 事件和自定义事件。HTTP 事件代表模拟交互、进入应用程序的请求和最终响应。自定义事件用于从任意来源生成数据。自定义事件包含标题和正文。我们在 apitest 中使用这种事件类型来记录数据库交互。
2. **Recorder** 记录测试执行期间发生的事件，如模拟交互、数据库交互以及与被测应用程序的 HTTP 交互。如果输入自己的记录器，就可以添加自定义事件，然后通过实现 ReportFormatter 来处理这些事件。这对于记录从亚马逊 S3 客户端等来源生成的自定义事件可能很有用。
3. **ReportFormatter** 用户可用于生成自定义报告的接口。接收报告记录器，该记录器会暴露事件。SequenceDiagramFormatter 是 apitest 中包含的此接口的实现，可根据事件数据渲染 HTML 序列图。

#### 7.1. Sequence diagrams

配置报告程序以创建序列图，如下所示

```go
apitest.New().
    Report(apitest.SequenceDiagram()).
    Handler(handler).
    Get("/user").
    Expect(t).
    Status(http.StatusOK).
    End()
```

在这个 [示例](https://github.com/steinfletcher/apitest/tree/master/examples/sequence-diagrams) 中，我们实现了一个 REST API，并生成了一个与 http 交互的序列图。

生成的下图说明了测试中协作者之间的交互。`sut` 块是被测系统。

![sequence diagram report](https://apitest.dev/static/images/seq-diagram.png)

对于每次交互，请求/响应的 http 线表示法都会呈现在图表下方的事件日志中

![sequence diagram report](https://apitest.dev/static/images/seq-diag-log.png)

### 8. 例子

`apitest` 实例：`https://github.com/steinfletcher/apitest/tree/master/examples`
