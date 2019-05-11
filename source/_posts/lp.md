---
title: 算法（四）：线性规划
date: 2019-01-09 14:15:44
tags: 线性规划
category: 课程复习
---

2018级习题

## 1.线性不等式的可行解

![](https://blog.idejie.com/pics/lp0.jpg)



![](https://blog.idejie.com/pics/lp1.jpg)



![](https://blog.idejie.com/pics/lp2.jpg)

![](https://blog.idejie.com/pics/lp3.jpg)

![](https://blog.idejie.com/pics/lp4.jpg)



## 2.教室分配

![](https://blog.idejie.com/pics/lp5.jpg)

![](https://blog.idejie.com/pics/lp6.jpg)



## 3.燃气站分配

![](https://blog.idejie.com/pics/lp7.jpg)

![](https://blog.idejie.com/pics/lp8.jpg)

## 4.配对

![](https://blog.idejie.com/pics/lp9.jpg)



![](https://blog.idejie.com/pics/lp10.jpg)

![](https://blog.idejie.com/pics/lp11.jpg)



![](https://blog.idejie.com/pics/lp12.jpg)

![](https://blog.idejie.com/pics/lp13.jpg)

![](https://blog.idejie.com/pics/lp14.jpg)

## 5.多物品流

![](https://blog.idejie.com/pics/lp15.jpg)

![](https://blog.idejie.com/pics/lp16.jpg)

![](https://blog.idejie.com/pics/lp17.jpg)

![](https://blog.idejie.com/pics/lp18.jpg)



## 6.对偶问题2

![](https://blog.idejie.com/pics/lp19.jpg)

## 7.飞机落地

![](https://blog.idejie.com/pics/lp20.jpg)

![](https://blog.idejie.com/pics/lp21.jpg)

## 8.志愿者分配

![](https://blog.idejie.com/pics/lp22.jpg)

![](https://blog.idejie.com/pics/lp23.jpg)

![](https://blog.idejie.com/pics/lp24.jpg)

![](https://blog.idejie.com/pics/lp25.jpg)

2016级习题

## 9.*****

![](https://blog.idejie.com/pics/lp26.jpg)

![](https://blog.idejie.com/pics/lp27.jpg)



2017级试题

![](https://blog.idejie.com/pics/lp28.jpg)

## 10.最小费用流

![](https://blog.idejie.com/pics/lp29.jpg)

## 11.最短路径

![](https://blog.idejie.com/pics/lp30.jpg)

in the single-pair shortest-path problem,we are given: a weigthed directed graph G=(U,E) ,a weight function w: E $\to \R^2$ mapping edges to positive real-valued weight

2016级试题

## 12.货物运输

![](https://blog.idejie.com/pics/lp31.jpg)
$$
min \quad \sum a_ix_i+b_i·I(x_i)
\\
s.t.=
\begin{cases}
I(x)=\begin{cases}
1 ，& x>0\\
0, &x=0
\end{cases}\\
 x_i \leq C_i &i=1,2...M\\
\sum _{to\  City_c }x_i =\sum _{from\ City_c }x_j\\
\sum_{from \ City_1}x_i=\sum_{to \ city_N} x_j = K
\\
x_i = 0，1,2,3,....,K\\
i,j = 1,2,...,M\\
c= 2,3,...,N-1
\end{cases}
$$
补充题