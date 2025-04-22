title: UI自动化测试神器-Cypress
date: 2022-06-14
category: 测试
tag: Cypress, 自动化测试

[TOC]

### 1. 简介

Cypress 是为现代网络而构建的下一代前端测试工具。我们解决开发人员和质量保证工程师在测试现代应用程序时面临的关键难题。

我们使它很简单：

- 设置测试
- 编写测试
- 运行测试
- 调试测试

Cypress 经常和 Selenium 相提并论；然而，Cypress 在结构和基础上与之有所不同。Cypress 不受 Selenium 限制。

这能够使你编写更快、更简单和更可靠的测试。

#### 1.1 谁能使用 Cypress ？

我们的用户通常是使用现代 JavaScript 构建 Web 应用程序的开发人员或者 QA 工程师。

Cypress 能够帮助你编写各种类型的测试：

- 端到端测试
- 集成测试
- 单元测试

Cypress可以测试运行在浏览器中的任何东西。

#### 1.2 Cypress 生态系统

Cypress 是一款免费、开源、本地安装的测试工具和记录测试的服务。

- **首先：** 在本地构建应用程序时，Cypress 能够容易的设置并编写测试。TDD 是最好的例子。
- **其次：** 在建立一套测试系统并将 Cypress 与的 CI 集成后，我们的控制台能够记录你的测试运行。

#### 1.3 特性

Cypress 支持全面。这里是一些 Cypress 能够但是其他框架不能够做到的：

- **安装简单**：在网络正常的情况下，10分钟就可以安装好Cypress框架，一天则可以入门，写一些简单的用例。

- **运行速度快**：相较于Selenium来说，Cypress的运行速度真的是相当快了，它不需要web driver来驱动浏览器。

- **脚本实时调试**：在脚本编写过程中，只要编辑器中进行保存，脚本就会自动运行，可以快速高效的知道脚本是否正确。

- **随时查看执行情况：** 当你执行测试的时候 Cypress 会进行快照。只需在命令日志中鼠标悬停，就能查看每一步的具体情况。

- **可调试性**：直接从熟悉的工具（如：Chrome DevTools）进行调试。

- **自动等待：** 不需要在测试中添加等待。在继续执行之前，Cypress 能够自动等待命令和断言。

- **截图和视频：** 脚本运行失败后，会在..\cypress\screenshots文件夹下面自动保存失败用例的截图，方便我们追踪到失败用例的原因。

- **脚本运行完成后**，会在..\cypress\videos文件夹下自动保存脚本运行过程录制的视频。

- **跨浏览器测试**：支持Firefox 和 Chrome 系列浏览器（包括 Edge 和 Electron）

##### 1.3.1 设置测试

没有服务器、驱动程序或者其他任何依赖项的安装或配置。你可以在 60 秒内写出你的第一个能够通过的测试。

##### 1.3.2 编写测试

使用 Cypress 编写的测试很容易阅读和理解。我们的 API 已经完全支持你已经熟悉的工具。

##### 1.3.3 运行测试

Cypress 的运行速度与浏览器渲染内容一样快。你可以在开发应用程序时实时观看测试。

##### 1.3.4 调试测试

可读的错误消息可帮助您快速调试。您还可以访问您熟悉并喜爱的任何开发调试工具。

### 2. 环境搭建

> 本次安装基于Windows10

#### 2.1 安装node

下载地址：`http://nodejs.cn/download/`

从上面的地址可下载你想要的版本，本次下载的是：`https://npmmirror.com/mirrors/node/v16.15.0/node-v16.15.0-x64.msi`

安装完成后，检查版本，如下：

```
# node -v
v16.15.0

# npm -v
8.5.5
```

均正常显示版本，则安装成功。

#### 2.2 安装Cypress

- 在要安装的地方，新建一个文件夹，如cypress，并进入

- 初始化项目：在当前目录下执行命令 `npm init`

- 安装Cypress：`npm install cypress --save-dev`

#### 2.3 打开Cypress

以下有多种打开方式：

