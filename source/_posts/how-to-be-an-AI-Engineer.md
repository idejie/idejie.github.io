---
title: 记一次知乎Live：如何成为AI工程师
date: 2017-04-07 18:45:30
tags: AI
category: 知乎Live
---

```python
#其实这个Live是很久之前报名的，但是今天才学习完
#总结一下，与诸君共享
```

> 主讲：腾讯技术总监 腾讯TEG专家工程师 朱建平（felix）

*注：*以下仅为个人学习交流总结

# 1.关于人工智能的几个常见错误认知

- 人工智能是AI工程师的事情，跟我没有什么庴
- 人工智能太厉害了，未来会代替人类

# 2.传统开发转行AI工程师的障碍

- 概念晕（急于求成）：LR, SVM, 决策树，DNN,CNN, AlexNet, GoogleNet, Caffee,TensorFlow, 智能驾驶，AlphaGo, 个性化推荐, 智能语音，GPU, FPGA....
- 数学公式繁杂（望而却步）：![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer0.jpg)
  - 建议：不要期望内部原理，许多数学公式目前没办法解释清楚；化整为零，有的放矢
- 自底向上的学习方法(误)
  - 不要从理论开始
  - 不要去学习机器学习所有的东西
  - 不要在算法里浪费光阴
  - 结合场景，先动动手实践，再逐步细化

# 3.AI工程师的知识结构

## 3.1机器学习的相关概念

![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer1.jpg)

- 人工智能/机器学习/深度学习
  - 人工智能是最大的范畴，只要你用计算机做了一点智能的事情都可以称为做了人工智能的工作。真正的人工智能应该是让机器拥有人的智能，让机器跟人一样能看、能听、能说，能用自然语言跟人进行交流。这个涉及到计算机视觉、语音识别、自然语言处理、人机交互、语音合成等等，是常规的我们研究讨论的人工智能的主要发力点，在互联网公司有着广阔应用场景的。
  - 机器学习是人工智能目前最火的一个领域、深度学习是机器学习最火的一个子领域

- 模型用途：分类、回归、聚类


  主要区分在于output的描述是什么性质:分类是指output是整数（即多个类别标签）；回归是指output是一个实数，例如预测股票的走势，input是时间，output就是股票价格；聚类一般都是应用于非监督的状态下，对output完全不知道，只能对input数据本身进行统计分析，比如用户画像，通过数据之间的关系如关联程度将数据分成好几簇。

- 训练过程: 监督、半监督和非监督

- 学习模型：LR/SVM/决策树（传统的分类和聚类）DNN(深度神经网络）  CNN（卷积神经网络）

  - 常用CNN模型：AlexNet, GoogleNet, ResNet

- 开源框架&平台：Caffee, TensorFlow（Google）,Torch (Facebook)

- 为什么有这么多深度学习框架，参考《Deep Learning System Design Concepts》[http://mxnet.io/architecture/index.html#deep-learning-system-design-concepts](http://mxnet.io/architecture/index.html#deep-learning-system-design-concepts)
- 硬件 GPU，FPGA

## 3.2机器学习解决问题的基本步骤

- 搞清楚目标问题

  目前还没有一个通用的框架来解决所有的问题，不同的问题有不同的适用模型，图片识别用卷积神经网络，推荐里面用DNN、LR

- 收集数据和特征过程

  机器学习是一个面向数据的编程，数据是基础

  样本数据拆成2部分，70%用作训练集，30%做测试集

  同一个机器学习算法，好的数据会让模型产生的结果更好，差的数据会让模型毫无用处，但好/差没有界限

  一般从结果来看，越符合我们期望结果的数据及时一个好的数据

  一个比较可行的办法，是想象人在解决问题时会用哪些数据和特征，这就是特征工程

  简单的说就是一个改错的过程

- 训练模型和评估模型效果

  把样本读进来，进行前项计算，得到的目标值跟样本的目标值对比误差，做一下反向的计算，修改一些参数

- 线上应用和持续优化

![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer2.jpg)

## 3.3DNN

- DNN深度神经网络

  ![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer3.jpg)

  

  

  ![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer14.jpg)
  ![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer15.jpg)

## 3.4CNN

  ![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer5.jpg)

  ![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer6.jpg)

## 3.5入门成为AI工程师的可行路径

AI算法研究

AI工程实现

AI应用

# 4.AI实践案例分享

![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer7.jpg)

![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer8.jpg)

![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer9.jpg)

# 5.腾讯云的GPU云、FPGA云

![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer10.jpg)

![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer11.jpg)

![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer12.jpg)

![](https://blog.idejie.com/pics/how-to-be-an-AI-Engineer13.jpg)