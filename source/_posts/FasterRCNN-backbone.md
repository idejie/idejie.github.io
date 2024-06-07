---
title: 探知「目标检测」
date: 2019-11-13 16:26:17
tags: FasterRCNN
category: 深度学习
---

# 1.目标检测

目标检测`Object Detection`解决的是图片中物体有哪些、在哪、是什么的问题，也就是在图片中找到关键物体，并且给出对应物体的位置`location`和标签`label`（如类别）。

通常包括大任务（图片），图像分类`Image Classification`和目标定位`Object Locazation`。

对于图像分是`图片`，输出的是`类别`，一般的评价方法是`准确率`.

![](https://blog.idejie.com/pics/20191113164303.png)

对于目标定位，输入的是`图片`,输出的是目标在图像上的`位置`，一般的评价方法是`IOU(intersection-over-union)`

![](https://blog.idejie.com/pics/20191113164454.png)

*注：* 
$$
IOU(A,B) = \frac{Size(A\cap B)}{Size(A\cup B)}
$$
![](https://blog.idejie.com/pics/20191114160124.png)

# 2.主要方法

## 2.1.R-CNN

论文：[CVPR2014: **Rich feature hierarchies for accurate object detection and semantic segmentation**](https://arxiv.org/abs/1311.2524)

![](https://blog.idejie.com/pics/20191113173548.png)

![](https://blog.idejie.com/pics/20191118100033.png)

模型包括两部分，`Region Proposals`和`Feature Extraction`，主要步骤如下

- 生成候选区域： 讲图片分成1~2K个较小的区域作为初始候选，采用`Selective Search`根据规则对现有区域进行合并，一般是讲颜色、纹理相近的进行合并，且合并后较均匀的(避免一个大区域陆续“吃掉”其他小区域 ，例：设有区域`a-b-c-d-e-f-g-h`。较好的合并方式是：`ab-cd-ef-gh -> abcd-efgh -> abcdefgh`。 不好的合并方法是：`ab-c-d-e-f-g-h ->abcd-e-f-g-h ->abcdef-gh -> abcdefgh`)，最终生成1K~2K个候选区域 。

- 提取特征： 对每个候选区域，使用CNN提取特征 

  ![](https://blog.idejie.com/pics/20191116102342.png)

- 分类： 特征送入每一类的SVM 分类器，判别是否属于该类  

- 位置精修： 使用回归器精细修正候选框位置，这里主要使用`IOU`对每一个类别去训练一个回归模型

  ![](https://blog.idejie.com/pics/20191116102308.png)

模型的主要贡献：

- 速度： 经典的目标检测算法使用滑动窗法依次判断所有可能的区域。本文则(采用Selective Search方法)预先提取一系列较可能是物体的候选区域，之后仅在这些候选区域上(采用CNN)提取特征，进行判断。
- 训练集： 经典的目标检测算法在区域中提取人工设定的特征。本文则采用深度网络进行特征提取。

代码参考：

- selective se[AlpacaDB/selectivesearch](https://github.com/AlpacaDB/selectivesearch.git)
- TF版RCNN:[Liu-Yicheng/R-CNN](https://github.com/Liu-Yicheng/R-CNN.git)

## 2.2 SPPNet

论文：[TAPMI2015: **Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition**](https://arxiv.org/pdf/1406.4729.pdf)

![](https://blog.idejie.com/pics/20191118100118.png)

**RCNN存在两个问题：**

- 速度瓶颈：重复为每个region proposal提取特征是极其费时的，Selective Search对于每幅图片产生2K左右个region proposal，也就是意味着一幅图片需要经过2K次的完整的CNN计算得到最终的结果。

- 性能瓶颈：对于所有的region proposal防缩到固定的尺寸会导致我们不期望看到的几何形变，而且由于速度瓶颈的存在，不可能采用多尺度或者是大量的数据增强去训练模型。

***但是为什么CNN需要固定的输入呢？***CNN网络可以分解为卷积网络部分以及全连接网络部分。我们知道卷积网络的参数主要是卷积核，完全能够适用任意大小的输入，并且能够产生任意大小的输出。但是全连接层部分不同，全连接层部分的参数是神经元对于所有输入的连接权重，也就是说输入尺寸不固定的话，全连接层参数的个数都不能固定。

![](https://blog.idejie.com/pics/20191116220550.png)

红色框是selective search 输出的可能包含物体的候选框（ROI）。一张图图片会有~2k个候选框，每一个都要单独输入CNN做卷积等操作很费时。SPP-net提出：**能否在feature map上提取ROI特征，这样就只需要在整幅图像上做一次卷积。**

![](https://blog.idejie.com/pics/20191116220708.png)

**1.如何在feature map上找到对应的ROI特征呢？**

![](https://blog.idejie.com/pics/20191117205400.png)

左上角的点$(x,y)$映射到 feature map上的$(x', y')$ ： 使得 $(x’,y')$ 在原始图上感受野（上图绿色框）的中心点 与$(x,y)$ 尽可能接近。

![](https://blog.idejie.com/pics/20191118095342.png)

**对应点之间的映射公式是啥？**

- 就是前面每层都填充padding/2 得到的简化公式 ： ![[公式]](https://www.zhihu.com/equation?tex=p_i+%3D+s_i+%5Ccdot+p_%7Bi%2B1%7D)

- 需要把上面公式进行级联得到 ![[公式]](https://www.zhihu.com/equation?tex=p_0+%3D+S+%5Ccdot+p_%7Bi%2B1%7D++++) 其中 ![[公式]](https://www.zhihu.com/equation?tex=+%28S+%3D+%5Cprod_%7B0%7D%5E%7Bi%7D+s_i%29)

- 对于feature map 上的 ![[公式]](https://www.zhihu.com/equation?tex=%28x%27%2Cy%27%29) 它在原始图的对应点为 ![[公式]](https://www.zhihu.com/equation?tex=%28x%2Cy%29+%3D+%28Sx%27%2C+Sy%27%29)

- 论文中的最后做法：把原始图片中的ROI映射为 feature map中的映射区域（上图橙色区域）其中 左上角取：![[公式]](https://www.zhihu.com/equation?tex=x%27+%3D++%5Clfloor+x%2FS+%5Crfloor+%2B1++%2C%5C%3B%0Ay%27+%3D++%5Clfloor+y%2FS+%5Crfloor+%2B1), ；右下角的点取： 界取y'的x值：![[公式]](https://www.zhihu.com/equation?tex=x%27+%3D++%5Clceil+x%2FS+%5Crceil+-+1++%2C%5C%3B%0Ay%27+%3D++%5Clceil+y%2FS+%5Crceil+-+1)。 下图可见 ![[公式]](https://www.zhihu.com/equation?tex=+%5Clfloor+x%2FS+%5Crfloor+%2B1+) , ![[公式]](https://www.zhihu.com/equation?tex=%5Clceil+x%2FS+%5Crceil+-+1+) 的作用效果分别是增加和减少。也就是 左上角要向右下偏移，右下角要想要向左上偏移。个人理解采取这样的策略是因为论文中的映射方法（左上右下映射）会导致feature map上的区域反映射回原始ROI时有多余的区域（下图左边红色框是比蓝色区域大的）

  ![](https://blog.idejie.com/pics/20191118095214.png)

**2.ROI输出的特征维度不符合fc的要求怎么办？**

- 这个问题涉及的流程主要有: 图像输入->卷积层1->池化1->...->卷积层n->池化n->全连接层。
- 引发问题的原因主要有：全连接层的输入维度是固定死的，导致池化n的输出必须与之匹配，继而导致图像输入的尺寸必须固定。

SPPNet在池化n 的地方做了一些手脚 （特殊池化手段：空间金字塔池化），使得 不同尺寸的图像也可以使 池化n 产生固定的 输出维度。

所谓空间金字塔池化就是沿着 金字塔的低端向顶端 一层一层做池化。

![](https://blog.idejie.com/pics/20191118094711.png)

假设原图输入是224x224，对于conv5出来后的输出是13x13x256的，可以理解成有256个这样的filter，每个filter对应一张13x13的reponse map。如果像上图那样将reponse map分成1x1(金字塔底座)，2x2(金字塔中间)，4x4（金字塔顶座）三张子图，分别做max pooling后，出来的特征就是(16+4+1)x256 维度。如果原图的输入不是224x224，出来的特征依然是(16+4+1)x256维度。这样就实现了不管图像尺寸如何 池化n 的输出永远是 （16+4+1）x256 维度。

将conv5的pool层改为SPP之后就不必把每一个都ROI抠出来送给CNN做繁琐的卷积了，整张图像做卷积一次提取所有特征再交给SPP即可。

## 2.3Fast-RCNN

论文:[ICCV2015:  **Fast R-CNN**][https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf]

事实上，RCNN还是不够快，Ross Girshick在2015年推出Fast R-CNN，构思精巧，流程更为紧凑，大幅提升了目标检测的速度。

![](https://blog.idejie.com/pics/20191116111648.png)

R-CNN和SPP-net在训练时pipeline是隔离的：提取proposal，CNN提取特征，SVM分类，bbox regression。

- 实现大部分end-to-end训练(提proposal阶段除外)： 所有的特征都暂存在显存中，就不需要额外的磁盘空。
- joint training （SVM分类，bbox回归 联合起来在CNN阶段训练）把最后一层的Softmax换成两个，一个是对区域的分类Softmax（包括背景），另一个是对bounding box的微调。这个网络有两个输入，一个是整张图片，另一个是候选proposals算法产生的可能proposals的坐标。（对于SVM和Softmax，论文在SVM和Softmax的对比实验中说明，SVM的优势并不明显，故直接用Softmax将整个网络整合训练更好。对于联合训练： 同时利用了分类的监督信息和回归的监督信息，使得网络训练的更加鲁棒，效果更好。这两种信息是可以有效联合的。）
- 提出了一个RoI层，算是SPP的变种，SPP是pooling成多个固定尺度，RoI只pooling到单个固定的尺度 （论文通过实验得到的结论是多尺度学习能提高一点点mAP，不过计算量成倍的增加，故单尺度训练的效果更好。）

![](https://blog.idejie.com/pics/20191118100521.png)

**ROI Pooling**

与SPP的目的相同：如何把不同尺寸的ROI映射为固定大小的特征。ROI就是特殊的SPP，只不过它没有考虑多个空间尺度，只用单个尺度（下图只是大致示意图）。

![](https://blog.idejie.com/pics/20191118101028.png)

ROI Pooling的具体实现可以看做是针对ROI区域的普通整个图像feature map的Pooling，只不过因为不是固定尺寸的输入，因此每次的pooling网格大小得手动计算，比如某个ROI区域坐标为![[公式]](https://www.zhihu.com/equation?tex=+%28x1%2Cy1%2Cx2%2Cy2%29)，那么输入size为 ![[公式]](https://www.zhihu.com/equation?tex=+%28y_2+-+y_1%29+%5Ccdot+%28x_2+-++x_1%29)，如果pooling的输出size为 ![[公式]](https://www.zhihu.com/equation?tex=pooledheight+%5Ccdot+pooledwidth)，那么每个网格的size为 ![[公式]](https://www.zhihu.com/equation?tex=%28+%28y_2+-+y_1%29+%2Fpooled+height%29+%5Ccdot++%28x_2-x_1%29%2Fpooled+width%29+)。

**Bounding-box Regression**

有了ROI Pooling层其实就可以完成最简单粗暴的深度对象检测了，也就是先用selective search等proposal提取算法得到一批box坐标，然后输入网络对每个box包含一个对象进行预测，此时，神经网络依然仅仅是一个图片分类的工具而已，只不过不是整图分类，而是ROI区域的分类，显然大家不会就此满足，那么，能不能把输入的box坐标也放到深度神经网络里然后进行一些优化呢？rbg大神于是又说了"yes"。在Fast-RCNN中，有两个输出层：第一个是针对每个ROI区域的分类概率预测![[公式]](https://www.zhihu.com/equation?tex=+p%3D%28p0%2Cp1%2C%5Ccdots+%2CpK%29)，第二个则是针对每个ROI区域坐标的偏移优化![[公式]](https://www.zhihu.com/equation?tex=t%5Ek%3D%28t%5Ek_x%2Ct%5Ek_y%2Ct%5Ek_w%2Ct%5Ek_h%29) ，![[公式]](https://www.zhihu.com/equation?tex=+0%5Cleq+k+%5Cleq+K)是多类检测的类别序号。这里我们着重介绍第二部分，即坐标偏移优化。



假设对于类别![[公式]](https://www.zhihu.com/equation?tex=+k%5E%2A)，在图片中标注了一个groundtruth坐标：![[公式]](https://www.zhihu.com/equation?tex=+t%5E%2A%3D%28t%5E%2A_x%2Ct%5E%2A_y%2Ct%5E%2A_w%2Ct%5E%2A_h%29+)，而预测值为 ![[公式]](https://www.zhihu.com/equation?tex=t%3D%28t_x%2Ct_y%2Ct_w%2Ct_h%29)，二者理论上越接近越好，这里定义损失函数：

![](https://blog.idejie.com/pics/20191118101535.png)

这里，![[公式]](https://www.zhihu.com/equation?tex=+smooth_%7BL_1%7D%28x%29+) 中的x即为![[公式]](https://www.zhihu.com/equation?tex=+t_i-t%5E%2A_i) 即对应坐标的差距。该函数在 (−1,1) 之间为二次函数，而其他区域为线性函数，作者表示这种形式可以增强模型对异常数据的鲁棒性，整个函数在matplotlib中画出来是这样的

![](https://blog.idejie.com/pics/20191118101550.png)



## 2.4Faster-RCNN

论文：[NIPS2015 **Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks**](https://arxiv.org/abs/1506.01497)

faster RCNN可以大致看做“区域生成网络+fast RCNN“的系统，用区域生成网络代替fast RCNN中的Selective Search方法)

![](https://blog.idejie.com/pics/20191118102335.png)

**区域生成网络 （ Region Proposal Networks ）**





# 参考

- [晓雷机器学习笔记 - 知乎专栏]( https://zhuanlan.zhihu.com/xiaoleimlnote)
- [大话目标检测经典模型（RCNN、Fast RCNN、Faster RCNN）](https://my.oschina.net/u/876354/blog/1787921)
- [深度学习调参实验室 - 知乎专栏](https://zhuanlan.zhihu.com/qianxiaosi)