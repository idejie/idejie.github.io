---
title: 算法（四）：线性规划
date: 2019-01-09 14:15:44
tags: 线性规划
category: 课程复习
---

2018级习题

## 1.线性不等式的可行解

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz8viizeolj30yw0940uv.jpg)



![](https://ws4.sinaimg.cn/large/006tNc79ly1fz9tzj70duj318k0oc1kx.jpg)



![](https://ws2.sinaimg.cn/large/006tNc79ly1fz9u04vzr3j317m0ti7wh.jpg)

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz9u0nera7j317a0ss4qp.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz9u0twojpj31800qc1kx.jpg)



## 2.教室分配

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz8vj0x657j30z6074769.jpg)

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz9tnw95xlj31bm0u0ag6.jpg)



## 3.燃气站分配

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz8vj8e9jwj30yw0eg0wd.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz9txm9i2ej30ye0geju3.jpg)

## 4.配对

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz8vjlfz8mj311y0lc444.jpg)



![](https://ws4.sinaimg.cn/large/006tNc79ly1fz9u8vsf8zj319w0s24qp.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz9u9cn044j31880iokbs.jpg)



![](https://ws3.sinaimg.cn/large/006tNc79ly1fz9ubqc25kj315u0kskcr.jpg)

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz9ucu5e6yj317y0r21kx.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz9ud1a5dgj31580l87pn.jpg)

## 5.多物品流

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz8vk56ejrj30zy05o3zt.jpg)

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz9ue4r0jvj317c0igdzd.jpg)

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz9v1xkhpsj311s0r0hb1.jpg)

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz9v1hshynj316a0to4qp.jpg)



## 6.对偶问题2

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz8vkjhe0rj30mi0egdgr.jpg)

## 7.飞机落地

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz8vl3chvdj30zy0ic0xk.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz9v3fafprj315i0rcx5y.jpg)

## 8.志愿者分配

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz8vlm2uovj30yw09mdi4.jpg)

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz9v3qbndhj318k07sn5z.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz9v42k3kmj318y0janiz.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz9v49nw2gj318m0om4p9.jpg)

2016级习题

## 9.*****

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz8vmw32htj310m0cw76v.jpg)

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz8vnc2ca2j30u00vln5e.jpg)



2017级试题

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz8vovqtnzj30po02k0wl.jpg)

## 10.最小费用流

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz8vpp5hfxj30yc0awtow.jpg)

## 11.最短路径

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz8vty2dvvj30ma04ijwk.jpg)

in the single-pair shortest-path problem,we are given: a weigthed directed graph G=(U,E) ,a weight function w: E $\to \R^2$ mapping edges to positive real-valued weight

2016级试题

## 12.货物运输

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz8vvha8vuj31100eety6.jpg)
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