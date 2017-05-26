---
title: 21天实战Caffe：第三天
date: 2017-03-09 09:06:30
tags: Caffe
category: 深度学习

---

# 第三天：深度学习工具汇总

## 1.Caffe

- 实现了前馈卷积神经网络架构
- 速度快，因为用了MKL，openBLAS、cuBLAS，支持GPU加速
- 特别适合做特征提取，实际上适合做二维图像数据的特征提取
- caffe完全开源

## 2.Torch & Overfeat

- 支持嵌入式设备：Android、iOS、FPGA
- 内置8个包：torch、lab&plot、qt、nn、image、optim、unsup、third-party
- overfea是在imageNet数据集中使用Torch7训练的特征提取器

## 3.MxNet

- N维数组接口
- 符合接口

## 4.TensorFlow

- 大规模机器学习框架、移植性好、支持多种深度学习模型

## 5.Theano

基于Python的一款

## 6.CNTK

微软旗下的，单机4GPU性能强