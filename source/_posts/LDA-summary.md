---
title: LDA学习笔记
date: 2017-07-25 00:11:04
tags: LDA
category: 数据科学
---

# 1.什么是 LDA？

举个例子，我们要写一个某品牌新车上市的软文，首先就得确定这篇文章的主题，比如你的主题定义在了该车的动力、外观和内饰。

第二步，便是从这些相关主题的词汇库里寻找相关的词语

- 动力：发动机、涡轮增压、功率、油耗、扭矩等
- 外观：氙气、天窗、后视镜、前脸、格栅灯等；
- 内饰: 仪表台、中控台、方向盘、座椅、靠背等

最后一步就是结合语法，将词语组织成句子。

由文档确定主题、由主题确定词汇的过程就是 **LDA（Latent Dirichlet Allocation）**

> LDA（Latent Dirichlet Allocation）是一种文档主题生成模型，也称为一个三层贝叶斯概率模型，包含词、主题和文档三层结构。所谓生成模型，即认为一篇文章的每个词都是通过“以一定概率选择了某个主题，并从这个主题中以一定概率选择某个词”这样一个过程得到。文档到主题服从多项式分布，主题到词服从多项式分布。
>
> 《百度百科》

# 2.LDA 的工作模式

- 从狄利克雷分布![img](http://img.blog.csdn.net/20141117160438989)中取样生成文档 i 的主题分布![img](http://img.blog.csdn.net/20141117160452327)
- 从主题的多项式分布![img](http://img.blog.csdn.net/20141117160452327)中取样生成文档i第 j 个词的主题![img](http://img.blog.csdn.net/20141117160518098)
- 从狄利克雷分布![img](http://img.blog.csdn.net/20141117160531515)中取样生成主题![img](http://img.blog.csdn.net/20141117160518098)对应的词语分布![img](http://img.blog.csdn.net/20141117160613962)
- 从词语的多项式分布![img](http://img.blog.csdn.net/20141117160613962)中采样最终生成词语![img](http://img.blog.csdn.net/20141117160656067)

其中，类似Beta分布是二项式分布的共轭先验概率分布，而狄利克雷分布（Dirichlet分布）是多项式分布的共轭先验概率分布。

​    此外，LDA的图模型结构如下图所示（类似[贝叶斯网络](http://blog.csdn.net/v_july_v/article/details/40984699#t6)结构）：

![img](http://img.blog.csdn.net/20141117152903751)

**各种分布**



​	首先先看**伯努利分布Bernoulli process**。

​	要理解什么是Bernoulli process，首先先看什么Bernoulli trial。

​	Bernoulli trial简单地说就是一个只有两个结果的简单trial，比如**抛硬币**。
​	那我们就用**抛一个(不均匀）硬币**来说好了，X = 1就是头，X = 0就是字，我们设定q是抛出字的概率。
​	那什么是bernoulli process？就是从Bernoulli population里随机抽样，或者说就是重复的独立Bernoulli trials，再或者说就是狂抛这枚硬币n次记结果吧。好吧，我们就一直抛吧，我们记下X=0的次数k.

现在问题来了。
Q：**我们如何知道这枚硬币抛出字的概率？**我们知道，如果可以一直抛下去，最后k/n一定会趋近于q；可是现实中有很多场合不允许我们总抛硬币，比如**我只允许你抛4次**。你该怎么回答这个问题？显然你在只抛4次的情况下，k/n基本不靠谱；那你只能"**猜一下q大致分布在[0,1]中间的哪些值里会比较合理**",但绝不可能得到一个准确的结果比如q就是等于k/n。

​	举个例子，比如：4次抛掷出现“头头字字”，你肯定觉得q在0.5附近比较合理，q在0.2和0.8附近的硬币抛出这个结果应该有点不太可能，q = 0.05和0.95那是有点扯淡了。
你如果把这些值画出来，你会发现q在[0,1]区间内呈现的就是一个中间最高，两边低的情况。从感性上说，这样应当是比较符合常理的。

那我们如果有个什么工具能描述一下这个q可能的分布就好了，比如用一个概率密度函数来描述一下? 这当然可以，可是我们还需要注意另一个问题，那就是随着n增长观测变多，**你每次的概率密度函数该怎么计算**？该怎么利用以前的结果更新（这个在形式上和计算上都很重要）？

到这里，其实很自然地会想到把bayes theorem引进来，因为Bayes能随着不断的观测而更新概率；而且每次只需要前一次的prior等等…在这先不多说bayes有什么好，接下来用更形式化语言来讲其实说得更清楚。

**我们现在用更正规的语言重新整理一下思路。**现在有个硬币得到random sample X  = (x1,x2,...xn)，我们需要基于这n次观察的结果来估算一下**q在[0,1]中取哪个值比较靠谱**，由于我们不能再用单一一个确定的值描述q，所以我们用一个分布函数来描述：有关q的概率密度函数（说得再简单点，即是q在[0,1]“分布律”）。当然，这应当写成一个条件密度：f(q|X)，因为我们总是观测到X的情况下，来猜的q。

现在我们来看看Bayes theorem，看看它能带来什么不同：
![](https://blog.idejie.com/pics/LDA-summary0.jpg)

在这里P(q)就是关于q的先验概率（所谓先验，就是在得到观察X之前，我们设定的关于q的概率密度函数）。P(q|x)是观测到x之后得到的关于q的后验概率。注意，到这里公式里出现的都是"概率"，并没有在[0,1]上的概率密度函数出现。为了让贝叶斯定理和密度函数结合到一块。我们可以从方程两边由P(q)得到f(q)，而由P(q|x)得到f(q|x)。
又注意到P(x)可以认定为是个常量（Q：why？），可以在分析这类问题时不用管。**那么，这里就有个简单的结论——****关于q的后验概率密度f(q|x)就和“关于q的****先验概率密度乘以一个条件概率"成比例，即：**
![f(q|x)\sim P(X=x|q)f(q)](https://www.zhihu.com/equation?tex=f%28q%7Cx%29%5Csim+P%28X%3Dx%7Cq%29f%28q%29)

带着以上这个结论，我们再来看这个抛硬币问题：
连续抛n次，即为一个bernoulli process，则在q确定时，n次抛掷结果确定时，又观察得到k次字的概率可以描述为：![P(X=x|p) = q^{k}(1-q)^{n-k} ](https://www.zhihu.com/equation?tex=P%28X%3Dx%7Cp%29+%3D+q%5E%7Bk%7D%281-q%29%5E%7Bn-k%7D+)
那么f(q|x)就和先验概率密度乘以以上的条件概率是成比例的：
![f(q|x) \sim q^{k}(1-q)^{n-k}f(q) ](https://www.zhihu.com/equation?tex=f%28q%7Cx%29+%5Csim+q%5E%7Bk%7D%281-q%29%5E%7Bn-k%7Df%28q%29+)
虽然我们不知道，也求不出那个P(x)，但我们知道它是固定的，我们这时其实已经得到了一个求f(q|x)的公式（只要在n次观测下确定了，f(q)确定了，那么f(q|x)也确定了)。

现在在来看f(q)。显然，在我们对硬币一无所知的时候，我们应当认为硬币抛出字的概率q有可能在[0,1]上任意处取值。f(q)在这里取个均匀分布的密度函数是比较合适的，即f(q) = 1 (for q in [0,1]) 。
有些同学可能发现了，这里面![f(q|x) \sim q^{k}(1-q)^{n-k}](https://www.zhihu.com/equation?tex=f%28q%7Cx%29+%5Csim+q%5E%7Bk%7D%281-q%29%5E%7Bn-k%7D)，**那个![q^{k}(1-q)^{n-k}](https://www.zhihu.com/equation?tex=q%5E%7Bk%7D%281-q%29%5E%7Bn-k%7D)乘上[0,1]的均匀分布不就是一个Beta distribution么**？
对，它就是一个Beta distribution。Beta distribution由两个参数alpha、beta确定；在这里对应的alpha等于k+1，beta等于n+1-k。而**均匀分布的先验密度函数，就是那个f(q)也可以被beta distribution描述**，这时alpha等于1，beta也等于1。

更有意思的是，当我们每多抛一次硬币，出现字时，我们只需要alpha = alpha + 1；出现头只需要beta = beta + 1。这样就能得到需要估计的概率密度f(q|x)…

其实之所以计算会变得这么简单，是因为被beta distribution描述的prior经过bayes formula前后还是一个beta distribution；这种不改变函数本身所属family的特性，叫**共轭(conjugate)**。

ok。讲到这你应该明白，对于有两个结果的重复Bernoulli trial，我们用beta prior/distribution就能解决。那么加入我们有n个结果呢？比如抛的是骰子？
这时候上面的Bernoulli trial就要变成有一次trial有k个可能的结果； Bernoulli distribution就变成multinomial distribution。而beta distribution所表述的先验分布，也要改写成一个多结果版本的先验分布。那就是dirichlet distribution。
均匀的先验分布Beta(1,1)也要变成k个结果的Dir(alpha/K)。dirichlet prior也有共轭的性质，所以也是非常好计算的。
简而言之，就是由2种外推到k种，而看待它们的视角并没有什么不同。
他们有着非常非常非常相似的形式。

**结论1：dirichlet distribution就是由2种结果bernoulli trial导出的beta distribution外推到k种的generalization**

如何通俗易懂地介绍Gaussian Process？ - 知乎用户的回答

如何用简单易懂的例子解释隐马尔可夫模型？ - 知乎用户的回答