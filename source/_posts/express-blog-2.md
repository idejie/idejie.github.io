---
title: Express入门（二）
date: 2016-10-21 14:04:12
tags: Express
category: 教程
---

## 七、使用Markdown编辑器

现在我们来给博客添加支持 markdown 发表文章的功能。  
假如你不还熟悉 markdown，请转到：[http://wowubuntu.com/markdown/](http://wowubuntu.com/markdown/)

打开 package.json ，添加一行代码：

```son
"markdown": "0.5.0"
```

使用 `npm install` 安装 markdown 模块。

打开 post.js，在 `mongodb = require('./db')` 后添加一行代码：

```
markdown = require('markdown').markdown;
```

在 `Post.get` 函数里的 `callback(null, docs);` 前添加以下代码：

```
//解析 markdown 为 html
docs.forEach(function (doc) {
  doc.post = markdown.toHTML(doc.post);
});
```

现在我们就可以使用 markdown 发表文章了。

**注意**：每当我们给博客添加新功能后，都要清空数据库（即删除 mongodb/blog 文件夹里所有文件）再启动我们的博客。以后每一章都是如此，后面便不再赘述。

运行我们的博客，如图所示：

**发表前**

![](https://github.com/nswbmw/N-blog/blob/master/public/images/2.1.jpg?raw=true)

**发表后**

![](https://github.com/nswbmw/N-blog/blob/master/public/images/2.2.jpg?raw=true)



## 八、添加文件上传功能

一个完整的博客怎么能缺少图片呢？现在，我们来给博客添加文件上传功能，这样我们就可以使用 markdown 来链接图片了。

我们使用express的第三方中间件 multer 实现文件上传功能。打开 package.json，在 dependencies 中添加：

```
"multer": "1.1.0"
```

并 npm install 安装模块。然后修改 index.js，添加：

```
var multer  = require('multer');
原版本使用方法
//app.use(multer({
//  dest: './public/images',
//  rename: function (fieldname, filename) {
//    return filename;
//  }
//}));
新的使用方法
var storage = multer.diskStorage({
    destination: function (req, file, cb){
        cb(null, './public/images')
    },
    filename: function (req, file, cb){
        cb(null, file.originalname)
    }
});
var upload = multer({
    storage: storage
});
```

其中，destination 是上传的文件所在的目录，filename 函数用来修改上传后的文件名，这里设置为保持原来的文件名。

打开 header.ejs ，在 `<span><a title="发表" href="/post">post</a></span>` 前添加一行代码：

```
<span><a title="上传" href="/upload">upload</a></span>
```

然后打开 index.js ，在 `app.get('/logout')` 函数后添加如下代码：

```
app.get('/upload', checkLogin);
app.get('/upload', function (req, res) {
  res.render('upload', {
    title: '文件上传',
    user: req.session.user,
    success: req.flash('success').toString(),
    error: req.flash('error').toString()
  });
});
```

**注意**：我们设置 `app.get('/upload', checkLogin);` 限制只有登陆的用户才能上传文件。

接下来，我们在 views 文件夹下新建 upload.ejs ，添加如下代码：

```
<%- include header %>
<form method='post' action='/upload' enctype='multipart/form-data' >
  <input type="file" multiple name='field1'/><br>
  <input type="submit" />
</form>
<%- include footer %>
```

现在我们就可以访问文件上传页面了。IE可能会产生多文件上传兼容问题。清空数据库，重新注册登录后，上传文件页面如下图：
页面未修改，实际上应该只剩下一个上传控件显示（新修改的）

![](https://github.com/nswbmw/N-blog/blob/master/public/images/3.1.jpg?raw=true)

我们现在只是有了一个可以上传文件的表单而已，并不能上传文件，接下来我们添加对上传文件的支持。

在 `app.get('/upload')` 后添加如下代码：

```
app.post('/upload', checkLogin);
app.post('/upload', upload.array('field1', 5), function (req, res) {
  req.flash('success', '文件上传成功!');
  res.redirect('/upload');
});
```

其中，第一个参数array表示可以同时上传多个文件，第二个参数5表示最多上传5个文件
**注意**：假如从桌面启动的博客上传图片时失败，尝试在命令行中从博客根目录下启动。

现在，我们给博客添加了文件上传功能。假如我们上传了一张名为 **lufei.jpg** 的图片，示例：

**发表前**

![](https://github.com/nswbmw/N-blog/blob/master/public/images/3.2.jpg?raw=true)

**发表后**

![](https://github.com/nswbmw/N-blog/blob/master/public/images/3.3.jpg?raw=true)

## 九、实现文章页面和用户页面

现在，我们来给博客添加用户页面和文章页面。

所谓用户页面就是当点击某个用户名链接时，跳转到：`域名/u/用户名` ，并列出该用户的所有文章。  
同理，文章页面就是当点击某篇文章标题时，跳转到：`域名/u/用户名/时间/文章名` ，进入到该文章的页面（也许还有该文章的评论等）。

在开始之前我们需要做一个工作，打开 post.js ，将 `Post.get` 修改为 `Post.getAll` ，同时将 index.js 中 `Post.get` 修改为 `Post.getAll` 。在 post.js 最后添加如下代码：

```
//获取一篇文章
Post.getOne = function(name, day, title, callback) {
  //打开数据库
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    //读取 posts 集合
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      //根据用户名、发表日期及文章名进行查询
      collection.findOne({
        "name": name,
        "time.day": day,
        "title": title
      }, function (err, doc) {
        mongodb.close();
        if (err) {
          return callback(err);
        }
        //解析 markdown 为 html
        doc.post = markdown.toHTML(doc.post);
        callback(null, doc);//返回查询的一篇文章
      });
    });
  });
};
```

简单解释一下：

- `Post.getAll` ：获取一个人的所有文章（传入参数 name）或获取所有人的文章（不传入参数）。
- `Post.getOne` ：根据用户名、发表日期及文章名精确获取一篇文章。

下面我们来实现用户页面和文章页面。

打开 index.js ，在 `app.post('/upload')` 后添加如下代码：

```
app.get('/u/:name', function (req, res) {
  //检查用户是否存在
  User.get(req.params.name, function (err, user) {
    if (!user) {
      req.flash('error', '用户不存在!'); 
      return res.redirect('/');//用户不存在则跳转到主页
    }
    //查询并返回该用户的所有文章
    Post.getAll(user.name, function (err, posts) {
      if (err) {
        req.flash('error', err); 
        return res.redirect('/');
      } 
      res.render('user', {
        title: user.name,
        posts: posts,
        user : req.session.user,
        success : req.flash('success').toString(),
        error : req.flash('error').toString()
      });
    });
  }); 
});
```

这里我们添加了一条路由规则 `app.get('/u/:name')`，用来处理访问用户页的请求，然后从数据库取得该用户的数据并渲染 user.ejs 模版，生成页面并显示给用户。  

接下来我们添加文章页面的路由规则。  
在 `app.get('/u/:name')` 后添加如下代码：  

```
app.get('/u/:name/:day/:title', function (req, res) {
  Post.getOne(req.params.name, req.params.day, req.params.title, function (err, post) {
    if (err) {
      req.flash('error', err); 
      return res.redirect('/');
    }
    res.render('article', {
      title: req.params.title,
      post: post,
      user: req.session.user,
      success: req.flash('success').toString(),
      error: req.flash('error').toString()
    });
  });
});
```

最后，我们创建用户页面和文章页面的模版文件。

在 views 文件夹下新建 user.ejs，添加如下代码，同时也将 index.ejs 也修改成如下代码：

```
<%- include header %>
<% posts.forEach(function (post, index) { %>
  <p><h2><a href="/u/<%= post.name %>/<%= post.time.day %>/<%= post.title %>"><%= post.title %></a></h2></p>
  <p class="info">
    作者：<a href="/u/<%= post.name %>"><%= post.name %></a> | 
    日期：<%= post.time.minute %>
  </p>
  <p><%- post.post %></p>
<% }) %>
<%- include footer %>
```

在 views 文件夹下新建 article.ejs ，添加如下代码：

```
<%- include header %>
<p class="info">
  作者：<a href="/u/<%= post.name %>"><%= post.name %></a> | 
  日期：<%= post.time.minute %>
</p>
<p><%- post.post %></p>
<%- include footer %>
```

然后将index.ejs中的href更改如下：

```
<%- include header %>
<% posts.forEach(function (post, index) { %>
  <p><h2><a href="u/<%= post.name %>/<%= post.time.day %>/<%= post.title %>"><%= post.title %></a></h2></p>
  <p class="info">
    作者：<a href="u/<%= post.name %>"><%= post.name %></a> |
    日期：<%= post.time.minute %>
  </p>
  <p><%- post.post %></p>
  <% }) %>
<%- include footer %>
```

现在，我们给博客添加了用户页面和文章页面。示例：

**用户页面**

![](https://github.com/nswbmw/N-blog/blob/master/public/images/4.1.jpg?raw=true)

**文章页面**

![](https://github.com/nswbmw/N-blog/blob/master/public/images/4.2.jpg?raw=true)

## 十、增加编辑和删除功能

现在，我们来给博客添加编辑文章与删除文章的功能。

我们设定：当一个用户在线时，只允许他在自己发表的文章页进行编辑或删除，编辑时，只能编辑文章内容，不能编辑文章标题。

打开 style.css ，添加如下样式：

```
.edit{margin:3px;padding:2px 5px;border-radius:3px;background-color:#f3f3f3;color:#333;font-size:13px;}
.edit:hover{text-decoration:none;background-color:#f00;color:#fff;-webkit-transition:color .2s linear;}
```

打开 article.ejs ，将代码修改成如下：

```
<%- include header %>
<p>
  <span><a class="edit" href="/edit/<%= post.name %>/<%= post.time.day %>/<%= post.title %>">编辑</a></span>
  <span><a class="edit" href="/remove/<%= post.name %>/<%= post.time.day %>/<%= post.title %>">删除</a></span>
</p>
<p class="info">
  作者：<a href="/u/<%= post.name %>"><%= post.name %></a> | 
  日期：<%= post.time.minute %>
</p>
<p><%- post.post %></p>
<%- include footer %>
```

至此，我们只是在文章页面添加了编辑和删除文章的链接。接下来，我们注册这两个链接的点击事件的响应。

打开 post.js ，在最后添加如下代码：

```
//返回原始发表的内容（markdown 格式）
  Post.edit = function(name, day, title, callback) {
  //打开数据库
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    //读取 posts 集合
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      //根据用户名、发表日期及文章名进行查询
      collection.findOne({
        "name": name,
        "time.day": day,
        "title": title
      }, function (err, doc) {
        mongodb.close();
        if (err) {
          return callback(err);
        }
        callback(null, doc);//返回查询的一篇文章（markdown 格式）
      });
    });
  });
};
```

打开 index.js ，在 `app.get('/u/:name/:day/:title')` 后添加如下代码：

```
app.get('/edit/:name/:day/:title', checkLogin);
app.get('/edit/:name/:day/:title', function (req, res) {
  var currentUser = req.session.user;
  Post.edit(currentUser.name, req.params.day, req.params.title, function (err, post) {
    if (err) {
      req.flash('error', err); 
      return res.redirect('back');
    }
    res.render('edit', {
      title: '编辑',
      post: post,
      user: req.session.user,
      success: req.flash('success').toString(),
      error: req.flash('error').toString()
    });
  });
});
```

在 views 下新建 edit.ejs ，添加如下代码：

```ejs
<%- include header %>
<form method="post" action="/edit/<%= post.name %>/<%= post.time.day %>/<%= post.title %>">
  标题：<br />
  <input type="text" name="title" value="<%= post.title %>" disabled="disabled" /><br />
  正文：<br />
  <textarea name="post" rows="20" cols="100"><%= post.post %></textarea><br />
  <input type="submit" value="保存修改" />
</form>
<%- include footer %>
```

现在，运行我们的博客看看吧。在文章页面，当我们点击 **编辑** 后就会跳转到该文章对应的编辑页面了。接下来我们实现将修改后的文章提交到数据库。

打开 post.js ，在最后添加如下代码：

```
//更新一篇文章及其相关信息
Post.update = function(name, day, title, post, callback) {
  //打开数据库
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    //读取 posts 集合
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      //更新文章内容
      collection.update({
        "name": name,
        "time.day": day,
        "title": title
      }, {
        $set: {post: post}
      }, function (err) {
        mongodb.close();
        if (err) {
          return callback(err);
        }
        callback(null);
      });
    });
  });
};
```

打开 index.js ，在 `app.get('/edit/:name/:day/:title')` 后添加如下代码：

```
app.post('/edit/:name/:day/:title', checkLogin);
app.post('/edit/:name/:day/:title', function (req, res) {
  var currentUser = req.session.user;
  Post.update(currentUser.name, req.params.day, req.params.title, req.body.post, function (err) {
    var url = encodeURI('/u/' + req.params.name + '/' + req.params.day + '/' + req.params.title);
    if (err) {
      req.flash('error', err); 
      return res.redirect(url);//出错！返回文章页
    }
    req.flash('success', '修改成功!');
    res.redirect(url);//成功！返回文章页
  });
});
```

现在，我们就可以编辑并保存文章了。赶紧试试吧！

接下来，我们实现删除文章的功能。打开 post.js ，在最后添加如下代码：

```
//删除一篇文章
Post.remove = function(name, day, title, callback) {
  //打开数据库
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    //读取 posts 集合
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      //根据用户名、日期和标题查找并删除一篇文章
      collection.remove({
        "name": name,
        "time.day": day,
        "title": title
      }, {
        w: 1
      }, function (err) {
        mongodb.close();
        if (err) {
          return callback(err);
        }
        callback(null);
      });
    });
  });
};
```

打开 index.js ，在 `app.post('/edit/:name/:day/:title')` 后添加如下代码：

```
app.get('/remove/:name/:day/:title', checkLogin);
app.get('/remove/:name/:day/:title', function (req, res) {
  var currentUser = req.session.user;
  Post.remove(currentUser.name, req.params.day, req.params.title, function (err) {
    if (err) {
      req.flash('error', err); 
      return res.redirect('back');
    }
    req.flash('success', '删除成功!');
    res.redirect('/');
  });
});
```

至此我们完成了大部分的工作，接下来我们实现页面权限的控制。假如你现在注册了两个帐号 A 和 B，那么当 B 访问 A 的用户页面时，也会出现编辑和删除的选项，虽然点击后并不能编辑和删除 A 的文章。那怎么才能实现一个账号只能编辑和删除自己发表的文章呢？很简单，添加一个判断即可。打开 article.ejs ，将：

```
<span><a class="edit" href="/edit/<%= post.name %>/<%= post.time.day %>/<%= post.title %>">编辑</a></span>
<span><a class="edit" href="/remove/<%= post.name %>/<%= post.time.day %>/<%= post.title %>">删除</a></span>
```

修改为：

```
<% if (user && (user.name == post.name)) { %>
  <span><a class="edit" href="/edit/<%= post.name %>/<%= post.time.day %>/<%= post.title %>">编辑</a></span>
  <span><a class="edit" href="/remove/<%= post.name %>/<%= post.time.day %>/<%= post.title %>">删除</a></span>
<% } %>
```

以上代码的意思是：通过检测 session 中的用户名是否存在，若存在且和当前文章页面的作者名相同，则显示编辑和删除按钮，否则不显示。

现在，我们完成了给博客添加编辑文章与删除文章的功能。

## 十一、实现留言功能

一个完整的博客怎么能缺少留言功能呢，当然我们可以用第三方社会化评论插件，既然我们有了数据库，我们不妨把留言保存到自己的数据库里。

我们设定：只有在文章页面才会显示留言板。

打开 post.js ，修改 `Post.prototype.save` 中要存入的文档为：

```
var post = {
    name: this.name,
    time: time,
    title:this.title,
    post: this.post,
    comments: []
};
```

我们在文档里增加了 comments 键（数组），用来存储此文章上的留言（一个个对象）。为了也让留言支持 markdown 语法，我们将 `Post.getOne` 函数里的：

```
doc.post = markdown.toHTML(doc.post);
```

修改为：

```
if (doc) {
  doc.post = markdown.toHTML(doc.post);
  doc.comments.forEach(function (comment) {
    comment.content = markdown.toHTML(comment.content);
  });
}
```

接下来我们在 models 下新建 comment.js 文件，添加如下代码：

```
var mongodb = require('./db');
```

```
function Comment(name, day, title, comment) {
  this.name = name;
  this.day = day;
  this.title = title;
  this.comment = comment;
}

module.exports = Comment;

//存储一条留言信息
Comment.prototype.save = function(callback) {
  var name = this.name,
      day = this.day,
      title = this.title,
      comment = this.comment;
  //打开数据库
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    //读取 posts 集合
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      //通过用户名、时间及标题查找文档，并把一条留言对象添加到该文档的 comments 数组里
      collection.update({
        "name": name,
        "time.day": day,
        "title": title
      }, {
        $push: {"comments": comment}
      } , function (err) {
          mongodb.close();
          if (err) {
            return callback(err);
          }
          callback(null);
      });   
    });
  });
};
```

修改 index.js ，在 `Post = require('../models/post.js')` 后添加一行代码：

```
Comment = require('../models/comment.js');
```

这里我们创建了 comment 的模型文件，用于存储新的留言到数据库，并在 index.js 中引入以作后用。

接下来我们创建 comment 的视图文件，在 views 文件夹下新建 comment.ejs ，添加如下代码(e.g.  首先要先插入一个留言再显示)：

```
<br />
<% post.comments.forEach(function (comment, index) { %>
  <p><a href="<%= comment.website %>"><%= comment.name %></a>
  <span class="info"> 回复于 <%= comment.time %></span></p>
  <p><%- comment.content %></p>
<% }) %>

<form method="post" action="/u/<%= post.name %>/<%= post.time.day %>/<%= post.title %>">
<% if (user) { %>
  姓名：<input type="text" name="name" value="<%= user.name %>" /><br />
  邮箱：<input type="text" name="email" value="<%= user.email %>" /><br />
  网址：<input type="text" name="website" value="/u/<%= user.name %>" /><br />
<% } else { %>
  姓名：<input type="text" name="name" /><br />
  邮箱：<input type="text" name="email" /><br />
  网址：<input type="text" name="website" value="http://" /><br />
<% } %>
  <textarea name="content" rows="5" cols="80"></textarea><br />
  <input type="submit" value="留言" />
</form>
```

**注意**：这里根据用户登录状态的不同，显示不同的提示信息。还需注意的一点是，未登录的用户在留言的时候， **网址** 这一项需要加上 `http://` 前缀，否则在生成连接的时候会基于当前 url （本地是 localhost:3000）。

打开 article.ejs ，在 `<%- include footer %>` 前添加一行代码：

```
<%- include comment %>
```

这样我们就在文章页面引入了留言模块。

最后，修改 index.js ，注册留言的 POST 响应，在 `app.get('/u/:name/:day/:title')` 后添加如下代码：

```
app.post('/u/:name/:day/:title', function (req, res) {
  var date = new Date(),
      time = date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate() + " " + 
             date.getHours() + ":" + (date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes());
  var comment = {
      name: req.body.name,
      email: req.body.email,
      website: req.body.website,
      time: time,
      content: req.body.content
  };
  var newComment = new Comment(req.params.name, req.params.day, req.params.title, comment);
  newComment.save(function (err) {
    if (err) {
      req.flash('error', err); 
      return res.redirect('back');
    }
    req.flash('success', '留言成功!');
    res.redirect('back');
  });
});
```

**注意**：这里我们使用 `res.redirect('back');` ，即留言成功后返回到该文章页。

现在，我们就给博客添加了留言的功能。

## 十二、实现分页

现在我们给博客的主页和用户页面增加分页功能。

我们设定：主页和用户页面每页最多显示十篇文章。

这里我们要用到 mongodb 的 skip 和 limit 操作，具体可查阅《mongodb权威指南》。

打开 post.js ，把 `Post.getAll` 函数修改如下：

```
//一次获取十篇文章
Post.getTen = function(name, page, callback) {
  //打开数据库
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    //读取 posts 集合
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      var query = {};
      if (name) {
        query.name = name;
      }
      //使用 count 返回特定查询的文档数 total
      collection.count(query, function (err, total) {
        //根据 query 对象查询，并跳过前 (page-1)*10 个结果，返回之后的 10 个结果
        collection.find(query, {
          skip: (page - 1)*10,
          limit: 10
        }).sort({
          time: -1
        }).toArray(function (err, docs) {
          mongodb.close();
          if (err) {
            return callback(err);
          }
          //解析 markdown 为 html
          docs.forEach(function (doc) {
            doc.post = markdown.toHTML(doc.post);
          });  
          callback(null, docs, total);
        });
      });
    });
  });
};
```

打开 index.js ，修改 `app.get('/', function(req,res){` 如下：

```
app.get('/', function (req, res) {
  //判断是否是第一页，并把请求的页数转换成 number 类型
  var page = parseInt(req.query.p) || 1;
  //查询并返回第 page 页的 10 篇文章
  Post.getTen(null, page, function (err, posts, total) {
    if (err) {
      posts = [];
    } 
    res.render('index', {
      title: '主页',
      posts: posts,
      page: page,
      isFirstPage: (page - 1) == 0,
      isLastPage: ((page - 1) * 10 + posts.length) == total,
      user: req.session.user,
      success: req.flash('success').toString(),
      error: req.flash('error').toString()
    });
  });
});
```

**注意**：这里通过 `req.query.p` 获取的页数为字符串形式，我们需要通过 `parseInt()` 把它转换成数字以作后用。同时把 `Post.getAll` 改成了 `Post.getTen` 。

修改 `app.get('/u/:name')` 如下：

```
app.get('/u/:name', function (req, res) {
  var page = parseInt(req.query.p) || 1;
  //检查用户是否存在
  User.get(req.params.name, function (err, user) {
    if (!user) {
      req.flash('error', '用户不存在!'); 
      return res.redirect('/');
    }
    //查询并返回该用户第 page 页的 10 篇文章
    Post.getTen(user.name, page, function (err, posts, total) {
      if (err) {
        req.flash('error', err); 
        return res.redirect('/');
      } 
      res.render('user', {
        title: user.name,
        posts: posts,
        page: page,
        isFirstPage: (page - 1) == 0,
        isLastPage: ((page - 1) * 10 + posts.length) == total,
        user: req.session.user,
        success: req.flash('success').toString(),
        error: req.flash('error').toString()
      });
    });
  }); 
});
```

接下来在 views 文件夹下新建 paging.ejs ，添加如下代码：

```
<br />
<div>
  <% if (!isFirstPage) { %>
    <span class="prepage"><a title="上一页" href="?p=<%= page-1 %>">上一页</a></span>
  <% } %>

  <% if (!isLastPage) { %>
    <span class="nextpage"><a title="下一页" href="?p=<%= page+1 %>">下一页</a></span>
  <% } %>
</div>
```

这里通过 `if(!isFirstPage)` 判断是否为第一页，不是第一页则显示 “上一页” ；通过 `if(!isLastPage)` 判断是否为最后一页，不是最后一页则显示 “下一页” 。

接下来在主页和用户页引入分页。修改 index.ejs 和 user.ejs ，在 `<%- include footer %>` 前添加一行代码：

```
<%- include paging %>
```

在主页和用户页面引入分页模块。

最后，在 style.css 中添加以下样式：

```
.prepage a{float:left;text-decoration:none;padding:.5em 1em;color:#ff0000;font-weight:bold;}
.nextpage a{float:right;text-decoration:none;padding:.5em 1em;color:#ff0000;font-weight:bold;}
.prepage a:hover,.nextpage a:hover{text-decoration:none;background-color:#ff0000;color:#f9f9f9;-webkit-transition:color .2s linear;}
```

现在，我们实现了博客的分页功能。

## 十三、增加存档页面

现在我们来给博客增加存档功能，当进入存档页时，按年份和日期的降序列出所有的文章。

首先，我们在主页左侧导航中添加存档页（archive）的链接，修改 header.ejs，在 `<span><a title="主页" href="/">home</a></span>` 下添加一行代码：

```
<span><a title="存档" href="/archive">archive</a></span>
```

打开 post.js ，在最后添加以下代码：

```
//返回所有文章存档信息
Post.getArchive = function(callback) {
  //打开数据库
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    //读取 posts 集合
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      //返回只包含 name、time、title 属性的文档组成的存档数组
      collection.find({}, {
        "name": 1,
        "time": 1,
        "title": 1
      }).sort({
        time: -1
      }).toArray(function (err, docs) {
        mongodb.close();
        if (err) {
          return callback(err);
        }
        callback(null, docs);
      });
    });
  });
};
```

接下来我们在 index.js 中添加 `/archive` 的路由规则。打开 index.js ，在 `app.get('/u/:name')` 前添加以下代码：

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
      error: req.flash('error').toString()
    });
  });
});
```

在 views 文件夹下新建 archive.ejs 模版文件，添加如下代码：

```
<%- include header %>
<ul class="archive">
<% var lastYear = 0 %>
<% posts.forEach(function (post, index) { %>
  <% if (lastYear != post.time.year) { %>
    <li><h3><%= post.time.year %></h3></li>
  <% lastYear=post.time.year } %>
  <li><time><%= post.time.day %></time></li>
  <li><a href="/u/<%= post.name %>/<%= post.time.day %>/<%= post.title %>"><%= post.title %></a></li>
<% }) %>
</ul>
<%- include footer %>
```

这里我们通过在模版中设置一个 lastYear 变量判断是否和上次已经显示的年份相同，相同则不再显示年份，不同则显示。

最后，在 style.css 中添加如下样式：

```
.archive{list-style:none;line-height:28px;}
.archive h3{margin:0.5em 0;}
.archive time{float:left;font-size:14px;color:#999999;margin-right:1.2em;}
```

现在，我们增加了文章的存档页面。

## 十四、实现标签功能

现在我们来给博客增加标签和标签页。

我们设定：每篇文章最多有三个标签（少于三个也可以），当点击主页左侧标签页链接时，跳转到标签页并列出所有已存在标签；当点击任意一个标签链接时，跳转到该标签页并列出所有含有该标签的文章。

### 添加标签

首先我们来实现给文章添加标签的功能。

打开 post.ejs ，在 `<input type="text" name="title" /><br />` 后添加：

```
标签：<br />
<input type="text" name="tag1" /><input type="text" name="tag2" /><input type="text" name="tag3" /><br />
```

打开 index.js ，将 `app.post('/post')` 内的：

```
var currentUser = req.session.user,
    post = new Post(currentUser.name, req.body.title, req.body.post);
```

修改为：

```
var currentUser = req.session.user,
    tags = [req.body.tag1, req.body.tag2, req.body.tag3],
    post = new Post(currentUser.name, req.body.title, tags, req.body.post);
```

打开 post.js ，将：

```
function Post(name, title, post) {
  this.name = name;
  this.title= title;
  this.post = post;
}
```

修改为：

```
function Post(name, title, tags, post) {
  this.name = name;
  this.title = title;
  this.tags = tags;
  this.post = post;
}
```

将：

```
var post = {
    name: this.name,
    time: time,
    title: this.title,
    post: this.post,
    comments: []
};
```

修改为：

```
var post = {
    name: this.name,
    time: time,
    title: this.title,
    tags: this.tags,
    post: this.post,
    comments: []
};
```

现在我们就可以在发表文章的时候添加标签了。接下来我们修改 index.ejs 、 user.ejs 和 article.ejs 来显示文章的标签。

修改 index.ejs 、 user.ejs 和 article.ejs，将：

```
<p class="info">
  作者：<a href="/u/<%= post.name %>"><%= post.name %></a> | 
  日期：<%= post.time.minute %>
</p>
```

修改为：

```
<p class="info">
  作者：<a href="/u/<%= post.name %>"><%= post.name %></a> | 
  日期：<%= post.time.minute %> | 
  标签：
  <% post.tags.forEach(function (tag, index) { %>
    <% if (tag) { %>
      <a class="tag" href="/tags/<%= tag %>"><%= tag %></a>
    <% } %>
  <% }) %>
</p>
```

最后，在 style.css 中添加如下样式：

```
.tag{background-color:#ff0000;border-radius:3px;font-size:14px;color:#ffffff;display:inline-block;padding:0 5px;margin-bottom:8px;}
.tag:hover{text-decoration:none;background-color:#ffffff;color:#000000;-webkit-transition:color .2s linear;}
```

至此，我们给博客添加了标签功能。赶紧看看效果吧！

### 添加标签页

接下来我们给博客增加标签页。

修改 header.ejs ，在 `<span><a title="存档" href="/archive">archive</a></span>` 下一行添加：

```
<span><a title="标签" href="/tags">tags</a></span>
```

修改 index.js ，在 `app.get('/archive')` 后添加如下代码：

```
app.get('/tags', function (req, res) {
  Post.getTags(function (err, posts) {
    if (err) {
      req.flash('error', err); 
      return res.redirect('/');
    }
    res.render('tags', {
      title: '标签',
      posts: posts,
      user: req.session.user,
      success: req.flash('success').toString(),
      error: req.flash('error').toString()
    });
  });
});
```

打开 post.js ，在最后添加：

```
//返回所有标签
Post.getTags = function(callback) {
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      //distinct 用来找出给定键的所有不同值
      collection.distinct("tags", function (err, docs) {
        mongodb.close();
        if (err) {
          return callback(err);
        }
        callback(null, docs);
      });
    });
  });
};
```

**注意**：这里我们用了 distinct （详见《mongodb权威指南》）返回 tags 键的所有不同值，因为有时候我们发表文章的标签是一样的，所以这样避免了获取重复的标签。

在 views 文件夹下新建 tags.ejs ，添加如下代码：

```
<%- include header %>
<% posts.forEach(function (tag, index) { %>
  <a class="tag" href="/tags/<%= tag %>"><%= tag %></a>
<% }) %>
<%- include footer %>
```

至此，我们就给博客添加了标签页。

### 添加特定标签的页面

现在我们来添加特定标签的页面，即当点击任意一个标签链接时，跳转到该标签页并列出所有含有该标签的文章信息。

修改 post.js ，在最后添加如下代码：

```
//返回含有特定标签的所有文章
Post.getTag = function(tag, callback) {
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      //查询所有 tags 数组内包含 tag 的文档
      //并返回只含有 name、time、title 组成的数组
      collection.find({
        "tags": tag
      }, {
        "name": 1,
        "time": 1,
        "title": 1
      }).sort({
        time: -1
      }).toArray(function (err, docs) {
        mongodb.close();
        if (err) {
          return callback(err);
        }
        callback(null, docs);
      });
    });
  });
};
```

修改 index.js ，在 `app.get('/tags')` 后添加如下代码：

```
app.get('/tags/:tag', function (req, res) {
  Post.getTag(req.params.tag, function (err, posts) {
    if (err) {
      req.flash('error',err); 
      return res.redirect('/');
    }
    res.render('tag', {
      title: 'TAG:' + req.params.tag,
      posts: posts,
      user: req.session.user,
      success: req.flash('success').toString(),
      error: req.flash('error').toString()
    });
  });
});
```

在 views 文件夹下新建 tag.ejs ，添加如下代码：

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

最后，别忘了修改 edit.ejs ，为了保持和 post.ejs 一致。将 edit.ejs 修改为：

```
<%- include header %>
<form method="post">
  标题：<br />
  <input type="text" name="title" value="<%= post.title %>" disabled="disabled" /><br />
  标签：<br />
  <input type="text" name="tag1" value="<%= post.tags[0] %>" disabled="disabled" />
  <input type="text" name="tag2" value="<%= post.tags[1] %>" disabled="disabled" />
  <input type="text" name="tag3" value="<%= post.tags[2] %>" disabled="disabled" /><br />
  正文：<br />
  <textarea name="post" rows="20" cols="100"><%= post.post %></textarea><br />
  <input type="submit" value="保存修改" />