- `./node_modules/.bin/cypress open`

- `$(npm bin)/cypress open`

- `npx cypress open`，需要`npm > v5.2`

- `yarn run cypress open`，需要提前安装`yarn`，命令如下：`npm install -g yarn`

然后Cypress会启动。

#### 2.3 添加npm脚本

如果启动正常，你可以在package.json中添加启动脚本，方便Cypress启动，如下：

```
{
  "scripts": {
    "cypress:open": "cypress open"
  }
}
```

然后就可以像下面那样启动Cypress了

```
npm run cypress:open
```

启动后会有"Welcome to Cypress！"字样出现，说明已经启动成功。

### 3. 编写第一个E2E测试用例

- 点击E2E Testing

- 选择对应的浏览器，进入页面后会看到一些例子，这个是Cypress自带的，在目录在.cypress\cypress\e2e下，本次我们选择Edge，然后点击`Start E2E Testing in Edge`。

- 然后点击右上角`+ New Spec`

- 再然后点击右侧`Create new empty spec`

- 默认或输入新名称，然后点击`Create Spec`

- 可以看到一个新的用例展示，可以直接支持，或者关掉窗口。
  
  ```
  # cypress\e2e\spec.cy.js
  
  describe('empty spec', () => {
    it('passes', () => {
      cy.visit('https://example.cypress.io')
    })
  })
  ```

- 然后就能在用例列表中找到他

### 4. 写你第一个自己的测试用例

- 先让我们看一个通过性测试的用例

```
describe('My First Test', () => {
  it('Does not do much!', () => {
    expect(true).to.equal(true)
  })
}
```

执行结果：

```
My First Test
√ Does not do much!
    TEST BODY
        assert expected true to equal true
```

尽管这个测试用例没有什么实际用处，但却是我们第一个执行通过的用例。

- 再看一个不能过的测试用例

```
describe('My First Test', () => {
  it('Does not do much!', () => {
    expect(true).to.equal(false)
  })
})
```

执行结果：

```
My First Test
✖ Does not do much!
    TEST BODY
    1  assert expected true to equal false
    !  AssertionError
    expected true to equal false
      cypress/e2e/false.cy.js:3:21
```

测试结果中会断言失败的地方高亮显示出来，并指出问题所在地方。

### 5. 写一个真正的测试用例

通常测试包括3个阶段：

- 编写测试用例

- 执行操作

- 对执行结果做一个断言

现在 ，我们通过Cypress来操作这些步骤

1. 访问一个页面

2. 查询一个元素

3. 元素间的交互

4. 页面内容的断言

> 步骤1：访问一个页面（visit），如下：

```
describe('第一个测试', () => {
  it('打开SiCAP', () => {
    cy.visit('https://192.168.214.55')
  })
})
```

执行结果：

- 可以看到第一行显示describe的内容，第二行显示it的内容

- TEST BODY显示所有的请求

- 右侧显示每一个请求的执行情况，当然你需要使用鼠标划过对应的请求

> 步骤2：查找一个元素（get、contains），如下：

```
describe('第一个测试', () => {
  it('打开SiCAP', () => {
    cy.visit('https://192.168.214.55')
    cy.get('#username')
    cy.contains('登 录')
  })
})
```

执行结果：

- 可以看到第一行显示describe的内容，第二行显示it的内容

- TEST BODY显示所有的请求

- 在对应的请求中，我们可以清晰的看到程序找到了`#username`，`登 录`

> 步骤3：给文本框输入值（type），如下

```
describe('登录SiCAP', () => {
  it('passes', () => {
    cy.visit('https://192.168.214.55/')
    cy.get('#username')
        .type('admin')
        .should('have.value', 'admin');
    cy.get('#password')
        .type('p@ssw0rd')
        .should('have.value', 'p@ssw0rd');
    cy.get('.login_btn').contains('登 录').click()
  })
})
```

执行结果：

- 用户和密码正常输入

> 步骤4：断言（should），如下

