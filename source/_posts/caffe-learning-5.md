---
title: 21天实战Caffe：第五天
date: 2017-03-11 13:59:28
tags: Caffe
category: 深度学习
---

# 第五天：Caffe依赖包解析

## 1.ProtoBuffer

`protoBuffer` 是Google开发的一种可以实现内存和非易失存储介质交换的协议接口。

caffe大量使用它作为权值和模型参数的载体。

## 2.Boost

Caffe主要是使用它的只能指针，避免共享指针时造成内存泄漏或者多次释放

## 3.GFlags

起到命令行参数解析的作用，与`protoBuffer`相似，但是输入源不同

## 4.GLog

Googlr开发的用于记录应用程序日志的使用库，提供基于C++标准输入输出流形式的接口

## 5.BLAS

卷积神经网络中用到数学计算。BLAS。OpenBLAS在Caffe中主要负责CPU端的数值计算

## 6.HDF5

NCSA 为了满足各种科研领域需求而研制的一种高效存储和分发科学数据的新型数据形式。他可以存储不同类型的图像和数码数据的文件，并且可以在不同类型的机器上传输，同时还有统一的文件格式的函数库。

## 7.OpenCV

开源计算机视觉库。

## 8.LMDB和LevelDB

- LMDB—— 闪电般的内存映射型数据管理器，在 Caffe 的作用主要是提供数据管理，将形形色色的原始数据转换成统一的 Key-Value存储。
- LevelDB 是 Caffe 早期版本使用的数据存储方式，由 Google 开发。他是一种持续的键值对存储方式

## 9.Snappy

Snappy 是一个用来压缩和解压缩的 C++库