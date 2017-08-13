---
title: 词嵌入的直觉理解：从计数向量到 Word2Vec
date: 2017-08-13 23:02:11
tags: Word
category: 数据科学
---

原文：[An Intuitive Understanding of Word Embeddings: From Count Vectors to Word2Vec](https://www.analyticsvidhya.com/blog/2017/06/word-embeddings-count-word2veec/)

## Instruction

我们在开始之前，看看下面的例子：

1.你打开Google搜索一篇关于正在进行的冠军奖杯比赛的新闻文章，你会得到它返回的数以百计的搜索结果。

2.Nate Silver分析了数百万条推文，并在2008年美国总统选举中正确地预测出了50个州中的49个州的结果。

3.你可以在 Google翻译中用英语输入一个句子，并得到一个同义的中文转换。

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/06052154/collage.png)

那么上面的例子有什么共同点呢？

你可能已经猜对了 --- **文本处理**。 上述三种情景都是通过处理大量文本，以执行不同范围的任务，如在Google搜索示例中的聚类，第二个情景中的分类和第三个中的机器翻译。

人类可以非常直观地处理文本格式，但是如果在一天内把生成的数百万个文档提供给我们，我们就不能通过人类去执行上述三个任务。 这种方法既不能扩展又不高效。

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/06064148/joke-297x300.jpg)

由于我们知道在执行处理字符串、文本或者任何大量结果时通常是低效的，那么我们如何使今天的计算机在文本数据上执行聚类，分类等？

当然，电脑可以匹配两个字符串，并告诉你是否相同。 但是，当您搜索梅西（Messi）时，我们如何让电脑告诉您足球或罗纳尔多（Ronaldo）？ 如何让电脑了解“苹果是一种美味的水果（Apple is a tasty fruit）”中的“苹果”（Apple）是一种可以吃的水果而不是一家公司？

上述问题的答案在于为单词创建一个表示，用于捕捉他们的意义（*meanings*），语义关系（*semantic relationships*）和他们使用的不同类型的上下文。

并且所有的这些都是通过使用词嵌入或文本的数字表示来实现的，以便计算机可以处理它们。

下面我们将正式看到词嵌入及其不同类型，以及我们如何在实际中来实现它们来执行诸如返回高效的Google搜索结果等任务。

## 目录

1.什么是词嵌入？
2.不同类型的词嵌入方式
​	2.1基于频率计算的嵌入
​		2.1.1计数向量
​		2.1.2 TF-IDF
​		2.1.3同现矩阵
​	2.2基于预测的嵌入
​		2.2.1 CBOW模型
​		2.2.2 Skip-Gram模型
3.词嵌入的用例（使用此前如可以完成什么？例如：相似性，其他特殊的结果等）
4.使用预先训练的词向量
5.训练你自己的词向量
6.总结



### 1.什么是词嵌入？

狭义上，词嵌入是将文本转化为数字，并且相同文本可能用不同数字表示。 但是在我们深入了解词嵌入的细节之前，应该问下面的问题 - 为什么我们需要词嵌入？

事实证明，许多机器学习算法和几乎所有的深度学习框架都无法处理原始形式的字符串或普通文本。 广义上，他们需要数字作为输入，以执行任何类型的工作，无论是分类，回归等。 而且在具有文本格式存在的大量数据，必定要从中提取知识并构建应用程序，诸如一些现实世界的文本应用像Amazon评论的情感分析，Google的文档或新闻的分类或聚类等。

现在让我们正式定义词嵌入。 词嵌入通常会尝试使用字典将字词映射到向量。 让我们把这个句子分解成更精细的细节，以便有一个清晰的看法。

看看这个例子 - **sentence**（句子）=”Word Embeddings are Word converted into numbers”

这句话中的一个**word**(单词)可能是“Embeddings”或“numbers”等。

**dictionary**(字典)是句子中所有独一无二的词的列表。 所以，字典可能看起来像 - [‘Word’,’Embeddings’,’are’,’Converted’,’into’,’numbers’]

单词的**vector**(向量)表示可以是独热编码（one-hot encoded ）向量，其中1表示单词存在的位置，0代表不存在。 根据上述字典，该格式的“numbers”向量表示为[0,0,0,0,0,1]，" converted"为[0,0,0,1,0,0]。