```
describe('登录SiCAP', () => {
  it('passes', () => {
    cy.visit('https://192.168.214.55/')
    cy.get('#username')
        .type('admin')
        .should('have.value', 'admin');
    cy.get('#password')
        .type('p@ssw0rd')
        .should('have.value', 'p@ssw0rd');
    cy.get('.login_btn').contains('登 录').click()
  })
})
```

执行结果：

- 用户和密码正常断言

> 步骤5：点击一个元素（click），如下

```
describe('登录SiCAP', () => {
  it('passes', () => {
    cy.visit('https://192.168.214.55/')
    cy.get('#username')
        .type('admin')
        .should('have.value', 'admin');
    cy.get('#password')
        .type('p@ssw0rd')
        .should('have.value', 'p@ssw0rd');
    cy.get('.login_btn').contains('登 录').click()
  })
})
```

执行结果：

- 点击后，正常进入系统

### 6. 执行测试用例

- 启动server

- 访问你的server

- 配置Cypress
  
  cypress\cypress.config.js
  
  如配置基础url，在后面的访问页面的时候就不需要写baseUrl。
  
  ```
  const { defineConfig } = require('cypress')
  
  module.exports = defineConfig({
    e2e: {
      baseUrl: 'http://localhost:8080'
    }
  })
  ```
  
  配置后，访问链接如下：
  
  ```
  describe('The Home Page', () => {
    it('successfully loads', () => {
      cy.visit('/')
    })
  })
  ```

#### 6.1 测试策略

在执行测试用例前，有时候需要做一些前置动作，所以Cypress安排了一个特定的命令来执行它，如下：

- `cy.exec()`：用来执行系统命令

- `cy.task()`：通过 setupNodeEvents 函数在 Node 中运行代码

- `cy.request()`：用来发出HTTP请求

如果你想在你的服务上执行npm，你可以加一个before或者beforeEach沟子去执行一个npm任务。如下：

```
describe('The Home Page', () => {
  beforeEach(() => {
    // reset and seed the database prior to every test
    cy.exec('npm run db:reset && npm run db:seed')
  })

  it('successfully loads', () => {
    cy.visit('/')
  })
})
```

再如，你可以在你的测试用例中，执行多个请求。

```
describe('The Home Page', () => {
  beforeEach(() => {
    // reset and seed the database prior to every test
    cy.exec('npm run db:reset && npm run db:seed')

    // seed a post in the DB that we control from our tests
    cy.request('POST', '/test/seed/post', {
      title: 'First Post',
      authorId: 1,
      body: '...',
    })

    // seed a user in the DB that we can control from our tests
    cy.request('POST', '/test/seed/user', { name: 'Jane' })
      .its('body')
      .as('currentUser')
  })

  it('successfully loads', () => {
    // this.currentUser will now point to the response
    // body of the cy.request() that we could use
    // to log in or work with in some way

    cy.visit('/')
  })
})
```

注意：第一 次测试时的登录不要去用UI，请使用request。

### 7. 命令

#### 7.1 查找页面元素的基本方法

| 命令         | 注释                      |
|:----------:|:-----------------------:|
| get()      | 通过选择器或别名获取一个或多个 DOM 元素。 |
| find()     | 获取特定选择器的下位DOM元素。        |
| contains() | 获取包含文本的 DOM 元素，可模糊匹配。   |

#### 7.2 查找页面元素的辅助方法

