---
title: Hadoop学习（二）：运行WordCount
date: 2016-12-13 20:47:03
tags: Hadoop
category: 教程
---

# 1.创建本地文件

```bash
mdkir file
cd file
echo "hello world">file1.txt
echo "hello hadoop">file2.txt
```

# 2.创建输入文件夹

```bash
hadoop fs -mkdir /input
```

# 3.上传本地文件

```bash
hadoop fs -put ./file/file*.txt /input
```

# 4.运行WordCount

```bash
hadoop jar ./libexec/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar wordcount /input /output
```

# 5.查看结果

```bash
hadoop fs -cat /output/part-r-00000
```

```txt
hadoop	1
hello	2
world	1
```

