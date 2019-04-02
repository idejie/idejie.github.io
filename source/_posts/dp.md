---
title: 算法（二）：动态规划
date: 2019-01-07 14:15:44
tags: 动态规划
category: 课程复习
---

## 1.抢金币

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz7kxqggwnj31b00dg41g.jpg)

------

$$
dp[n]=\begin{cases}
w[1] & n=1 \\
max(dp[1],dp[2]) & n=2 \\
max(dp[n-1],dp[n-2]+w[n]) & n\geq3 
\end{cases}
$$

第二问随机选一个标号为1

选1就不能选2和n，剩余n-3个房子用第一问求

不选1就等于求等于剩余n-1个房子用第一问求

$max(w[1]+dp[n-3],dp[n-1])$

## 2.节点选择

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz7lb55q7rj319m0403zj.jpg)

如果选择root，最大值=四个孙子树的最大值之和

如果不选择root，最大值=两个子树的最大值之和
$$
dp[n]=\begin{cases}
node_n.v & if \ node \ is \ leaf\\
max(node_n.v+\sum dp[n_{grandson}],\sum dp[n_{son}]) & if \ node \ is \ not \ leaf
\end{cases}
$$

## *3.解码

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz7llhy0drj31a80jego6.jpg)
$$
dp[i]=\begin{cases}
1 & if \ i = 1,0 \\
0 &if \ S_i=0\ and \ S_{i-1} \ne 1 \ or \  2\\
dp[i-1]+dp[i-2] & if \ 10<(S_{i-1}*10+S_i)\leq26 \ and  \ (S_{i-1}*10+S_i)\neq20\\
dp[i-2] &if \ (S_{i-1}*10+S_i)=10\ or \ 20 \\
dp[i-1] & others
\end{cases}
$$
这道题最终可以转化成斐波那契数列进行计算。

首先要确定的是，只有在数值小于26的时候，才可能出现多种解码。

- 例如，当数字是12，可以解码成AB或者L，当数值大于26则只有唯一解码
- 例如，当数字是34，解码只有CD

因此可从这个角度出发来解决这个问题，即先对数字进行判断

- 如果大于2，则进行切分
- 如果等于二，考虑后面一个数是否大于6
  - 如果大于6，则切分
  - 不大于6则不变
  - 例如：
    - 12213411可以切分成12213、4、11三部分
    - 1227126可以切分为122、7、126三部分
- 之后对拆分之后的每个子集进行分析，分析的主要依据和之前类似，由于无论如何组合，能够进行解码的数字一定不能是三位数，所以对每一个子集再进行组合，这时候你会发现，在上面讨论的前提下，会形成一个解码个数随子集中元素个数变化的斐波那契数列(这个斐波那契数列没有第一项的1)，求得每个子集解码个数之后，将这些数字相乘就得到了最终结果。

```python
a = input()
b = []
id_head = 0
for i in range(len(a)):
    if int(a[i])>2:
        b.append(a[id_head:i+1])
        id_head = i+1
    elif i == len(a)-1:
            b.append(a[id_head:i + 1])

num = 1
fib = lambda n:1 if n<=2 else fib(n-1)+fib(n-2)

for i in range(len(b)):
    num = num * fib(len(b[i])+1)
print(num)
```

## 4.最长连续数列

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz8aorruy6j31b803a3z7.jpg)
$$
OPT[i]=max\begin{cases}
opt[i-1] & if \ L[i] \ not \ in \ longest
\\
i-first[r],r = \sum_{w=0}^{i}L[w] \mod k & if \ L[i] \ in \ longest 
\end{cases}
$$
j=first[r]是指第一次,即  $arg \min\sum_{w=0}^{j}L[w]=r$

## 5.最大交易利润

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz8dwubqbcj31900a876a.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz8eqo18nij31ep0u0x1k.jpg)

## 6.最长增序列

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz8ercw6u9j31b00c641g.jpg)

opt[i]表示如果找长度为i的单增数列，最小的结尾是opt[i]

nums表示输入的数组

如果nums[j]>opt[i]那么就让opt[i+1]=nums[j]

如果nums[j]<opt[i-1],就去比opt[j-1]、opt[i-2]，