| 命令                  | 注释                                                                                |
|:-------------------:|:---------------------------------------------------------------------------------:|
| children()          | 获取一组DOM元素中每个DOM元素的子元素。                                                            |
| parents()           | 获取一组DOM元素的父DOM元素。请注意 .parents() 在 DOM 树中向上移动多个级别，而不是.parent ()命令在 DOM 树中向上移动一个级别。 |
| parent()            | 获取一组DOM元素的父DOM元素。请注意，与.parents（）命令相反， .parent() 仅沿DOM树向上移动一个级别。                   |
| siblings()          | 获取同级DOM元素。                                                                        |
| first()             | 获取一组DOM元素中的第一个DOM元素。                                                              |
| last()              | 获取一组DOM元素中的最后一个DOM元素。                                                             |
| next()              | 获取一组 DOM 元素中每个 DOM 元素的紧随其后的元素。                                                    |
| nextAll()           | 在一组匹配的 DOM 元素中获取每个 DOM 元素的所有后续元素。                                                 |
| nextUntil(selector) | 获取一组匹配的 DOM 元素中每个 DOM 元素的所有后续元素，但不包括提供的元素。                                        |
| prev()              | 获取一组元素中每个元素的前一个同级元素。                                                              |
| prevUntil()         | 获取一组匹配的 DOM 元素中每个 DOM 元素的所有前置元素，但不包括提供的元素。                                        |
| each()              | 遍历类似结构的数组（具有 length 属性的数组或对象）                                                     |
| eq()                | 在一个元素数组的特定索引处获取一个DOM元素。                                                           |
| closest()           | 获取与选择器相匹配的第一个DOM元素(无论是它本身还是它的一个祖先)。                                               |

#### 7.3 点击命令

| 命令           | 作用   |
|:------------:|:----:|
| click()      | 单击   |
| dbclick()    | 双击   |
| rightclick() | 右键点击 |

#### 7.4 操作页面元素的命令

| 命令               | 作用            |
|:----------------:|:-------------:|
| type()           | 输入框输入文本元素     |
| focus()          | 聚焦DOM元素       |
| blur()           | DOM元素失去焦点     |
| clear()          | 清空DOM元素       |
| submit()         | 提交表单          |
| click()          | 点击DOM元素       |
| dbclick()        | 双击            |
| rightclick()     | 右键点击          |
| check()          | 选中单选框、复选框     |
| uncheck()        | 取消选中复选框       |
| select()         | select        |
| scrollIntoView() | 将DOM元素滑动到可视区域 |
| trigger()        | DOM元素上触发事件    |
| scrollTo()       | 滑动滚动条         |

#### 7.5 获取页面全局对象的命令

| 命令         | 作用                          |
|:----------:|:---------------------------:|
| window()   | 获取当前页面的窗口对象                 |
| title()    | 获取当前页面的title                |
| url()      | 获取当前页面的URL                  |
| location() | 获取当前页面的全局window.location对象  |
| document() | 获取当前页面的全局windowd.document对象 |
| hash()     | 获取当前页面的URL                  |
| root()     | 获取根DOM元素                    |

#### 7.6 操作浏览器的命令

| 命令         | 作用            |
|:----------:|:-------------:|
| go()       | 浏览器前进、后退      |
| reload()   | 刷新页面          |
| viewport() | 控制浏览器窗口的大小和方向 |
| visit()    | 访问指定的         |
| wait()     | 强制等待          |

#### 7.7 操作上一条命令返回结果的命令

| 命令       | 作用                       |
|:--------:|:------------------------:|
| then()   | 将上一条命令返回的结果注入到下一个命令中     |
| and()    | 创建一个断言。断言将自动重试，直到它们通过或超时 |
| should() | and()的别名                 |
| invoke() | 对上一条命令的结果执行调用方法操作        |
| its()    | 获取对象的属性值                 |
| as()     | 取别名                      |
| within() | 限定命令作用域                  |
| each()   | 遍历当前元素                   |
| spread() | 将数组内容作为单独的参数传回到回调函数      |

#### 7.8 操作文件相关命令

| 命令          | 作用           |
|:-----------:|:------------:|
| fixture()   | 加载数据文件       |
| readFile()  | 读取文件并生成其内容。  |
| writeFile() | 把指定同内容写入一个文件 |

#### 7.9 网络相关命令

| 命令          | 作用                                  |
|:-----------:|:-----------------------------------:|
| request()   | 发送HTTP请求。                           |
| route()     | 用来管理网络请求的行为                         |
| server()    | 启动服务器以开始将响应路由到cy.route()并更改网络请求的行为。 |
| intercept() | 监视和存根网络请求和响应。                       |

#### 7.10 操作 Cookie 相关命令

