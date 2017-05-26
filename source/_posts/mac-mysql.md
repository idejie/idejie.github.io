---
title: Mac下快速安装MySQL
date: 2016-11-16 20:40:41
tags: MySQL
category: 教程
---

在 Mac 下用 Homebrew 安装 MySQL, 网上的教程倒是很多，不过大多数都很默契地雷同。如果稍有点定制要求，就无从下手了。

我先也不免俗，从基本的开始：

# 一、首先安装 Homebrew

```
$ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
$ brew install git
$ brew update

```

# 二、安装 MySQL

用下面的命令就可以自动安装了：

```
$ brew install mysql

```

如果想让 MySQL 开机自动启动，可以如下操作：

```
$ mkdir -p ~/Library/LaunchAgents
$ ln -sfv /usr/local/opt/mysql/*.plist ~/Library/LaunchAgents
$ find /usr/local/Cellar/mysql/ -name "homebrew.mxcl.mysql.plist" -exec cp {} ~/Library/LaunchAgents/ \;
$ launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist

```

设置 MySQL 用户以及数据存放地址

```
$ unset TMPDIR$ mysql_install_db --verbose --user=`whoami` --basedir="$(brew --prefix mysql)" --datadir=/usr/local/var/mysql --tmpdir=/tmp

```

好了，可以启动了

```
$ mysql.server start

```

另外的参数还有 `{start|stop|restart|reload|force-reload|status}`

大部分的介绍就在此结束了。

# 三、配置文件 

作为用惯了 Linux 的人， 一定会去 `/etc` 下找 `my.cnf`, 让你失望了，这个文件要自己建立。如果看一下帮助

```
$ mysqld --help --verbose

```

就会发现系统会按这个顺序去找 my.cnf

```
1. /etc/my.cnf
2. /etc/mysql/my.cnf
3. /usr/local/etc/my.cnf
4. ~/.my.cnf

```

一般网上大虾都会这么教小白建立 `my.cnf`, 其实这个默认的文件里面几乎没什么内容。

```
$ sudo cp $(brew --prefix mysql)/support-files/my-default.cnf /etc/my.cnf

```

所以，还是自己老老实实参考 linux 下的配置文件吧。

\##错误日志

错误日志默认会存在数据目录下，也就是上面所定义的 `/usr/local/var/mysql/`，如果 Mac 电脑名字是 MacBook，那日志的全路径就是 `/usr/local/var/mysql/MacBook.local.err`

\##让别的电脑访问数据库

取消下面两个文件中关于绑定 127.0.0.1 的语句
/etc/my.cnf

`bind-address = 127.0.0.1`

~/Library/LaunchAgents/homebrew.mxcl.mysql.plist

`--bind-address=127.0.0.1`

就我个人而言，不需要 MySQL 自启动，所以只要在 `/etc/my.cnf` 改一下就好了。