​	如果opt[1~i-1]都大于nums[j]，更新opt[1]=nums[j]

​	如果存在opt[m]<nums[j]<opt[n],利用二分法去找n，更新opt[n]=nums[j]

最终len(opt)就是最大长度
$$
opt[i] = \begin{cases}
nums[1] &if \ i=1\\
nums[i] &if \ opt[i-1]<nums[i]\\
nums[j] &if \ opt[i-1]<nums[j]<opt[i]
\end{cases}
$$

## 7.机器人移动

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz8f69hy6uj31aq0asmzj.jpg)

令opt[i,j]表示在（i，j）的所有解
$$
opt[i,j]=\begin{cases}
top_k[s[1,1]] & if \ i,j=1,1\\
top_k[opt[1,1].join(s[1,2])] & if \ i,j=1,2\\
top_k[opt[1,1].join( s[2,1])]& if \ i,j=2,1\\
top_k[opt[i-1,j].join( s[i,j]) \cup  opt[i,j-1].join(s[i,j])] & other
\end{cases}
$$
2017年习题

## 8.最大整除集

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz8f96ejxtj319603qmxy.jpg)

将数组从小到大排列，记opt[i]为输入数列遍历到i时最大的整除集长度
$$
opt[i] = \begin{cases}
max(opt[j]+1) & if \ s[i]\% s[j]=0\\
1 & other
\end{cases}
$$

## 9.字符串分割

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz8f9epvugj31ae0860u8.jpg)
$$
dp[i]=\begin{cases}
0 & if \ s[i:] is \ palindrome \\
min(dp[j])+1 & for \  j=i+1 \to n  \ and \ s[i:j] is\  palindrome
\end{cases}
$$
定义状态数组：cut[s.length()+1]，其中：cut[i]代表：string[i..n]字符串从i开始到末尾的最小划分数。 
状态转移方程： cut[i] = min(cut[i], cut[j+1]+1);  i+1<=j<=n-1
状态转移方程的意思是，string[i..j]是一个回文字符串，所以不用再划分。所以从i开始到末尾以j为划分点的最小划分数为： cut_num_array[j+1]+1 和 cut_num_array[i]中的最小值。
cut_num_array[i]的初值设为：s.length() - i; 也就是按照字符串中的每个字母都单独被划分来计算。

2016年习题

## 10.蛙跳

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz8fdujebkj31ak0du779.jpg)

青蛙过河，上一次跳k长度，下一次只能跳k­-1,k或者k+1。 因此对于到达了某一个点，我们可以查看其上一次是从哪个点跳过来的。 

设dp\[ j ][ i ] 为从i到达j 的步数，初始时把所有的石头存放进hash表。然后设置dp\[0][0] = 0. 接着对于每个石头，从 可以到达该石头的所有石头中取出步数k(k > 0)，然后当前的stone + k看其是否是合法的石头，是的话就有 d\[stone + k ][stone] = k 

```python
def can_cross(stones):
    dp = {stone: {} for stone in stones}
    dp[0][0] = 0
    for stone in stones:
        for step in dp[stone].values():
            for k in [step + 1, step, step ‐ 1]:
                if k > 0 and stone + k in dp:
                    dp[stone + k][stone] = k
     return len(dp[stones[‐1]].keys()) > 0
```

优化



```python
def canCross(self, stones):
    """
        :type stones: List[int]
        :rtype: bool
        """
    stone_set, fail = set(stones), set()
    stack = [(0, 0)]
    while stack:
        stone, jump = stack.pop()
        for j in (jump-1, jump, jump+1):
            s = stone + j
            if j > 0 and s in stone_set and (s, j) not in fail:
                if s == stones[-1]:
                    return True
                stack.append((s, j))
        fail.add((stone, jump))
    return False
```



2015年习题

## 11.最小路径和

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz8fakaihij311u0dqjw2.jpg)

贪心加递归:

每一次都是往左下或者右下
$$
opt[Node_n]=min\{opt[node_{P_l}],opt[node_{p_r}]\}+Node_n.v
$$
![](https://ws3.sinaimg.cn/large/006tNc79ly1fz8v47vo06j30vv0u07wh.jpg)

## 12.子序列

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz8fb0pdm9j317m0bsk0r.jpg)
$$
dp[i][j]=
dp[i-1][j-1] \and S[i]==T[j]
$$
dp\[i][j]表示S[0:i]是否为T[0:j]的子序列