| 命令             | 作用      |
|:--------------:|:-------:|
| getCookies()   | 获取所有    |
| setCookie()    | 设置一个    |
| clearCookie()  | 清除指定名称的 |
| clearCookies() | 清除所有    |

#### 7.11 Cypress API 命令大全

| 命令               |     |
|:----------------:|:---:|
| Cypress.Commands |     |
| Cypress.Cookies  |     |
| Cypress.config   |     |
| Cypress.env      |     |
| Cypress.dom      |     |
| Cypress.platform |     |
| Cypress.version  |     |
| Cypress.arch     |     |
| Cypress.spec     |     |
| Cypress.browser  |     |
| Cypress.log      |     |

### 8. 断言

#### 8.1 BDD 断言

这些链接器可用于 BDD 断言（`expect`/`should`）。 列出的别名可以与其原始链接器互换使用。 您可以在 [此处](http://chaijs.com/api/bdd/) 查看可用 BDD Chai 断言的完整列表。

| Chainer                                                                 | Example                                                                                                                               |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| not                                                                     | `expect(name).to.not.equal('Jane')`                                                                                                   |
| deep                                                                    | `expect(obj).to.deep.equal({ name: 'Jane' })`                                                                                         |
| nested                                                                  | `expect({a: {b: ['x', 'y']}}).to.have.nested.property('a.b[1]')`<br>`expect({a: {b: ['x', 'y']}}).to.nested.include({'a.b[1]': 'y'})` |
| ordered                                                                 | `expect([1, 2]).to.have.ordered.members([1, 2]).but.not.have.ordered.members([2, 1])`                                                 |
| any                                                                     | `expect(arr).to.have.any.keys('age')`                                                                                                 |
| all                                                                     | `expect(arr).to.have.all.keys('name', 'age')`                                                                                         |
| a(*type*)<br>**Aliases:** an                                            | `expect('test').to.be.a('string')`                                                                                                    |
| include(*value*)<br>**Aliases:** contain, includes, contains            | `expect([1,2,3]).to.include(2)`                                                                                                       |
| ok                                                                      | `expect(undefined).to.not.be.ok`                                                                                                      |
| true                                                                    | `expect(true).to.be.true`                                                                                                             |
| false                                                                   | `expect(false).to.be.false`                                                                                                           |
| null                                                                    | `expect(null).to.be.null`                                                                                                             |
| undefined                                                               | `expect(undefined).to.be.undefined`                                                                                                   |
| exist                                                                   | `expect(myVar).to.exist`                                                                                                              |
| empty                                                                   | `expect([]).to.be.empty`                                                                                                              |
| arguments<br>**Aliases:** Arguments                                     | `expect(arguments).to.be.arguments`                                                                                                   |
| equal(*value*)<br>**Aliases:** equals, eq                               | `expect(42).to.equal(42)`                                                                                                             |
| deep.equal(*value*)                                                     | `expect({ name: 'Jane' }).to.deep.equal({ name: 'Jane' })`                                                                            |
| eql(*value*)<br>**Aliases:** eqls                                       | `expect({ name: 'Jane' }).to.eql({ name: 'Jane' })`                                                                                   |
| greaterThan(*value*)<br>**Aliases:** gt, above                          | `expect(10).to.be.greaterThan(5)`                                                                                                     |
| least(*value*)<br>**Aliases:** gte                                      | `expect(10).to.be.at.least(10)`                                                                                                       |
| lessThan(*value*)<br>**Aliases:** lt, below                             | `expect(5).to.be.lessThan(10)`                                                                                                        |
| most(*value*)<br>**Aliases:** lte                                       | `expect('test').to.have.length.of.at.most(4)`                                                                                         |
| within(*start*, *finish*)                                               | `expect(7).to.be.within(5,10)`                                                                                                        |
| instanceOf(*constructor*)<br>**Aliases:** instanceof                    | `expect([1, 2, 3]).to.be.instanceOf(Array)`                                                                                           |
| property(*name*, *[value]*)                                             | `expect(obj).to.have.property('name')`                                                                                                |
| deep.property(*name*, *[value]*)                                        | `expect(deepObj).to.have.deep.property('tests[1]', 'e2e')`                                                                            |
| ownProperty(*name*)<br>**Aliases:** haveOwnProperty, own.property       | `expect('test').to.have.ownProperty('length')`                                                                                        |
| ownPropertyDescriptor(*name*)<br>**Aliases:** haveOwnPropertyDescriptor | `expect({a: 1}).to.have.ownPropertyDescriptor('a')`                                                                                   |
| lengthOf(*value*)                                                       | `expect('test').to.have.lengthOf(3)`                                                                                                  |
| match(*RegExp*)<br>**Aliases:** matches                                 | `expect('testing').to.match(/^test/)`                                                                                                 |
| string(*string*)                                                        | `expect('testing').to.have.string('test')`                                                                                            |
| keys(*key1*, *[key2]*, *[...]*)<br>**Aliases:** key                     | `expect({ pass: 1, fail: 2 }).to.have.keys('pass', 'fail')`                                                                           |
| throw(*constructor*)<br>**Aliases:** throws, Throw                      | `expect(fn).to.throw(Error)`                                                                                                          |
| respondTo(*method*)<br>**Aliases:** respondsTo                          | `expect(obj).to.respondTo('getName')`                                                                                                 |
| itself                                                                  | `expect(Foo).itself.to.respondTo('bar')`                                                                                              |
| satisfy(*method*)<br>**Aliases:** satisfies                             | `expect(1).to.satisfy((num) => { return num > 0 })`                                                                                   |
| closeTo(*expected*, *delta*)<br>**Aliases:** approximately              | `expect(1.5).to.be.closeTo(1, 0.5)`                                                                                                   |
| members(*set*)                                                          | `expect([1, 2, 3]).to.include.members([3, 2])`                                                                                        |
| oneOf(*values*)                                                         | `expect(2).to.be.oneOf([1,2,3])`                                                                                                      |
| change(*function*)<br>**Aliases:** changes                              | `expect(fn).to.change(obj, 'val')`                                                                                                    |
| increase(*function*)<br>**Aliases:** increases                          | `expect(fn).to.increase(obj, 'val')`                                                                                                  |
| decrease(*function*)<br>**Aliases:** decreases                          | `expect(fn).to.decrease(obj, 'val')`                                                                                                  |

These getters are also available for BDD assertions. They don't actually do anything, but they enable you to write clear, english sentences.

| Chainable getters                                                                           |
| ------------------------------------------------------------------------------------------- |
| `to`, `be`, `been`, `is`, `that`, `which`, `and`, `has`, `have`, `with`, `at`, `of`, `same` |

#### 8.2 TDD 断言

这些断言可用于 TDD 断言（`assert`）。 您可以在 [此处](http://chaijs.com/api/assert/) 查看可用 Chai 断言的完整列表。

| Assertion                                                   | Example                                                |
| ----------------------------------------------------------- | ------------------------------------------------------ |
| .isOk(*object*, *[message]*)                                | `assert.isOk('everything', 'everything is ok')`        |
| .isNotOk(*object*, *[message]*)                             | `assert.isNotOk(false, 'this will pass')`              |
| .equal(*actual*, *expected*, *[message]*)                   | `assert.equal(3, 3, 'vals equal')`                     |
| .notEqual(*actual*, *expected*, *[message]*)                | `assert.notEqual(3, 4, 'vals not equal')`              |
| .strictEqual(*actual*, *expected*, *[message]*)             | `assert.strictEqual(true, true, 'bools strict eq')`    |
| .notStrictEqual(*actual*, *expected*, *[message]*)          | `assert.notStrictEqual(5, '5', 'not strict eq')`       |
| .deepEqual(*actual*, *expected*, *[message]*)               | `assert.deepEqual({ id: '1' }, { id: '1' })`           |
| .notDeepEqual(*actual*, *expected*, *[message]*)            | `assert.notDeepEqual({ id: '1' }, { id: '2' })`        |
| .isAbove(*valueToCheck*, *valueToBeAbove*, *[message]*)     | `assert.isAbove(6, 1, '6 greater than 1')`             |
| .isAtLeast(*valueToCheck*, *valueToBeAtLeast*, *[message]*) | `assert.isAtLeast(5, 2, '5 gt or eq to 2')`            |
| .isBelow(*valueToCheck*, *valueToBeBelow*, *[message]*)     | `assert.isBelow(3, 6, '3 strict lt 6')`                |
| .isAtMost(*valueToCheck*, *valueToBeAtMost*, *[message]*)   | `assert.isAtMost(4, 4, '4 lt or eq to 4')`             |
| .isTrue(*value*, *[message]*)                               | `assert.isTrue(true, 'this val is true')`              |
| .isNotTrue(*value*, *[message]*)                            | `assert.isNotTrue('tests are no fun', 'val not true')` |
| .isFalse(*value*, *[message]*)                              | `assert.isFalse(false, 'val is false')`                |
| .isNotFalse(*value*, *[message]*)                           | `assert.isNotFalse('tests are fun', 'val not false')`  |
| .isNull(*value*, *[message]*)                               | `assert.isNull(err, 'there was no error')`             |
| .isNotNull(*value*, *[message]*)                            | `assert.isNotNull('hello', 'is not null')`             |
| .isNaN(*value*, *[message]*)                                | `assert.isNaN(NaN, 'NaN is NaN')`                      |
| .isNotNaN(*value*, *[message]*)                             | `assert.isNotNaN(5, '5 is not NaN')`                   |
| .exists(*value*, *[message]*)                               | `assert.exists(5, '5 is not null or undefined')`       |
| .notExists(*value*, *[message]*)                            | `assert.notExists(null, 'val is null or undefined')`   |
| .isUndefined(*value*, *[message]*)                          | `assert.isUndefined(undefined, 'val is undefined')`    |
| .isDefined(*value*, *[message]*)                            | `assert.isDefined('hello', 'val has been defined')`    |
| .isFunction(*value*, *[message]*)                           | `assert.isFunction(x => x * x, 'val is func')`         |
| .isNotFunction(*value*, *[message]*)                        | `assert.isNotFunction(5, 'val not funct')`             |
| .isObject(*value*, *[message]*)                             | `assert.isObject({num: 5}, 'val is object')`           |
| .isNotObject(*value*, *[message]*)                          | `assert.isNotObject(3, 'val not object')`              |
| .isArray(*value*, *[message]*)                              | `assert.isArray(['unit', 'e2e'], 'val is array')`      |
| .isNotArray(*value*, *[message]*)                           | `assert.isNotArray('e2e', 'val not array')`            |
| .isString(*value*, *[message]*)                             | `assert.isString('e2e', 'val is string')`              |
| .isNotString(*value*, *[message]*)                          | `assert.isNotString(2, 'val not string')`              |
| .isNumber(*value*, *[message]*)                             | `assert.isNumber(2, 'val is number')`                  |
| .isNotNumber(*value*, *[message]*)                          | `assert.isNotNumber('e2e', 'val not number')`          |
| .isFinite(*value*, *[message]*)                             | `assert.isFinite('e2e', 'val is finite')`              |
| .isBoolean(*value*, *[message]*)                            | `assert.isBoolean(true, 'val is bool')`                |
| .isNotBoolean(*value*, *[message]*)                         | `assert.isNotBoolean('true', 'val not bool')`          |
| .typeOf(*value*, *name*, *[message]*)                       | `assert.typeOf('e2e', 'string', 'val is string')`      |
| .notTypeOf(*value*, *name*, *[message]*)                    | `assert.notTypeOf('e2e', 'number', 'val not number')`  |

#### 8.3 Chai-jQuery

这些链接器在断言 DOM 对象时可用。 在使用 DOM 命令后，您通常会使用这些链接器，例如： [`cy.get()`](https://docs.cypress.io/api/commands/get), [`cy.contains()`](https://docs.cypress.io/api/commands/contains),等。

| Chainers                | Assertion                                                            |
| ----------------------- | -------------------------------------------------------------------- |
| attr(*name*, *[value]*) | `expect($el).to.have.attr('foo', 'bar')`                             |
| prop(*name*, *[value]*) | `expect($el).to.have.prop('disabled', false)`                        |
| css(*name*, *[value]*)  | `expect($el).to.have.css('background-color', 'rgb(0, 0, 0)')`        |
| data(*name*, *[value]*) | `expect($el).to.have.data('foo', 'bar')`                             |
| class(*className*)      | `expect($el).to.have.class('foo')`                                   |
| id(*id*)                | `expect($el).to.have.id('foo')`                                      |
| html(*html*)            | `expect($el).to.have.html('I love testing')`                         |
| text(*text*)            | `expect($el).to.have.text('I love testing')`                         |
| value(*value*)          | `expect($el).to.have.value('test@dev.com')`                          |
| visible                 | `expect($el).to.be.visible`                                          |
| hidden                  | `expect($el).to.be.hidden`                                           |
| selected                | `expect($option).not.to.be.selected`                                 |
| checked                 | `expect($input).not.to.be.checked`                                   |
| focus[ed]               | `expect($input).not.to.be.focused`<br>`expect($input).to.have.focus` |
| enabled                 | `expect($input).to.be.enabled`                                       |
| disabled                | `expect($input).to.be.disabled`                                      |
| empty                   | `expect($el).not.to.be.empty`                                        |
| exist                   | `expect($nonexistent).not.to.exist`                                  |
| match(*selector*)       | `expect($emptyEl).to.match(':empty')`                                |
| contain(*text*)         | `expect($el).to.contain('text')`                                     |
| descendants(*selector*) | `expect($el).to.have.descendants('div')`                             |

#### 8.4 Sinon-Chai

这些链接器用于带有 [`cy.stub()`](https://docs.cypress.io/api/commands/stub) and [`cy.spy()`](https://docs.cypress.io/api/commands/spy).

| Sinon.JS property/method | Assertion                                                               |
| ------------------------ | ----------------------------------------------------------------------- |
| called                   | `expect(spy).to.be.called`                                              |
| callCount                | `expect(spy).to.have.callCount(n)`                                      |
| calledOnce               | `expect(spy).to.be.calledOnce`                                          |
| calledTwice              | `expect(spy).to.be.calledTwice`                                         |
| calledThrice             | `expect(spy).to.be.calledThrice`                                        |
| calledBefore             | `expect(spy1).to.be.calledBefore(spy2)`                                 |
| calledAfter              | `expect(spy1).to.be.calledAfter(spy2)`                                  |
| calledWithNew            | `expect(spy).to.be.calledWithNew`                                       |
| alwaysCalledWithNew      | `expect(spy).to.always.be.calledWithNew`                                |
| calledOn                 | `expect(spy).to.be.calledOn(context)`                                   |
| alwaysCalledOn           | `expect(spy).to.always.be.calledOn(context)`                            |
| calledWith               | `expect(spy).to.be.calledWith(...args)`                                 |
| alwaysCalledWith         | `expect(spy).to.always.be.calledWith(...args)`                          |
| calledWithExactly        | `expect(spy).to.be.calledWithExactly(...args)`                          |
| alwaysCalledWithExactly  | `expect(spy).to.always.be.calledWithExactly(...args)`                   |
| calledWithMatch          | `expect(spy).to.be.calledWithMatch(...args)`                            |
| alwaysCalledWithMatch    | `expect(spy).to.always.be.calledWithMatch(...args)`                     |
| returned                 | `expect(spy).to.have.returned(returnVal)`                               |
| alwaysReturned           | `expect(spy).to.have.always.returned(returnVal)`                        |
| threw                    | `expect(spy).to.have.thrown(errorObjOrErrorTypeStringOrNothing)`        |
| alwaysThrew              | `expect(spy).to.have.always.thrown(errorObjOrErrorTypeStringOrNothing)` |
