---
title: 语义分析（文本语义分析）
date: 2017-05-12 19:57:02
tags: 语义分析
category: NLP
---

### 2 文本语义分析

前面讲到一些文本基本处理方法。一个文本串，对其进行分词和重要性打分后（当然还有更多的文本处理任务），就可以开始更高层的语义分析任务。

#### 2.1 Topic Model

首先介绍主题模型。说到主题模型，第一时间会想到pLSA，NMF，LDA。关于这几个目前业界最常用的主题模型，已经有相当多的介绍了，譬如文献[60，64]。在这里，主要想聊一下主题模型的应用以及最新进展(考虑到LDA是pLSA的generalization，所以下面只介绍LDA)。

##### LDA训练算法简单介绍

LDA的推导这里略过不讲，具体请参考文献[64]。下面我们主要看一下怎么训练LDA。

在Blei的原始论文中，使用variational inference和EM[算法](http://lib.csdn.net/base/datastructure)进行LDA推断(与pLSA的推断过程类似，E-step采用variational inference)，但EM算法可能推导出局部最优解，且相对复杂。目前常用的方法是基于gibbs sampling来做[57]。

- Step1: 随机初始化每个词的topic，并统计两个频率计数矩阵：Doc-Topic 计数矩阵N(t,d)，描述每个文档中的主题频率分布；Word-Topic 计数矩阵N(w,t)，表示每个主题下词的频率分布。
- Step2: 遍历训练语料，按照概率公式(下图所示)重新采样每个词所对应的topic, 更新N(t,d)和N(w,t)的计数。
- Step3: 重复 step2，直到模型收敛。

对文档d中词w的主题z进行重新采样的公式有非常明确的物理意义，表示为P(w|z)P(z|d)，直观的表示为一个“路径选择”的过程。

![lda_sampling](http://dataunion.org/wp-content/uploads/2015/02/lda_sampling.png)

图10. gibbs sampling过程图

以上描述过程具体请参考文献[65]。

对于LDA模型的更多理论介绍，譬如如何实现正确性验证，请参考文献[68]，而关于LDA模型改进，请参考Newman团队的最新文章《Care and Feeding of Topic Models》[12]。

##### 主题模型的应用点

- 在广点通内部，主题模型已经在很多方面都得到成功应用[65]，譬如文本分类特征，相关性计算，ctr预估，精确广告定向，矩阵分解等。具体来说，基于主题模型，可以计算出文本，用户的topic分布，将其当作pctr，relevance的特征，还可以将其当作一种矩阵分解的方法，用于降维，推荐等。不过在我们以往的成功运用中，topic模型比较适合用做某些机器学习任务的特征，而不适合作为一种独立的方法去解决某种特定的问题，例如触发，分类。Blei是这样评价lda的：it can easily be used as a module in more complicated models for more complicated goals。
- 为什么topic model不适合作为一种独立的方法去解决某种特定的问题(例如分类，触发等)。
  - 个人总结，主要原因是lda模型可控性可解释性相对比较差：对于每个topic，不能用很明确的语义归纳出这个topic在讲什么；重新训练一遍lda模型，每个topic id所对应的语义可能发生了变化；有些topic的准确性比较好，有些比较差，而对于比较差的topic，没有特别好的针对性的方法去优化它；
  - 另外一个就是topic之间的重复，特别是在topic数目比较多的情况，重复几乎是不可避免的，当时益总(yiwang)在开发peacock的时候，deduplicate topic就是一个很重要的任务。如果多个topic描述的意思一致时，用topic id来做检索触发，效果大半是不好的，后来我们也尝试用topic word来做，但依旧不够理想。

##### 主题模型最新进展

首先主题模型自PLSA, LDA后，又提出了很多变体，譬如HDP。LDA的topic number是预先设定的，而HDP的topic number是不固定，而是从训练数据中学习得到的，这在很多场景是有用的，具体参考[hdp vs lda](http://datascience.stackexchange.com/questions/128/latent-dirichlet-allocation-vs-hierarchical-dirichlet-process)。想了解更多LDA模型的升级，请参考文献[73,74]。

[深度学习](http://lib.csdn.net/base/deeplearning)方面，Geoff Hinton及其学生用Deep Boltzmann Machine研究出了类似LDA的隐变量文本模型[82]，文章称其抽取的特征在文本检索与文本分类上的结果比LDA好。[heavenfireray](http://weibo.com/u/2387864597)在其微博评论道：lda结构是word-hidden topic。类lda结构假设在topic下产生每个word是条件独立而且参数相同。这种假设导致参数更匹配长文而非短文。该文章提出word-hidden topic-hidden word，其实是(word,hidden word)-hidden topic，增加的hidden word平衡了参数对短文的适配，在分类文章数量的度量上更好很自然。

其次，随着目前互联网的数据规模的逐渐增加，大规模并行PLSA，LDA训练将是主旋律。大规模主题模型训练，除了从系统[架构](http://lib.csdn.net/base/architecture)上进行优化外，更关键的，还需要在算法本身上做升级。variational方法不太适合并行化，且速度相对也比较慢，这里我们着重看sampling-base inference。

- collapsed Gibbs sampler[57]：O(K)复杂度，K表示topic的总个数。
- SparseLDA[66]：算法复杂度为O(Kd + Kw)，Kd表示文档d所包含的topic个数，Kw表示词w所属的topic个数，考虑到一个文档所包含的topic和一个词所属的topic个数是有限的，肯定远小于K，所以相比于collapsed Gibbs，复杂度已有较大的下降。
- AliasLDA[56]：利用alias table和Metropolis-Hastings，将词这个维度的采样复杂度降至O(1)。所以算法总复杂度为O(Kd)。
- Metropolis-Hastings sampler[13]：复杂度降至O(1)。这里不做分析了，具体请参考文献[13]

##### 主题模型并行化

在文献[67]中，Newman团队提出了LDA算法的并行化版本Approximate distributed-LDA，如下图所示：

![ad_lda](http://dataunion.org/wp-content/uploads/2015/02/ad_lda.png)

图11. AD-LDA算法

在原始gibbs sampling算法里，N(w,t)这个矩阵的更新是串行的，但是研究发现，考虑到N(w,t)矩阵在迭代过程中，相对变化较小，多个worker独立更新N(w,t)，在一轮迭代结束后再根据多个worker的本地更新合并到全局更新N(w,t)，算法依旧可以收敛[67]。

那么，主题模型的并行化(不仅仅是主题模型，其实是绝大部分[机器学习](http://lib.csdn.net/base/machinelearning)算法)，主要可以从两个角度来说明：数据并行和模型并行。

- 数据并行。这个角度相对比较直观，譬如对于LDA模型，可以将训练数据按照worker数目切分为M片(M为worker数)，每个worker保存一份全局的N(w,t)矩阵，在一轮迭代里，各个worker独立计算，迭代结束后，合并各个worker的本地更新。这个思路可以借用目前通用的并行计算框架，譬如Spark，Hadoop，Graphlab等来实现。
- 模型并行。考虑到矩阵N(w,t)在大规模主题模型中相当巨大，单机内存不可能存下。所以直观的想法，可以将N(w,t)也切分成多个分片。N(w,t)可以考虑使用全局的parameter server来存储，也可以考虑存储在不同worker上，利用MPI AllReduce来通信。

数据与模型并行，可以形象的描述为一个棋盘。棋盘的行按照数据划分，棋盘的列按照模型划分。LDA的并行化，就是通过这样的切分，将原本巨大的，不可能在单机存储的矩阵切分到不同的机器，使每台机器都能够将参数存储在内存。再接着，各个worker相对独立计算，计算的过程中不时按照某些策略同步模型数据。

最近几年里，关于LDA并行化已有相当多的开源实现，譬如：

- PLDA，[PLDA+](https://code.google.com/p/plda/)
- [Yahoo LDA](https://github.com/sudar/Yahoo_LDA)
- [Parameter server](https://github.com/mli/parameter_server)

最近的并行LDA实现Peacock[70,65]和LigthLda[13]没有开源，但我们可以从其论文一窥究竟，总体来说，并行化的大体思路是一致的。譬如LightLDA[13]，下图是实现架构框图，它将训练数据切分成多个Block，模型通过parameter server来同步，每个data block，类似于sliding windows，在计算完V1的采样后，才会去计算V2的采样(下图中V1,V2,V3表示word空间的划分，即模型的划分)。

![parallelism_lda](http://dataunion.org/wp-content/uploads/2015/02/parallelism_lda.png)

图12. LightLda并行结构图

#### 2.2 词向量，句向量

##### 词向量是什么

在文本分析的vector space model中，是用向量来描述一个词的，譬如最常见的One-hot representation。One-hot representation方法的一个明显的缺点是，词与词之间没有建立关联。在深度学习中，一般用Distributed Representation来描述一个词，常被称为“Word Representation”或“Word Embedding”，也就是我们俗称的“词向量”。

词向量起源于hinton在1986年的论文[11]，后来在Bengio的ffnnlm论文[3]中，被发扬光大，但它真正被我们所熟知，应该是word2vec[14]的开源。在ffnnlm中，词向量是训练语言模型的一个副产品，不过在word2vec里，是专门来训练词向量，所以word2vec相比于ffnnlm的区别主要体现在：

- 模型更加简单，去掉了ffnnlm中的隐藏层，并去掉了输入层跳过隐藏层直接到输出层的连接。
- 训练语言模型是利用第m个词的前n个词预测第m个词，而训练词向量是用其前后各n个词来预测第m个词，这样做真正利用了上下文来预测，如下图所示。

![word2vec](http://dataunion.org/wp-content/uploads/2015/02/word2vec.png)

图13. word2vec的训练算法

上图是word2vec的两种训练算法：CBOW(continuous bag-of-words)和Skip-gram。在cbow方法里，训练目标是给定一个word的context，预测word的概率；在skip-gram方法里，训练目标则是给定一个word，预测word的context的概率。

关于word2vec，在算法上还有较多可以学习的地方，例如利用huffman编码做层次softmax，negative sampling，工程上也有很多trick，具体请参考文章[16][17]。

##### 词向量的应用

词向量的应用点：

- 可以挖掘词之间的关系，譬如同义词。
- 可以将词向量作为特征应用到其他机器学习任务中，例如作为文本分类的feature，Ronan collobert在Senna[37]中将词向量用于POS, CHK, NER等任务。
- 用于机器翻译[28]。分别训练两种语言的词向量，再通过词向量空间中的矩阵变换，将一种语言转变成另一种语言。
- word analogy，即已知a之于b犹如c之于d，现在给出 a、b、c，C(a)-C(b)+C(c)约等于C(d)，C(*)表示词向量。可以利用这个特性，提取词语之间的层次关系。
- Connecting Images and Sentences，image understanding。例如文献，DeViSE: A deep visual-semantic em-bedding model。
- Entity completion in Incomplete Knowledge bases or ontologies，即relational extraction。Reasoning with neural tensor net- works for knowledge base completion。
- more word2vec applications，点击[link1](http://www.quora.com/Do-you-know-any-interesting-applications-using-distributed-representations-of-words-obtained-from-NNLM-eg-word2vec)，[link2](https://www.quora.com/What-are-some-interesting-Word2Vec-results)

除了产生词向量，word2vec还有很多其他应用领域，对此我们需要把握两个概念：doc和word。在词向量训练中，doc指的是一篇篇文章，word就是文章中的词。

- 假设我们将一簇簇相似的用户作为doc（譬如QQ群），将单个用户作为word，我们则可以训练user distributed representation，可以借此挖掘相似用户。
- 假设我们将一个个query session作为doc，将query作为word，我们则可以训练query distributed representation，挖掘相似query。

##### 句向量

分析完word distributed representation，我们也许会问，phrase，sentence是否也有其distributed representation。最直观的思路，对于phrase和sentence，我们将组成它们的所有word对应的词向量加起来，作为短语向量，句向量。在参考文献[34]中，验证了将词向量加起来的确是一个有效的方法，但事实上还有更好的做法。

Le和Mikolov在文章《Distributed Representations of Sentences and Documents》[20]里介绍了sentence vector，这里我们也做下简要分析。

先看c-bow方法，相比于word2vec的c-bow模型，区别点有：

- 训练过程中新增了paragraph id，即训练语料中每个句子都有一个唯一的id。paragraph id和普通的word一样，也是先映射成一个向量，即paragraph vector。paragraph vector与word vector的维数虽一样，但是来自于两个不同的向量空间。在之后的计算里，paragraph vector和word vector累加或者连接起来，作为输出层softmax的输入。在一个句子或者文档的训练过程中，paragraph id保持不变，共享着同一个paragraph vector，相当于每次在预测单词的概率时，都利用了整个句子的语义。
- 在预测阶段，给待预测的句子新分配一个paragraph id，词向量和输出层softmax的参数保持训练阶段得到的参数不变，重新利用梯度下降训练待预测的句子。待收敛后，即得到待预测句子的paragraph vector。

![sentence2vec0](http://dataunion.org/wp-content/uploads/2015/02/sentence2vec0.png)

图14. sentence2vec cBow算法

sentence2vec相比于word2vec的skip-gram模型，区别点为：在sentence2vec里，输入都是paragraph vector，输出是该paragraph中随机抽样的词。

![sentence2vec1](http://dataunion.org/wp-content/uploads/2015/02/sentence2vec1.png)

图15. sentence2vec Skip-gram算法

下面是sentence2vec的结果示例。先利用中文sentence语料训练句向量，然后通过计算句向量之间的cosine值，得到最相似的句子。可以看到句向量在对句子的语义表征上还是相当惊叹的。

![sentence2vec4](http://dataunion.org/wp-content/uploads/2015/02/sentence2vec4.png)

图16. sentence2vec 结果示例

##### 词向量的改进

- 学习词向量的方法主要分为：Global matrix factorization和Shallow Window-Based。Global matrix factorization方法主要利用了全局词共现，例如LSA；Shallow Window-Based方法则主要基于local context window，即局部词共现，word2vec是其中的代表；Jeffrey Pennington在word2vec之后提出了[GloVe](http://nlp.stanford.edu/projects/glove/)，它声称结合了上述两种方法，提升了词向量的学习效果。它与word2vec的更多对比请点击[GloVe vs word2vec](http://www.quora.com/How-is-GloVe-different-from-word2vec)，[GloVe & word2vec评测](http://radimrehurek.com/2014/12/making-sense-of-word2vec/)。
- 目前通过词向量可以充分发掘出“一义多词”的情况，譬如“快递”与“速递”；但对于“一词多义”，束手无策，譬如“苹果”(既可以表示苹果手机、电脑，又可以表示水果)，此时我们需要用多个词向量来表示多义词。

#### 2.3 卷积神经网络

##### 卷积

介绍卷积神经网络(convolutional neural network，简记cnn)之前，我们先看下卷积。

在一维信号中，卷积的运算，请参考[wiki](http://zh.wikipedia.org/wiki/%E5%8D%B7%E7%A7%AF)，其中的图示很清楚。在图像处理中，对图像用一个卷积核进行卷积运算，实际上是一个滤波的过程。下面是卷积的数学表示：

[![QQ截图20150210203448](http://dataunion.org/wp-content/uploads/2015/02/QQ%E6%88%AA%E5%9B%BE20150210203448.png)](http://dataunion.org/wp-content/uploads/2015/02/QQ%E6%88%AA%E5%9B%BE20150210203448.png)

f(x,y)是图像上点(x,y)的灰度值，w(x,y)则是卷积核，也叫滤波器。卷积实际上是提供了一个权重模板，这个模板在图像上滑动，并将中心依次与图像中每一个像素对齐，然后对这个模板覆盖的所有像素进行加权，并将结果作为这个卷积核在图像上该点的响应。如下图所示，卷积操作可以用来对图像做边缘检测，锐化，模糊等。

![convolution1](http://dataunion.org/wp-content/uploads/2015/02/convolution1-235x300.png)

![convolution2](http://dataunion.org/wp-content/uploads/2015/02/convolution2.png)

图17. 卷积操作示例

##### 什么是卷积神经网络

卷积神经网络是一种特殊的、简化的深层神经网络模型，它的每个卷积层都是由多个卷积滤波器组成。它最先由lecun在LeNet[40]中提出，网络结构如下图所示。在cnn中，图像的一小部分（局部感受区域）作为层级结构的最低层的输入，信息再依次传输到不同的层，每层通过多个卷积滤波器去获得观测数据的最显著的特征。[![lenet5](http://dataunion.org/wp-content/uploads/2015/02/lenet5.png)](http://dataunion.org/wp-content/uploads/2015/02/lenet5.png)

[![convolution5](http://dataunion.org/wp-content/uploads/2015/02/convolution5.png)](http://dataunion.org/wp-content/uploads/2015/02/convolution5.png)

图18. Lenet5网络结构图

卷积神经网络中的每一个特征提取层（卷积层）都紧跟着一个用来求局部平均与二次提取的计算层（pooling层），这种特有的两次特征提取结构使网络在识别时对输入样本有较高的畸变容忍能力。如下图所示，就是一个完整的卷积过程[21]。

![convolution6](http://dataunion.org/wp-content/uploads/2015/02/convolution6.jpg)

图19. 一次完整的卷积过程

它的特殊性体现在两点：(1)局部感受野(receptive field)，cnn的神经元间的连接是非全连接的；(2)同一层中同一个卷积滤波器的权重是共享的（即相同的）。局部感受野和权重共享这两个特点，使cnn网络结构更类似于生物神经网络，降低了网络模型的复杂度，减少了神经网络需要训练的参数的个数。

##### 卷积神经网络的一些细节

接下来结合文献[25]，再讲讲卷积神经网络的一些注意点和问题。

- 激励函数，要选择非线性函数，譬如tang，sigmoid，rectified liner。在CNN里，relu用得比较多，原因在于：(1)简化BP计算；(2)使学习更快。(3)避免饱和问题(saturation issues)
- Pooling：其作用在于(1)对一些小的形态改变保持不变性，Invariance to small transformations；(2)拥有更大的感受域，Larger receptive fields。pooling的方式有sum or max。
- Normalization：Equalizes the features maps。它的作用有：(1) Introduces local competition between features；(2)Also helps to scale activations at each layer better for learning；(3)Empirically, seems to help a bit (1–2%) on ImageNet
- 训练CNN：back-propagation；stochastic gradient descent；Momentum；Classification loss，cross-entropy；Gpu实现。
- 预处理：Mean removal；Whitening(ZCA)
- 增强泛化能力：Data augmentation；Weight正则化；在网络里加入噪声，包括DropOut，DropConnect，Stochastic pooling。
  - DropOut：只在全连接层使用，随机的将全连接层的某些神经元的输出置为0。
  - DropConnect：也只在全连接层使用，Random binary mask on weights
  - Stochastic Pooling：卷积层使用。Sample location from multinomial。
- 模型不work，怎么办？结合我自身的经验，learning rate初始值设置得太大，开始设置为0.01，以为很小了，但实际上0.001更合适。

##### 卷积神经网络在文本上的应用

卷积神经网络在image classify和image detect上得到诸多成功的应用，后文将再详细阐述。但除了图片外，它在文本分析上也取得一些成功的应用。

基于CNN，可以用来做文本分类，情感分析，本体分类等[36,41,84]。传统文本分类等任务，一般基于bag of words或者基于word的特征提取，此类方法一般需要领域知识和人工特征。利用CNN做，方法也类似，但一般都是基于raw text，CNN模型的输入可以是word series，可以是word vector，还可以是单纯的字符。比起传统方法，CNN不需要过多的人工特征。

- 将word series作为输入，利用CNN做文本分类。如下图所示[36]，该CNN很简单，共分四层，第一层是词向量层，doc中的每个词，都将其映射到词向量空间，假设词向量为k维，则n个词映射后，相当于生成一张n*k维的图像；第二层是卷积层，多个滤波器作用于词向量层，不同滤波器生成不同的feature map；第三层是pooling层，取每个feature map的最大值，这样操作可以处理变长文档，因为第三层输出只依赖于滤波器的个数；第四层是一个全连接的softmax层，输出是每个类目的概率。除此之外，输入层可以有两个channel，其中一个channel采用预先利用word2vec训练好的词向量，另一个channel的词向量可以通过backpropagation在训练过程中调整。这样做的结果是：在目前通用的7个分类评测任务中，有4个取得了state-of-the-art的结果，另外3个表现接近最好水平。
  [![cnn_text_classify](http://dataunion.org/wp-content/uploads/2015/02/cnn_text_classify.png)](http://dataunion.org/wp-content/uploads/2015/02/cnn_text_classify.png)图20.基于CNN的文本分类利用cnn做文本分类，还可以考虑到词的顺序。利用传统的”bag-of-words + maxent/svm”方法，是没有考虑词之间的顺序的。文献[41]中提出两种cnn模型：seq-cnn, bow-cnn，利用这两种cnn模型，均取得state-of-the-art结果。
- 将doc character作为输入，利用CNN做文本分类。文献[86]介绍了一种方法，不利用word，也不利用word vector，直接将字符系列作为模型输入，这样输入维度大大下降(相比于word)，有利于训练更复杂的卷积网络。对于中文，可以将汉字的拼音系列作为输入。

#### 2.4 文本分类

文本分类应该是最常见的文本语义分析任务了。首先它是简单的，几乎每一个接触过nlp的同学都做过文本分类，但它又是复杂的，对一个类目标签达几百个的文本分类任务，90%以上的准确率召回率依旧是一个很困难的事情。这里说的文本分类，指的是泛文本分类，包括query分类，广告分类，page分类，用户分类等，因为即使是用户分类，实际上也是对用户所属的文本标签，用户访问的文本网页做分类。

几乎所有的机器学习方法都可以用来做文本分类，常用的主要有：lr，maxent，svm等，下面介绍一下文本分类的pipeline以及注意点。

- 建立分类体系。

  - 分类相比于topic model或者聚类，一个显著的特点是：类目体系是确定的。而不像在聚类和LDA里，一个类被聚出来后，但这个类到底是描述什么的，或者这个类与另外的类是什么关系，这些是不确定的，这样会带来使用和优化上的困难。
  - 一般而言，类目体系是由人工设定的。而类目体系的建立往往需要耗费很多人工研究讨论，一方面由于知识面的限制，人工建立的类目体系可能不能覆盖所有情况；另一方面，还可能存在类目之间instance数的不平衡。比较好的方法，是基于目前已有的类目体系再做一些加工，譬如ODP，FreeBase等。
  - 还可以先用某种无监督的聚类方法，将训练文本划分到某些clusters，建立这些clusters与ODP类目体系的对应关系，然后人工review这些clusters，切分或者合并cluster，提炼name，再然后根据知识体系，建立层级的taxonomy。
  - 如果类目标签数目很多的话，我们一般会将类目标签按照一定的层次关系，建立类目树，如下图所示。那么接下来就可以利用层次分类器来做分类，先对第一层节点训练一个分类器，再对第二层训练n个分类器(n为第一层的节点个数)，依次类推。利用层次类目树，一方面单个模型更简单也更准确，另一方面可以避免类目标签之间的交叉影响，但如果上层分类有误差，误差将会向下传导。
    [![taxonomy](http://dataunion.org/wp-content/uploads/2015/02/taxonomy-300x165.png)](http://www.flickering.cn/wp-content/uploads/2015/01/taxonomy.png) 图21. 层次类目体系

- 获取训练数据

  - 一般需要人工标注训练数据。人工标注，准确率高，但标注工作量大，耗费人力。

  - 为了减少标注代价，利用无标记的样本，提出了半监督学习(Semi-supervised Learning)，主要考虑如何利用少量的标注样本和大量的未标注样本进行训练和分类的问题。这里介绍两种常见的半监督算法，希望了解更多请参考文献[49]。

    - Self-learning：两个样本集合，Labeled，Unlabeled。执行算法如下：

      - 用Labeled样本集合，生成分类策略F
      - 用F分类Unlabeled样本，计算误差
      - 选取Unlabeled中误差小的子集u，加入到Labeled集合。

      接着重复上述步骤。

      举一个例子：以前在做page分类器时，先对每一个类人工筛选一些特征词，然后根据这些特征词对亿级文本网页分类，再然后对每一个明确属于该类的网页提取更多的特征词，加入原有的特征词词表，再去做分类；中间再辅以一定的人工校验，这种方法做下来，效果还是不错的，更关键的是，如果发现那个类有badcase，可以人工根据badcase调整某个特征词的权重，简单粗暴又有效。

    - Co-training：其主要思想是：每次循环，从Labeled数据中训练出两个不同的分类器，然后用这两个分类器对Unlabeled中数据进行分类，把可信度最高的数据加入到Labeled中，继续循环直到U中没有数据或者达到循环最大次数。

    - 协同训练，例如Tri-train算法：使用三个分类器.对于一个无标签样本，如果其中两个分类器的判别一致，则将该样本进行标记，并将其纳入另一个分类器的训练样本；如此重复迭代，直至所有训练样本都被标记或者三个分类器不再有变化。

  - 半监督学习，随着训练不断进行，自动标记的示例中的噪音会不断积累，其负作用会越来越大。所以如term weighting工作里所述，还可以从其他用户反馈环节提取训练数据，类似于推荐中的隐式反馈。

  - 我们看一个具体的例子，在文献[45]中，twitter利用了三种方法，user-level priors（发布tweet的用户属于的领域），entity-level priors（话题，类似于微博中的#***#），url-level priors（tweet中的url）。利用上面三种数据基于一定规则获取到基本的训练数据，再通过Co-Training获取更多高质量的训练数据。上述获取到的都是正例数据，还需要负例样本。按照常见的方法，从非正例样本里随机抽取作为负例的方法，效果并不是好，文中用到了Pu-learning去获取高质量的负例样本，具体请参考文献[58]。
    [![training_data_acquisition](http://dataunion.org/wp-content/uploads/2015/02/training_data_acquisition1.png)](http://dataunion.org/wp-content/uploads/2015/02/training_data_acquisition1.png)图22.文献[45]训练数据获取流程图

- 特征提取

  - 对于每条instance，运用多种文本分析方法提取特征。常见特征有：
    - 分词 or 字的ngram，对词的权重打分，计算词的一些领域特征，又或者计算词向量，词的topic分布。
    - 文本串的特征，譬如sentence vector，sentence topic等。
  - 提取的特征，从取值类型看，有二值特征，浮点数特征，离线值特征。
  - 特征的预处理包括：
    - 一般来说，我们希望instance各维特征的均值为0，方差为1或者某个有边界的值。如果不是，最好将该维度上的取值做一个变换。
    - 特征缺失值和异常值的处理也需要额外注意。
  - 特征选择，下面这些指标都可以用作筛选区分度高的特征。
    - Gini-index: 一个特征的Gini-index越大，特征区分度越高。
    - 信息增益(Information Gain)
    - 互信息(Mutual Information)
    - 相关系数(Correlation)
    - 假设检验(Hypothesis Testing)

- 模型训练

  - - 模型选择：通常来说，常用的有监督模型已经足够了，譬如lr, svm, maxent, naive-bayes，决策树等。这些基本模型之间的效果差异不大，选择合适的即可。上一小节讲到cnn时，提到深度神经网络也可以用来做文本分类。深度神经网络相比较于传统方法，特征表示能力更强，还可以自学习特征。
    - 模型的正则化：一般来说，L1正则化有特征筛选的作用，用得相对较多，除此外，L2正则化，ElasticNet regularization(L1和L2的组合)也很常用。
    - 对于多分类问题，可以选择one-vs-all方法，也可以选择multinomial方法。两种选择各有各的优点，主要考虑有：并行训练multiple class model更复杂；不能重新训练 a subset of topics。
    - model fine-tuning。借鉴文献[72]的思路(训练深度神经网络时，先无监督逐层训练参数，再有监督调优)，对于文本分类也可以采用类似思路，譬如可以先基于自提取的大规模训练数据训练一个分类模型，再利用少量的有标注训练数据对原模型做调优。下面这个式子是新的loss function，w是新模型参数，w0是原模型参数，l(w,b|xi,yi)是新模型的likelihood，优化目标就是最小化“新模型参数与原模型参数的差 + 新模型的最大似然函数的负数 + 正则化项”。

  minw,bδ2||w−w0||22–1−δn∑i=1nl(w,b|xi,yi)+λ(α||w||1+1−α2||w||22)

  - model ensemble：也称“Multi-Model System”，ensemble是提升机器学习精度的有效手段，各种竞赛的冠军队伍的是必用手段。它的基本思想，充分利用不同模型的优势，取长补短，最后综合多个模型的结果。Ensemble可以设定一个目标函数(组合多个模型)，通过训练得到多个模型的组合参数(而不是简单的累加或者多数)。譬如在做广告分类时，可以利用maxent和决策树，分别基于广告title和描述，基于广告的landing page，基于广告图片训练6个分类模型。预测时可以通过ensemble的方法组合这6个模型的输出结果。

- 评测

  - 评测分类任务一般参考Accuracy，recall, precision，F1-measure，micro-recall/precision，macro-recall/precision等指标。