2017级考题

## 13.爬楼梯

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz8fhkdpykj30qq03gwjp.jpg)

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz8fizd0myj30le02gmzo.jpg)
$$
dp[i]= \begin{cases}
i & if\ i\leq3 \\
dp[i-1]+dp[i-1-2] & other
\end{cases}
$$
2016级考题

## 14.同义子集

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz8fgieeelj30qw024tbl.jpg)

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz8fgqswj1j30ou03sq6w.jpg)

每次都需要比i-1次,复杂度为$O(n^2)$

令dp[i]表示，有i个相同句子的集合

利用并查集这一数据结构，如果存在$s_i=s_j$(i<j),那么就让$s_j$中移走，并让$dp[s_i]=dp[s_i]+1$

如果$s_j$和S中的句子都不相等，那么就让$dp[s_j]=1$，然后继续遍历下一个

## 15.回文

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz8ffltn8wj30oi07246y.jpg)



补充题

**一、简单基础dp**

**这类dp主要是一些状态比较容易表示，转移方程比较好想，问题比较基本常见的。主要包括递推、背包、LIS（最长递增序列），LCS（最长公共子序列），下面针对这几种类型，推荐一下比较好的学习资料和题目。**

## **- 16.递推：**

**递推一般形式比较单一，从前往后，分类枚举就行。**

简单:

