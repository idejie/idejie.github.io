---
title: Nosql学习：安装HBase
date: 2016-11-11 20:38:08
tags: Nosql
category: 教程
---

## 1.环境要求

- java 1.6+
- brew in Terminal
  - 打开Terminal输入`ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

## 2.开始安装

- 打开Terminal输入`$ brew install hbase`

- 等待结果

  ```
  To have launchd start hbase now and restart at login:
    brew services start hbase
  Or, if you don't want/need a background service you can just run:
    /usr/local/opt/hbase/bin/start-hbase.sh

  ```

  ​

## 3.启动HBase

```
$ cd /usr/local/Cellar/hbase/1.2.2
$ ./bin/start-hbase.sh

```

出现结果：

```
starting master, logging to /usr/local/var/log/hbase/hbase-Yang-master-MacdeMacBook-Pro.local.out
Java HotSpot(TM) 64-Bit Server VM warning: ignoring option PermSize=128m; support was removed in 8.0
Java HotSpot(TM) 64-Bit Server VM warning: ignoring option MaxPermSize=128m; support was removed in 8.0

```

## 4.验证运行

```
$ jps

3269 Jps
3215 HMaster # 有HMaster则说明安装成功

```

## 5.启动HBase

```
$ ./bin/hbase.shell

```

结果：

```
2016-11-11 17:13:25,287 WARN  [main] util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
HBase Shell; enter 'help<RETURN>' for list of supported commands.
Type "exit<RETURN>" to leave the HBase Shell
Version 1.2.2, r3f671c1ead70d249ea4598f1bbcc5151322b3a13, Fri Jul  1 08:28:55 CDT 2016

hbase(main):001:0> list
TABLE                                                                                                                                                                                                                          
0 row(s) in 0.2960 seconds

=> []
hbase(main):002:0>
```