</form>
<%- include footer %>
```

**注意**：这里我们设定了编辑时不能编辑文章的标题和标签。

现在，我们的博客就增加了标签和标签页的功能。

十四、实现PV统计和留言统计

现在我们来给每篇文章增加 pv 统计和留言统计。

我们设定：在主页、用户页和文章页均显示 pv 统计和留言统计。  

修改 post.js ，将：

```
var post = {
    name: this.name,
    time: time,
    title:this.title,
    tags: this.tags,
    post: this.post,
    comments: []
};
```

修改为：

```
var post = {
    name: this.name,
    time: time,
    title:this.title,
    tags: this.tags,
    post: this.post,
    comments: [],
    pv: 0
};
```

**注意**：我们给要存储的文档添加了 pv 键并直接赋初值为 0。

打开 post.js ，将 `Post.getOne()` 修改为：

```
//获取一篇文章
Post.getOne = function(name, day, title, callback) {
  //打开数据库
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    //读取 posts 集合
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      //根据用户名、发表日期及文章名进行查询
      collection.findOne({
        "name": name,
        "time.day": day,
        "title": title
      }, function (err, doc) {
        if (err) {
          mongodb.close();
          return callback(err);
        }
        if (doc) {
          //每访问 1 次，pv 值增加 1
          collection.update({
            "name": name,
            "time.day": day,
            "title": title
          }, {
            $inc: {"pv": 1}
          }, function (err) {
            mongodb.close();
            if (err) {
              return callback(err);
            }
          });
          //解析 markdown 为 html
          doc.post = markdown.toHTML(doc.post);
          doc.comments.forEach(function (comment) {
            comment.content = markdown.toHTML(comment.content);
          });
          callback(null, doc);//返回查询的一篇文章
        }
      });
    });
  });
};
```

更多关于 `$inc` 的知识请参阅《mongodb权威指南》。

增加留言统计就简单多了，直接取 `comments.length` 即可。修改 index.ejs 、user.ejs 及 article.ejs ，在：

```
<p><%- post.post %></p>
```

下一行添加一行代码：

```
<p class="info">阅读：<%= post.pv %> | 评论：<%= post.comments.length %></p>
```

现在，我们给博客增加了 pv 统计和留言统计。

## 十五、增加检索功能

现在我们来给博客增加文章检索功能，即根据关键字模糊查询文章标题，且字母不区分大小写。  
首先，我们修改 header.ejs ，在 `</nav>` 前添加一行代码：

```
<span><form action="/search" method="GET"><input type="text" name="keyword" placeholder="SEARCH" class="search" /></form></span>
```

在 style.css 中添加一行样式：

```
.search{border:0;width:6em;text-align:center;font-size:1em;margin:0.5em 0;}
```

打开 post.js ，在最后添加如下代码：

```
//返回通过标题关键字查询的所有文章信息
Post.search = function(keyword, callback) {
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      var pattern = new RegExp(keyword, "i");
      collection.find({
        "title": pattern
      }, {
        "name": 1,
        "time": 1,
        "title": 1
      }).sort({
        time: -1
      }).toArray(function (err, docs) {
        mongodb.close();
        if (err) {
         return callback(err);
        }
        callback(null, docs);
      });
    });
  });
};
```

修改 index.js ，在 `app.get('/u/:name')` 前添加如下代码：

```
app.get('/search', function (req, res) {
  Post.search(req.query.keyword, function (err, posts) {
    if (err) {
      req.flash('error', err); 
      return res.redirect('/');
    }
    res.render('search', {
      title: "SEARCH:" + req.query.keyword,
      posts: posts,
      user: req.session.user,
      success: req.flash('success').toString(),
      error: req.flash('error').toString()
    });
  });
});
```

在 views 文件夹下新建 search.ejs ，添加如下代码：

```
<%- include header %>
<ul class="archive">
<% var lastYear = 0 %>
<% posts.forEach(function (post, index) { %>
  <% if(lastYear != post.time.year) { %>
    <li><h3><%= post.time.year %></h3></li>
  <% lastYear = post.time.year } %>
    <li><time><%= post.time.day %></time></li>
    <li><a href="/u/<%= post.name %>/<%= post.time.day %>/<%= post.title %>"><%= post.title %></a></li>
<% }) %>
</ul>
<%- include footer %>
```

**注意**：目前为止，你会发现 tag.ejs 和 search.ejs 代码完全一样，因为我们都用相同的布局。这也突出了模版的优点之一 —— 可以重复利用，但我们这里并没有把这两个文件用一个代替，因为每一个文件的名字代表了不同的意义。

现在，我们给博客添加了文章检索功能。

## 十六、增加友链

现在我们来给博客添加友情链接。

打开 header.ejs ，在：

```
<span><a title="标签" href="/tags">tags</a></span>
```

下一行添加一行代码：

```
<span><a title="友情链接" href="/links">links</a></span>
```

修改 index.js ，在 `app.get('/search')` 前添加如下代码：

```
app.get('/links', function (req, res) {
  res.render('links', {
    title: '友情链接',
    user: req.session.user,
    success: req.flash('success').toString(),
    error: req.flash('error').toString()
  });
});
```

在 views 文件夹下新建 links.ejs ，添加如下代码：

```
<%- include header %>
<ul style="list-style:none">
  <li><h3><a href="https://love.alipay.com/donate/donateSingle.htm?name=201304201216494301">支付宝公益网</a></h3>天佑四川，为雅安地震捐款</li>
  <li><h3><a href="http://www.onefoundation.cn/html/cn/beneficence.html">壹基金</a></h3>壹基金雅安地震救援，刻不容缓！</li>
