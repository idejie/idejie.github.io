---
title: 算法（一）：分而治之
date: 2019-01-02 14:15:44
tags: 分而治之
category: 课程复习
---

## 1.两个数组的中位数

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz7912jcwfj319g0f8789.jpg)

------

当 n= 1时，中位数就是𝑚𝑖𝑛(𝐴[0],𝐵[0])当n>=2时，需要比较𝑀𝑙和𝑀𝑟如果两个数相等，那么中位数就是这个值如果𝑀𝑙>𝑀𝑟,那么就开始求𝐴𝑙和𝐵𝑟两部分的中位数如果𝑀𝑙<𝑀𝑟,那么就开始求𝐴𝑟和𝐵𝑙两部分的中位数。

**算法复杂度**：$O(log \ n)$

------

## 2.二叉树中的最远距离

Given a binary tree, suppose that the distance between two adjacent nodes is 1, please give a solution to find the maximum distance of any two node in the binary tree.

------

将树分成左子树和右子树子问题就是求左右两棵树的到根节点最大距离的点最大距离的点是，比较左右子树的根节点到叶子节点的最大值，并返回这个点最终，我们在左子树上能找到一个距离最大的叶子节点，右子树能找到一个到跟节点最大的叶子节点这两个点就是距离最远的节点对

**算法复杂度**:$O(log\ n)$

------

## 3.二叉树中的局部最小值

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz791sed76j319m0biade.jpg)

------

如果子节点都大于根节点，那么根节点就满足如果存在子节点小于根节点，那么可以将这个节点当做根节点形成新树去求解，这样就减少了一半

**复杂度**：𝑂(𝑙𝑜𝑔𝑛)

------

## 4.棋盘中的局部最小值

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz792apttwj31ag0b8tc2.jpg)

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz78e4xm5yj30xd0u0tc8.jpg)





n = 1 时，就是局部最小值

Divider:如图，将大棋盘G分割成4个 的小棋盘𝑔𝑖

Conquer:然后找出棋盘边上的𝑥𝑖的最小值min

- 如果最小值位于原大棋盘G的边上，那么就选择它所在的小棋盘𝑔𝑖为大棋盘再进行Divider，即𝐺=𝑔𝑖
- 如果min位于两个小棋盘的相交的边，那么就去比较它上下或者左右两个邻居
  - 如果min最小，那么min就是局部最小值如果
  - 不是min最小，那么选择最小邻居所在的棋盘作为大棋盘再进行处理如果
- min位于四个小棋盘的交汇点，那么就去比较它周围的四个邻居
  - 如果min仍是最小，输出min
  - 否则选择最小邻居所在的小棋盘作为大棋盘进行Divider

**算法复杂度**：$O(n)$

------

## 5.归并排序的特例

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz792pudvdj319i0asdiy.jpg)

------

和归并排序一样，只需要在换位置的时候判断一下，并且合理加上数值

$O(n\ log \ n)$

------

## 6.棋盘填充

Given a table M consisting of 2n ∗ 2n blocks, we want to fill it with a L-shaped module (consisting of three blocks). The L-shaped module is shown below.

![替代文字](https://ws2.sinaimg.cn/large/006tNc79ly1fz77z7yrwxj306604yt8k.jpg)

Please give a fill method, so that the last element of the table (M2n,2n) is empty.

![w](https://ws1.sinaimg.cn/large/006tNc79ly1fz780cwzrdj30uy0b2t91.jpg)

------

分成四个小正方形，相当于四个子问题

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz78gwh2p6j31ck0hw4mz.jpg)

$O(n^2)$

------

## 7.第k大元素

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz791ku38ij31a806cq3z.jpg)

------

快排，但是只需要关心第k个数可能在的那部分就好

$O(n)$

------

## 8.最近点对

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz794b4x91j313404aq3s.jpg)

------

最近点对 分成两部分，找出最小的𝛿

合并时，找|𝛿|附近的最近点对

$O(n\ log \ n )$

## 9.凸包特例：捉鬼敢死队

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz78xvignoj315e0iqqum.jpg)

------

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz7cke3uggj30s4118qbv.jpg)

------

## 10.凸包问题：多边形转化成三角

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz78yx3mllj316k06oth6.jpg)

------

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz7is86vz6j30qg0v2x0t.jpg)

## 11.数组中的局部最大值

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz78zmye1mj30nq066jxq.jpg)

Divider:从数组的中间元素$A_m=A [\frac{n}{2}]$开始比

Conquer:

- 如果元素$A_m$比两边邻居大，那么就返回$A_m$
- 如果不是最大，就选比它的其中一个邻居所在的$\frac{n}{2}$个元素当成新数列A，进行divider

$O(log \ n)$

## 12.奶牛跳房子

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz790j4009j319y0m844j.jpg)

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz790rrup0j3198098wgw.jpg)