这只是一个非常简单的方法来表示向量形式的单词。 我们来看看不同类型的词嵌入（或词向量化）及其优缺点。

### 2.不同类型的词嵌入

不同类型的词嵌入可以大致分为两类：

基于频率的词嵌入
基于预测的词嵌入
让我们尝试详细了解这些方法。



#### 2.1基于频率的词嵌入

在这个类别下，我们通常会遇到三种类型的向量。

- 计数向量
- 使用TF-IDF的向量
- 使用共生矩阵的向量

让我们详细研究这些向量化方法。

##### 2.1.1计数向量

设文档D的语料库C{d1，d2 ... ..dD}和从语料库C中提取的N个独特的标记（单词）。N个标记(token)将形成我们的字典，并且计数向量矩阵M的大小将由DX N给出。D（i）为 矩阵M中的每行包含文档中标记(token)的频率。

让我们用一个简单的例子来理解这个。

D1: He is a lazy boy. She is also lazy.

D2: Neeraj is a lazy person.

创建的字典可以是语料库中的具有唯一标记的单词：[‘He’,’She’,’lazy’,’boy’,’Neeraj’,’person’]

这里，D = 2，N = 6

大小为2×6的计数矩阵M将被表示为 -

![](https://ws3.sinaimg.cn/large/006tNc79ly1fgxtqaxbu2j30ct033q31.jpg)

现在，列也可以被理解为矩阵M中的对应单词的词向量。例如，上述矩阵中的“lazy”的词向量是[2,1]等等。这里的行对应于 语料库和列中的文档对应于字典中的标记。 上述矩阵中的第二行可以被读取为 - D2包含“lazy”：一次，“Neeraj”：一次和“person”一次。

现在在准备上述矩阵M时可能存在相当多的变化。这些变化将通常是在

1.字典的准备方式。
为什么呢？ 因为在现实世界的应用中，我们可能会有一个包含数百万个文档的语料库。 并且在数百万的文档中，我们可以提取数亿个独特的词。 所以基本上，上面准备的矩阵将是非常稀疏的，对于任何计算都是低效的。 所以使用每一个独特的单词作为字典元素的替代方法是根据频率来选择上一个万字，然后准备一个字典。
2.每个单词的计数方式。
我们可以采取频率（单词在文档中出现的次数）或存在（将文档中出现的单词？）作为计数矩阵M中的条目。但通常，频率方法优于后者。

下面是矩阵M的表示图像，以便于理解。

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/04164920/count-vector.png)

##### 2.1.2TF-IDF 向量化

这是基于频率方法的另一种方法，但它与计数向量化不同，在于它不仅考虑单个文档中的单词而是在整个语料库中的出现。那么这背后的理由是什么呢？让我们试着去了解一下。

一个对文档中像‘is’, ‘the’, ‘a’等常用单词往往要比很重要的单词频繁。例如，与其他文件相比，Lionel Messi的档件A将会包含更多的“Messi”一词。但是，几乎每个文档中，像“the”等这样的常用词也将以更高的频率存在。

理想情况下，我们想要的是减少几乎所有文件中都会出现的常见单词，并更加重视出现在文档子集中的其他单词。

TF-IDF通过对这些常用词进行降低权重来忽略他们同时重视特定文档中的像Messi等这样的词。

那么，TF-IDF究竟如何工作？

考虑下面的示例表，其给出了两个文档中的词项的计数（标记/单词）。

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/04171138/Tf-IDF.png)

现在我们来定义一些与TF-IDF相关的术语。

TF =（词项t在文档中出现的次数）/（在文档中的总词项数）

所以，TF（This，Document1）= 1/8

TF（This，Document2）= 1/5

它表示文字对文件的贡献，即与文件相关的词应该是频繁的。 例如：关于Messi的文件应该包含大量的“Messi”这个词。

IDF = log（N / n），其中，N是总文档数量，n是出现词项t的文档数量。

其中N是文档数量，n是术语t出现的文档数量。（原文档是不是排版错误）

所以，IDF（This）= log（2/2）= 0。

那么，我们如何解释IDF背后的原因呢？ 理想情况下，如果所有文档中都出现一个单词，那么这个词大概与特定文档无关。 但是如果它出现在文档的一个子集中，那么可能这个词与它所存在的文档有某些关联。