</ul>
<%- include footer %>
```

现在，我们给博客添加了友情链接。

## 十七、实现404

现在我们来给博客添加 404 页面，即当访问的路径都不匹配时，跳转到 404 页面。

打开 index.js ，在：

```
function checkLogin(req, res, next){ ... }
```

前添加如下代码：

```
app.use(function (req, res) {
  res.render("404");
});
```

在 views 文件夹下新建 404.ejs ，添加如下代码：

```
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Blog</title>
</head>
<body>
<script type="text/javascript" src="http://www.qq.com/404/search_children.js" charset="utf-8"></script>
</body>
</html>
```

现在，我们给博客添加了 404 页面。

## 十八、增加头像

现在我们来给博客添加用户头像，注册的用户根据注册时的邮箱获取 gravatar 头像，未注册的用户则根据留言填的邮箱获取 gravatar 头像。  
什么是 gravatar ？详情请戳：[http://www.gravatar.com](http://www.gravatar.com)

我们设定：在主页和用户页的文章标题右侧显示作者头像，在文章页面留言的人的头像显示在留言板左侧。

我们需要用到 Node.js 中的 crypto 模块，之前已经引入过，所以这里可以直接使用。  

### 添加已注册用户的头像

打开 user.js ，在最上面添加一行代码：

```
var crypto = require('crypto');
```

然后将 `User.prototype.save` 内的:

```
var user = {
    name: this.name,
    password: this.password,
    email: this.email
};
```

修改为:

```
var md5 = crypto.createHash('md5'),
    email_MD5 = md5.update(this.email.toLowerCase()).digest('hex'),
    head = "http://www.gravatar.com/avatar/" + email_MD5 + "?s=48";
