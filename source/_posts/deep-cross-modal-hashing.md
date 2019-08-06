---
title: 深度跨模态哈希
date: 2019-08-02 11:03:43
tags: CMH
category: 跨模态
---

> 原文：[Deep Cross-Modal Hashing](https://arxiv.org/abs/1602.02255)

## 摘要

由于跨模态哈希（Cross-Modal Hashing，CMH）低存储成本和快速的查询速度，它已被广泛用于多媒体检索应用中的相似性搜索。 但是，大多数现有的CMH方法都是基于手工制作的特征，这些特征可能与哈希码学习过程不能最佳兼容。 因此，使用手工提取的特征的现有CMH方法可能无法实现令人满意的性能。 在本文中，我们通过将特征学习和哈希码学习集成到同一框架中，提出了一种新的CMH方法，称为深度跨模态哈希（Deep Cross-Modal Hashing,DCMH）。 DCMH是一个端到端的学习框架，具有深度神经网络，每个模态对应一个神经网络从头开始进行特征学习。 在具有图像-文本模态的三个真实数据集上的实验表明，DCMH可以胜过其他baseline，实现了跨模态检索应用中的最佳性能。

## 1.Introduction

近似最近邻（Approximate nearest neighbor ,ANN）搜索在机器学习和信息检索等相关应用中起着重要作用。 由于哈希的低存储成本和快速的检索速度，它最近引起了人工神经网络研究界的广泛关注。 哈希的目标是将来自原始空间的数据点映射到二进制代码的汉明（Hamming）空间，其中原始空间中的相似性保留在汉明空间中。 通过使用二进制哈希码来表示原始数据，可以显着降低存储成本。 此外，我们可以通过使用哈希码构建索引，从而实现搜索的常数级或亚线性级的时间复杂度。 因此，哈希在大规模数据集近似最近邻搜索中越来越受到欢迎。

在许多应用中，数据可以具有多种模态。 例如，除了图像内容之外，还存在文本信息，例如Flickr和许多其他社交网站中的图像的标签。 这种数据总是被称为多模态数据。 随着多模态数据在实际应用中的快速增长，尤其是多媒体应用，多模态哈希（Multi-Modal Hashing, MMH）最近被广泛用于多模态数据集的近似最近邻检索。

现有的MMH方法可分为两大类：多源哈希（Multi-Source Hashing，MSH）和跨模态哈希（Cross-Modal Hashing, CMH)。 MSH的目标是通过利用来自多种模态的所有信息来学习哈希码。因此，MSH要求所有数据点（包括查询数据点和数据库中的数据点）都应保留所有模态。在实际中，MSH的应用是有限的，因为在许多情况下难以获得所有数据点的所有模态。相反，CMH的应用场景比MSH的应用场景更灵活。在CMH中，查询点的模态与数据库中的点的模态不同。此外通常查询数据点只有一种模态，数据库中的数据点可以有一个或多个模态。例如，我们可以使用文本查询来检索数据库中的图像，我们还可以使用图像查询来检索数据库中的文本。由于CMH的广泛应用，CMH比MSH更受关注。

最近提出了许多CMH方法。 现有的代表性方法包括跨模态相似度敏感哈希（cross modality similarity sensitive hashing，CMSSH,通过最小化不同模态的相似样本之间的汉明距离, 最大化不同模态的不相似样本间的汉明距离, 学习哈希函数)，跨视图哈希（cross
view hashing, CVH, 把谱哈希扩展到
跨模态检索, 通过最小化加权距离, 保持相似样本
(模态内和模态间) 的相似性），多模态潜在二进制嵌入（Multi-modal latent binary embedding, MLBE, 提出一个概率生成模型, 通过保持多模态样本的模
态内和模态间的相似度来学习哈希函数），联合正则化的哈希（co-regularized hashing，CRH）， 语义相关最大化（semantic correlation maximization,SCM），协同矩阵分解哈希（collective matrix factorization
hashing,CMFH），语义主题多模态哈希（semantic topic
multi-modal hashing, STMH）和语义保留哈希（semantics preserving hashing, SePH）。 几乎所有这些现有的CMH方法都基于手工制作的功能。 这些手工制作的基于特征的方法的一个缺点是特征提取过程独立于哈希码的学习过程，这意味着手工制作的特征可能与哈希码学习过程不是最佳兼容的。 因此，这些具有手工制作特征的现有CMH方法在实际应用中可能无法获得令人满意的性能。

