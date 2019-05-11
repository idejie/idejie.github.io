---
title: 《现代信息检索》复习
date: 2018-11-25 01:30:20
tags: 课程学习
category: 信息检索
---

>目前进度：20/20



>未经允许，不得转载或其他使用。
>
>如有问题，请联系[本文作者](mailto:i@idejie.com)



![](https://blog.idejie.com/pics/ir-review0.gif)

## 0-Introduction

### (1)什么是信息检索

①首先，互联网大部分应用（搜索引擎、在线购物、婚恋网站）所共同具有的特征：

- 给定需求(或者是对象)，从信息库中找出与之最匹配的信息(或对象)，如在Google中搜“信息检索”应该返回相关的研究网站和书籍，在Amazon上搜“天王表”应该返回手表……
- 不同场景下的“匹配”定义不同。如，你在网上买了微波炉之后，再给你推荐的不应该还是微波炉了；微博推荐好友时，不应该向你老婆推荐前女友了……
- 返回的数据形式都是以结构化的数据和无固定结构的自由文本。

②然后，信息检索就是要满足上述需求的一门技术和学科。

- 给定用户需求返回满足该需求信息的一门学科。通常涉及信息的获取、存储、组织和访问。
- 从大规模非结构化数据(通常是文本)的集合(通常保存在计算机上)中找出满足用户信息需求的资料(通常是文档)的过程。
- “找对象”的学科，即定义并计算某种匹配“相似度”的学科。

③信息检索应用广泛，如搜索引擎、推荐系统、舆情分析 、情报分析、数据挖掘、内容安全等等。

④信息检索分类。

- 从规模上
  - 个人信息检索：个人相关信息的组织、整理、搜索等。桌面搜索(Desktop Search)、个人信息管理(PIM = Personal Information Management)、个人数字记忆(Personal Digital Memory)
  - 企业级信息检索：在企业内容文档的组织、管理、搜索等。企业级信息检索是内容管理(Content Management)的重要组成部分。局域网/内网搜索
  - Web信息检索：在超大规模数据集上的检索。

### (2)为什么要信息检索

①市场发展的需求

- 用户(国家、企业、个人等)需要信息检索技术：互联网的信息量太大、噪音太多，寻找所需要的信息非常不容易
- 公司需要信息检索技术：
- - 搜索引擎改变了很多传统的生活方式，Yahoo、Google、Baidu，还有一些公司如Microsoft、Sina、Sohu、Tencent、Netease、360、Facebook都加入到这个搜索技术的竞争。
  - 目前搜索引擎公司甚至整个互联网正常运转的计算广告的核心技术是信息检索技术
  - 不只是搜索引擎才需要信息检索技术，电子商务(如亚马逊网站、淘宝等)、社交网(微博、Facebook、twitter、校内网)、数字图书馆、大规模数据分析(金融证券行业等)等都需要信息检索技术
  - 人才的竞争：搜索相关人才人数出现缺口，他们非常抢手，待遇如日中天
  - 是不是泡沫：2000年左右出现的网络泡沫和现在的互联网有什么不同，搜索引擎在其中占什么位置？

②众多应用的需求

- 移动搜索
- 产品搜索
- 专利搜索
- 广告推荐
- 社会网络分析
- 消费行为分析
- 网络评论分析
- SEO营销
- ……

### (3)信息检索的三个层次

①应用层次：搜索是一项非常重要的应用！（搜索引擎）

②中间层次：搜索是极其重要的API（站内检索，内容检索，数据分析）

③核心层次：搜索是未来操作系统的重要组成部分！

![](https://blog.idejie.com/pics/ir-review0.gif)

## 1-Boolean Retrieval

### (1)信息检索概述

①**信息检索**是从大规模非结构化数据(通常是文本)的集合 (通常保存在计算机上)中找出满足用户信息需求的资料 (通常是文档)的过程。 

②特点：文档（结构化、半结构化、非结构化）、信息需求、文档集合语料库

③主要应用：**文本检索**

④数据：

i. IR vs数据库: 结构化 vs ⾮非结构化数据(结构化数据即指“表”中的数据,数据库常常支持范围或者精确匹配查询 。e.g.,Salary < 60000 AND Manager = Smith.)

ii. ⾮非结构化数据:通常指自由文本(free text),允许关键词加上操作符号的查询(奥运会AND游泳),允许更加复杂的概念性的查询找(出所有的有关药物滥用(drug abuse)的网页);经典的检索模型一般都针对自由文本进行处理

iii. 半结构化数据:没有数据是完全无结构的，比如网页就是一种半结构化数据.半结构化查询( Title contains data AND Bullets contain search) 严格来说，即使是文本也是有“语言”结构, 比如主谓宾结构 

⑤传统信息检索 vs. 现代信息检索：

- 传统信息检索主要关注非结构化、半结构化数据 
- 现代信息检索中也处理结构化数据 

⑥布尔检索

针对布尔查询的检索，布尔查询是指利用 AND,OR 或者 NOT操作符将词项 连接起来的查询

### (2)倒排索引

①《莎士比亚全集》查找一个布尔表达式的结果

- 暴力方法：从头到尾查
  - 优点：方法简单；支持文档的动态变化
  - 缺点：慢；不容易处理not；不支持其他操作（近义词）；不支持排序
- 词项-文档的关联矩阵：行（人名）在列（章节）是否出现，是为1，反之为0
  - 能够对布尔表达式进行向量运算

②信息检索的基本假设：

- 文档集（Collection）：由固定数量的文档组成（不变）

- 目标：返回与用户需求相关的文档并辅助用户来完成某项任务

- 相关性：

  - 主观的概念
  - 反映对象的匹配程度
  - 不同应用的相关性不同

- 典型的搜索过程：

  ![](https://blog.idejie.com/pics/ir-review2.jpg)

- 检索效果的评价

  - 正确率（Precision）：返回中正确结果占返回结果的比例。
  - 召回率（Recall）：返回中正确结果占所有正确结果的比例。
  - 二者缺一不可：
    - 全部返回，正确率低，召回率100%
    - 只返回一个正确结果，正确率100%，召回率低

③倒排索引

- 场景：词项-文档矩阵非常大，而且是非常稀疏的矩阵，如何检索

- 通常采用变长表方式 

  ▪ 磁盘上，顺序存储方式比较好，便于快速读取 

  ▪ 内存中，采用链表或者可变长数组方式 

  ![](https://blog.idejie.com/pics/ir-review3.jpg)

- 倒排索引的构建

![](https://blog.idejie.com/pics/ir-review4.jpg)

- 索引构建过程

  - 构建词条序列：<词条，docID>二元组

  - 排序：按词项排序，然后每个词项按docID排序 

  - 合并：某个词项在单篇文档出现多次会被合并

  - 拆分：拆分成词典和倒排记录表两部分

  - 最终：<（词项，频率），docIDs>

    ![](https://blog.idejie.com/pics/ir-review5.jpg)

### (3)布尔查询处理

- 场景：如何用倒排索引来处理查询

- AND：

  - 在索引中定位A，返回A的倒排记录表
  - 在索引中定位B，返回B的倒排记录表
  - Merge两个倒排记录表，求交集

- Merge的方法

  - 线性搜索法：每个倒排记录表都有一个定位指针，两个指针同时从前往后扫描, 每次比较当前指针对应倒排记录，然后移动某个或两个指针。合并时间为两个表长之和的线性时间

  - 调表指针法：

    ![](https://blog.idejie.com/pics/ir-review6.jpg)

    查询52时，直接先查2处，比2和41都大，那就要调到41处再往后查48，64

    **调表指针的位置：**

    - 简单的启发式策略：对于长度为$L$的倒排记录表，每$ \sqrt L$ 处放一个跳表指针，即均匀放置。均匀放置方法忽略了查询词项的分布情况
      - 如果索引相对静态，均匀方式方法是一种很简便的方法，但是如果索引经常更新造成L经常变化，均匀方式方式就很不方便
      - 跳表方式在过去肯定是有用的，但是对于现代的硬件设备而言，如果合并的倒排记录表不能全部放入内存的话，上述方式不一定有用,更大的倒排记录表(含跳表)的 I/O开销可能远远超过内存中合并带来的好处

- 查询优化

  - 按照表从小到大合并（这也是为什么倒排索引要按DF排序的原因）
  - 转换成合取范式，获得每个词项的df，将词项相加，估计每个or表达式对应的大小，再从大到小处理or

- 优点

  - 构建过程简单

- 缺点

  - 布尔查询构建复杂，不适合普通用户。构建不当，检索结果过多或者过少
  - 没有充分利用词项的频率信息，通常出现的越多越好，需要利用词项在文档中的词项频率(term frequency, tf)信息
  - 不能对检索结果进行排序

![](https://blog.idejie.com/pics/ir-review0.gif)

## 2-Dictionary

### （1）文档

- 确定文档的格式：额外的转换过程（&amp；）
- 文档的编码方式：多语言并存（该判断过程看成一个基于机器学习的分类问题 1(我们将在第 13
  章讨论)来处理，但在实际中往往通过启发式方法来实现，也可以利用文档的元信息或者直接
  由用户手工选择来确定。）
  - 字符序列化：不一定线性
- 文档单位选择：
  - 如果索引粒度太小，那么由于词项散布在多个细粒度文档中，我们就很可能错过那些重要的段落，也就是说此时正确率高而召回率低;反之，如果索引粒度太大，我们就很可能找到很多不相关的匹配结果，即正确率低而召回率高
  - 索引粒度过大造成的问题也可以通过采用显式或隐式的邻近搜索方法来缓解

### （2）词条

- 词条化：
  - 在这个过程中，可能会同时去掉一些特殊字符，如标点符号等。![](https://blog.idejie.com/pics/ir-review8.jpg)
  - 词条：在文档中出现的字符序列的一个实例
  - 词条类：相同词条构成的集合
  - 词项：在信息检索系统词典中所包含的某个可能经过归一化处理的词条类
  - to sleep perchance to dream：五个词条、4个词条类、3个词项（停用词to会被去掉）
  - 词条化的主要任务就是确定哪些才是正确的词条，际上即使对于单词之间存在空格的英文来说也存在很多难以处理的问题。比如，英文中的上撇号“ ’” 既可以代表所有关系也可以代表缩写
    - 一个非常简单的做法就是在既非字母也非数字的字符处进行拆分（并不好）
    - 词条化处理往往与语言本身有关，不同语言下的词条化处理并不相同。很多语言的分词方法不通用，歧义。
  - 问题
    - 多语言分词
    - 单个语言里面，索引单位的选择，一个字？一个词 ？怎么确定词（歧义，多种分割）？
    - 重音符/时间格式
    - 大小写
  - 中文分词：是否使用词典；是否基于规则或者 统计的方法
    - 正向最大匹配；逆向最大匹配的方法
    - 问题：新词，歧义（两种多种分法）
    - 解决歧义和未登录词识别的基本方法:
    - - 规则方法：分词过程中或者分词结束后根据规则进行处理；
      - 统计方法：分词过程中或者分词结束后根据统计训练信息进行处理。
      - 规则+统计
    - 结论：
      - 并非分词精度高一定检索精度高
      - 检索中的分词，查询和文档都分词
      - 搜索引擎中的分词方法
      - - 猜想：大词典+统计+启发式规则
- 去停用词
  - 一个常用的生成停用词表的方法就是将词项按照文档集频率(collection frequency，每个词项在文档集中出现的频率)从高到低排列，然后手工选择那些语义内容与文档主题关系不大的高频词作为停用词。
- 词项归一化
  - 词条归一化(token normalization)就是将看起来不完全一致的多个词条归纳成一个等价类，以便在它们之间进行匹配的过程 1。最常规的做法是隐式地建立等价类 2，每类可以用其中的某个元素来命名。
  - 问题：
    - 重音及变音符号问题。
    - 大小写转换问题。
    - 英语中的其他问题。colour color（拼写错误：soundex）
    - 其他语言的问题。
- 词干还原和词形归并
  - 词干还原(stemming)和词形归并(lemmatization)这两个术语所代表的意义是不同的。前者通常指的是一个很粗略的**去除单词两端词缀**的启发式过程，并且希望大部分时间它 都能达到这个正确目的，这个过程也常常包括去除派生词缀。而词形归并通常指利用词汇表和 词形分析来去除**屈折**（？）词缀，从而返回词的原形或词典中的词的过程，返回的结果称为词元 (lemma)。 
  - Porter 算法

### （3）跳表

- 基于跳表的倒排记录表快速合并算法
  - 跳表指针只对 AND 类型的查询有用
  - 如果索引相对固定的话，建立有效的跳表指针则比较容易。
- 含位置信息的倒排记录表及短语查询
  - 二元词索引：将每个接续词对看成词项，这样马上就能处理两个词构成的短语查询，更长的查询可以分成多个短查询来处理 。用名词和名词短语来表述用户所查询的概念具有相当特殊的地位
    - the abolition of slavery       renegotiation of the constitution
      - 对文本进行词条化
      - 词性标注
      - 将形式为NX*N非词项序列看成一个扩展的二元词
    - 二元词索引的概念可以扩展到更长的词序列，如果索引中包含变长的词序列，通常就称为**短语索引**
  - 位置索引：不只是简单地判断两个词项是否出现在同一文档中，而且还需要检查它们出现的位置关系和查询短语的一致性。这就需要计算出词之间的偏移距离。（距离跳远不是词组）
  - 混合索引机制：对某些查询使用短语索引或只使用二元词索引，而对其他短语查询则采用位置索引。短语索引所收录的那些较好的查询可以根据用户最近的访问行为日志统计得到，也就是说，它们往往是那些高频常见的查询。当然，这并不是唯一的准则。处理开销最大的短语查询往往是这样一些短语，它们中的每个词都非常常见，但是组合起来却相对很少见 

![](https://blog.idejie.com/pics/ir-review0.gif)

## 3-Tolerant Retrieval

### （1）词典搜索的数据结构

- 区分：
  - 倒排索引：词典+倒排记录表
  - 词典是指存储词项词汇表的数据结构
  - 词项词汇表(Term vocabulary): 指的是具体数据
  - 词典(Dictionary): 指的是数据结构
- 形式：
  - 定长数组：空间消耗大
  - 用于词项定位的即查词典：哈希表、树
- 采用哈希表或树的准则:
  - 词项数目是否固定或者说词项数目是否持续增长？
  - 词项的相对访问频率如何？
  - 词项的数目有多少？
- 哈希表：
  - 每个词项通过哈希函数映射成一个整数，尽可能避免冲突，查询处理时： 对查询词项进行哈希，如果有冲突，则解决冲突，最后在定长数组中定位
  - 优点: 
    - 在哈希表中的定位速度快于树中的定位速度，查询时间是常数
  - 缺点：
    - 无法处理词项的微小变形 (resume vs. résumé)
    - 不支持前缀搜索 (比如所有以automat开头的词项)
    - 如果词汇表不断增大，需要定期对所有词项重新哈希
- 树：
  - 树可以支持前缀查找(相当于对词典再建一层索引)
  - 最简单的树结构：二叉树
  - 搜索速度略低于哈希表方式： O(logM), 其中 M 是词汇表大小，即所有词项的数目O(logM) 仅仅对平衡树成，使二叉树重新保持平衡开销很大
  - B-树 能够减轻上述问题
    B-树定义：每个内部节点的子节点数目在 [a, b]之间，其中 a, b 为合适的正整数, e.g., [2, 4].

### （2）通配查询

- 找出所有某个前缀开头的单词或者某个后缀结尾的单词

- 这个时候比较适合用树（B树）

  ![](https://blog.idejie.com/pics/ir-review10.jpg)

- 词项中间的 *号处理：轮排索引

- 轮排索引的基本思想：

  - 将每个通配查询旋转，使*出现在末尾
  - 将每个旋转后的结果存放在词典中，即B-树中

- 轮排索引的一个示例：

  ![](https://blog.idejie.com/pics/ir-review11.jpg)

- 查找过程：

- - 将查询进行旋转，将通配符旋转到右部

- - 同以往一样查找B-树，得到匹配的所有词项，将这些词项对应的倒排记录表取出

- - 问题：相对于通常的B-树，轮排索引(轮排树)的空间要大4倍以上 (经验值)

- 为了解决轮排索引空间大的问题，又出现了**k-gram**

- k-gram

  - 需要注意的是，这里有两个倒排索引：词项-文档、**k-gram**-词项![](https://blog.idejie.com/pics/ir-review12.jpg)

  - 这个时候就需要把通配查询转换成布尔查询了

    ![](https://blog.idejie.com/pics/ir-review13.jpg)

- k-gram索引 vs. 轮排索引

  - k-gram索引的空间消耗小
  - 轮排索引不需要进行后过滤

- 问题: 为什么Google对通配查询并不充分支持？

```
问题 1: 一条通配符查询往往相当于执行非常多的布尔查询
对于 [gen* universit*]: geneva university OR geneva université OR genève university OR genève université OR general universities OR . . .
开销非常大

问题 2: 用户不愿意敲击更多的键盘
如果允许[pyth* theo*]代替 [pythagoras’ theorem]的话，用户会倾向于使用前者
这样会大大加重搜索引擎的负担
Google Suggest是一种减轻用户输入负担的好方法
```

### （3）编辑距离

- 主要用途是拼写校正（纠正文档【一般不会这么做】、纠正用户查询）

- 拼写校正的方法：

  - 词独立(Isolated word)法

    - 只检查每个单词本身的拼写错误
    - 如果某个单词拼写错误后变成另外一个单词，则无法查出, e.g., an asteroid that fell form the sky

    上下文敏感(Context-sensitive)法

    - 纠错时要考虑周围的单词
    - 能纠正上例中的错误 form/from

- 编辑距离属于词独立法

- 简单的词独立法：根据词汇表

- 复杂的就是：编辑距离法、k-gram重叠率

- 编辑距离

  - Levenshtein距离: 采用的基本操作是插入(insert)、删除(delete)和替换(replace)
  - Damerau-Levenshtein距离：除了上述三种基本操作外，还包括两个字符之间的交换（transposition）操作
  - 带权重的编辑距离：比如键盘上，相比起p错写为q的代价要高于错写成o

- k-gram

  - 例子：采用2-gram索引, 错误拼写的单词为bordroom     2-gram: *bo, or, rd, dr, ro, oo, om*
  - ![](https://blog.idejie.com/pics/ir-review14.jpg)

- 基于上下文的

  - 一种方法: 基于命中数(hit-based) 的拼写校正![](https://blog.idejie.com/pics/ir-review15.jpg)

  - 从查询库(比如历史查询)中搜索而不是从文档库中搜索（大家经常写错的一个库）

    ![](https://blog.idejie.com/pics/ir-review16.jpg)

- ![](https://blog.idejie.com/pics/ir-review17.jpg)

- Peter-Noring工具

  对用户输入的单词进行编辑距离≤2的变换，包括插入、删除、修改以及它们的组合操作，这样我们就得到了若干个与原始输入编辑距离≤2的字符串，然后分别用它们在字典中进行查询。

  这个方法虽然比朴素的拼写校正算法好了许多，但仍然有很高的复杂度，而且与具体的语言相关。例如在英语中只有26个字母，变换得到字符串个数还不是很多。而汉语有几千个常用字，这种方法就不可行了。

### （4）soundex

- Soundex是寻找发音相似的单词的方法
- 具体算法:
  - 将词典中每个词项转换成一个4字符缩减形式
- 对查询词项做同样的处理
- 基于4-字符缩减形式进行索引和搜索

![](https://blog.idejie.com/pics/ir-review18.jpg)

![](https://blog.idejie.com/pics/ir-review19.jpg)

![](https://blog.idejie.com/pics/ir-review0.gif)

## 4-Index Construction

（2，3，4，5，6参考[csdn-xiazdong](https://www.cnblogs.com/xiazdong/archive/2012/01/06/3058356.html)）

### （1）硬件基础

- 内存比硬盘对文件读写快，尽量用硬盘
- 磁盘不光文件读写慢，切换时也慢，需要磁头寻道
- 所以相对于多个小文件，不如一个大文件读的快
- 硬盘缓存：缓存是硬盘与外部总线交换数据的场所，近期频繁访问的数据会自动存放在缓存中，从缓存读取数据无需磁头定位。硬盘缓存通常都不大，例如64MB
- 容错处理的代价非常昂贵：采用多台普通机器会比一台提供容错的机器的价格更便宜

### （2）基于块的排序索引方法

- BSBI

  (1)把整个文档集分成大小相同的部分（每个部分正好是一个块大小）并放入内存；

  (2)把每个部分解析成词项ID->文档ID对；(我们为了能够使得索引构建的效率更高，我们用词项ID代替词项本身，当然同时需要维护一个词项->词项ID的映射表，并把他放入内存)；

  (3)把这个块的词项ID->文档ID对按照词项排序，并对相同词项ID对应的文档ID构建临时posting；

  (4)将此结果写回磁盘，并进行下一个block的解析；

  (5)当全部的文档集都解析完毕后，对每个block的倒排索引进行合并，并最后成为一个完整的倒排索引；

- 而BSBI的核心算法是(2),(3)，因此其核心算法的复杂度为O(TlogT)，在这个复杂度中并没有考虑(5)步的外部归并排序；因此只针对解析文档+生成临时posting；

### （3）内存式单遍扫描构建的方法

- SPIMI(Simple Pass in memory indexing)，操作流程如下：

  (1)把整个文档集都分割成词项->文档ID对；

  (2)把这个一系列的词项->文档ID对作为一个流，如果还有内存，则逐个进入内存；

  (3)内存中预先已经构建了一个dictionary（hash实现），因此只需要利用词项寻找到文档ID应该放入的位置，并放入文档ID即可；

  (4)当内存满时，将dictionary按照词项进行排序，并将排序后的dictionary和posting写回磁盘；

  (5)将全部的文档集解析完后在磁盘中应该有多个已排序的dictionary-posting；将这些合并即可；

- SPIMI的核心算法为(2)(3)，因此算法复杂度为O(T);

- ![](https://blog.idejie.com/pics/ir-review21.jpg)

### （4）分布式索引构建方法

上面所讲的都只是针对一般大的文档集，但是如果是对于海量的文档集，则在一台机器处理明显是不行的；因此我们想到了分而治之的思想；

主要思想：将文档集分布在计算机集群上进行处理，采用Master-Slave模式，Master电脑控制处理过程，比如一台计算机在处理文档集时突然坏了，则Master会将此电脑处理的文档集任务交给另一台机器处理；

Map阶段：将文档集划分成n个数据片，并通过**分析器**进行处理，变成排好序的词项->文档ID对,这就是一般的BSBI或SPIMI算法；

Reduce阶段：比如将每台机器的dictionary划分成a-i和j-z两个部分，然后将a-j部分统一交给一个**倒排器**完成，因此这里只需要两个倒排器即可；

注意：

(1)分析器和倒排器是一台计算机，并且一台机器既可以作为倒排器也可以作为分析器；

 

- Map阶段细化：

(1)文档集存在一台独立的机器中，将文档集分成数据片，并分别传送到作为分析器的机器中（这里需要考虑IO时间）；

(2)进行BSBI或者SPIMI分成词项ID-->文档ID（涉及比较次数消耗时间）；

Reduce阶段细化：

(1)将分区文件通过IO传送到倒排器中（这里需要考虑IO时间）；

(2)将每个倒排器中的词项ID-->文档ID排序   O（nlogn） n为词条数目；

(3)将倒排记录表写到独立的机器中； （注意：这里需要考虑dictionary的大小和posting的大小，dictionary的大小是词项大小，posting大小是词条大小,并且注意IO时间）；

### （5）动态索引构建方法

在以上讨论中，都是以文档不变化为前提，但实际上文档会更新、插入、删除等；因此我们需要引入动态索引；

主要思想：主索引继续维护，构造一个辅助索引（表示添加的文档），维护一个无效位向量（表示删除的文档），当辅助索引足够大时，就和主索引合并；

在检索时，我们必须要将主索引和辅助索引的检索结果合并，并在无效位向量中进行过滤即可；

**改进方法：**

引入log(T/n)个索引I0，I1，....Ii......;每个索引大小分别为(2^i)*n;

这些索引构建过程：

在内存中始终维护一个辅助索引；

(1)一开始当辅助索引满时，就构建I0并将I0存入磁盘，清空辅助索引；

(2)辅助索引第二次满时，和I0合并，并成为I1（I0被去除）；

(3)辅助索引第三次满时，构建I0；

(4)辅助索引第四次满时，将I0、I1和辅助索引合并，成为I2（I0和I1被清除）；

以此类推，可以看到有一个规律：构建索引的过程是以二进制数增加的方式构建的；即：

```
I3   I2  I1   I0

0    0    0    0
0    0    0    1
0    0    1    0
0    0    1    1
0    1    0    0
0    1    0    1
0    1    1    0
0    1    1    1
```

### （6）其他索引构建方法

一般倒排索引的posting都是按照文档ID进行排序，这样有助于压缩，而且插入数据时只需要在最后；但是对于ranked retrieval来说，需要按照权重进行排序，但是如果要添加数据，则需要扫描一遍确定插入位置；

一般地，访问授权是指一个用户对于文档是否有权访问，通过ACL（Access Control List）进行处理，而访问控制表也可以用一个倒排索引结构进行组建；

dictionary表示每个用户，而posting表示用户所能访问的文档ID；简单的来说就是一个用户-文档ID矩阵；

![](https://blog.idejie.com/pics/ir-review0.gif)

## 5-Index Compression

### (1)压缩

- 将长编码串用短编码串来代替

- 为什么压缩

- - 减少磁盘空间 (节省开销)
  - 增加内存存储内容 (加快速度)
  - 加快从磁盘到内存的数据传输速度 (同样加快速度)

- IR为什么需要压缩？

  ![](https://blog.idejie.com/pics/ir-review23.jpg)

- 有损压缩：丢弃一些信息

- 无损压缩：所有信息都保留

### (2)词项统计量

- 词汇表大小：
  - Heaps定律：$M=kT^b$
    - M 是词汇表大小, *T* 是文档集的大小(所有词条的个数，即所有文档大小之和)
    - $30\leq k\leq100,b\approx 0.5$
- 词项的分布
  - Zipf定律：![](https://blog.idejie.com/pics/ir-review24.jpg)
  - 第$i$常见的词项的频率$cf_i$ 和$\frac{1}{i}$ 成正比

### (3)词典压缩

- 将词典看成单一字符串的压缩方法
- 按块存储
  - 前端编码

### (4)倒排记录表压缩

- VB编码
  - 先写出二进制来，再取最后7位，并置首位为1，如果不足0补齐例如5：二进制101，vb编码1 000101；多于7位的部分，首位为0补上7位，不足补0 比如例如130化为二进制为 1000, 0010，总共需要8位，一个Byte表示不了，因而需要两个Byte来表示，第一个Byte表示后7位，并且在最高位置1来表示后面还有一个Byte，所以为(1) 0000010，第二个Byte表示第8位，并且最高位置0来表示后面没有其他的Byte了，所以为(0) 0000001。总的vb编码是0 0000001 1 0000010
  - 好处，存的是间隔，而且是变长整数型
  - 特点，基于字节
- γ编码
  - 一元码，n个1+一个0表示n
  - 将间隔表示成长度+偏移
  - 偏移对应G的二进制编码，只不过将首部的1去掉，13->1101偏移是101
  - 长度是3（101偏移部分），长度编码（一元码）是1110
  - γ编码的长度
    - 偏移部分是 ⌊log2 G⌋ 比特位
    - 长度部分需要 ⌊log2 G⌋ + 1 比特位
    - 因此，全部编码需要2⌊log2 G⌋ + 1比特位
    - ϒ 编码的长度均是奇数
    - ϒ 编码在最优编码长度的2倍左右
  - γ编码的性质
    - *ϒ* 编码是前缀无关的，也就是说一个合法的ϒ 编码不会是任何一个其他的合法*ϒ* 编码的前缀，也保证了解码的唯一性。
    - 编码在最优编码的2或3倍之内
      - 上述结果并不依赖于间隔的分布！
      - 因此， *ϒ* 编码适用于任何分布，也就说ϒ 编码是通用性(universal)编码
    - ϒ编码是无参数编码，不需要通过拟合得到参数
  - γ编码的对其问题
    - 机器通常有字边界 – 8, 16, 32 位
    - 按照位进行压缩或其他处理可能会较慢
    - 可变字节码通常按字边界对齐，因此可能效率更高
    - 除去效率高之外，可变字节码虽然额外增加了一点点开销，但是在概念上也要简单很多

![](https://blog.idejie.com/pics/ir-review0.gif)

## 6-TF-IDF

### (1)参数化索引和域索引

- 参数化索引：字段，不只是文档内容，还有文档属性
- 域索引：域是 自由文本（字段同时是任意文本，不过把字段当成了一个域，可以在这个域里面检索），一种域索引的实现方法就是把域的信息放在倒排记录表里面。
- 域加权评分：$\sum_{i=1}^lg_i=1,\sum_{i=1}^lg_is_i$
  - $g_i$是每个域的权重，$s_i$是第i域的得分
  - 权重的设置
    - 专家 
    - 权重学习
- 权重学习：
  - 给定一批已经标记得训练样本：<d,q,d与q的相关性>
  - 学习得$g_i$
  - 最优权重：![](https://blog.idejie.com/pics/ir-review26.jpg)

### (2)词项频率和权重计算

- 当tf>0是，$tf$ -$idf_{t,d}=（1+\log tf _{t,d})\times \log \frac{N}{df_t}$，tf=0时等于0
- 文档d的得分$Score(q,d)=\sum_{t \in q}tf$-$idf_{t,d}$
- 另外一种计算方法：$Score(q,d)=J(q,d)=\frac{|q \cap d|}{|q\cup d|}$

### （3）向量空间模型

- 余弦相似度

![](https://blog.idejie.com/pics/ir-review27.jpg)



### （4）其他权重计算方法

- 长度向量归一化：![](https://blog.idejie.com/pics/ir-review28.jpg)

  长度长的文档词项也多；长度长的文档TF高（q,d都是归一化的向量）

- 回转归一化：余弦归一化倾向于短文档，即对短文档产生的归一化因子太大，而平均而言对长文档产生的归一化因子太小。

  - 于是可以先找到一个支点(pivot，平衡点)，然后通过这个支点对余弦归一化操作进行线性调整。
  - 效果：短文档的相似度降低，而长文档的相似度增大

![](https://blog.idejie.com/pics/ir-review29.jpg)

![](https://blog.idejie.com/pics/ir-review30.jpg)

![](https://blog.idejie.com/pics/ir-review31.jpg)

![](https://blog.idejie.com/pics/ir-review0.gif)

## 7-System

### （1）快速评分及排序

- 

- 精确k：

  - 一般步骤：算cos、排序、topk
  - 加快cos:查询很短的话是有加速运算的
    - 特例：不考虑查询词项的权重(查询的词项只出现一次）
  - 堆排序
  - 提前终止计算：

  ![](https://blog.idejie.com/pics/ir-review33.jpg)

  ![image-20181130113107548](/Users/idejie/Library/Application%20Support/typora-user-images/image-20181130113107548.png)

- 非精确k：

  - 索引去除术：
    - 最容易想到的优化点，就是我们可不可以考虑针对原始查询做一些取舍，只关注查询中那些`idf`值比较高的那些词，即文档频率高的那些词。举个例子，我们在3C电商搜索中，根据“苹果手机”检索出排名最高的前20个商品。根据以往做法，根据分词后的“苹果”和“手机”两个词分别找到相应的倒排表，并依次扫描计算出最终的所有关联的商品，并根据计算的权重值按从高到低排序，并取出前２０个商品。但是细想下，针对3C商城来说，一个商品中包含“苹果”已经足够说明用户的意愿。而“手机”基本会出现在所有手机商品描述中，它的`idf`值是很低的，想当于那些“的，地，是”之类的停用词。所以可以把这些idf值低的词直接去掉，而这些词的倒排表是很长的，所以可以节省很大部分的计算量。
    - （1）只考虑idf超过一定阈值(对于查询 catcher in the rye 仅考虑包含catcher和rye的文档的得分)
    - （2）只考虑几个查询词项,对于多词项查询而言，只需要计算包含其中大部分词项的文档
  - 胜者表：对每个词项t，预先计算出其倒排记录表中权重最高的r篇文档，如果采用tfidf机制，即tf最高的r篇;上面的`索引去除`方法是从查询进行优化裁剪。`胜者表`是从倒排表进行处理优化。我们针对每个查询词项，只取其倒排表中排名靠前的r个文档。这个r值的设置根据场景不同而异。而排名的依据可以用tf（词项频率）。
  - 静态得分和排序：每片文档都有一个与查询无关的静态得分，这个分数基于用户的正面评价；所以先按这个分数排序；权威度
  - ![](https://blog.idejie.com/pics/ir-review34.jpg)
    - net-score评价法（高分文档先被遍历）

  ![](https://blog.idejie.com/pics/ir-review35.jpg)

  - 高低端表：一个词项的文档集分成两部分：高端版、低端版；如果高端版满足就不查低端了

  - 影响度排序：把文档按wf排序（好处：可以提前结束查询；按idf得分排序就可以先获得贡献大的了）

    - 提前结束法：遍历了固定数目r，wf低于某个阈值了；然后将词项的集合合并；计算他们的得分
    - 将词项按照idf排序

  - 簇剪枝方法：

    选一个leader

    ![](https://blog.idejie.com/pics/ir-review36.jpg)

### （2）信息检索系统的组成

- 层次型索引

  该例中，第 1 层索引中的 tf 阈值是 20，第 2 层阈值是 10。这意味着第 1 层索引只保留 tf 值超过 20 的倒排记录，而第 2 层的记录只保留 tf 值超过 10 的倒排记录。本例中每层的倒排记录表均按照文档 ID 排序。

  ![](https://blog.idejie.com/pics/ir-review37.jpg)

- 查询词项邻近性

  对于检索中的查询，特别是Web上的自由文本查询来说(参见第 19 章)，用户往往希望返 回的文档中大部分或者全部查询词项之间的距离比较近，因为这表明返回文档中具有聚焦用户 查询意图的文本。考虑一个由两个或者多个查询词项构成的查询t1, t2, . . . , tk。 令文档d中包含所 有查询词项的最小窗口大小为ω，其取值为窗口内词的个数。例如，假设某篇文档仅仅包含一 个句子The quality of mercy is not strained，那么查询strained mercy 在此文档中的最小窗口大小是 4。

- 查询分析和文档评分函数的设计

  ![](https://blog.idejie.com/pics/ir-review38.jpg)

- 搜索系统的组成

![](https://blog.idejie.com/pics/ir-review39.jpg)

### （3）向量空间模型对各种查询操作的支持

- 布尔查询

  一方 面，向量空间查询的处理基本上是证据累加(evidence accumulation)的方式，即多个查询词项 的出现会增加文档的得分;另一方面，布尔检索需要用户指定一个表达式，通过词项的出现与 不出现的组合方式来选择最终的文档，文档之间并无次序可言。数学上实际上存在一种称为p 范式(p-norm)1的方法来融合布尔和向量空间查询

- 通配符查询

  如果搜索引擎允许用户在自由文本查询中同时给定通配符(比如， 输入查询 rom* restaurant)，那么就可以把查询中的通配符解释成向量空间模型中的一系列查询 词项(上例中，rome 和 roman 就是两个可能的查询词项)，然后将所有查询词项加入到查询向 量中去。最后，上述向量空间查询按照通常的方式进行处理，结果文档评分并排序输出。显然， 一篇同时包含 rome 和 roma 的文档要比只包含其中一个词的文档的得分要高。 当然，最终文档 的精确排序主要取决于不同词项在文档中的相对权重。

- 短语查询

  用于向量空间方法的索引通常并不能用于短语查询的处理。

![](https://blog.idejie.com/pics/ir-review0.gif)

## 8-Evaluation

### （1）信息检索系统的评价

- 为什么评价IR
  - 评价技术的优劣、各种因素对系统的影响，有利于促进研究，提高技术水平
  - 目标是尽快、消耗少、返回准确
  - 计算机学科本身就是研究“更好”
- IR评价的指标
  - 效率
    - 时间开销、空间开销、响应速度
  - 效果
    - 返回了多少相关文档，占所有相关文档多少，返回的靠不靠前
  - 其他
    - 覆盖率，访问量，数据更新速度
- 如何评价
- 评价指标分类
  - 单个查询的评价
    - 召回率（查全率）+正确率（查准率）
    - ![](https://blog.idejie.com/pics/ir-review41.jpg)
    - ![](https://blog.idejie.com/pics/ir-review42.jpg)
    - 精准率：![](https://blog.idejie.com/pics/ir-review43.jpg)
    - ![](https://blog.idejie.com/pics/ir-review44.jpg)
    - ![](https://blog.idejie.com/pics/ir-review45.jpg)
    - 平均正确率
      - 未插值的AP：【未插值的AP(常用): 某个查询Q共有6个相关结果，某系统排序返回了5篇相关文档，其位置分别是第1，第2，第5，第10，第20位，则AP=(1/1+2/2+3/5+4/10+5/20+0)/6
      - 插值的AP：【在召回率分别为0,0.1,0.2,…,1.0的十一个点上的正确率求平均，等价于11点平均
      - 不考虑召回率【Precision@N：在第N个位置上的正确率，对于搜索引擎，大量统计数据表明，大部分搜索引擎用户只关注前一、两页的结果
  - 多个查询的评价
    - 平均的求法
      - 宏平均(Macro Average): 对每个查询求出某个指标，然后对这些指标进行算术平均
      - 微平均(Micro Average): 将所有查询视为一个查询，将各种情况的文档总数求和，然后进行指标的计算，如：Micro Precision=(对所有查询检出的相关文档总数)/(对所有查询检出的文档总数)
    - MAP(Mean AP)：对所有查询的AP求宏平均
  - 相关性试图度量用户的满意程度，但是用户是否满意取决于很多因素。
  - 面向用户的指标
    - ![](https://blog.idejie.com/pics/ir-review46.jpg)
    - ![](https://blog.idejie.com/pics/ir-review47.jpg)
    - ![](https://blog.idejie.com/pics/ir-review48.jpg)
  - Bpref
    - 基本的思想：在相关性判断(Relevance Judgment) 不完全的情况下，计算在进行了相关性判断的文档集合中，在判断到相关文档前，需要判断的不相关文档的篇数
    - ![image-20181201143103572](https://blog.idejie.com/pics/ir-review49.jpg)
  - GMAP
    - ![](https://blog.idejie.com/pics/ir-review50.jpg)
    - GMAP和MAP各有利弊，可以配合使用，如果存在难Topic时，GMAP更能体现细微差别
  - NDCG
    - ![](https://blog.idejie.com/pics/ir-review51.jpg)
    - ![](https://blog.idejie.com/pics/ir-review52.jpg)
    - ![](https://blog.idejie.com/pics/ir-review53.jpg)
    - ![](https://blog.idejie.com/pics/ir-review54.jpg)
    - ![](https://blog.idejie.com/pics/ir-review55.jpg)
    - 

### （2）标准测试集

### （3）无序检索集合的评价

![](https://blog.idejie.com/pics/ir-review56.jpg)

### （4）有序检索结果的评价

- map
- roc
- ndcg

### （5）相关性判定

![](https://blog.idejie.com/pics/ir-review57.jpg)

### （6）系统质量和用户效用

### （7）结果片段

![](https://blog.idejie.com/pics/ir-review0.gif)

## 9-Query Expansion

（1）相关性反馈及伪相关反馈

- Rocchio 相关反馈
  - Cr表示相关文档集，Cnr表示不相关文档集，那么我们希望找到的最优的 qr 是
    - ![](https://blog.idejie.com/pics/ir-review59.jpg)
    - ![](https://blog.idejie.com/pics/ir-review60.jpg)
    - ![](https://blog.idejie.com/pics/ir-review61.jpg)
- 基于概率的相关反馈方法：![](https://blog.idejie.com/pics/ir-review62.jpg)
- 相关反馈策略的评价
  - 首先计算出原始查询 q0 的正确率—召回率曲线，一轮相关反馈之后，我们计算出修改后的
    查询 qm 并再次计算出新的正确率—召回率曲线。
  - 利用剩余文档集(residual collection，所有文档集中除去用户判定的相关文档
    后的文档集)对反馈后的结果进行评价
- 伪相关反馈
- 

![](https://blog.idejie.com/pics/ir-review0.gif)

## 10-Probabilistic Model

- 基于Logistic回归的检索模型
  - ![](https://blog.idejie.com/pics/ir-review64.jpg)
- 经典的二值独立概率模型BIM
  - ![](https://blog.idejie.com/pics/ir-review65.jpg)
- 经典的BM25模型 (BestMatch25)
  - ![](https://blog.idejie.com/pics/ir-review66.jpg)
  - ![](https://blog.idejie.com/pics/ir-review67.jpg)
- 贝叶斯网络模型：本讲义不介绍，请参考有关文献。
- 基于语言建模的检索模型

![](https://blog.idejie.com/pics/ir-review0.gif)

## 11- Language Model

- SLM广泛使用于语音识别和统计机器翻译领域，利用概率统计理论研究语言。

- - 规则方法：词、句、篇章的生成比如满足某些规则，不满足该规则就不应存在。
  - 统计方法：任何语言片断都有存在的可能，只是可能性大小不同
  - ![](https://blog.idejie.com/pics/ir-review69.jpg)

- 查询似然模型

  - ![](https://blog.idejie.com/pics/ir-review70.jpg)

  - 几种平滑方法

    ![](https://blog.idejie.com/pics/ir-review71.jpg)

![](https://blog.idejie.com/pics/ir-review0.gif)

## 12-Navie Bayes

- 传统的分类

  - 基于手工
  - 基于规则

- 贝叶斯分类器

  ![](https://blog.idejie.com/pics/ir-review73.jpg)

  ![](https://blog.idejie.com/pics/ir-review74.jpg)

  ![](https://blog.idejie.com/pics/ir-review75.jpg)

  ![](https://blog.idejie.com/pics/ir-review76.jpg)

- 生成式模型：![](https://blog.idejie.com/pics/ir-review77.jpg)

- 贝努力模型：

  ![](https://blog.idejie.com/pics/ir-review78.jpg)

![](https://blog.idejie.com/pics/ir-review0.gif)

## 13-vector classify

- 特征选择方法主要基于其所使用特征效用(Utility)指标来定义。

- 特征效用指标：

  - 频率法 (DF)– 选择高频词项
  - 互信息(MI-Mutual information) – 选择具有最高互信息的那些词项。
  - 这里的互信息也叫做信息增益(IG-information gain)
  - 卡方(Chi-square)

- 互信息

  ![](https://blog.idejie.com/pics/ir-review80.jpg)

- 信息增益

  ![](https://blog.idejie.com/pics/ir-review81.jpg)

- 如何计算互信息

  ![](https://blog.idejie.com/pics/ir-review82.jpg)

  ![](https://blog.idejie.com/pics/ir-review83.jpg)

- 另一种互信息

  ![](https://blog.idejie.com/pics/ir-review84.jpg)

- 基于DF的选择方法 (DF Thresholding)

- - Term的DF小于某个阈值去掉(太少，没有代表性)
  - 实现十分简单，现有实验效果还不错

- 卡方选择法

![](https://blog.idejie.com/pics/ir-review85.jpg)

- 基于向量空间模型的分类

  -  利用Rocchio方法进行向量空间分类

  ![](https://blog.idejie.com/pics/ir-review123.jpg)
  ![](https://blog.idejie.com/pics/ir-review124.jpg)

  - KNN分类

  ![](https://blog.idejie.com/pics/ir-review87.jpg)

  - 线性分类器
    - ![](https://blog.idejie.com/pics/ir-review88.jpg)
    - ![](https://blog.idejie.com/pics/ir-review89.jpg)
    - ![](https://blog.idejie.com/pics/ir-review90.jpg)
    - ![](https://blog.idejie.com/pics/ir-review91.jpg)

![](https://blog.idejie.com/pics/ir-review0.gif)

## 14-svm ltr

- ![](https://blog.idejie.com/pics/ir-review93.jpg)

- ![](https://blog.idejie.com/pics/ir-review94.jpg)

- 权重学习

  - 域加权

    ![](https://blog.idejie.com/pics/ir-review95.jpg)

    ![](https://blog.idejie.com/pics/ir-review96.jpg)

    ![](https://blog.idejie.com/pics/ir-review97.jpg)

    ![](https://blog.idejie.com/pics/ir-review98.jpg)

    ![](https://blog.idejie.com/pics/ir-review99.jpg)

    ![](https://blog.idejie.com/pics/ir-review100.jpg)

    ![](https://blog.idejie.com/pics/ir-review101.jpg)

    ![](https://blog.idejie.com/pics/ir-review102.jpg)


![](https://blog.idejie.com/pics/ir-review0.gif)

## 15- lsi



- 层次聚类
  - ![](https://blog.idejie.com/pics/ir-review104.jpg)
  - ![](https://blog.idejie.com/pics/ir-review105.jpg)

![](https://blog.idejie.com/pics/ir-review106.jpg)





![](https://blog.idejie.com/pics/ir-review0.gif)

## 16- Neural IR



![](https://blog.idejie.com/pics/ir-review108.jpg)

![](https://blog.idejie.com/pics/ir-review109.jpg)

![](https://blog.idejie.com/pics/ir-review110.jpg)

![](https://blog.idejie.com/pics/ir-review111.jpg)



![](https://blog.idejie.com/pics/ir-review0.gif)

## 17- WebSearch

![](https://blog.idejie.com/pics/ir-review113.jpg)

![](https://blog.idejie.com/pics/ir-review114.jpg)

- 近似重复检测
  - 将每篇文档表示成一个**shingle**集合
    - ![](https://blog.idejie.com/pics/ir-review115.jpg)
    - ![](https://blog.idejie.com/pics/ir-review116.jpg)
  - 将文档表示成梗概(sketch)
    - ![](https://blog.idejie.com/pics/ir-review117.jpg)
    - ![image-20181202144354952](/Users/idejie/Library/Application%20Support/typora-user-images/image-20181202144354952.png)
    - ![](https://blog.idejie.com/pics/ir-review118.jpg)
    - ![](https://blog.idejie.com/pics/ir-review119.jpg)
    - 
    - ![](https://blog.idejie.com/pics/ir-review120.jpg)



![](https://blog.idejie.com/pics/ir-review0.gif)

## 18 -Crawling

![](https://blog.idejie.com/pics/ir-review0.gif)

## 19-LinkAnalysis



 HITS算法和PageRank算法可以说是搜索引擎链接分析的两个最基础且最重要的算法。从以上对两个算法的介绍可以看出，两者无论是在基本概念模型还是计算思路以及技术实现细节都有很大的不同，下面对两者之间的差异进行逐一说明。      

```
1.HITS算法是与用户输入的查询请求密切相关的，而PageRank与查询请求无关。所以，HITS算法可以单独作为相似性计算评价标准，而PageRank必须结合内容相似性计算才可以用来对网页相关性进行评价；

2.HITS算法因为与用户查询密切相关，所以必须在接收到用户查询后实时进行计算，计算效率较低；而PageRank则可以在爬虫抓取完成后离线计算，在线直接使用计算结果，计算效率较高；

3.HITS算法的计算对象数量较少，只需计算扩展集合内网页之间的链接关系；而PageRank是全局性算法，对所有互联网页面节点进行处理；

4.从两者的计算效率和处理对象集合大小来比较，PageRank更适合部署在服务器端，而HITS算法更适合部署在客户端；

5.HITS算法存在主题泛化问题，所以更适合处理具体化的用户查询；而PageRank在处理宽泛的用户查询时更有优势；

6.HITS算法在计算时，对于每个页面需要计算两个分值，而PageRank只需计算一个分值即可；在搜索引擎领域，更重视HITS算法计算出的Authority权值，但是在很多应用HITS算法的其它领域，Hub分值也有很重要的作用；

7.从链接反作弊的角度来说，PageRank从机制上优于HITS算法，而HITS算法更易遭受链接作弊的影响。

8.HITS算法结构不稳定，当对“扩充网页集合”内链接关系作出很小改变，则对最终排名有很大影响；而PageRank相对HITS而言表现稳定，其根本原因在于PageRank计算时的“远程跳转”。
```

## 参考

1.[《An Introduction to Information Retrieval》]( http://www.informationretrieval.org/)

2.何苯-中国科学院大学-《现代信息检索》课程PPT