最小间隔<d<L

然后用二分法夹逼出这个d来

每次试d，如果Di大于d就不用移走石头



## 13.排序

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz793nqrtpj319g0a4411.jpg)

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz793vhjfhj316u02u74x.jpg)

## 14.矩阵乘法

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz7953hbzpj319e03cjs2.jpg)

## 15.大数乘法

![](https://ws2.sinaimg.cn/large/006tNc79ly1fz795a5s77j319s02sdgi.jpg)

## 16.旋转数组

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz797l1j9bj30sa06ewnt.jpg)

 divide：

- 初始化,start 和end为数组的第一个和最后一个
- 如果start<end，那么start就是最小值
- 如果start>end，那么去数组中间的那个数mid，可知mid要么大于start，要么小于end
  - 如果mid>start,那么让start=mid，end=end在数组A[start~end]再进行divide
  - 如果mid<end,那么让start=start,end=mid在数组A[start~end]再进行divide

## 17.汉诺塔

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz7k6dvon8j30it08aabn.jpg)

对于n个盘子的汉诺塔问题，总有3根柱子，当前所有n个盘子都在柱子a上，那么如何通过柱子b将所有盘子挪到柱子c上？

对于n＝1，好吧，从a到c没有问题；

如果n>1，可以考虑为a有两个盘子一个是最下面的盘子，一个是上面的n-1个盘子（n-1个盘子看作一个整体），那么问题就是首先将n-1个盘子挪到b柱子上，然后把最下面的盘子放到c柱子上；

剩下的问题就是如何将n-1个盘子由b挪到c上

## 18.凸包问题

分治法解决凸包问题的大体思路就是，

- 取横坐标最小的点$P_0$和横坐标最大$P_n$的点（这两个点一定在凸包上，这个仔细想想能想明白）
- 然把这两个点连成一条直线，直线上面的半个凸包叫上凸包，直线下面的半个凸包叫下凸包
- 分别在上凸包和下凸包找出距离直线最大的点$P_{max}$，连接$P_1   P_{max}$和$P_nP_{max}$如下图

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz7krdczuxj30je0huq6o.jpg)

- 又可以把上下两个凸包分解成更小的上凸包和下凸包，为什么说是更小的上凸包和下凸包，
- 我们看上图如果我们把$P_1P_n$这条线段看成是一条有向线段，那么下凸包在它的右方，上凸包在它的左方，以上凸包为例，连接$P_1P_{max}$之后再找下一个$P_{max}$的时候我们肯定是要在$P_1P_{max}$这条有向线段的左方进行查找，因此我们可以将$P_1P_{max}$这条线段的左方看成一个更小的上凸包，同理，连接$P_1P_{max}$我们要找到下一个$P_{max}$肯定要在$P_1P_{max}$的右方查找，这就和下凸包的查找方式一样了，我们可以将它看成一个下凸包。

## 19.最大子序和

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

![](https://ws1.sinaimg.cn/large/006tNc79ly1fz7k2vn7r3j31vs06stae.jpg)

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz7k02v1muj30v90u048w.jpg)

## 20.循环赛表

设有n=2^k个运动员要进行网球循环赛。现要设计一个满足以下要求的比赛日程表：

(1)每个选手必须与其他n-1个选手各赛一次；

 (2)每个选手一天只能参赛一次；

(3)循环赛在n-1天内结束。

 请按此要求将比赛日程表设计成有n行和n-1列的一个表。在表中的第i行，第j列处填入第i个选手在第j天所遇到的选手。



按分治策略，我们可以将所有的选手分为两半。则n个选手的比赛日程表可以通过n/2个选手的比赛日程表来决定。

递归地用这种一分为二的策略对选手进行划分，直到只剩下两个选手时，比赛日程表的制定就变得很简单。

这时只要让这两个选手进行比赛就可以了。

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz7ka3oswqj307704taac.jpg)

如上图，所列出的正方形表是8个选手的比赛日程表。其中左上角与左下角的两小块分别为选手1至选手4和选手5至选手8前3天的比赛日程。据此，将左上角小块中的所有数字按其相对位置抄到右下角，又将左下角小块中的所有数字按其相对位置抄到右上角，这样我们就分别安排好了选手1至选手4和选手5至选手8在后4天的比赛日程。依此思想容易将这个比赛日程表推广到具有任意多个选手的情形。

当成一个nx(n-1)的矩阵

Divide：排序后分组，直到分成2，如有单数，虚拟出一个选手与其竞赛

Conquer：为两名选手安排竞赛

merge:使组A只与组B的选手进行竞赛

特殊情况的处理，单数:

![](https://ws4.sinaimg.cn/large/006tNc79ly1fz7kn42pqlj31580h8aav.jpg)

![](https://ws3.sinaimg.cn/large/006tNc79ly1fz7kncv39sj317w0h8js8.jpg)