//要存入数据库的用户信息文档
var user = {
    name: this.name,
    password: this.password,
    email: this.email,
    head: head
};
```

这里我们在用户文档里添加了 `head` 键，方便后面使用。

**注意**：需要把 email 转化成小写再编码。

打开 index.js ，将 `app.post('/post')` 中的：

```
post = new Post(currentUser.name, req.body.title, tags, req.body.post);
```

修改成：

```
post = new Post(currentUser.name, currentUser.head, req.body.title, tags, req.body.post);
```

修改 post.js ，将：

```
function Post(name, title, tags, post) {
  this.name = name;
  this.title = title;
  this.tags = tags;
  this.post = post;
}
```

修改为：

```
function Post(name, head, title, tags, post) {
  this.name = name;
  this.head = head;
  this.title = title;
  this.tags = tags;
  this.post = post;
}
```

将：

```
var post = {
    name: this.name,
    time: time,
    title:this.title,
    tags: this.tags,
    post: this.post,
    comments: [],
    pv: 0
};
```

修改为：

```
var post = {
    name: this.name,
    head: this.head,
    time: time,
    title:this.title,
    tags: this.tags,
    post: this.post,
    comments: [],
    pv: 0
};
```

最后，修改 index.ejs 和 user.ejs ，在 `</h2>` 后添加一行代码：

```
<a href="/u/<%= post.name %>"><img src="<%= post.head %>" class="r_head" /></a>
```

至此，我们实现了给已注册的用户添加头像的功能。

### 添加未注册用户的头像

修改 `app.post('/u/:name/:day/:title')`，将：

```
var comment = {
    name: req.body.name,
    email: req.body.email,
    website: req.body.website,
    time: time,
    content: req.body.content
};
```

修改为：

```
var md5 = crypto.createHash('md5'),
    email_MD5 = md5.update(req.body.email.toLowerCase()).digest('hex'),
    head = "http://www.gravatar.com/avatar/" + email_MD5 + "?s=48"; 