让我们计算“Messi”一词的IDF。

IDF(Messi) = log(2/1) = 0.301.

现在，我们将TF-IDF与一个通用单词“This”和似乎与文献1相关的“Messi”进行比较。

TF-IDF(This,Document1) = (1/8) * (0) = 0

TF-IDF(This, Document2) = (1/5) * (0) = 0

TF-IDF(Messi, Document1) = (4/8)*0.301 = 0.15

因为，您可以看到Document1，TF-IDF方法严重忽略“This”这个词，但是赋予“Messi”更大的权重。 所以，这可以被理解为“Messi”是整个语料库上下文在Document1中的重要词。

##### 2.1.3具有固定上下文边界（Context Window）的同现矩阵

大的思想（The Big Idea） - 类似的词汇往往会发生在一起，并将具有类似的上下文，例如 - 苹果是一个水果。 芒果是水果。
苹果和芒果往往具有类似的背景，即水果。

在深入了解如何构建同现矩阵的细节之前，有两个需要澄清的概念 - 同现和上下文 边界。

同现 - 对于给定的语料库，一对词的w1和w2 的共生是它们在上下文边界中一起出现的次数。

上下文边界 - 上下文边界由数字和方向指定。 那么2（周围）的上下文边界是什么意思？ 下面我们来看一个例子，

