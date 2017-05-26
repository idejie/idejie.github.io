---
title: 使用Github + Hexo 搭建个人博客
date: 2016-09-13 20:35:01
tags: Hexo
category: 教程
---

### 〇.准备工作

> 环境：OS X 10.11（Linux系统应该也没问题，Windows如果使用Ubuntu Bash也可以尝试）

#### 1.安装Node.js

- 打开Terminal试一下`node --version`和`npm --version`如果有版本号，那么你可以跳过此步骤了。

- 下载Node.js下载安装对应版本就好[官网下载](https://nodejs.org/en/download/)

- Mac安装一直`Next`就好

- 如果是Ubuntu的话可以尝试

  ```shell
  curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -

  sudo apt-get install nodejs
  ```


#### 2.安装Hexo

- 打开Terminal试一下`hexo --version`如果有版本号，那么你可以跳过此步骤了。
- Linux和Mac一样Terminal键入`sudo npm install -g hexo`

#### 3.安装git

- 打开Terminal试一下`git --version`如果有版本号，那么你可以跳过此步骤了。
- Ubuntu使用`sudo apt-get install git`

#### 4.注册Github并使用

- 注册地址：[官网](www.github.com)
- 创建一个新的`Repository`，名字必须使用`username.github.io`，当然`username`就是你的账号名称了[如何在github上创建repository](http://jingyan.baidu.com/article/f7ff0bfc7181492e27bb1360.html)
- 创建时不要点选`Initialize this repository with a README`

### 一.开始创建

**可以移步[官网](https://hexo.io/zh-cn/docs/setup.html)，它讲的比较详细**

#### 1.初始化

```shell
$ hexo init blog   
$ cd blog
$ npm install
$ hexo g
$ hexo s
```

在浏览器打开[http://localhost:4000/](http://localhost:4000/)你就看到它的一个静态网站啦

#### 2.配置

新建完成后，指定文件夹的目录如下：

```
.
├── _config.yml
├── package.json
├── scaffolds
├── source
|   └── _posts
└── themes
```

`_config.yml`网站的 [配置](https://hexo.io/zh-cn/docs/zh-cn/docs/configuration.html) 信息，您可以在此配置大部分的参数。

大家可以参考我的配置

```yaml
# Hexo Configuration
## Docs: https://hexo.io/docs/configuration.html
## Source: https://github.com/hexojs/hexo/

# Site
title: 杨德杰
subtitle: idejie.com
description: 杨德杰的个人博客
author: Mr.Y
language: zh-CN
timezone:

# URL
## If your site is put in a subdirectory, set url as 'http://yoursite.com/child' and root as '/child/'
url: http://blog.idejie.com
root: /
permalink: :year/:month/:day/:title/
permalink_defaults:

# Directory
source_dir: source
public_dir: public
tag_dir: tags
archive_dir: archives
category_dir: categories
code_dir: downloads/code
i18n_dir: :lang
skip_render:

# Writing
new_post_name: :title.md # File name of new posts
default_layout: post
titlecase: false # Transform title into titlecase
external_link: true # Open external links in new tab
filename_case: 0
render_drafts: false
post_asset_folder: false
relative_link: false
future: true
highlight:
  enable: false
  line_number: true
  auto_detect: false
  tab_replace:

# Category & Tag
default_category: 
category_map:
tag_map:

# Date / Time format
## Hexo uses Moment.js to parse and display date
## You can customize the date format as defined in
## http://momentjs.com/docs/#/displaying/format/
date_format: YYYY-MM-DD
time_format: HH:mm:ss

# Pagination
## Set per_page to 0 to disable pagination
per_page: 8
pagination_dir: page

# Extensions
## Plugins: https://hexo.io/plugins/
## Themes: https://hexo.io/themes/
theme: fexo #这里替换成你的主题名称

# Deployment
## Docs: https://hexo.io/docs/deployment.html
deploy:
  type: git
  repo: https://github.com/YangDejie/yangdejie.github.io.git #这里替换成你创建repository的地址
  branch: master
```

#### 3.部署到github

```shell
$ npm install hexo-deployer-git --save
$ hexo clean 
$ hexo g 
$ hexo d
```

打开你的repository地址`username.github.io`

### 二.正式使用

#### 1.一些常用命令

```shell
hexo new "postName" #新建文章 ,等同于hexo n "postName"
hexo new page "pageName" #新建页面 ，等同于hexo n page "pageName"
hexo generate #生成静态页面至public目录，等同于hexo g
hexo server #开启预览访问端口（默认端口4000，'ctrl + c'关闭server）等同于hexo s
hexo deploy #将.deploy目录部署到GitHub，等同于hexo d
hexo clean #清空本地cache
```

#### 2.Markdown语法

Markdown语法[参考链接](http://sspai.com/25137)

#### 3.每次部署到github都需要在你的目录下

```shell
$ hexo clean 
$ hexo g 
$ hexo d
```

### 三.个性配置

- 以后更新

#### 1.主题

[官网推荐主题](https://hexo.io/themes/)

#### 2.插件

[官方插件](https://hexo.io/plugins/)