var comment = {
    name: req.body.name,
    head: head,
    email: req.body.email,
    website: req.body.website,
    time: time,
    content: req.body.content
};
```



打开 comment.ejs ，将：

```
<% post.comments.forEach(function (comment, index) { %>
  <p><a href="<%= comment.website %>"><%= comment.name %></a>
  <span class="info"> 回复于 <%= comment.time %></span></p>
  <p><%- comment.content %></p>
<% }) %>
```

修改为：

```
<% post.comments.forEach(function (comment, index) { %>
  <div style="padding-left:4em">
    <p><img src="<%= comment.head %>" class="l_head" /><a href="<%= comment.website %>"><%= comment.name %></a>
    <span class="info"> 回复于 <%= comment.time %></span></p>
    <p><%- comment.content %></p>
  </div>
<% }) %>
```

最后，在 style.css 中添加两行样式：

```
.l_head{float:left;margin-left:-4em;box-shadow:0px 1px 4px #888;}
.r_head{float:right;margin-top:-2.5em;box-shadow:0px 1px 4px #888;}
```

现在，我们给博客添加了头像的功能。

## 十九、添加转载及统计

现在，我们来给博客添加转载文章和转载数统计的功能。

我们的设计思路是：当在线用户满足特定条件时，文章页面才会显示 `转载` 链接字样，当用户点击 `转载` 后，复制一份存储当前文章的文档，修改后以新文档的形式存入数据库，而不是单纯的添加一条指向被转载的文档的 "引用" ，这种设计是合理的，因为这样我们也可以将转载来的文章进行修改。

首先，我们来完成转载文章的功能。

打开 post.js ，将 `Post.prototype.save` 内的：

```
var post = {
    name: this.name,
    head: this.head,
    time: time,
    title:this.title,
    tags: this.tags,
    post: this.post,
    comments: [],
    pv: 0
};
```

修改为：

```
var post = {
    name: this.name,
    head: this.head,
    time: time,
    title:this.title,
    tags: this.tags,
    post: this.post,
    comments: [],
    reprint_info: {},
    pv: 0
};
```

这里我们给文档里添加了 `reprint_info` 键，最多为以下形式：

```
{
  reprint_from: {name: xxx, day: xxx, title: xxx},
  reprint_to: [
    {name: xxx, day: xxx, title: xxx},
    {name: xxx, day: xxx, title: xxx},
    ...
  ]
}
```

`reprint_from` 表示转载来的原文章的信息，`reprint_to` 表示该文章被转载的信息。为了节约存储空间，我们初始设置 `reprint_info` 键为 `{}`，而不是以下形式：

```
{
  reprint_from: {},
  reprint_to: []
}
```

这是因为大多数文章是没有经过任何转载的，所以为每个文档都添加以上形式的 `reprint_info` 是有点浪费的。假如某篇文章是转载来的，我们只需给 `reprint_info` 添加上 `reprint_from` 键即可，假如某篇文章被转载了，我们只需给 `reprint_info` 添加上 `reprint_to` 键即可，假如某篇文章是转载来的且又被转载了，那我们就给 `reprint_info` 添加上 `reprint_from` 和 `reprint_to` 键即可。

打开 post.js ，在最后添加如下代码：

```
//转载一篇文章
Post.reprint = function(reprint_from, reprint_to, callback) {
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      //找到被转载的文章的原文档
      collection.findOne({
        "name": reprint_from.name,
        "time.day": reprint_from.day,
        "title": reprint_from.title
      }, function (err, doc) {
        if (err) {
          mongodb.close();
          return callback(err);
        }

        var date = new Date();
        var time = {
            date: date,
            year : date.getFullYear(),
            month : date.getFullYear() + "-" + (date.getMonth() + 1),
            day : date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate(),
            minute : date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate() + " " + 
            date.getHours() + ":" + (date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes())
        }

        delete doc._id;//注意要删掉原来的 _id

        doc.name = reprint_to.name;
        doc.head = reprint_to.head;
        doc.time = time;
        doc.title = (doc.title.search(/[转载]/) > -1) ? doc.title : "[转载]" + doc.title;
        doc.comments = [];
        doc.reprint_info = {"reprint_from": reprint_from};
        doc.pv = 0;

        //更新被转载的原文档的 reprint_info 内的 reprint_to
        collection.update({
          "name": reprint_from.name,
          "time.day": reprint_from.day,
          "title": reprint_from.title
        }, {
          $push: {
            "reprint_info.reprint_to": {
              "name": doc.name,
              "day": time.day,
              "title": doc.title
          }}
        }, function (err) {
          if (err) {
            mongodb.close();
            return callback(err);
          }
        });

        //将转载生成的副本修改后存入数据库，并返回存储后的文档
        collection.insert(doc, {
          safe: true
        }, function (err, post) {
          mongodb.close();
          if (err) {
            return callback(err);
          }
          callback(err, post[0]);
        });
      });
    });
  });
};
```

这里我们在 `Post.reprint()` 内实现了被转载的原文章的更新和转载后文章的存储。

打开 index.js ，在 `app.get('/remove/:name/:day/:title')` 后添加如下代码：

```
app.get('/reprint/:name/:day/:title', checkLogin);
app.get('/reprint/:name/:day/:title', function (req, res) {
  Post.edit(req.params.name, req.params.day, req.params.title, function (err, post) {
    if (err) {
      req.flash('error', err); 
      return res.redirect(back);
    }
    var currentUser = req.session.user,
        reprint_from = {name: post.name, day: post.time.day, title: post.title},
        reprint_to = {name: currentUser.name, head: currentUser.head};
    Post.reprint(reprint_from, reprint_to, function (err, post) {
      if (err) {
        req.flash('error', err); 
        return res.redirect('back');
      }
      req.flash('success', '转载成功!');
      var url = encodeURI('/u/' + post.name + '/' + post.time.day + '/' + post.title);
      //跳转到转载后的文章页面
      res.redirect(url);
    });
  });
});
```

至此，我们给 `转载` 链接注册了路由响应。

**注意**：我们需要通过 `Post.edit()` 返回一篇文章 markdown 格式的文本，而不是通过 `Post.getOne` 返回一篇转义后的 HTML 文本，因为我们还要将修改后的文档存入数据库，而数据库中应该存储 markdown 格式的文本。

最后，我们在文章页（article.ejs）添加转载链接。

打开 article.ejs ，在：

```
<% if (user && (user.name == post.name)) { %>
  <span><a class="edit" href="/edit/<%= post.name %>/<%= post.time.day %>/<%= post.title %>">编辑</a></span>
  <span><a class="edit" href="/remove/<%= post.name %>/<%= post.time.day %>/<%= post.title %>">删除</a></span>
<% } %>
```

后添加如下代码：

```
<% var flag = 1 %>
<% if (user && (user.name != post.name)) { %>
  <% if ((post.reprint_info.reprint_from != undefined) && (user.name == post.reprint_info.reprint_from.name)) { %>
    <% flag = 0 %>
  <% } %>
  <% if ((post.reprint_info.reprint_to != undefined)) { %>
    <% post.reprint_info.reprint_to.forEach(function (reprint_to, index) { %>
      <% if (user.name == reprint_to.name) { %>
        <% flag = 0 %>
      <% } %>
    <% }) %>
  <% } %>
<% } else { %>
  <% flag = 0 %>
<% } %>
<% if (flag) { %>
  <span><a class="edit" href="/reprint/<%= post.name %>/<%= post.time.day %>/<%= post.title %>">转载</a></span>
<% } %>
```

以上代码的意思是：我们设置一个 flag 标志，如果用户是游客，或者是该文章的目前作者，或者是该文章的上一级作者，或者已经转载过该文章，都会将 flag 设置为 0 ，即不显示 `转载` 链接，即不能转载该文章。最后判断 flag 为 1 时才会显示 `转载` 链接，即才可以转载这篇文章。

最后，我们需要添加一个 **原文链接** 来指向被转载的文章。  
打开 index.ejs 、user.ejs 、article.ejs，在第一个 `<p class="info">` 里最后添加如下代码：

```
<% if (post.reprint_info.reprint_from) { %>
  <br><a href="/u/<%= post.reprint_info.reprint_from.name %>/<%= post.reprint_info.reprint_from.day %>/<%= post.reprint_info.reprint_from.title %>">原文链接</a>
<% } %>
```

现在我们就给博客添加了转载功能。

接下来我们添加转载统计。  
添加转载统计就简单多了，我们只需使用 `reprint_info.reprint_to.length` 即可。

打开 index.ejs 、user.ejs 、article.ejs ，将：

```
<p class="info">阅读：<%= post.pv %> | 评论：<%= post.comments.length %></p>
```

修改为：

```
<p class="info">
  阅读：<%= post.pv %> | 
  评论：<%= post.comments.length %> | 
  转载：
  <% if (post.reprint_info.reprint_to) { %>
    <%= post.reprint_info.reprint_to.length %>
  <% } else { %>
    <%= 0 %>
  <% } %>