![](https://ws4.sinaimg.cn/large/006tNc79ly1fgxtw4epz5j30ey018wej.jpg)

绿色单词是“Fox”一词的2（周围）上下文边界，并且为了计算共现，只会计算这些单词。 让我们看看“Over”这个词的上下文边界。

![](https://ws4.sinaimg.cn/large/006tNc79ly1fgxtwmtvw7j30ev01dwej.jpg)

现在我们来举个例子来计算一个同现矩阵。

语料库 = He is not lazy. He is intelligent. He is smart.

![](https://ws3.sinaimg.cn/large/006tNc79ly1fgxtxf3r0yj30eq06s3z0.jpg)

让我们通过看到上表中的两个例子来理解这个同现矩阵。 红色和蓝色框。

红色框 - 在上下文边界2中出现了“He”和“is”的次数，可以看出，这个数字是4。下表将帮助您显示计数。

![](https://ws2.sinaimg.cn/large/006tNc79ly1fgxtxz7hswj30jd058gm9.jpg)

而“Lazy”一词在上下文边界中从未出现过“intelligent”，因此在蓝盒中已被赋值为0。

**同现矩阵的变化**

假设语料库中有V个独特的词。所以词汇表大小= V。同现矩阵的列形成上下文单词。同现矩阵的不同变化是 - 

1.大小V X V的同现矩阵。现在，对一个正规的语料库V变得非常大，这将难以处理。因此，一般来说，这种框架在实践中不是首选。
2.大小为V×N的同现矩阵，其中N是V的子集，并且可以通过例如去除诸如无效词等的不相关词来获得。这仍然是非常大的并且存在计算困难。
但是，请记住，这种同现矩阵通常不用于词向量表示。相反，该同现矩阵使用诸如PCA，SVD等技术被分解成因子，并且这些因子的组合形成了词向量的表示。

让我更清楚地说明这一点。例如，您在上述VXV大小的矩阵上执行PCA。您将获得V个主要组件。您可以从这些V个组件中选择k个组件。所以，新的矩阵将是V X k的形式。

而且，一个单词，将被表示为k维而不是V 维，同时仍然能捕捉几乎相同的语义信息。 k通常是数百的数量级。

那么PCA在后面要做的是将同现矩阵分解为三个矩阵U，S和V，其中U和V都是正交矩阵。重要的是U和S的点积给出了词向量的表示，V给出了单词上下文的表示。

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/04224842/svd2.png)

**同现矩阵的优点**

1.它保留了词之间的语义关系。 例如男人和女人之前的关系往往比男人和苹果更接近。
2.它在其核心使用SVD，它产生的词项量表示要比现有方法更准确。
3.它使用的分解是一个已经明确定义的问题并且可以有效地解决。
4.它只需被计算一次，并且之后就可以随时使用。 在这个意义上，它比其他的快。

**同现矩阵的缺点**

1.它需要巨大的内存来存储同现矩阵。
但是，例如在Hadoop集群将矩阵从系统中分解出来等可以避免这个问题，并且可以被保存。

#### 2.2基于预测的词嵌入

**先决条件**：本部分假设您了解神经网络工作原理的知识以及神经网络中权重更新的机制。如果您是神经网络的新人，我建议您通过Sunil的[这篇令人敬畏的文章](https://www.analyticsvidhya.com/blog/2017/05/neural-network-from-scratch-in-python-and-r/)，了解神经网络的工作原理。

到目前为止，我们已经看到确定性的方法来确定词向量。但是，这些方法已经被证明在他们的词表示中会受到限制，直到Mitolov等人将word2vec引入NLP社区。这些方法是基于某些意义上的预测，如它们为单词提供概率，这些方法并被证明是处理像词类比和词相似性等任务的最新技术。他们也能够实现像King -man + women= Queen的任务，这被认为是几乎神奇的结果。所以让我们来看一下今天使用的word2vec模型来生成单词向量。

Word2vec不是一个单一的算法，而是两种技术的组合 - CBOW（连续的词袋）和Skip-gram模型。这两个都是浅层神经网络，它也是将单词映射到一个目标变量。这两种技术都学习了用词向量表示的权重。让我们分开讨论这两种方法，并获得深入理解他们的工作。

 

##### 2.2.1 CBOW（连续的词袋）

CBOW的工作方式是倾向于在给定上下文情况下预测单词的概率。上下文可以是单个单词或一组单词。但为了简单起见，我将采用单个的上下文单词，并尝试预测单个目标词。

假设我们有一个语料库C =“Hey, this is sample corpus using only one context word”，并且我们定义了一个上下文边界1.该语料库可以转换为如下CBOW模型的训练集合。输入如下所示。下图中右侧的矩阵包含从左侧输入的独热编码。

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/04205949/cbow1.png)

使用单个数据点的目标表示数据点4如下所示

![](https://ws2.sinaimg.cn/large/006tNc79ly1fgxu3bnn87j30ik02bweo.jpg) 

将上述图像中所示的矩阵发送到具有三层的浅层神经网络：输入层，隐藏层和输出层。输出层是一个softmax层，它用于将输出层中获得的概率求和为1.现在让我们看看正向传播如何用于计算隐藏层激活。

我们首先看看CBOW模型的图解表示。

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/04224109/Screenshot-from-2017-06-04-22-40-29.png)

用单个数据点表示上述图像的矩阵如下。

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/04222108/Screenshot-from-2017-06-04-22-19-202.png)

流程如下：

1. 输入层和目标都是大小为[1 X V]的独热编码。这里在上述示例中V = 10。
2. 有两个权重集。一个是在输入层和隐藏层之间，第二个在隐藏层和输出层之间。
   输入-隐藏层矩阵大小= [V X N]，隐藏 - 输出层矩阵大小= [N X V]：其中N是我们选择代表我们的单词的维数。它是神经网络的任意的超参数。此外，N是隐藏层中的神经元数量。这里，N = 4。
3. 任何层之间都没有激活功能（我的意思是它不是线性激活）
4. 输入被乘以输入-隐藏层权重，并称为隐藏激活。它只是复制输入-隐藏层矩阵中的相应行。
5. 隐藏层输入乘以隐藏层输出的权重并计算输出。
6. 输出和目标之间的误差被计算出来并传播回来重新调整权重。
7. 隐藏层和输出层之间的权重取为单词的词向量表示。

我们看到上述步骤是为单个上下文单词的情况。现在，如果我们有多个上下文单词呢？下面的图片描述了多个上下文单词的架构。

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/04220606/Screenshot-from-2017-06-04-22-05-44-261x300.png)

以下是上述架构的矩阵表示，以便于理解。

![img](./Intuitive Understanding of Word Embeddings_ Count Vectors to Word2Vec_files/Screenshot-from-2017-06-04-22-14-311.png)

上图需要3个上下文单词，然后预测目标单词的概率。可以将输入假设为从输入层中去三个读热编码向量，如上所示为红色，蓝色和绿色。

因此，输入层将在输入中具有3个 [1 X V]矢量，如上所示，输出层中有1个 [1 XV]。架构的其余部分与单上下文单词的CBOW相同。

步骤保持不变，只有隐藏激活的计算更发生了变化。不是将输入-隐藏的权重矩阵的相应行复制到隐藏层，而是取矩阵的所有相应行的平均值。我们可以用上图来理解。计算的平均向量成为隐藏激活。因此，如果我们对单个目标词处理需要三个上下文单词，那么我们将有三个初始隐藏激活，然后对元素进行平均得到最终激活。

在单个上下文单词和多个上下文单词中，因为CBOW与简单MLP网络不同，我已经展示了直到隐藏激活的计算的图像。隐藏层计算后的步骤与本文所述MLP的步骤相同 - [从头开始理解和编码神经网络](https://www.analyticsvidhya.com/blog/2017/05/neural-network-from-scratch-in-python-and-r/)。

下文澄清MLP和CBOW之间的差异：

1. MLP中的目标函数是一个MSE（均方差），而在CBOW中，给定一组上下文（即-log（p（wo / wi））的单词的负对数似然，其中给出了p（wo / wi）如

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/04230048/AAEAAQAAAAAAAA18AAAAJGNkMGYxMDIxLWY5NjgtNGEzMy1hMjAyLWU4MmI4ZWUwNDNhYw-300x91.jpg)

wo：输出单词
wi：上下文单词

相对于隐藏-输出的权重，输入-隐藏权重的误差梯度是不同的，因为MLP具有S形激活（通常），但CBOW具有线性激活。然而，计算梯度的方法与MLP相同。

 

**CBOW的优势：**

1. 概率是自然的，它应该优于确定性方法（一般）。
2. 耗费内存低。 它不需要像共生矩阵那样需要存储三个巨大的矩阵的巨大的RAM要求。

**CBOW的缺点：**

1. CBOW取一个单词的上下文的平均值（如上面在隐藏-激活的计算中所见）。例如，苹果可以是一个水果和一个公司，但是CBOW只能在一个水果的集群和公司的集群之间进行平均的上下文的分析。
2. 如果不适当优化，要从头开始训练CBOW。

##### 2.2.2 Skip - Gram模型

Skip - gram遵循与CBOW相同的拓扑。它只是颠覆了CBOW的架构。skip-gram的目的是预测给定一个单词的上下文。让我们对同样的语料库C=”Hey, this is sample corpus using only one context word.”建立我们的CBOW模型。接下来我们来构建训练数据。

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/04235354/Capture1-300x222.png)

