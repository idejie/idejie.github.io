---
title: 21天实战Caffe：第四天
date: 2017-03-10 19:06:30
tags: Caffe
category: 深度学习
---

# 第四天：准备Caffe环境

## 1.Mac

- 安装`homebrew`

- 安装`caffe`

  ![](https://blog.idejie.com/pics/caffe-learning-40.jpg)

- 下载Caffe源码

  ![](https://blog.idejie.com/pics/caffe-learning-41.jpg)

- 修改config

  `#CPU_ONLY :=1`前面的`#`去掉

  *注：*

  ​	主要是因为我的机器不是N卡    我是黑苹果TnT           A卡

  ​	其实还是关了吧，caffe就是入门，用不到GPU加速

- 编译

  `make -j`

## 2.Ubuntu

> 由于本人用的是黑苹果，并没有下载Xcode这种与我无关 `“TnT”` 的App
>
> 故选择Ubuntu了

- apt-get

  ```shell
  $ sudo apt-get git
  $ sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
  $ sudo apt-get install -no-install-recommends libboost-all-dev
  $ sudo apt-get install libatlas-base-dev
  $ sudo apt-get install python-dev
  $ sudo apt-get install libflags-dev libgoogle-glog-dev liblmdb-dev
  ```

  ​

- 下载源码、修改config、编译同上

## 3.CentOS、Windows等

请移步搜索引擎 今天太累了，周五想休息休息，不想写了QwQ