[hdu 2084 数塔](http://acm.hdu.edu.cn/showproblem.php?pid=2084) 简单从上往下递推

[hdu 2018 母牛的故事](http://acm.hdu.edu.cn/showproblem.php?pid=2018) 简单递推计数

[hdu 2044 一只小蜜蜂...](http://acm.hdu.edu.cn/showproblem.php?pid=2044) 简单递推计数（Fibonacci）

[hdu 2041 超级楼梯](http://acm.hdu.edu.cn/showproblem.php?pid=2041) Fibonacci

[hdu 2050 折线分割平面](http://acm.hdu.edu.cn/showproblem.php?pid=2050) 找递推公式

推荐：

[CF 429B B.Working out](http://blog.csdn.net/cc_again/article/details/25691925) 四个角递推

[zoj 3747 Attack on Titans](http://blog.csdn.net/cc_again/article/details/24841249) 带限制条件的计数递推dp

[uva 10328 Coin Toss](http://blog.csdn.net/cc_again/article/details/24844911) 同上题

[hdu 4747 Mex ](http://blog.csdn.net/cc_again/article/details/11856847)

[hdu 4489 The King's Ups and Downs](http://blog.csdn.net/cc_again/article/details/9918313)

[hdu 4054 Number String](http://blog.csdn.net/cc_again/article/details/10858813)

## **17.背包**

经典的背包九讲：<http://love-oriented.com/pack/>

推荐博客：<http://blog.csdn.net/woshi250hua/article/details/7636866>

**主要有0-1背包、完全背包、分组背包、多重背包。**

简单：

[hdu 2955 Robberies](http://acm.hdu.edu.cn/showproblem.php?pid=2955) 01背包

[hdu 1864 最大报销额](http://acm.hdu.edu.cn/showproblem.php?pid=1864) 01背包

[hdu 2602 Bone Collector](http://acm.hdu.edu.cn/showproblem.php?pid=2602) 01背包

[hdu 2844 Coins](http://acm.hdu.edu.cn/showproblem.php?pid=2844) 多重背包

[hdu 2159 FATE](http://acm.hdu.edu.cn/showproblem.php?pid=2159) 完全背包

推荐：

[woj 1537 A Stone-I](http://blog.csdn.net/cc_again/article/details/22728273)  转化成背包

[woj 1538 B Stone-II](http://blog.csdn.net/cc_again/article/details/22728273) 转化成背包

[poj 1170 Shopping Offers](http://blog.csdn.net/cc_again/article/details/12200343) 状压+背包

[zoj 3769 Diablo III](http://blog.csdn.net/cc_again/article/details/25984915) 带限制条件的背包

[zoj 3638 Fruit Ninja ](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=3638)背包的转化成组合数学

[hdu 3092 Least common multiple](http://blog.csdn.net/cc_again/article/details/11518329) 转化成完全[背包问题](https://www.baidu.com/s?wd=%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)

[poj 1015 Jury Compromise](http://blog.csdn.net/cc_again/article/details/25426159) 扩大区间+输出路径

[poj 1112 Team Them UP](http://blog.csdn.net/cc_again/article/details/10162471) 图论+背包

## **18.LIS**

**最长递增子序列，朴素的是o(n^2)算法，二分下可以写成o(nlgn)：维护一个当前最优的递增序列——找到恰好大于它更新**

简单：

[hdu 1003 Max Sum](http://acm.hdu.edu.cn/showproblem.php?pid=1003)

[hdu 1087 Super Jumping!](http://acm.hdu.edu.cn/showproblem.php?pid=1087)

推荐：

[uva 10635 Prince and Princess](http://blog.csdn.net/cc_again/article/details/18372521) LCS转化成LIS

[hdu 4352 XHXJ's LIS](http://blog.csdn.net/cc_again/article/details/11821361)　数位dp+LIS思想

[srm div2 1000 ](http://blog.csdn.net/cc_again/article/details/12113809) 状态压缩+LIS

[poj 1239 Increasing Sequence](http://blog.csdn.net/cc_again/article/details/12208725) 两次dp

## **19.LCS**

最长公共子序列，通常o(n^2)的算法

[hdu 1503 Advanced Fruits](http://acm.hdu.edu.cn/showproblem.php?pid=1503)

[hdu 1159 Common Subsequence](http://acm.hdu.edu.cn/showproblem.php?pid=1159)

[uva 111 History Grading](http://blog.csdn.net/cc_again/article/details/8554454) 要先排个序

[poj 1080 Human Gene Functions](http://poj.org/problem?id=1080)



**二、区间dp**

推荐博客：<http://blog.csdn.net/woshi250hua/article/details/7969225>

**区间dp,一般是枚举区间，把区间分成左右两部分，然后求出左右区间再合并。**

[poj 1141 Brackets Sequence](http://blog.csdn.net/cc_again/article/details/10169643) 括号匹配并输出方案

[hdu 4745 Two Rabbits](http://blog.csdn.net/cc_again/article/details/11852367) 转化成求回文串 

[zoj 3541 The Last Puzzle ](http://blog.csdn.net/cc_again/article/details/10977751) 贪心+区间dp

[poj 2955 Brackets](http://poj.org/problem?id=2955)

[hdu 4283 You Are the One](http://blog.csdn.net/woshi250hua/article/details/7973824)  常见写法

[hdu 2476 String Printer](http://acm.hdu.edu.cn/showproblem.php?pid=2476) 

[zoj 3537 Cake](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=3537)

[CF 149D Coloring Brackets](http://codeforces.com/problemset/problem/149/D)

[zoj 3469 Food Delivery](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=3469)



## **20.树形dp**

比较好的博客：<http://blog.csdn.net/woshi250hua/article/details/7644959>

一篇论文：<http://doc.baidu.com/view/f3b19d0b79563c1ec5da710e.html>

**树形dp是建立在树这种数据结构上的dp,一般状态比较好想，通过dfs维护从根到叶子或从叶子到根的状态转移。**

[hdu 4123 Bob's Race](http://blog.csdn.net/cc_again/article/details/12011757) 二分+树形dp+单调队列

[hdu 4514](http://blog.csdn.net/cc_again/article/details/8911480)  求树的直径

[poj 1655 Balancing Act](http://blog.csdn.net/cc_again/article/details/13004997) 

[hdu 4714 Tree2Cycle](http://blog.csdn.net/cc_again/article/details/11407157) 思维

[hdu 4616 Game](http://blog.csdn.net/cc_again/article/details/10312393)

[hdu 4126 Genghis Kehan the Conqueror](http://blog.csdn.net/cc_again/article/details/12060191) MST+树形dp 比较经典

[hdu 4756 Install Air Conditioning](http://blog.csdn.net/cc_again/article/details/12092021) MST+树形dp 同上

[hdu 3660 Alice and Bob's Trip](http://blog.csdn.net/cc_again/article/details/12346065) 有点像对抗搜索

[CF 337D Book of Evil ](http://blog.csdn.net/cc_again/article/details/10226673) 树直径的思想 思维

[hdu 2196 Computer](http://acm.hdu.edu.cn/showproblem.php?pid=2196) 搜两遍



## **21.数位dp**

推荐一篇论文：<http://wenku.baidu.com/view/d2414ffe04a1b0717fd5dda8.html>

**数位dp,主要用来解决统计满足某类特殊关系或有某些特点的区间内的数的个数，它是按位来进行计数统计的，可以保存子状态，速度较快。数位dp做多了后，套路基本上都差不多，关键把要保存的状态给抽象出来，保存下来。**

[hdu 2089 不要62](http://acm.hdu.edu.cn/showproblem.php?pid=2089) 简单数位dp

[hdu 3709 Balanced Number](http://acm.hdu.edu.cn/showproblem.php?pid=3709) 比较简单

[CF 401D Roman and Numbers](http://blog.csdn.net/cc_again/article/details/25053071) 状压+数位dp

[hdu 4398 X mod f(x)](http://blog.csdn.net/cc_again/article/details/8872355) 把模数加进状态里面

[hdu 4734 F(x) ](http://blog.csdn.net/cc_again/article/details/11747555) 简单数位dp

[hdu 3693 Math teacher's homework](http://blog.csdn.net/cc_again/article/details/12257445) 思维变换的数位dp

[hdu 4352 XHXJ's LIS](http://blog.csdn.net/cc_again/article/details/11821361)　数位dp+LIS思想

[CF 55D Beautiful Numbers](http://blog.csdn.net/cc_again/article/details/8815450)  比较巧妙的数位dp

[hdu 3565 Bi-peak Numbers](http://blog.csdn.net/cc_again/article/details/8872073) 比较难想

[CF 258B Little Elephant and Elections](http://blog.csdn.net/cc_again/article/details/8877603) 数位dp+组合数学+逆元



## **22.概率(期望) dp**

推荐博客：<http://www.cnblogs.com/kuangbin/archive/2012/10/02/2710606.html>

推荐博客：<http://blog.csdn.net/woshi250hua/article/details/7912049>

推荐论文：

[《走进概率的世界》](http://wenku.baidu.com/view/1c41152de2bd960590c677a8.html)

[《浅析竞赛中一类数学期望问题的解决方法》](http://wenku.baidu.com/view/90adb02acfc789eb172dc8a8.html)

[《有关概率和期望问题的研究》](http://wenku.baidu.com/view/56147518a8114431b90dd81e.html)

**一般来说概率正着推，期望逆着推。有环的一般要用到高斯消元解方程。期望可以分解成多个子期望的加权和，权为子期望发生的概率，即 E(aA+bB+...) = aE(A) + bE(B) +...** 

[ural 1776 Anniversiry Firework](http://blog.csdn.net/cc_again/article/details/8974277) 比较基础

[hdu 4418 Time travel ](http://blog.csdn.net/cc_again/article/details/10493543) 比较经典BFS+概率dp+高斯消元

[hdu 4586 Play the Dice](http://blog.csdn.net/cc_again/article/details/10456837) 推公式比较水

[hdu 4487 Maximum Random Walk](http://blog.csdn.net/cc_again/article/details/9926597) 

[jobdu 1546 迷宫问题](http://blog.csdn.net/cc_again/article/details/12408505) 高斯消元+概率dp+BFS预处理

[hdu 3853 LOOPS](http://blog.csdn.net/cc_again/article/details/11536347) 简单概率dp

[hdu 4405 Aeroplane chess](http://blog.csdn.net/cc_again/article/details/11554945) 简单概率dp,比较直接

[hdu 4089 Activation](http://blog.csdn.net/cc_again/article/details/10431451) 比较经典

[poj 2096 Collecting Bugs](http://blog.csdn.net/cc_again/article/details/9936197) 题目比较难读懂

[zoj 3640 Help me Escape](http://blog.csdn.net/cc_again/article/details/11532517) 从后往前，比较简单

[hdu 4034 Maze](http://blog.csdn.net/cc_again/article/details/11544753) 经典好题，借助树的概率dp

[hdu 4336 Card Collector](http://blog.csdn.net/cc_again/article/details/11099749) 状态压缩+概率dp

[hdu 4326 Game ](http://blog.csdn.net/cc_again/article/details/10442931) 这个题状态有点难抽象



## **23.状态压缩dp**

这类问题有**TSP**、**插头dp**等。

推荐论文：<http://wenku.baidu.com/view/ce445e4f767f5acfa1c7cd51.html>

推荐博客：<http://blog.csdn.net/sf____/article/details/15026397>

推荐博客：<http://www.notonlysuccess.com/index.php/plug_dp/>

[hdu 1693 Eat the Trees  插头dp](http://blog.csdn.net/cc_again/article/details/9393357)

[hdu 4568 Hunter](http://blog.csdn.net/cc_again/article/details/9984961) 最短路+TSP

[hdu 4539 ](http://blog.csdn.net/cc_again/article/details/9954921) 插头dp

[hdu 4529 状压dp](http://blog.csdn.net/cc_again/article/details/9060019)

[poj 1185 炮兵阵地](http://poj.org/problem?id=1185)

[poj 2411 Mandriann's Dream](http://blog.csdn.net/cc_again/article/details/9390475) 轮廓线dp

[hdu 3811 Permutation](http://acm.hdu.edu.cn/showproblem.php?pid=3811)

[poj 1038](http://poj.org/problem?id=1038)

[poj 2441](http://poj.org/problem?id=2441)

[hdu 2167](http://acm.hdu.edu.cn/showproblem.php?pid=2167)

[hdu 4026](http://acm.hdu.edu.cn/showproblem.php?pid=4026)

[hdu 4281](http://acm.hdu.edu.cn/showproblem.php?pid=4281)



**七、数据结构优化的dp**

**有时尽管状态找好了，转移方程的想好了，但时间复杂度比较大，需要用数据结构进行优化。常见的优化有二进制优化、单调队列优化、斜率优化、四边形不等式优化等。**

## **24.二进制优化**

主要是优化背包问题，背包九讲里面有介绍，比较简单，这里只附上几道题目。

[hdu 1059 Diving](http://acm.hdu.edu.cn/showproblem.php?pid=1059) 

[hdu 1171 Big Event in Hdu](http://acm.hdu.edu.cn/showproblem.php?pid=1059)

[poj 1048 Follow My Magic](http://poj.org/problem?id=1048)

## **25.单调队列优化**

推荐论文：<http://wenku.baidu.com/view/4d23b4d128ea81c758f578ae.html>

推荐博客：<http://www.cnblogs.com/neverforget/archive/2011/10/13/ll.html>

[hdu 3401 Trade ](http://blog.csdn.net/cc_again/article/details/9328243) 

[poj 3245 Sequece Partitioning](http://blog.csdn.net/cc_again/article/details/9335795) 二分+单调队列优化

## **26.斜率优化**

推荐论文：[用单调性优化动态规划](http://wenku.baidu.com/view/ef259400bed5b9f3f90f1c3a.html)

推荐博客：<http://www.cnblogs.com/ronaflx/archive/2011/02/05/1949278.html>

[hdu 3507 Print Article](http://acm.hdu.edu.cn/showproblem.php?pid=3507)

[poj 1260 Pearls](http://poj.org/problem?id=1260)

[hdu 2829 Lawrence](http://acm.hdu.edu.cn/showproblem.php?pid=2829)

[hdu 2993 Max Average Problem](http://acm.hdu.edu.cn/showproblem.php?pid=2993)

## **27.四边形不等式优化**

推荐博客：<http://www.cnblogs.com/ronaflx/archive/2011/03/30/1999764.html>

推荐博客：<http://www.cnblogs.com/zxndgv/archive/2011/08/02/2125242.html>

[hdu 2952 Counting Sheep](http://acm.hdu.edu.cn/showproblem.php?pid=2952)

[poj 1160 Post Office](http://poj.org/problem?id=1160)

[hdu 3480 Division](http://acm.hdu.edu.cn/showproblem.php?pid=3480)

[hdu 3516 Tree Construction](http://acm.hdu.edu.cn/showproblem.php?pid=3516)

[hdu 2829 Lawrence](http://acm.hdu.edu.cn/showproblem.php?pid=2829)