Skip - Gram的输入向量将与单上下文单词的CBOW模型相似。此外，隐藏激活的计算将是相同的。差异是在目标变量中。由于我们已经在两边定义了一个单个上下文单词的边界，所以在图像的蓝色部分中可以看到“ **“2”个独热编码的目标变量**和“ **“2”个对应的输出**。

对于两个目标变量计算出两个单独的误差，并且获得的两个误差向量也被逐个地添加以获得最终误差向量，这里使用了向后传播。

输入和隐藏层之间的权重作为训练后的词向量的表示。损失函数或目标函数与CBOW模型类型相同。

 Skip-Gram架构如下所示。

![](file:///Users/idejie/Downloads/005/Intuitive%20Understanding%20of%20Word%20Embeddings_%20Count%20Vectors%20to%20Word2Vec_files/Capture2-276x300.png)

 

为了更好的理解，计算的矩阵样式结构如下所示。

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/05122225/skip.png)

 

让我们分解上面的图像。

输入层大小 - [1 X V]，输入-隐藏权重矩阵大小 - [VXN]，隐层中的神经元数量N，隐藏 - 输出权重矩阵大小 - [N X V]，输出层大小 - C [1 XV]

在上述例子中，C是上下文单词的数量= 2，V = 10，N = 4

1. 红色的行是对应于输入独热编码向量的隐藏激活。它基本上是对应的输入隐藏矩阵行。
2. 黄色矩阵是隐层和输出层之间的权重。
3. 蓝色矩阵通过隐藏激活和隐藏输出权重的矩阵乘法获得。将为两个目标单词（上下文）计算两行。
4. 将蓝色矩阵的每一行分别转换成其softmax概率，如绿色框所示。
5. 灰色矩阵包含两个上下文单词（目标）的独热编码向量。
6. 通过从绿色矩阵（输出）的第一行逐元素的减去灰色矩阵（目标）的第一行元素来计算错误。下一行重复这一步。因此，对于**n个 **目标语境单词，我们将有**n个**错误向量。
7. 对所有误差向量进行元素和求和以获得最终误差向量。
8. 该错误向量被传播回来以更新权重。

