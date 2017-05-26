---
title: Express入门（三）
date: 2016-10-21 14:35:43
tags: Express
category: 教程
---

## 番外一：部署到Heroku

### 1.使用 MongoHQ

在把我们的博客部署到 Heroku 之前，我们首先学习下如何使用 MongoHQ 。MongoHQ 是一个提供 MongoDB 存储服务的云平台，使用起来非常简单，提供了在线查询和修改数据库的功能。MongoHQ 的免费套餐提供了 512MB 的存储空间。

#### 注册

[https://bridge.mongohq.com/signup](https://bridge.mongohq.com/signup)

#### 创建一个数据库

注册后，选择一个 **Free** 的数据库类型，并给数据库起一个名字，点击 **Create Database** 创建数据库。此时跳转到如下界面：

![](https://github.com/nswbmw/N-blog/blob/master/public/images/19.1.jpg?raw=true)

如图所示，我们可以在命令行中连接远程数据库，也可以通过 Mongo URL 使用数据库。接下来，我们修改博客的代码，使用 MongoHQ 提供的云端数据库取代使用本地数据库。

首先，我们需要给数据库添加一个用户。点击左侧的 **Admin** ，然后点击 **Users** 进入用户管理页面。在 username 和 password 处分别填写用户名和密码：

```
db.addUser('username','password')
```

点击 **Add user** 添加用户。

修改 settings.js 为：

```
module.exports = { 
  cookieSecret: 'myblog', 
  url: 'your_Mongo_URI'
};
```

将 your\_Mongo\_URI 替换为你自己创建的数据库的 URL ，将 `<user>` 和 `<password>` 分别替换为刚才添加的用户的名字和密码。

打开 app.js ，将 `app.use(express.session(...));` 修改为：

```
app.use(express.session({
  secret: settings.cookieSecret,
  cookie: {maxAge: 1000 * 60 * 60 * 24 * 30},//30 days
  url: settings.url
}));
```

删除 db.js ，打开 post.js 、 user.js 和 comment.js ，均作以下修改：

- 将 `mongodb = require('./db')` 修改为 `mongodb = require('mongodb').Db`
- 添加 `var settings = require('../settings');`
- 将所有 `mongodb.open(function (err, db) {` 修改为 `mongodb.connect(settings.url, function (err, db) {`
- 将所有 `mongodb.close();` 修改为 `db.close();`

现在，无需启动你的本地数据库，运行你的博客试试吧~

**注意**：Heroku 也提供了 MongoHQ 的 Add-ons ，但需要填写信用卡信息，所以我们这里直接使用外链的 MongoHQ 。

### 2.部署到 Heroku

Heroku 是一个主流的 PaaS 提供商，在开发人员中广受欢迎。这个服务围绕着基于 Git 的工作流设计，假如你熟悉 Git ，那部署就十分简单。这个服务原本是为托管 Ruby 应用程序而设计的，但 Heroku 之后加入了对 Node.js 、Clojure 、Scala 、Python 和 Java 等语言的支持。Heroku 的基础服务是免费的。

下面我们使用 Heroku 部署我们的博客。

#### 注册

[https://www.heroku.com/](https://www.heroku.com/)

#### 创建一个应用

注册成功后，就进入了控制面板页面，如图所示：

![](https://github.com/nswbmw/N-blog/blob/master/public/images/19.2.jpg?raw=true)

点击 **Create a new app** ，填写独一无二的应用名称后，点击 **creat app** 即创建成功，然后点击 **Finish up** 。

此时跳转到控制面板页，并且可以看到我们创建的应用了。我们通过 **应用名称.herokuapp.com** 即可访问我们的应用主页。如图所示：

![](https://github.com/nswbmw/N-blog/blob/master/public/images/19.3.jpg?raw=true)

### 3.安装 Heroku Toolbelt

Heroku 官方提供了 Heroku Toolbelt 工具更方便地部署和管理应用。它包含三个部分：

- **Heroku client** ：创建和管理 Heroku 应用的命令行工具
- **Foreman** ：一个在本地运行你的 app 的不错的选择
- **Git** ：分布式版本控制工具，用来把应用推送到 Heroku

Heroku Toolbelt 下载地址：[https://toolbelt.heroku.com/](https://toolbelt.heroku.com/) 。

**注意**：假如你的电脑上已经安装了 Git ，那么在安装的时候选择 **Custom Installation** 并去掉安装 Git 的选项，否则选择 **Full Installation** 。

安装成功后，打开 Git Bash ，输入 `heroku login` ，然后输入在 Heroku 注册的帐号和密码进行登录。Git 会检测是否有 SSH 密钥，如果有，则使用此密钥并上传，如果没有，则创建一个密钥并上传。

**Tips**：SSH 密钥通常用于授予用户访问服务器的权限。可将它们用于某些配置中，以便无需密码即可访问服务器。许多 PaaS 提供商都使用了此功能。

### 4.Procfile

在工程的根目录下新建一个 **Procfile** 文件，添加如下内容：

```
web: node app.js
```

**Procfile** 文件告诉了服务器该使用什么命令启动一个 web 服务，这里我们通过 `node app.js` 执行 Node 脚本。为什么这里声明了一个 `web` 类型呢？官方解释为：

> The name “web” is important here. It declares that this process type will be attached to the HTTP routing stack of Heroku, and receive web traffic when deployed.

### 5.上传应用

打开 Git Bash ，输入：

```
$ git init
$ git add .
$ git commit -m "init"
$ git remote add heroku git@heroku.com:yourAppName.git
```

**注意**：将 yourAppName 修改为你自己的应用名。

在 push 到 heroku 服务器之前，我们还需要做一个工作。由于我国某些政策的原因，我们需到 **~/.ssh/** 目录下，新建一个 **config** 文件，内容如下：

```
Host heroku.com
User yourName
Hostname 107.21.95.3
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa
port 22
```

然后回到 Git Bash ，输入：

```
$ git push heroku master
```

稍等片刻即上传成功。现在你就可以访问 **http://yourAppName.herokuapp.com/** 了，如图所示：

![](https://github.com/nswbmw/N-blog/blob/master/public/images/19.4.jpg?raw=true)

**注意**：假如出现了 **Application Error**，可能是没有启动应用，到应用面板页勾选 **web node app.js** ，然后点击 **Apply Changes** 启动应用。

## 番外二：使用_id查询

我们知道，MongoDB 会自动为每个文档添加一个特殊的 `_id` 键，这个 `_id` 键的值是经过特殊计算的长度为 24 的字符串的 ObjectId 对象（详见《MongoDB 权威指南》），因此保证了每个文档的 `_id` 都是独一无二的。那我们可不可以使用 `_id` 键查询一个独一无二的文档呢？当然可以，这也是设计 `_id` 的原因所在。

**注意**：使用 `name` 、`day` 、`title` 查询一篇文章有个小 bug ，即不能在同一天发表相同标题的文章，或者说发表了相同标题的文章后只能返回最近发表的那篇文章。使用 `_id` 就可以很好的避免这个 bug 。

下面我们举例使用 `_id` 代替使用 `name` 、`day` 、`title` 来查询一篇文章，即将：

```
app.get('/u/:name/:day/:title')
```

修改为以下形式：

```
app.get('/p/:_id')
```



打开 post.js ，在最上面添加：

```
var ObjectID = require('mongodb').ObjectID;
```

将：

```
Post.getOne = function(name, day, title, callback) {
```



修改为：

```
Post.getOne = function(_id, callback) {
```

并将 `Post.getOne()` 内两处的：

```
"name": name,
"time.day": day,
"title": title
```

都修改为：

```
"_id": new ObjectID(_id)
```

打开 index.js ，将 `app.get('/u/:name/:day/:title')` 修改如下：

```
app.get('/p/:_id', function (req, res) {
  Post.getOne(req.params._id, function (err, post) {
    if (err) {
      req.flash('error', err); 
      return res.redirect('/');
    }
    res.render('article', {
      title: post.title,
      post: post,
      user: req.session.user,
      success: req.flash('success').toString(),
      error: req.flash('error').toString()
    });
  });
});
```

**注意**：我们将文章页面的路由修改为 `app.get('/p/:_id')` 而不是 `app.get('/u/:_id')` 是为了防止和上面的用户页面的路由 `app.get('/u/:name')` 冲突，况且，`p` 也代表 `post` ，表示发表的文章的意思。

打开 index.ejs ，将：

```
<p><h2><a href="/u/<%= post.name %>/<%= post.time.day %>/<%= post.title %>"><%= post.title %></a></h2>
```

修改为：

```
<p><h2><a href="/p/<%= post._id %>"><%= post.title %></a></h2>
```

现在，运行你的博客并发表一篇文章，从主页点击标题进入该文章页面，就变成了以下的 url 形式：

```
http://localhost:3000/p/52553dcd5bb408ec11000002
```

**注意**：MongoDB 数据库中是以以下形式存储 `_id` 的：

```
"_id" : ObjectId("52553dcd5bb408ec11000002")
```

我们可以直接使用 `post._id` 从数据库中获取 _id 的值（24 位长字符串），但在查询的时候，要把 _id 字符串包装成 MongoDB 特有的 ObjectId 类型。

读者可依此类推，自行将剩余的工作完成。

## 番外三：使用Async

Async 是一个流行的异步编程类库，提供了直接而强大的 JavaScript 异步功能。虽然是为 Node.js 设计的，但是它也可以直接在浏览器中使用。

Async 提供了大约 20 个函数，包括常用的 map, reduce, filter, forEach 等等，也有常用的异步流程控制函数，包括 parallel, series, waterfall 等等。所有这些函数都是假设你遵循了 Node.js 的约定：在异步函数的最后提供一个回调函数作为参数。

Async 包括三部分：

1. 流程控制：简化十种常见流程的处理
2. 集合处理：如何使用异步操作处理集合中的数据
3. 工具类：几个常用的工具类

这里我们不会讲解 Async 的使用，读者可去以下链接学习 Async 的相关知识：

- Async ： [https://github.com/caolan/async](https://github.com/caolan/async)
- stackoverflow ： [http://stackoverflow.com/](http://stackoverflow.com/)
- Async详解之一：流程控制 ： [http://freewind.me/blog/20120515/917.html](http://freewind.me/blog/20120515/917.html)
- Async详解之二：工具类 ： [http://freewind.me/blog/20120517/931.html](http://freewind.me/blog/20120517/931.html)
- Async详解之三：集合操作 ： [http://freewind.me/blog/20120518/932.html](http://freewind.me/blog/20120518/932.html)
- Nodejs异步流程控制Async ： [http://blog.fens.me/nodejs-async/](http://blog.fens.me/nodejs-async/)

我们在操作数据库的时候经常会这样写，以 `Post.getOne` 为例：

```
Post.getOne = function(name, day, title, callback) { 
  mongodb.open(function (err, db) {
    if (err) { ... }
    db.collection('posts', function (err, collection) {
      if (err) { ... }
      collection.findOne({ ... }, function (err, doc) {
        if (err) { ... }
        collection.update({ ... }, function (err) {
          mongodb.close();
          callback( ... );
        });
      });
    });
  });
};
```

这就是典型的深度嵌套回调，代码看起来并不美观。下面我们使用 Async 解决这个问题。

首先，在 `package.json` 中添加对 Async 的依赖：

```
"async": "*"
```

并 `npm install` 安装 Async 包。

在使用 Async 之前，我们先学习下 `async.waterfall` 的基本用法。

`waterfall(tasks, [callback])` ：多个函数依次执行，且前一个的输出为后一个的输入，即每一个函数产生的值，都将传给下一个函数。如果中途出错，后面的函数将不会被执行。错误信息以及之前产生的结果，将传给 waterfall 最终的 callback，一个简单的例子：

```
var async = require('async');
```

```
async.waterfall([
    function(callback){
        callback(null, 'one', 'two');
    },
    function(arg1, arg2, callback){
        console.log('arg1 => ' + arg1);
        console.log('arg2 => ' + arg2);
        callback(null, 'three');
    },
    function(arg3, callback){
        console.log('arg3 => ' + arg3);
        callback(null, 'done');
    }
], function (err, result) {
   console.log('err => ' + err);
   console.log('result => ' + result);
});
```

运行结果为：

```
arg1 => one
arg2 => two
arg3 => three
err => null
result => done
```

将 `callback(null, 'three');` 修改为：

```
callback('error occurred !', 'three');
```

运行结果为：

```
arg1 => one
arg2 => two
err => error occurred !
result => three
```

我们以修改 user.js 为例，将 user.js 修改如下：

```
var mongodb = require('./db');
var crypto = require('crypto');
var async = require('async');

function User(user) {
  this.name = user.name;
  this.password = user.password;
  this.email = user.email;
};

module.exports = User;

User.prototype.save = function(callback) {
  var md5 = crypto.createHash('md5'),
      email_MD5 = md5.update(this.email.toLowerCase()).digest('hex'),
      head = "http://www.gravatar.com/avatar/" + email_MD5 + "?s=48";
  var user = {
      name: this.name,
      password: this.password,
      email: this.email,
      head: head
  };
  async.waterfall([
    function (cb) {
      mongodb.open(function (err, db) {
        cb(err, db);
      });
    },
    function (db, cb) {
      db.collection('users', function (err, collection) {
        cb(err, collection);
      });
    },
    function (collection, cb) {
      collection.insert(user, {
        safe: true
      }, function (err, user) {
        cb(err, user);
      });
    }
  ], function (err, user) {
    mongodb.close();
    callback(err, user[0]);
  });
};

User.get = function(name, callback) {
  async.waterfall([
    function (cb) {
      mongodb.open(function (err, db) {
        cb(err, db);
      });
    },
    function (db, cb) {
      db.collection('users', function (err, collection) {
        cb(err, collection);
      });
    },
    function (collection, cb) {
      collection.findOne({
        name: name
      }, function (err, user) {
        cb(err, user);
      });
    }
  ], function (err, user) {
    mongodb.close();
    callback(err, user);
  });
};
```

关于 Async 的使用详见 [https://github.com/caolan/async](https://github.com/caolan/async) ，读者可自行完成剩余的修改工作。

## 番外四：使用Disqus

前面我们搭建的博客使用了自建的留言系统，支持 Markdown ，并且将留言存到了数据库中。现在我们来使用 Disqus 代替原来的留言系统。

### 0.什么是 Disqus？

Disqus 是一个第三方社会化评论系统，主要为网站主提供评论托管服务。CNN、NBC、Fox News、Engadget、Time 等知名网站均使用了 Disqus 提供的社会化评论系统。WordPress、Blogger、Tumblr 等第三方博客平台均提供了 Disqus 第三方评论插件。目前，第三方社会化评论系统在美国，基本是主流网站的标配。

Disqus 的主要目标是通过提供功能强大的第三评论系统，将当前不同网站的相对孤立、隔绝的评论系统，连接成具有社会化特性的大网。通过 Disqus 评论系统所具备的评论回复通知、评论分享和热文分享等社会化功能，网站主可以有效的提高网站用户的活跃度和流量。用户使用 Disqus，在不同网站上评论，无需重复注册账号，只需使用 Disqus 账号或者第三方平台账号，即可方便的进行评论，且所有评论都会存储、保存在 Disqus 账号后台，方便随时查看、回顾。而且，当有用户回复自己的评论时，可以选择使用邮箱接收相关信息，保证所有评论的后续行为都可以随时掌握。与此同时，Disqus 将社交交友功能也很好的融入到了评论系统中，当用户在某一网站上看到有与自己类似观点的评论时，可对该评论的评论者进行关注，关注后，该评论者以后的所有评论都会显示在自己的账号后台。

### 1.为什么使用 Disqus？

- 相比较使用自建的留言系统，使用 Disqus 有以下几点优势：
- 支持评论嵌套
- 支持使用 Disqus 或第三方账号评论
- 简单安全。不用存储到自己的数据库，安全性也得到提高
- 方便并且强大的评论管理功能
- 集成良好，自适应，简洁优美
- 等等

### 2.注册 Disqus

[https://disqus.com/profile/signup/](https://disqus.com/profile/signup/)

### 3.使用 Disqus

使用 Disqus 非常简单！

第一步：登陆后进入到 http://disqus.com/dashboard/ 页面，点击左侧的 +add 按钮创建一个站点，填写好信息后点击 Finish registration 完成创建。

第二步：此时进入到了 Choose your platform 页面。这里根据我们的实际情况点击第一个 Universal Code 按钮。

第三步：此时进入到了 Disqus 安装说明页。这里有详细的说明步骤，我们这里只需复制第一个代码块中的代码。然后打开 comment.ejs ，删除所有代码并粘贴刚才复制的代码，保存即可。

现在运行我们的博客，发表篇文章试试吧，如下图所示：

![](https://raw.github.com/nswbmw/N-blog/master/public/images/24.1.jpg)

读者可自行删除有关存储评论的代码，这里不再赘述。

### 4.参考文献

Disqus 百度百科 ： [http://baike.baidu.com/view/5941866.htm](http://baike.baidu.com/view/5941866.htm)

## 番外五：使用generic-tool

目前为止，我们都是这样处理请求的，比如：当用户访问某个文章页的时候，系统会创建一个数据库连接，通过该连接到数据库中查找并返回该文章的数据，然后关闭该连接。但是当我们的博客访问量巨大的时候，频繁的创建和销毁连接会产生非常大的系统开销。这个时候，我们就需要引入数据库连接池了。

什么是连接池（connection pool）呢？维基百科中是这样定义的：

> connection pool is a cache of database connections maintained so that the connections can be reused when future requests to the database are required.

说白了就是，我们一开始就创建一沓数据库连接，并保持长连不断开。当我们需要访问数据库的时候，就去那一沓连接（俗称连接池）中拿来一个用，用完（对数据库增删改查完）后再把这条连接释放到连接池中（依然不断开）。这样我们只在一开始创建一沓数据库连接时会有一些开销，而这种开销总比频繁的创建和销毁连接小得多。

在 Node.js 中，我们可以使用 generic-pool 这个模块帮助我们创建和管理数据库连接池。

首先，在 package.json 中添加对 generic-pool 的依赖：

```
"generic-pool": "*"
```

并 npm install 安装 generic-pool 模块。

打开 db.js ，将：

```
module.exports = new Db(settings.db, new Server(settings.host, settings.port), {safe: true});
```

修改为：

```
module.exports = function() {
  return new Db(settings.db, new Server(settings.host, settings.port), {safe: true, poolSize: 1});
}
```

这里我们导出一个函数，每次调用该函数则创建一个数据库连接。

打开 post.js ，将：

```
var mongodb = require('./db'),
    markdown = require('markdown').markdown;
```

修改为：

```
var Db = require('./db');
var markdown = require('markdown').markdown;
var poolModule = require('generic-pool');
var pool = poolModule.Pool({
  name     : 'mongoPool',
  create   : function(callback) {
    var mongodb = Db();
    mongodb.open(function (err, db) {
      callback(err, db);
    })
  },
  destroy  : function(mongodb) {
    mongodb.close();
  },
  max      : 100,
  min      : 5,
  idleTimeoutMillis : 30000,
  log      : true
});
```

以上就创建了一个 mongodb 连接池，其中 name 指明该连接池的名字，create 指明创建一条数据库连接的方法，并返回创建的连接，destroy 指明如何销毁连接，max 指明连接池中最大连接数，min 指明连接池中最小连接数，idleTimeoutMillis 指明不活跃连接销毁的毫秒数，这里为 30000 即当一条连接 30 秒处于不活跃状态（即没有被使用过）时则销毁该连接。log 指明是否打印连接池日志，这里我们选择打印。

如何使用连接池呢？很简单。只需将所有:

```
mongodb.open(function (err, db) {
  ...
  mongodb.close();
});
```

修改为：

```
pool.acquire(function (err, mongodb) {
  ...
  pool.release(mongodb);
});
```

这里我们使用 `pool.acquire` 去连接池中获取一条可用连接，使用完毕后通过 `pool.release` 释放该连接，而不是 close 掉。

读者可自行完成剩余的修改工作。

## 番外六：使用handlebars

前面我们在 Express 中使用的 EJS 模板引擎进行渲染视图和页面的展示。当模版文件代码比较多且逻辑复杂时，代码就变得非常难看了，满眼的 `<%` 和 `%>`。下面我们尝试使用 Handlebars 这个模版引擎替换 EJS ，代码会变得整洁许多。

Handlebars 是 JavaScript 一个语义模板库，通过对 view 和 data 的分离来快速构建 Web 模板。它采用 "Logic-less template"（无逻辑模版）的思路，在加载时被预编译，而不是到了客户端执行到代码时再去编译，这样可以保证模板加载和运行的速度。Handlebars 兼容 Mustache，你可以在 Handlebars 中导入 Mustache 模板。

Handlebars 的语法也非常简单易学。这里我们不会讲解 Handlebars 的语法，官网（ [http://handlebarsjs.com/](http://handlebarsjs.com/) ）的文档非常全面。

我们使用 express-handlebars 这个第三方包添加对 Handlebars 的支持。

**注意**：也许你会非常自觉的认为应该使用 `npm install handlebars` 安装 Handlebars 然后开始大刀阔斧地修改代码。但在这里我们不使用官方提供的 Handlebars 包，Express 默认支持的模板引擎中不包含 Handlebars ，虽然我们可以通过 consolidate.js + handlebars 实现，但仍然有一个缺点是不支持从一个模版文件加载另一个模版文件，而在 EJS 中可以使用 `<%- include someTemplate %>` 轻松实现。express-handlebars 包弥补了该缺点，所以我们使用 express-handlebars 来完成代码的修改。

首先，打开 package.json ，删除 ejs 并添加对 express-handlebars 的依赖：

```
"express-handlebars": "*"
```

并 `npm install` 安装 express-handlebars 包。

打开 app.js ，添加一行：

```
var exphbs  = require('express-handlebars');
```

然后将：

```
app.set('view engine', 'ejs');
```

修改为：

```
app.engine('hbs', exphbs({
  layoutsDir: 'views',
  defaultLayout: 'layout',
  extname: '.hbs'
}));
app.set('view engine', 'hbs');
```

这里我们注册模板引擎处理后缀名为 hbs 的文件，然后通过 `app.set('view engine', 'hbs');` 设置模板引擎。以上参数的意思是：

`layoutsDir: 'views'`： 设置布局模版文件的目录为 views 文件夹
`defaultLayout: 'layout'`： 设置默认的页面布局模版为 layout.hbs 文件，跟 Express 2.x 中的 layout.ejs 作用类似。
`extname: '.hbs'`： 模版文件使用的后缀名，这个 `.hbs` 是我们自定的，我们当然可以使用 `.html` 和 `.handlebars` 等作为后缀，只需把以上的 `hbs` 全部替换即可。

我们还可以设置其他几个参数，详见 [https://github.com/ericf/express-handlebars](https://github.com/ericf/express-handlebars)。

我们以修改主页为例，学习如何使用 Handlebars 。为了测试修改后能否正常显示文章及其相关信息，在开始之前，我们先注册几个用户并发表几篇文章，然后进行一些互相转载、访问和留言等工作，而不是清空数据库。

然后打开 views 文件夹，删除 header.ejs 和 footer.ejs ，新建 layout.hbs ，添加如下代码：

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<title>Blog</title>
<link rel="stylesheet" href="/stylesheets/style.css">
</head>
<body>

<header>
<h1>{{title}}</h1>
</header>

<nav>
<span><a title="主页" href="/">home</a></span>
<span><a title="存档" href="/archive">archive</a></span>
<span><a title="标签" href="/tags">tags</a></span>
<span><a title="友情链接" href="/links">links</a></span>
{{#if user}}
  <span><a title="上传" href="/upload">upload</a></span>
  <span><a title="发表" href="/post">post</a></span>
  <span><a title="登出" href="/logout">logout</a></span>
{{else}}
  <span><a title="登录" href="/login">login</a></span>
  <span><a title="注册" href="/reg">register</a></span>
{{/if}}
<span><form action="/search" method="GET"><input type="text" name="keyword" placeholder="SEARCH" class="search" /></form></span>
</nav>

<article>

{{#if success}}
  <div>{{success}}</div>
{{/if}}
{{#if error}}
  <div>{{error}}</div>
{{/if}}

{{{body}}}

</article>
</body>
</html>
```

这里我们定义了一个默认的页面布局模版（layout.hbs）。其余所有的模版都将 "继承" 该模版，即替换掉 `  { { { body } } }` 部分。

删除 index.ejs ，新建 index.hbs ，添加如下代码：

```ejs
{{#each posts}}
  <p><h2><a href="/u/{{name}}/{{time.day}}/{{title}}">{{title}}</a></h2>
  <a href="/u/{{name}}"><img src="{{head}}" class="r_head" /></a></p>
  <p class="info">
    作者：<a href="/u/{{name}}">{{name}}</a> | 
    日期：{{time.minute}} | 
    标签：
    {{#each tags}}
      {{#if this}}
        <a class="tag" href="/tags/{{this}}">{{this}}</a>
      {{/if}}
    {{/each}}
    {{#if reprint_info.reprint_from}}
      <br><a href="/u/{{reprint_info.reprint_from.name}}/{{reprint_info.reprint_from.day}}/{{reprint_info.reprint_from.title}}">原文链接</a>
    {{/if}}
  </p>
  <p>{{{post}}}</p>
  <p class="info">
    阅读：{{pv}} | 
    评论：{{comments.length}} | 
    转载：
    {{#if reprint_info.reprint_to}}
      {{reprint_info.reprint_to.length}}
    {{else}}
      0
    {{/if}}
  </p>
{{/each}}
```

这样就可以了，现在运行你的博客试试吧。

当我们渲染 index.hbs 的`res.render('index', { ... });`时，index.hbs 会替换 layout.hbs 中的 `{ { { body } } }` 部分，然后渲染视图。需要注意的是，我们在 `{ { #each } } ... { { /each } }` 中使用了 `this` ，这里的 `this` 指向当前上下文，即代表遍历的每一项。

注意**：Handlebars 中的 `{ { { htmlContext } } }`，相当于 EJS 中的 `<%- htmlContext %>` ，`{ { textContext } }` 相当于 `<%= textContext %>` 。

在 ejs 中，我们可以随意使用 JavaScript 表达式，如 `<% if (1 + 1 === 2) { %> ... <% } %>` ，但在 Handlebars 中我们却不能这样写 `{ { #if (1 + 1 === 2) } } ... { { /if } }` ，那么该如何修改 archive.ejs 呢？archive.ejs 代码如下：

```
<%- include header %>
<ul class="archive">
<% var lastYear = 0 %>
<% posts.forEach(function (post, index) { %>
  <% if (lastYear != post.time.year) { %>
    <li><h3><%= post.time.year %></h3></li>
  <% lastYear = post.time.year } %>
    <li><time><%= post.time.day %></time></li>
    <li><a href="/u/<%= post.name %>/<%= post.time.day %>/<%= post.title %>"><%= post.title %></a></li>
<% }) %>
</ul>
<%- include footer %>
```

我们通过定义了一个 lastYear 变量实现了判断并只显示一次年份的功能。在 Handlebars 中，我们可以通过 registerHelper 实现以上功能，关于 registerHelper 的使用详见 [http://handlebarsjs.com/block_helpers.html](http://handlebarsjs.com/block_helpers.html)。在 express-handlebars 中使用 registerHelper 也很简单，具体如下。

打开 index.js ，将 `app.get('/archive')` 修改如下：

```
app.get('/archive', function (req, res) {
  Post.getArchive(function (err, posts) {
    if (err) {
      req.flash('error', err); 
      return res.redirect('/');
    }
    res.render('archive', {
      title: '存档',
      posts: posts,
      user: req.session.user,
      success: req.flash('success').toString(),
      error: req.flash('error').toString(),
      helpers: {
        showYear: function(index, options) {
          if ((index == 0) || (posts[index].time.year != posts[index - 1].time.year)) {
            return options.fn(this);
          }
        }
      }
    });
  });
});
```

删除 archive.ejs ，新建 archive.hbs ，添加如下代码：

```
<ul class="archive">
{{#each posts}}
  {{#showYear @index}}
    <li><h3>{{this.time.year}}</h3></li>
  {{/showYear}}
  <li><time>{{this.time.day}}</time></li>
  <li><a href="/u/{{this.post.name}}/{{this.time.day}}/{{this.title}}">{{this.title}}</a></li>
{{/each}}
</ul>
```

假如你了解如何使用 Handlebars 中的 registerHelper ，那么上面的代码就很容易理解了。其中，`{ { #each } } ... { { /each } }` 内的 @index 表示当前遍历的索引。

最后，还需提醒的一点是：我们每次渲染一个视图文件时，都会结合 layout.hbs 然后渲染，有时候我们并不需要 layout.hbs ，比如 404 页面，需设置为：

```
res.render('404', {
  layout: false
});
```

通过设置 `layout: false` 就取消了自动加载 layout.hbs 页面布局模版。

至此，我们通过采用 layout 的方式实现了视图文件的加载及渲染，express-handlebars 还提供了另一种类似于 EJS 中 include 的加载方式——使用 partial ，前面的修改中我们并没有添加分页模版（paging.hbs），要想引入分页模版使用 `{ { > paging } }` 即可。详细使用见 [https://github.com/ericf/express-handlebars](https://github.com/ericf/express-handlebars)。

读者可自行完成剩余的修改工作。

## 番外七：使用KindEditor

前面我们搭建的博客使用了 Markdown 来写文章，假如普通用户使用的话不懂什么是 Markdown ，加之 Markdown 的表现力还并不是很丰富。这个时候，我们就需要一款强大的编辑器了，我们不妨试试 KindEditor。

### 0.什么是 KindEditor

KindEditor 是一套开源的在线 HTML 编辑器，主要用于让用户在网站上获得所见即所得编辑效果，开发人员可以用 KindEditor 把传统的多行文本输入框（textarea）替换为可视化的富文本输入框。KindEditor 使用 JavaScript 编写，可以无缝地与 Java、.NET、PHP、ASP 等程序集成，比较适合在 CMS、商城、论坛、博客、Wiki、电子邮件等互联网应用上使用。

**主要特点**

- 快速：体积小，加载速度快 
- 开源：开放源代码，高水平，高品质 
- 底层：内置自定义 DOM 类库，精确操作 DOM 
- 扩展：基于插件的设计，所有功能都是插件，可根据需求增减功能 
- 风格：修改编辑器风格非常容易，只需修改一个 CSS 文件 
- 兼容：支持大部分主流浏览器，比如 IE、Firefox、Safari、Chrome、Opera 

### 1.使用 KindEditor

到官网 [http://www.kindsoft.net/](http://www.kindsoft.net/) 下载最新的 KindEditor 压缩包，解压后将文件夹重命名为 kindEditor 并放到 public 文件夹下。

**注意**：可以根据自己需求删除文件夹或文件，我们删除以下文件夹：

- asp - ASP程序
- asp.net - ASP.NET程序
- php - PHP程序
- jsp - JSP程序
- examples - 演示文件

首先，我们来将多行文本输入框（textarea）替换为 kindEditor 编辑器。打开 header.ejs ，在：

```
<link rel="stylesheet" href="/stylesheets/style.css">
```

下一行添加如下代码：

```
<script charset="utf-8" src="/KindEditor/kindeditor-min.js"></script>
<script charset="utf-8" src="/KindEditor/lang/zh_CN.js"></script>
<script>
var editor;
KindEditor.ready(function(K) {
  editor = K.create('textarea', {
  allowImageUpload : false,
  items : [
    'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold', 'italic',
    'underline', 'removeformat', '|', 'justifyleft', 'justifycenter', 'justifyright',
    'insertorderedlist', 'insertunorderedlist', '|', 'emoticons', 'image', 'link']
  });
});
</script>
```

**注意**：这里我们通过 create 创建了一个编辑器，第一个参数为 CSS 选择器，设置为 textarea ，则发表、编辑及留言的 textarea 都会变为编辑器。假如我们只想让发表和编辑时使用编辑器，留言时不使用编辑器，则只需将 `textarea` 修改为 `textarea[name="post"]` 即可。第二个参数可以设置编辑器的编辑选项，这里我们通过自定义 items 配置编辑器的工具栏，其中可用 "/" 表示换行，"|" 表示分隔符。，并设置 `allowImageUpload : false` 取消编辑器的图片上传按钮。详细的编辑器配置请查阅 [http://www.kindsoft.net/docs/option.html](http://www.kindsoft.net/docs/option.html)。

以上是简单的（simple）编辑器样式，我们也可以使用 KindEditor 默认的（default）编辑器样式，将以上 `KindEditor.ready` 替换为以下代码即可(这里我们不做修改)：

```
var editor;
KindEditor.ready(function(K) {
  editor = K.create('#kindeditor');
});
```

最后，删除有关转换 Markdown 的代码。打开 post.js ，删除：

```
markdown = require('markdown').markdown
```

删除 `Post.getTen` 内的：

```
docs.forEach(function (doc) {
  doc.post = markdown.toHTML(doc.post);
}); 
```

删除 `Post.getOne` 内的：

```
doc.post = markdown.toHTML(doc.post);
doc.comments.forEach(function (comment) {
  comment.content = markdown.toHTML(comment.content);
});
```

现在，运行你的博客试试吧。

**发表前**

![](https://github.com/nswbmw/N-blog/blob/master/public/images/22.1.jpg?raw=true)

**发表后**

![](https://github.com/nswbmw/N-blog/blob/master/public/images/22.2.jpg?raw=true)

**注意**：添加图片地址时，引用站外的图片要用绝对地址，引用站内的图片则用相对地址，如：/images/lufei.jpg 。

更多关于 KindEditor 的使用详见官方文档。

### 2.参考文献

- KindEditor ： [http://www.kindsoft.net/](http://www.kindsoft.net/)
- 可视化HTML编辑器 KindEditor ： [http://www.oschina.net/p/kindeditor/](http://www.oschina.net/p/kindeditor/)

## 番外八：使用mongoose

Mongoose 是 MongoDB 数据库的模型工具，为 Node.js 设计，工作于异步环境下，基于 node-mongodb-native。

与使用 node-mongodb-native 相比，使用 Mongoose 可以简化不少代码。这里我们不会讲解 Mongoose 的使用，读者可去以下链接学习 Mongoose 的相关知识：

- mongoosejs ： [http://mongoosejs.com/](http://mongoosejs.com/)
- stackoverflow ： [http://stackoverflow.com/](http://stackoverflow.com/)
- Mongoose学习参考文档——基础篇 ： [http://cnodejs.org/topic/504b4924e2b84515770103dd](http://cnodejs.org/topic/504b4924e2b84515770103dd)
- Mongoose 基本功能使用 ： [http://www.csser.com/board/4f4e92dbeb0defac5700011e](http://www.csser.com/board/4f4e92dbeb0defac5700011e)
- Mongoose - 让NodeJS更容易操作Mongodb数据库 ： [http://www.csser.com/board/4f3f516e38a5ebc9780004fe](http://www.csser.com/board/4f3f516e38a5ebc9780004fe)

下面我们尝试在博客应用中使用 Mongoose 。

首先，在 `package.json` 中添加对 mongoose 的依赖：

```
"mongoose": "*"
```

并 `npm install` 安装 mongoose 包。

**注意**：完全使用 mongoose 的话可以删除 mongodb 模块，但我们这里只是局部使用 mongoose ，所以暂时保留。

修改 user.js 如下：

```
var crypto = require('crypto');
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/blog');// 优化可参考 [#57](https://github.com/nswbmw/N-blog/issues/57)

var userSchema = new mongoose.Schema({
  name: String,
  password: String,
  email: String,
  head: String
}, {
  collection: 'users' 
});

var userModel = mongoose.model('User', userSchema);

function User(user) {
  this.name = user.name;
  this.password = user.password;
  this.email = user.email;
};

User.prototype.save = function(callback) {
  var md5 = crypto.createHash('md5'),
      email_MD5 = md5.update(this.email.toLowerCase()).digest('hex'),
      head = "http://www.gravatar.com/avatar/" + email_MD5 + "?s=48";
  var user = {
      name: this.name,
      password: this.password,
      email: this.email,
      head: head
  };

  var newUser = new userModel(user);

  newUser.save(function (err, user) {
    if (err) {
      return callback(err);
    }
    callback(null, user);
  });
};

User.get = function(name, callback) {
  userModel.findOne({name: name}, function (err, user) {
    if (err) {
      return callback(err);
    }
    callback(null, user);
  });
};

module.exports = User;
```

**注意**：Mongoose 会自动为每一个文档添加一个 `__v` 即 versionKey （版本锁），如下所示：

```
> db.users.find()
{ "name" : "nswbmw", "password" : "d41d8cd98f00b204e9800998ecf8427e", "email" :
"gxqzk@126.com", "head" : "http://www.gravatar.com/avatar/11c35a5b58d99d2c8a9501
65b795917d?s=48", "_id" : ObjectId("527ae6e8d38086540a000001"), "__v" : 0 }
```

关于 versionKey 的使用详见： [http://mongoosejs.com/docs/guide.html#versionKey](http://mongoosejs.com/docs/guide.html#versionKey) 。

读者可自行完成剩余的修改工作。

## 番外九：使用Passport

前面我们自己写了一个简单的登陆认证系统，即用户在登陆时，通过输入事先注册的用户名和密码，服务器确认用户的身份后，从而获得操作权限。这也是最传统的登陆认证方式。

随着互联网的不断开放与发展，又出现了一种新的登陆认证方式——第三方登陆认证，即我们常说的oAuth/oAuth2.0。

**什么是 oAuth？**

> OAUTH协议为用户资源的授权提供了一个安全的、开放而又简易的标准。与以往的授权方式不同之处是OAUTH的授权不会使第三方触及到用户的帐号信息（如用户名与密码），即第三方无需使用用户的用户名与密码就可以申请获得该用户资源的授权，因此OAUTH是安全的。

**什么是 Passport？**

> Passport是一个基于Node.js的认证中间件。极其灵活并且模块化，Passport可以很容易地跟任意基于Express的Web应用结合使用。

现在我们来修改代码，使得我们的博客既支持本地登陆又支持使用 GitHub 账户登录。

首先，登录 GitHub ，点击右上角的 Account settings ，然后点击左侧的 Applications ，然后点击右上角的 Register new application 创建一个 GitHub 应用。

创建成功后如下图所示：

![](https://raw.github.com/nswbmw/N-blog/master/public/images/25.1.jpg)

稍后我们将会用到 **Client ID** 、**Client Secret** 和 **Authorization callback URL**。

打开 package.json ，添加 passport 和 passport-github 模块：

```
"passport": "*",
"passport-github": "*"
```

并 npm install 安装这两个模块。

至此，准备工作都已完成，接下来我们修改代码支持使用 GitHub 账户登录。

首先，添加使用 GitHub 登陆的链接。打开 login.ejs，在：

```
<%- include footer %>
```

上一行添加如下代码：

```
<a href="/login/github">使用 GitHub 登录</a>
```

然后打开 app.js ，在 `var app = express();` 下添加如下代码：

```
var passport = require('passport')
    , GithubStrategy = require('passport-github').Strategy;
```

在 `app.use(app.router);` 上添加一行代码：

```
app.use(passport.initialize());//初始化 Passport
```

在 `if ('development' == app.get('env'))` 上添加如下代码：

```
passport.use(new GithubStrategy({
  clientID: "xxx",
  clientSecret: "xxx",
  callbackURL: "xxx"
}, function(accessToken, refreshToken, profile, done) {
  done(null, profile);
}));
```

**注意**：将 clientID、clientSecret 和 callbackURL 分别替换为刚才创建 GitHub 应用得到的信息。

以上代码的意思是：我们定义了一个 Passport 策略，并尝试从 GitHub 获得授权，从 GitHub 登陆并授权成功后以跳转到 **callbackURL** 并以 JSON 形式返回用户的一些相关信息，并将这些信息存储在 `req.user` 中。

打开 index.js ，在上方添加一行代码：

```
var passport = require('passport');
```

并在 `app.get('/login')` 后添加如下代码：

```
app.get("/login/github", passport.authenticate("github", {session: false}));
app.get("/login/github/callback", passport.authenticate("github", {
  session: false,
  failureRedirect: '/login',
  successFlash: '登陆成功！'
}), function (req, res) {
  req.session.user = {name: req.user.username, head: "https://gravatar.com/avatar/" + req.user._json.gravatar_id + "?s=48"};
  res.redirect('/');
});
```

这里我们可以直接使用 Express 的 session 功能，所以禁掉 Passport 的 session 功能，前面提到过 Passport 默认会将取得的用户信息存储在 `req.user` 中而不是 `req.session.user`，为了保持兼容，所以我们提取并序列化有用的数据保存到 `req.session.user` 中。

至此，我们的博客也支持 GitHub 登录了，是不是很简单？目前还存在三个问题：

1. GitHub 用户名和本地数据库用户名重名的问题。
2. 不能访问使用 GitHub 账户登录的用户的用户页。
3. 无法从 GitHub 获得用户的邮箱。

第一个问题的简单粗暴的解决方法是当用户以 GitHub 账户登录时，把获取的用户名到本地数据库查一下，若存在则禁止登录，若不存在则允许登陆。

第二个问题修改一下代码即可解决，删除 index.js 中 `app.get('/u/:name')` 内的那层判断数据库中是否存在该用户名的函数即可。

第三个问题暂时无法解决，因为 GitHub 返回的信息中并不包含有效的用户邮箱。