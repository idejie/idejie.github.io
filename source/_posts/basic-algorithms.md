---
title: 慢慢总结一些基础算法（一）
date: 2019-09-11 10:32:36
tags: 算法
category: 算法
---

[TOC]

![](https://pic2.zhimg.com/80/v2-714c1843f78b6aecdb0c57cdd08e1c6a_hd.jpg)

详见：[【如何用简单易懂的例子解释条件随机场（CRF）模型？它和HMM有什么区别？ - Scofield的回答 - 知乎】](https://www.zhihu.com/question/35866596/answer/236886066)

## 1.贝叶斯 Bayes

- **贝叶斯定理**：（英语：Bayes' theorem）是[概率论](https://zh.wikipedia.org/wiki/概率論)中的一个[定理](https://zh.wikipedia.org/wiki/定理)，描述在已知一些条件下，某[事件](https://zh.wikipedia.org/wiki/事件_(概率论))的发生概率。比如，如果已知某癌症与寿命有关，使用贝叶斯定理则可以通过得知某人年龄，来更加准确地计算出他罹患癌症的概率。

- **公式**：
  $$
  P(A|B)=\frac{P(B|A)P(B)}{P(B)}
  $$
  其中$P(A|B)$表示已知B发生的情况下，然后A再发生的概率

  - ![P(A|B)](https://wikimedia.org/api/rest_v1/media/math/render/svg/2133a4f7790e55022dcc8e9f889dfffe4b177c5e)是已知发生后，的[条件概率](https://zh.wikipedia.org/wiki/条件概率)。也由于得自![B](https://wikimedia.org/api/rest_v1/media/math/render/svg/47136aad860d145f75f3eed3022df827cee94d7a)的取值而被称作![A](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3)的[后验概率](https://zh.wikipedia.org/wiki/后验概率)。
  - ![P(A)](https://wikimedia.org/api/rest_v1/media/math/render/svg/4f264d19e21604793c6dc54f8044df454db82744)是![A](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3)的[先验概率](https://zh.wikipedia.org/wiki/先验概率)（或[边缘概率](https://zh.wikipedia.org/wiki/边缘概率)）。之所以称为"先验"是因为它不考虑任何方面的因素。
  - ![{\displaystyle P(B|A)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5c2f9b12e7f5b5987b2c2cf6aeeea6500ccf38b1)是已知![A](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3)发生后，![B](https://wikimedia.org/api/rest_v1/media/math/render/svg/47136aad860d145f75f3eed3022df827cee94d7a)的条件概率。也由于得自![A](https://wikimedia.org/api/rest_v1/media/math/render/svg/7daff47fa58cdfd29dc333def748ff5fa4c923e3)的取值而被称作![B](https://wikimedia.org/api/rest_v1/media/math/render/svg/47136aad860d145f75f3eed3022df827cee94d7a)的[后验概率](https://zh.wikipedia.org/wiki/后验概率)。
  - ![P(B)](https://wikimedia.org/api/rest_v1/media/math/render/svg/e593d180a26fd68657ea50368dbfe1a661e652aa)是![B](https://wikimedia.org/api/rest_v1/media/math/render/svg/47136aad860d145f75f3eed3022df827cee94d7a)的[先验概率](https://zh.wikipedia.org/wiki/先验概率)。
  - 根据[条件概率](https://zh.wikipedia.org/wiki/条件概率)的定义。在事件*B*发生的条件下事件*A*发生的概率是：

  ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/c7f0ff7bcd50dd11514f9f02b1273dab360a4cef)

  ​			其中 $A$与$B$的联合概率表示为![P(A\cap B)](https://wikimedia.org/api/rest_v1/media/math/render/svg/f22276bc48d131dadc7e4dacbf38cee3ed05d536)或者![P(A,B)](https://wikimedia.org/api/rest_v1/media/math/render/svg/1fbb8f1ddf09ccf8e57829d1fa681355677c2961)或者![{\displaystyle P(AB)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/115cbcb066074dc28df1a0862863116c8c284b7a)。

  ​			同样地，在事件*A*发生的条件下事件*B*发生的概率

  ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/087dafd1afed425d2acb943da2e708603639eef7)

  ​			整理与合并这两个方程式，我们可以得到

  ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/0eba64686e8cab42885e8c317968d3ea93124d48)

  ​			这个引理有时称作概率乘法规则。上式两边同除以P(*B*)，若P(*B*)是非零的，我们可以得到贝叶斯定理:

  ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/484657d99185dac789f4cacaae5d3203aab1e69f)

- **贝叶斯公式**：
  $$
  P(B_i|A）=\frac{P(B_i)P(A|B_i)}{\sum_i [P(B_i)P(A|B_i)]}
  $$
  

  上式即为贝叶斯公式（Bayes formula)，$B_i$ 常被视为导致试验结果A发生的”原因“，$P(B_i)\quad{}_{(i=1,2,…)}$表示各种原因发生的可能性大小，故称先验概率；$P(B_i|A)\quad {}_{(i=1,2…)}$则反映当试验产生了结果A之后，再对各种原因概率的新认识，故称后验概率。

- 举例：

  报台分别以概率0.6和0.4发出信号“∪”和“—”。由于通信系统受到干扰，当发出信号“∪”时，收报台分别以概率0.8和0.2受到信号“∪”和“—”；又当发出信号“—”时，收报台分别以概率0.9和0.1收到信号“—”和“∪”。求当收报台收到信号“∪”时，发报台确系发出“∪”的概率。

  ​         解：

  
  $$
  P(B_1|A）=\frac{P(B_1)P(A|B_1)}{P(B_1)P(A|B_1)+P(B_2)P(A|B_2)}= \frac{(0.6*0.8)}{(0.6*0.8+0.4*0.1)}=0.923
  $$
  

  

## 2.条件随机场 CRF



## 3. 遗传算法 EM

## 4.高斯混合模型 GMM

## 5.隐马尔科夫 HMM

## 6.极大似然估计 MLE

## 7.上采样与下采样

## 8.图卷积网络

## 9.多层感知机MLP

 