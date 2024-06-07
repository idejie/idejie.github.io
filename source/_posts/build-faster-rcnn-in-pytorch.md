---
title: 使用Pytorch构建Faster-RCNN
date: 2019-11-21 11:21:15
tags: Pytorch
category: 深度学习
---

# Introduction

**Faster RCNN**是「目标检测 」领域提出较早、使用广泛，且比较有效的框架之一。它是建立在 **Fast RCNN**的基础之上进行的改进，而 **Fast RCNN**又是建立在 **RCNN** 和 **SPPNet**之上，之前有介绍过这两个网络，在此不再赘述。**Faster RCNN**的改进之一就是不再使用传统的像 **Selective Search**这样的计算机视觉基础算法，采用了深度学习框架，性能较好。其次就是和 **Fast RCNN**的比较，如下：

![](https://blog.idejie.com/pics/20191121112908.png)

我们可以看到，较 **Fast RCNN**， **Faster RCNN**使用了一个 **RPN**(Region Proposal Network)取代了 **Selective Search**，**Selective Search**是使用**SIFT**和**HOG**生成目标候选区域的算法，它需要在CPU上处理图片，大约每张需要2s，这个花费是很大的。这使得**Fast RCN**在每张图片上生成预测需要2.3s，而**Faster RCNN**即使是在使用**VGGNet**等深度图像分类模型时也可以每秒处理5张图片。

接下来，我们大约需要四步完成**Faster RCNN**的构建。

1. Region Proposal Network（RPN）
2. RPN Loss Functions
3. Region of Intrest Pooling(ROI)
4. ROI Loss Functions

RPN网络还引入了一个概念叫做**Anchor Boxes**, 这个概念目前已经成为目标检测流程的一个黄金标准。

通常数据流在**Faster RCNN**中训练时通常要经过如下步骤：

1. 从图片中提取特征
2. 创建锚点目标
3. 从RPN网络中获得位置和目标的预测分数
4. 选择top n的位置和目标分数，这部分又被称作他们的候选网络层
5. 通过**Faster RCNN**选出top N的位置，并对步骤4中的每个位置都生成位置和类别的预测
6. 对4中的位置生成候选目标
7. 使用2-3计算rpn的分类loss和回归loss
8. 使用5，6计算roi的分类loss和回归loss

我们使用vgg16作为特征提取网络。

# 特征提取

规定输入图片的大小为`800*800`，下采样为`16`，box的坐标为左上，右下`(y1,x1,y2,x2)`

```python
import torch
bbox = torch.FloatTensor([[20, 30, 400, 500], [300, 400, 500, 600]]) # [y1, x1, y2, x2] format
labels = torch.LongTensor([6, 8]) # 0 represents background
sub_sample = 16
```

![](https://blog.idejie.com/pics/20191122092420.png)

**vgg16**被用作特征提取，同时也是**RPN**网络和**Faster RCNN**的骨干网络，但是我们需要进行一下改动，因为我们采样比例为`16`，所以只取到倒数第二层。

```python
vgg = torchvision.models.vgg16(pretrained=True)
self.rcnn_base = nn.Sequential(*list(vgg.features)[:-1]) 
out_map = faster_rcnn_fe_extractor(image)
print(out_map.size())
```

现在我们可以输出特征送入**RPN**网络了，它能找到一些比较有趣的区域，返回的就是这些区域，判断是否为物体的 loss,以及坐标定位的loss。 

# RPN网络

在了解RPN网络之前，要了解一个概念叫`Anchor Box`,他是不同大小的一个box，能帮我们检测一些物体，比如车、人，一般设置成3个scale（长）和3个ratio（长宽比），共9个大小的`anchor box`,在`feature map`上的每个点我们都会生成这样9个box。

![](https://blog.idejie.com/pics/20191122100551.png)