**Skip-Gram模型的优点**

1. Skip-gram模型可以捕获单个单词的两个语义。即它将苹果用两个向量表示。一个为公司和一个为水果。
2. 一般来说，采用负因子采样的跳过优于其他方法。

[这](http://bit.ly/wevi-online)  是一个优秀的交互式工具，可视化的 CBOW和skip-gram 的动作。我建议你真正阅读这个链接，以便更好地了解。

### **3.词嵌入的用例场景**

由于词嵌入或词向量化是单词之间的上下文相似性的数值表示，因此可以对其进行操纵并执行令人惊奇的任务，如 -

1. 找出两个词之间的相似度。
   `model.similarity('woman','man')`
   `0.73723527`
2. 找出奇怪的一个。
   `model.doesnt_match('breakfast cereal dinner lunch';.split())`
   `'cereal'`
3. 惊人的东西，像womam+king=queen
   `model.most_similar(positive=['woman','king'],negative=['man'],topn=1)`
   `queen: 0.508`
4. 在模型下计算文本的概率
   `model.score(['The fox jumped over the lazy dog'.split()])`
   `0.21`

以下是word2vec的一个有趣的可视化。

![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/05003425/graph1-300x277.jpg)

上述图像是t-SNE的2维词向量表示，您可以看到苹果的两个上下文已被捕获。一个是水果，另一个是公司。

5.可用于执行机器翻译。
![](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/06/05003807/ml-300x211.png)

上图是双语词向量中文为绿色和英文为黄色。如果我们知道汉语和英语具有相似意义的词，上述双语向量化可用于将一种语言翻译成另一种语言。

 

### 4.使用预先训练的词向量

我们将使用谷歌的预训练模型。它包含字词向量，用于从谷歌新闻数据集大约1000亿字节训练的300万个词汇的词汇。这个模型的downlaod链接是[这样的](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit)。当心这是一个1.5 GB的下载。

```python
from gensim.models import Word2Vec

#loading the downloaded model
model = Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True, norm_only=True)

#the model is loaded. It can be used to perform all of the tasks mentioned above.

# getting word vectors of a word
dog = model['dog']

#performing king queen magic
print(model.most_similar(positive=['woman', 'king'], negative=['man']))

#picking odd one out
print(model.doesnt_match("breakfast cereal dinner lunch".split()))

#printing similarity index
print(model.similarity('woman', 'man'))
```

### 5.训练你自己的词向量

我们将在自定义语料库上训练我们自己的word2vec。对于训练模型，我们将使用gensim，步骤如下图所示。

word2Vec要求列出列表中每个文档包含在列表中的列表格式，每个列表都包含该文档的标记列表。我不会在这里覆盖预处理的部分。所以我们来列举列表来训练我们的word2vec模型。

sentence= [[‘Neeraj’,’Boy’],[‘Sarwan’,’is’],[‘good’,’boy’]]

```python
#training word2vec on 3 sentences
model = gensim.models.Word2Vec(sentence, min_count=1,size=300,workers=4)
```

让我们尝试了解这个模型的参数。

sentence - 我们的语料库列表
min_count = 1 - 词的阈值。频率大于此值的词将被包含在模型中。
size = 300 - 我们希望它代表我们的单词的维度数。这是词向量的大小。
worker = 4 - 用于并行化

```python
#using the model
#The new trained model can be used similar to the pre-trained ones.

#printing similarity index
print(model.similarity('woman', 'man'))
```

### 6.总结

词嵌入是一个活跃的试图找出比现有的更好的词表示的研究领域。但随着时间的推移，数量越来越多，复杂程度越来越大。本文旨在简化这些嵌入模型的一些工作，而不会带来数学方面的开销。如果你觉得我能够化解你的一些困惑，请在下面评论。欢迎任何变更或建议。