最近，使用神经网络的深度学习被广泛用于从头开始进行的特征学习，并且具有很好的性能。 还有一些采用深度学习进行单模态哈希的方法。 这些方法表明端到端深度学习架构更适合于哈希学习。 对于CMH设置，还出现了一种方法，称为深度视觉语义哈希（deep visual-semantic hashing, DVSH），一个用于特征学习的深度神经网络。 但是，DVSH只能用于特殊的CMH情况，也就是其中一种模态必须是时间动态。

在本文中，我们提出了一种新的CMH方法，称为深度跨模态哈希（DCMH），用于跨模态的检索应用。 DCMH的主要贡献概述如下：

- DCMH是一个端到端的学习框架，具有深度神经网络，每个模态一个网络，用于从头开始进行特征学习。
- 哈希码学习问题本质上是一个离散的学习问题，很难学习。 因此，大多数现有的CMH方法通过将原始的离散学习问题松弛为连续学习问题来解决这个问题。 这种放松过程可能会降低学习的哈希码的准确性。 与这些基于松弛的方法不同，DCMH直接学习离散哈希码而不放松。
- 使用图像-文本真实数据集对模型进行的实验表明，DCMH可以胜过其他baseline，以实现跨模态检索应用程序中最先进的性能。

## 2.Problem Definition

### 2.1 Notation

