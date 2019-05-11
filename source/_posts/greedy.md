---
title: 算法（三）：贪心算法
date: 2019-01-08 14:15:44
tags: 贪心
category: 课程复习
---

# Greedy

2018级习题

## 1.多边形与度

![](https://blog.idejie.com/pics/greedy0.jpg)

![](https://blog.idejie.com/pics/greedy1.jpg)

## 2.工作分配

![](https://blog.idejie.com/pics/greedy2.jpg)

![](https://blog.idejie.com/pics/greedy3.jpg)

![](https://blog.idejie.com/pics/greedy4.jpg)

最后一个在PC上结束的时间
$$
Time_{job_i}=\sum_{0\to i-1}Super\ time + PC_i
\\
job_i\text{必须等前面i-1个job执行完，并且再在PC上执行完，所以结束时间：max{Time of Job i}}
$$

## 3.子序列匹配

![](https://blog.idejie.com/pics/greedy5.jpg)

## 4.剪绳子

![](https://blog.idejie.com/pics/greedy6.jpg)

**动态规划**
$$
dp[n]=max\{dp[i]*dp[n-i]\}
$$
**贪心：**

取尽量多的3，然后是2

if n%3=0 全分成3

if n%3=1 分成 n-4/3个3 和两个2

if n%3=2 分分成n-1个3和一个2

**证明：**

数学归纳法：(并不完备，只能证明有效性，不能证明最优)

- n=1，2，3，4不讨论，原因：1不能剪，2，3，4的话剪了反而不会增大
- 从n=5开始，显然2，3是最优解
- n=6~10通过枚举法也易得分配最优

对于n>=10时来讨论

2(n-2)>n ;3(n-3)>2(n-2)

## 5.负重过河

![](https://blog.idejie.com/pics/greedy7.jpg)

![](https://blog.idejie.com/pics/greedy8.jpg)



## 6.猴子香蕉

![](https://blog.idejie.com/pics/greedy9.jpg)

排序就完了

第i个猴子拿第i个香蕉

2016级习题

## 7.雷达布测

![](https://blog.idejie.com/pics/greedy10.jpg)

![](https://blog.idejie.com/pics/greedy11.jpg)

## 8.乘数

![](https://blog.idejie.com/pics/greedy12.jpg)

排序，小的和小的乘

## 9.霍夫曼编码

![](https://blog.idejie.com/pics/greedy13.jpg)

参考：https://blog.csdn.net/FX677588/article/details/70767446



## 10.最短路径

![](https://blog.idejie.com/pics/greedy14.jpg)

https://blog.csdn.net/yalishadaa/article/details/55827681 

2015级习题

## 11.聚会

![](https://blog.idejie.com/pics/greedy15.jpg)

都排序，和猴子分香蕉的一样

2017级试题题



## 12.做作业

![](https://blog.idejie.com/pics/greedy16.jpg)

和下面14.deadline的一样

## 13.滑雪比赛

![](https://blog.idejie.com/pics/greedy17.jpg)

都排序，和猴子分香蕉的一样

2016级试题

## 14.Deadline

![](https://blog.idejie.com/pics/greedy18.jpg)

按扣分项降序，然后把作业都放在deadline那一天，如果当天有多个扣分项，试着往前移第一个次大的p，如果前一天没有作业，或者扣得分少于p,那么就可以换；如果不可以，就继续试着往前换，直到所有都不满足

## 15.DotA猪队友神对手

![](https://blog.idejie.com/pics/greedy19.jpg)

![](https://blog.idejie.com/pics/greedy20.jpg)

按DSP/HP降序排列，先打最高的

补充题

教程：https://blog.csdn.net/qq_32400847/article/details/51336300

①最典型的例子就是 会场安排问题nyoj14, 按节目结束时间排序,再遍历每一个节目时,有选择地更新结束时间,计算出最大节目数

```
可分割背包问题,按单位价值排序,每次选择单位价值大的物品。有道题跟可分割背包类似,但是需要考虑多一点点路程成本的问题,nyoj248

有几道也是比较容易找出最优策略的题目:  nyoj824 nyoj236   nyoj71  nyoj91(需要有点小技巧)  
```

②区间覆盖问题,  poj1328(典型),nyoj6   nyoj1036(比较难理解的是题意...看不懂算了)  nyoj891  建议可以先做poj1328,后面的两道也就可以想出来了。

③二分+贪心: 通过题目可以已知结果所在的范围,然后又有某个限定条件的存在,这个条件可供我们作为贪心的检验条件 nyoj586 nyoj914  poj3122 poj3258 hdu4190

④寻找最大数系列(要在某个范围内贪心):  nyoj448  nyoj1057 nyoj1170

⑤需要很细心地贪心策略  nyoj364(我有试着用二分图但是超时了,选择贪心策略去做吧)  nyoj791(记得要充分利用所有的油漆) hdu1735

⑥很难但是很有学习价值的题目: nyoj30(列举出每种情况,解题报告一句话让我恍然大悟,贪心策略很巧妙)  nyoj1309(看了解题报告很久才懂的题目,好题) hdu4415(难) hdu3697(贪心+枚举)

⑦策略好找,但是需要小技巧防止超时的题目: hdu4544  hdu4864

⑧以小见大,举例子去找到排序策略,体会一下这三道题,nyoj47(经典过河)hdu4296  hdu4442 nyoj1218(涉及高精度运算)

⑨如何将a配凑成b,用 '就近原则' nyoj915 hdu5821 

nyoj  http://acm.nyist.net/JudgeOnline/problemset.php         hdu   http://acm.hdu.edu.cn        poj  http://poj.org/

这里只是列举了一些题目,如果你是刚学贪心算法正在找题目做的同学可以先刷完这些题,我的博客也有部分题目的题解,希望有所帮助.

PS:因为huffman树,迪杰斯特拉算法,最小生成树算法,二分图最大匹配(匈牙利算法)和二分图最佳匹配(KM算法)  也用到了贪心思想,所以我也看了一下,下面都是一些很好的文章:

huffman树:   http://blog.csdn.net/ns_code/article/details/19174553  poj3253  nyoj801 

迪杰斯特拉算法: http://www.cnblogs.com/Braveliu/p/3458671.html     poj1502

最小生成树算法: http://www.cnblogs.com/biyeymyhjob/archive/2012/07/30/2615542.html#commentform

二分图最大匹配:http://blog.csdn.net/dark_scope/article/details/8880547/   hdu2063  hdu1281  poj1274 poj1469 

最佳匹配: http://www.cnblogs.com/Lanly/p/6291214.html#3738044    