</p>
```

现在我们就给博客添加了转载统计的功能。但工作还没有完成，假如我们要删除一篇转载来的文章时，还要将被转载的原文章所在文档的 `reprint_to` 删除遗留的转载信息。

打开 post.js ，将 `Post.remove` 修改为：

```
//删除一篇文章
Post.remove = function(name, day, title, callback) {
  //打开数据库
  mongodb.open(function (err, db) {
    if (err) {
      return callback(err);
    }
    //读取 posts 集合
    db.collection('posts', function (err, collection) {
      if (err) {
        mongodb.close();
        return callback(err);
      }
      //查询要删除的文档
      collection.findOne({
        "name": name,
        "time.day": day,
        "title": title
      }, function (err, doc) {
        if (err) {
          mongodb.close();
          return callback(err);
        }
        //如果有 reprint_from，即该文章是转载来的，先保存下来 reprint_from
        var reprint_from = "";
        if (doc.reprint_info.reprint_from) {
          reprint_from = doc.reprint_info.reprint_from;
        }
        if (reprint_from != "") {
          //更新原文章所在文档的 reprint_to
          collection.update({
            "name": reprint_from.name,
            "time.day": reprint_from.day,
            "title": reprint_from.title
          }, {
            $pull: {
              "reprint_info.reprint_to": {
                "name": name,
                "day": day,
                "title": title
            }}
          }, function (err) {
            if (err) {
              mongodb.close();
              return callback(err);
            }
          });
        }

        //删除转载来的文章所在的文档
        collection.remove({
          "name": name,
          "time.day": day,
          "title": title
        }, {
          w: 1
        }, function (err) {
          mongodb.close();
          if (err) {
            return callback(err);
          }
          callback(null);
        });
      });
    });
  });
};
```

**注意**：我们使用了 `$pull` 来删除数组中的特定项，关于 `$pull` 的详细使用请查阅 《MongoDB 权威指南》。

至此，我们给博客添加了转载功能和转载统计。

## 二十、添加日志功能

现在我们来给博客增加日志，实现访问日志（access.log）和错误日志（error.log）功能。

前面我们介绍过，使用 Express 自带的 logger 中间件实现了终端日志的输出：

```
app.use(logger('dev'));
```

那我们想把日志保存为日志文件该怎么办呢？很简单，我们只需在以上代码的下一行添加：

```
app.use(logger({stream: accessLog}));
```

并在 var app = express(); 之前添加如下代码即可：

```
var fs = require('fs');
var accessLog = fs.createWriteStream('access.log', {flags: 'a'});
var errorLog = fs.createWriteStream('error.log', {flags: 'a'});
```

这样，我们每一次访问的请求信息，不仅显示在了命令行中，也都保存在了工程根目录下的 access.log 文件里。但 Express 并没有提供记录错误日志的功能，所以我们需自己写一个简单的中间件，在 app.use(express.static(path.join(__dirname, 'public'))); 下一行添加如下代码 ：

```
app.use(function (err, req, res, next) {
  var meta = '[' + new Date() + '] ' + req.url + '\n';
  errorLog.write(meta + err.stack + '\n');
  next();
});
```

这样，当有错误发生时，就将错误信息保存到了根目录下的 error.log 文件夹里。

至此，我们就给博客添加了日志的功能。