像$\bold w$这样的粗体字小写字母用于表示向量。 像$\bold W$这样的粗体大写字母用于表示矩阵，$\bold W$的第$row$行和第$column$列中的元素表示$\bold W_{i,j}$。 $\bold W$的第$row$行表示为$\bold W_{𝑖*}$， $\bold W$的第$column$行表示为$\bold W_{*𝑗}$。$\bold W^{𝑇}$是 $\bold W$的转置。我们用$\bold 1$来表示一个向量，其中所有元素都是1. $\operatorname{tr}(\cdot)$和$\|\cdot\|_{F}$分别表示矩阵的迹和矩阵的Frobenius范数。 $sign（⋅）$是一个元素符号函数，定义如下：
$$
\operatorname{sign}(x)=\left\{\begin{array}{rl}{1} & {x \geq 0} \\ {-1} & {x<0}\end{array}\right.
$$

### 2.2Cross-Modal Hashing

虽然本文提出的方法可以很容易地适用于具有两种以上模态的情况，但我们只关注这里有两种模态的情况。

假设我们有$𝑛$个训练实体（数据点），每个实体都有两种特征形式。 在不失一般性的情况下，我们在本文中使用图像-文本数据集进行说明，这意味着每个训练点都具有文本模态和图像模态。 我们使用$\mathbf{X}=\left\{\mathbf{x}_{i}\right\}_{i=1}^{n}$来表示图像模态，其中$\mathbf{x}_{i}$可以是图像$i$的手工制作的特征或原始像素。 此外，我们使用$\mathbf{Y}=\left\{\mathbf{y}_{i}\right\}_{i=1}^{n}$来表示文本模态，其中$\mathbf{y}_{i}$通常是与图像$i$相关的标签信息。 此外，我们还给出了跨模态相似度矩阵$\mathbf{S}$. $S_{i j}=1$表示图像$\mathbf{x}_{i}$和文本$\mathbf{y}_{j}$相似的，否则$S_{i j}=0$。 这里，相似性通常由诸如类标签的一些语义信息来定义。 例如，我们可以说如果图像共享相同的类标签，则图像$\mathbf{x}_{i}$和文本$\mathbf{y}_{j}$是相似的。 否则图像$\mathbf{x}_{i}$和文本$\mathbf{y}_{j}$来自不同的类，则它们是不相似的。

给定上述训练信息$\mathbf{X}, \mathbf{Y}$ 和 $\mathbf{S}$，跨模态哈希的目标是学习两种模态的两个散列函数：$h^{(x)}(\mathbf{x}) \in\{-1,+1\}^c$用于图像模态和$h^{(y)}(\mathbf{y}) \in\{-1,+1\}^{c}$为文本模态，其中$𝑐$是二进制代码的长度。 这两个散列函数应该在$\mathbf{S}$中保留跨模态的相似性。更具体地说，如果$S_{i j}=1$，则为在二进制代码之间的汉明距离
$\mathbf{b}_{i}^{(x)}=h^{(x)}\left(\mathbf{x}_{i}\right)$和$\mathbf{b}_{i}^{(y)}=h^{(y)}\left(\mathbf{y}_{i}\right)$应该很小。 否则，如果$S_{i j}=$，相应的汉明距离0应该很大。

我们假设获取到训练集中每个点的两种特征模态，尽管我们的方法也可以很容易地适应其他一些训练点只能获取到一种特征形态的设置。 请注意，我们只对训练点做出此假设。 在我们训练模型之后，我们可以使用学习的模型为一个模态或两个模态的查询和数据库点生成哈希码，特别是完全可以匹配跨模态检索应用程序的设置。

## 3.Deep Cross-Modal Hashing

在本节中，我们将介绍有关深度CMH（DCMH）方法的详细信息，包括模型公式和学习算法。

### 3.1 Model

整个DCMH模型如图1所示，它是一个端到端的学习框架，它通过无缝集成两个部分：特征学习部分和哈希码学习部分。 在学习过程中，每个部分都可以向其他部分提供反馈。

![](https://blog.idejie.com/pics/20190802165935.png)

#### 3.1.1 **Feature Learning Part**

特征学习部分包含两个深度神经网络，一个用于图像模态，另一个用于文本模态。
图像模态的深度神经网络是改编自卷积神经网络（CNN）。 这个CNN模型有八层, 前七层与CNN-F中的相同, 第八层是全连接层，其输出是学习到的图像特征。

![](https://blog.idejie.com/pics/20190802170119.png)

表1显示了用于图像模态的CN-N的详细配置。 更具体地，八层被分成五个卷积层和三个全连接层，它们分别在表1中表示为“conv1-conv5”和“full6-full8”。每个卷积层都可以从以下几方面描述：

- "f、 $𝑛𝑢𝑚×𝑠𝑖𝑧𝑒×𝑠𝑖𝑧𝑒$"表示卷积滤波器的数量及其感受野大小。
- “st”表示卷积步长stride。
- “pad”表示要添加（padding）到每个输入的像素数大小。
- “LRN”表示是否应用了局部响应归一化（Local Response Normalization,LRN）。
- “Pool”表示下采样参数。
- 全连接层中的数字，例如“4096”，表示该层中的节点数。 它也是该层输出的维数。

所有前七层都使用线性整流函数（Rectified Linear Unit，Re-LU）[16]作为激活函数。 对于第八层，我们选择恒等函数作为激活函数。

为了从文本中执行特征学习，我们首先将每个文本$\mathbf{y}_{j}$表示为词袋（BOW）表示模型的向量。 然后使用词袋向量作为具有两个完全连接层的深度神经网络（表示为“full1 -  full2”）的输入。 文本深度神经网络的详细配置如表2所示，其中配置显示了每层中的节点数。 第一层的激活函数是ReLU，第二层的激活功能是恒等函数。

![](https://blog.idejie.com/pics/20190802171741.png)

请注意，本文的主要目的是表明通过使用深度神经网络从头开始进行特征学习，可以设计一个用于跨模态哈希的端到端学习框架。 但是如何设计不同的神经网络并不是本文的重点。 其他深度神经网络也可用于为我们的DCMH模型执行特征学习，这将留待将来的研究。

#### 3.1.2 **Hash-Code Learning Part**

令$f\left(\mathbf{x}_{i} ; \theta_{x}\right) \in \mathbb{R}^{c}$表示对于点$i$学习的图像特征，其对应于用于图像模态的CNN的输出。 此外，让$g\left(\mathbf{y}_{j} ; \theta_{y}\right) \in \mathbb{R}^{c}$表示点$i$学习到的文本特征，它对应于文本模态的深度神经网络的输出。 这里，$\theta_{x}$是用于图像模态的CNN的网络参数，$\theta_{y}$是用于文本模态的深度神经网络的网络参数。

DCMH的目标函数定义如下：
$$
\begin{aligned} \min _{\mathbf{B}^{(x)}, \mathbf{B}^{(y)}, \theta_{x}, \theta_{y}} \mathcal{J} &=-\sum_{i, j=1}^{n}\left(S_{i j} \Theta_{i j}-\log \left(1+e^{\Theta_{i j}}\right)\right) \\ &+\gamma\left(\left\|\mathbf{B}^{(x)}-\mathbf{F}\right\|_{F}^{2}+\left\|\mathbf{B}^{(y)}-\mathbf{G}\right\|_{F}^{2}\right) \\ &+\eta\left(\|\mathbf{F} \mathbf{1}\|_{F}^{2}+\|\mathbf{G} \mathbf{1}\|_{F}^{2}\right) \\ \text { s.t. } \quad \mathbf{B}^{(x)} & \in\{-1,+1\}^{c \times n} \\ \mathbf{B}^{(y)} & \in\{-1,+1\}^{c \times n} \end{aligned}  \tag {1}
$$
其中 

$\mathbf{F}_{* i}=f\left(\mathbf{x}_{i} ; \theta_{x}\right)$且$\mathbf{F} \in \mathbb{R}^{c \times n}$ ，$\mathbf{G}_{* j}=g\left(\mathbf{y}_{j} ; \theta_{y}\right)$且$\mathbf{G} \in \mathbb{R}^{c \times n}$，

$\Theta_{i j}=\frac{1}{2} \mathbf{F}_{* i}^{T} \mathbf{G}_{* j}$。

$\mathbf{B}_{* i}^{(x)}$是图像 $\mathbf{x}_{i}$的二进制哈希码。$\mathbf{B}_{* j}^{(y)}$是文本$\mathbf{y}_{j}$的二进制哈希码

$\gamma$ and $\eta$ 是超参数。

等式（1）中$-\sum_{i, j=1}^{n}\left(S_{i j} \Theta_{i j}-\log \left(1+e^{\Theta_{i j}}\right)\right)$是跨模态相似性的负的log似然，似然函数定义如下：
$$
p\left(S_{i j} | \mathbf{F}_{* i}, \mathbf{G}_{* j}\right)=\left\{\begin{array}{ll}{\sigma\left(\Theta_{i j}\right)} & {S_{i j}=1} \\ {1-\sigma\left(\Theta_{i j}\right)} & {S_{i j}=0}\end{array}\right.
$$
其中$\Theta_{i j}=\frac{1}{2} \mathbf{F}_{* i}^{T} \mathbf{G}_{* j}$ ，$\sigma\left(\Theta_{i j}\right)=\frac{1}{1+e^{-\Theta_{i j}}}$

很容易最小化负对数似然，等价于最大化似然，可以使$\mathbf{F}_{* i}$和$\mathbf{G}_{* j}$之间的相似性（内积）在$S_{i j}=1$时大，当$S_{i j}=0$时小。因此，优化等式（1）中的第一项可以保留将$\mathbf{S}$中的图像特征表示$\mathbf{F}$和文本特征表示$\mathbf{G}$的跨模态相似性。

通过优化第二项$\gamma \left( \left\| \mathbf{B}^{(x)} - \mathbf{F} \right\|_{F}^{2}+\| \mathbf{B}^{(y)}-\mathbf{G} \|_{F}^{2} )\mathbf{G} \|_{F}^{2}\right )$,我们可以得到$\mathbf{B}^{(x)}=\operatorname{sign}(\mathbf{F})$和$\mathbf{B}^{(y)}=\operatorname{sign}(\mathbf{G})$.因此相对的，我们认为$\mathbf{F}$和$\mathbf{G}$分别是$\mathbf{B}^{(x)}$和$\mathbf{B}^{(y)}$的连续替代.因为$\mathbf{F}$和$\mathbf{G}$能够保留$\mathbf{S}$中的跨模态相似性，所以二进制的哈希码$\mathbf{B}^{(x)}$和$\mathbf{B}^{(y)}$也被期望能够保留$\mathbf{S}$中的跨模态相似性，也就是说能够匹配跨模式哈希的目标。

第三项$\eta\left(\|\mathbf{F} \mathbf{1}\|_{F}^{2}+\|\mathbf{G} \mathbf{1}\|_{F}^{2}\right)$被用作在所有训练点上使哈希码的每一位均衡。 更具体地说，所有训练点上每个比特的+1和-1的数量应该几乎相同。 该约束可用于最大化每位提供的信息。在我们的实验中，我们发现如果来自两个模态的二进制代码对于相同的训练点被设置为相同，则可以实现更好的性能。 因此，我们设置$\mathbf{B}^{(x)}=\mathbf{B}^{(y)}=\mathbf{B}$.然后，等式（1）中的问题可以转换为以下公式：
$$
\begin{aligned} \min _{\mathbf{B}, \theta_{x}, \theta_{y}} \mathcal{J} &=-\sum_{i, j=1}^{n}\left(S_{i j} \Theta_{i j}-\log \left(1+e^{\Theta_{i j}}\right)\right) \\ &+\gamma\left(\|\mathbf{B}-\mathbf{F}\|_{F}^{2}+\|\mathbf{B}-\mathbf{G}\|_{F}^{2}\right) \\ &+\eta\left(\|\mathbf{F} \mathbf{1}\|_{F}^{2}+\|\mathbf{G} \mathbf{1}\|_{F}^{2}\right) \\ \text { s.t. } \mathbf{B} & \in\{-1,+1\}^{c \times n} \end{aligned} \tag 2
$$
这是我们DCMH最终要学习的目标函数。

从（2）中，我们可以发现深度神经网络（$\theta_{x}$ and $\theta_{y}$）和二进制哈希码（$\mathbf{B}$）的参数是从同一目标函数中学习的。 也就是说，DCMH将特征学习和哈希码学习集成到同一个深度学习框架中。

请注意，我们只训练点$\mathbf{B}^{(x)}=\mathbf{B}^{(y)}$。 在我们学习了等式（2）中的问题后，我们对于相同点$i$的两个不同模态如果点$𝑖$是查询点, 或该点来自数据库而不是训练点，仍然需要生成不同的二级制$\mathbf{b}_{i}^{(x)}=h^{(x)}\left(\mathbf{x}_{i}\right)$和$\mathbf{b}_{i}^{(y)}=h^{(y)}\left(\mathbf{y}_{i}\right)$。 这将在3.3节中进一步说明。

### 3.2 Learning

我们采用交替学习策略来学习$\theta_{x}$，$\theta_{y}$和$\mathbf{B}$.每次我们学习一个参数，其他参数固定。 在算法1中简要概述了用于DCMH的整个交替学习算法，并且将在本小节的以下内容中引入详细的推导。

#### **3.2.1 Learn** 𝜃𝑥**, with** 𝜃𝑦 **and** B **Fixed**

当$\theta_{y}$和$\mathbf{B}$固定时，我们通过使用反向传播（BP）算法来学习图像模态的CNN参数$\theta_{x}$。 作为大多数现有的深度学习方法，我们利用随机梯度下降（SGD）和BP算法来学习$\theta_{x}$。 更具体地说，在每次迭代中，我们从训练集中采样mini-batch点，然后基于采样数据执行我们的学习算法。

特别是，对于每个采样点$\mathbf{x}_{i}$，我们首先计算以下梯度：
$$
\begin{aligned} \frac{\partial \mathcal{J}}{\partial \mathbf{F}_{* i}}=& \frac{1}{2} \sum_{j=1}^{n}\left(\sigma\left(\Theta_{i j}\right) \mathbf{G}_{* j}-S_{i j} \mathbf{G}_{* j}\right) \\ &+2 \gamma\left(\mathbf{F}_{* i}-\mathbf{B}_{* i}\right)+2 \eta \mathbf{F} \mathbf{1} \end{aligned} \tag 3
$$
然后我们使用链式法则（基于此法则BP可以用于更新参数$\theta_{x}$）通过$\frac{\partial \mathcal{J}}{\partial \mathbf{F}_{* i}}$计算$\frac{\partial \mathcal{J}}{\partial \theta_{x}}$.

#### 3.2.2 **Learn** 𝜃𝑦**, with** 𝜃𝑥 **and** B **Fixed**

当$\theta_{x}$和$\mathbf{B}$固定时，我们还通过使用SGD和BP算法来学习文本模态的神经网络参数$\theta_{y}$。 更具体地说，对于每个采样点$\mathbf{y}_{j}$，我们首先计算以下梯度：
$$
\begin{aligned} \frac{\partial \mathcal{J}}{\partial \mathbf{G}_{* j}}=& \frac{1}{2} \sum_{i=1}^{n}\left(\sigma\left(\Theta_{i j}\right) \mathbf{F}_{* i}-S_{i j} \mathbf{F}_{* i}\right) \\ &+2 \gamma\left(\mathbf{G}_{* j}-\mathbf{B}_{* j}\right)+2 \eta \mathbf{G} \mathbf{1} \end{aligned} \tag 4
$$


然后我们使用链式法则（基于此法则BP可以用于更新参数$\theta_{y}$）通过$\frac{\partial \mathcal{J}}{\partial \mathbf{G}_{* i}}$计算$\frac{\partial \mathcal{J}}{\partial \theta_{y}}$.

#### 3.2.3 **Learn B,**, with 𝜃𝑦 and **𝜃𝑥 **Fixed

当$\theta_{x}$和$\theta_{y}$固定时，前面提到的问题（相同点$i$的两个不同模态如果点$𝑖$是查询点, 或该点来自数据库而不是训练点，仍然需要生成不同的二级制$\mathbf{b}_{i}^{(x)}=h^{(x)}\left(\mathbf{x}_{i}\right)$和$\mathbf{b}_{i}^{(y)}=h^{(y)}\left(\mathbf{y}_{i}\right)$），可以重新计算为：

$\max _{\mathbf{B}} \operatorname{tr}\left(\mathbf{B}^{T}(\gamma(\mathbf{F}+\mathbf{G}))\right)=\operatorname{tr}\left(\mathbf{B}^{T} \mathbf{V}\right)=\sum_{i, j} B_{i j} V_{i j} \\ s.t. \mathbf{B} \in\{-1,+1\}^{c \times n}$

其中$\mathbf{V}=\gamma(\mathbf{F}+\mathbf{G})$。

很容易发现二进制代码$B_{i j}$应该与$V_{i j}$保持相同的符号。 因此，我们有：

$$
\mathbf{B}=\operatorname{sign}(\mathbf{V})=\operatorname{sign}(\gamma(\mathbf{F}+\mathbf{G})) \tag 5
$$

### 3.3 Out-of-Sample Extension

对于不在训练集中的任何点，只要观察到其中一个模态（图像或文本），我们就可以获得其哈希码。 特别是，给定点$q$的图像模态$\mathbf{x}_{q}$，我们可以采用前向传播来生成哈希码，如下所示：
$$
\mathbf{b}_{q}^{(x)}=h^{(x)}\left(\mathbf{x}_{q}\right)=\operatorname{sign}\left(f\left(\mathbf{x}_{q} ; \theta_{x}\right)\right)
$$
特别的，如果点$q$只有文本模态$\mathbf{y}_{q}$，我们可以生成它的哈希码：
$$
\mathbf{b}_{q}^{(y)}=h^{(y)}\left(\mathbf{y}_{q}\right)=\operatorname{sign}\left(g\left(\mathbf{y}_{q} ; \theta_{y}\right)\right)
$$
因此，我们的DCMH模型可以用在跨模态搜索上，尤其是查询点只有一种模态，或者该数据点是在数据库中的点且具有其他模态。

``` pseudocode
算法1： DMCH的学习算法

输入：图像集X,文本集Y和跨模态相似矩阵S

输出：神经网络参数𝜃𝑥和𝜃𝑦，以及二进制码矩阵B

初始化：
	初始化神经网络参数：𝜃𝑥和𝜃𝑦
  最小批大小：𝑁𝑥 = 𝑁𝑦 = 128
  迭代序号： 𝑡𝑥 = ⌈𝑛/𝑁𝑥⌉,𝑡𝑦 = ⌈𝑛/𝑁𝑦 ⌉.
  
循环（知道迭代序号到达固定值）：
  // 学习𝜃𝑥
	for iter = 1,2,..., 𝑡𝑥 do
  	从X中随机采样𝑁𝑥个数据点构建一个mini-batch
  	对于mini-batch中采样的每个数据点都使用前向传播算法计算F∗𝑖 = 𝑓(x𝑖;𝜃𝑥)
  	根据等式（3）求导
  	使用后向传播算法更新参数𝜃𝑥
  end for
  //学习𝜃𝑦
  for iter = 1,2,...,𝑡𝑦 do
  	从Y中随机采样𝑁𝑦个数据点构建一个mini-batch
  	对于mini-batch中采样的每个数据点都使用前向传播算法计算G∗𝑗 =𝑔(y𝑗;𝜃𝑦)
  	根据等式（4）求导
  	使用后向传播算法更新参数𝜃𝑦
  end for
  //学习矩阵B
  根据等式（5）学习矩阵B
```

## 4.Experiment

我们在图像-文本数据集上进行试验，以验证DCMH的高效性。DCMH使用开源深度学习工具包`MatConvNet`实现，在NVIDIA K80的GPU服务器上运行。

### 4.1 Dataset

三个数据集用作评估：*MIRFLICKR-25K* , *IAPR TC-12* 
和 *NUS-WIDE* 

*MIRFLICKR-25K*原始数据包含了25000张从Flickr网站上收集的图片。每张图片都和几个文本标签关联。因此每个数据点都是图像-文本对。并且我们在试验中选择的每张图片都有至少20个文本标签。每个数据点的文本都用1386维的词袋向量表示。基于手工提取特征的方法，每张图片都用512维的GIST特征向量表示。而且，每个数据点都使用24个唯一标签之一手动注释。

*IAPR TC-12*数据集包含了20000张图像-文本对，共有255类标签。我们实验使用了整个数据集。每个数据点的文本都用2912维的词袋向量表示。基于手工提取特征的方法，每张图片都用512维的GIST特征向量表示。

*NUS-WIDE*数据集包含260648个网站图片，一些图片是关联了文本标签。他是一个多标签数据集，也就是说每个图片都有一个或者多个标签（共81个概念标签）。我们选取了21个最频繁的概念，其中包括195834个图像-文本数据对。每个数据点的文本都用1000、维的词袋向量表示。基于手工提取特征的方法，每张图片都用500维的视觉词袋特征向量表示。

对于所有的数据集，图像$i$和文本$j$如果点$i$和点$j$是有至少一个共同标签，我们就认为他们是相似的，否则我们认为不相似。

### 4.2 **Evaluation Protocol and Baseline**

#### 4.2.1 **Evaluation Protocol**

对于*MIRFLICKR-25K*和*IAPR TC-12*数据集，我们随机抽样2,000个数据点作为测试（查询）集，其余点作为检索集（数据库）。对于*NUS-WIDE*数据集，我们将2,100个数据点作为测试集，其余数据作为检索集。此外，我们从检索集中采样10,000个数据点作为*MIRFLICKR-25K*和*IAPR TC-12*的训练集。对于NUS-WIDE数据集，我们从检索集中将10,500个数据点作为训练集进行采样。实际的上邻居是被定义为共享至少一个共同标签的那些图像-文本对。

对于基于哈希的检索，汉明排名（Hamming Ranking）和哈希查找（Hash look up）是两种广泛使用的检索协议。我们还采用这两个协议来评估我们的方法和其他baseline。汉明排名协议按照递增顺序对给定查询点的汉明距离对数据库中的点（检索集）进行排序。平均精度均值（MAP）是衡量汉明排名协议准确性而广泛使用的度量标准。哈希查找协议返回的是离查询点在某个汉明半径内的所有点。准确率-召回率PR曲线是用于衡量哈希查找协议准确性的广泛使用的度量标准。

#### 4.2.2 Baseline

采用六种最先进的跨模式散列方法作为比较基线，包括SePH ，STMH ，SCM ，CMFH ，CCA 和DVSH 。。 由于DVSH只能用于其中一种模态必须是时间动态的特殊CMH情况，我们仅在IAPR TC-12数据集上比较DCMH和DVSH，其中原始文本是可被视为时间动态的句子。 *MIRFLICKR-25K*和*NUS-WIDE*中的文本是不适合DVSH的标签。 请注意，除了DVSH之外，所有评估方法的文本都表示为BOW向量。

SePH，STMH和SCM的源代码由相应的作者提供。 对于没有代码的CMFH和CCA，我们自己仔细实现的。 SePH是一种基于内核的方法，我们使用RBF内核，并按照作者的建议，将500个随机选择的点作为内核基础。 在SePH中，作者提出了两种策略来根据是否观察到两个点的模态来构造检索（数据库）点的哈希码。 然而，在本文中，我们只使用一种模态用于数据库（检索）点，因为本文的重点是跨模态检索。 所有基线的所有其他参数都是根据这些基线的原始论文的建议设定的。

对于DCMH，我们使用验证集来选择超参数$\gamma$和$\eta$，并发现在$\gamma=\eta=1$时可以实现良好的性能。 因此，对于DCMH，我们设置$\gamma=\eta=1$。 我们利用在ImageNet数据集上预训练的CNN-F网络来初始化CNN的前七层并用于图像模态。 DCMH中的深度神经网络的所有其他参数都是被随机初始化的。 图像模态的输入是原始像素，文本模态的输入是BOW矢量。 我们将mini-batch大小固定为128，并将算法1中外环的迭代次数设置为500.学习率从$10^{-6}$到$10^{-1}$中选择，并带有验证集。 所有实验运行五次，并报告平均性能。

### **4.3. Accuracy**

#### **4.3.1 Hamming Ranking**

在*MIRFLICKR-25K*，*IAPR TC-12*和*NUS-WIDE*数据集上DCMH和其他具有手工制作特征的基线的MAP结果在表3中报告。这里，“$I \rightarrow T$”表示查询是图像的情况而数据库是文本，”$I \rightarrow T$表示查询是文本而数据库是图像的情况。 我们可以发现DCMH可以超越所有其他通过手工制作的特征方法的基线。

![](https://blog.idejie.com/pics/20190806101757.png)

为了进一步验证DCMH的有效性，我们利用在ImageNet数据集上预训练的CNN-F深度网络，以提取CNN特征，该网络与DCMH中图像模态的初始CNN相同。 所有基线都基于这些CNN特征进行训练。 表4中报告了DCMH和其他具有CNN特征的基线在三个数据集上的MAP结果。我们可以发现在NUS-WIDE上图像到文本的检索，DCMH可以胜过除SePH之外的所有其他基线。

![](https://blog.idejie.com/pics/20190806103537.png)

#### **4.3.2 Hash Lookup**

在哈希查询协议中，我们可以计算给定任何汉明半径内的返回点的精度和召回率。 通过使用步长1将汉明半径从0变为$c$，我们可以得到准确率-召回率曲线。

图2显示了三个数据集在编码长度是16位个准确率-召回率PR曲线，在图中的每行，其中前两个子图基于手工制作的特征，最后两个子图基于CNN-F特征。 我们可以发现DCMH可以显着优于其他方法无论是基于手工制作的特征和CNN-F特征。 我们的DCMH还可以在具有不同编码长度值的其他情况下实现最佳性能，例如32位和64位。 由于空间限制，省略了这些结果。

![](https://blog.idejie.com/pics/20190806105537.png)

### **4.4. Comparison with DVSH**

由于DVSH的源代码不公开，并且重新实现DVSH也很困难，我们采用与DVSH相同的实验设置来评估DCMH并直接将结果用于DVSH进行比较。 表5中列出了*IAPR TC-12*数据集上的前500个MAP比较结果。请注意，DVSH的文本输入是句子，我们将句子表示为DCMH的相同的BOW向量。 我们可以发现DCMH在大多数情况下可以胜过DVSH。

![](https://blog.idejie.com/pics/20190806105834.png)

### **4.5. Sensitivity to Parameters**

我们探讨了超参数$\gamma$和$\eta$的影响。 图3列出了具有不同 $\gamma$ 和$\eta$值的在*MIRFLICKR-25K*数据集的MAP结果，其中编码长度为16位。 我们可以看出DCMH对$\gamma$和$\eta$不敏感，其中$0.01<\gamma<2$且$0.01<\eta<2$。

![](https://blog.idejie.com/pics/20190806110155.png)

### **4.6. Further Analysis**

为了进一步验证特征学习的有效性，我们评估了DCMH的一些变体，即DCMH-I，DCMH-T，DCMH-IT。 DCMH-I表示没有图像特征学习的变体，其中我们在训练期间固定图像模态的前七层的参数。 DCMH-T表示没有文本特征学习的变体，其中我们将文本模态的深度神经网络替换为线性投影。 DCMH-IT表示没有图像和文本特征学习的变体。

图4报告了*IAPR TC-12*上的MAP结果。 我们可以发现DCMH可以实现比DCMH-I，DCMH-T和DCMH-IT更高的准确性，这证明了同时进行哈希码学习和特征学习的重要性。

![](https://blog.idejie.com/pics/20190806122850.png)

## 5.Conclusion

在本文中，我们提出了一种新的哈希方法，称为DCMH，用于跨模态检索应用。 DCMH是一个端到端的深度学习框架，可以同时执行特征学习和哈希码学习。 对三个数据集的实验表明，DCMH可以明显优于其他基线，以在实际应用中实现最先进的性能。

## 总结与思考