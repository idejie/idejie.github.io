---
title: 《信息检索导论》课后习题
date: 2018-11-25 01:30:20
tags: 答案
category: 信息检索
---

>目前进度：2/15
>
>参考：[《An Introduction to Information Retrieval》Preliminary draft (c)2007]( http://www.informationretrieval.org/)
>
>未经允许，不得转载或其他使用。
>
>如有问题，请联系[本文作者](mailto:i@idejie.com)

## 第一章

![](https://ws3.sinaimg.cn/large/006tNbRwly1fx0rlfrxovj30tc07qgn3.jpg)

```
forecast->1
home->1->2->3->4 
in->2->3
increase->3 
july->2->3 
new->1->4 
rise->2->4 
sale->1->2->3->4 
top->1
```

![](https://ws4.sinaimg.cn/large/006tNbRwly1fx0rnl8fnqj30n80b0jth.jpg)

```
Term-Document matrix: 
              d1 d2 d3 d4 
Approach      0  0  1  0 
breakthrough  1  0  0  0 
drug          1  1  0  0 
for           1  0  1  1 
hopes         0  0  0  1 
new           0  1  1  1 
of            0  0  1  0 
patients      0  0  0  1 
schizophrenia 1  1  1  1 
treatment     0  0  1  0

Inverted Index: 
Approach -> 3 
breakthrough ->1 
drug ->1->2 
for ->1->3- >4 
hopes ->4 
new ->2->3->4 
of ->3 
patients ->4 
schizophrenia ->1->2->3->4 
treatment >3
```

![](https://ws1.sinaimg.cn/large/006tNbRwly1fx0rrntb0wj30z404i0ts.jpg)

```
a  doc1 doc2
b  doc4
```

![](https://ws1.sinaimg.cn/large/006tNbRwly1fx0rtr64w3j313i05sq4q.jpg)

```
a. O(x+y)
b. 不能。不可以在O(x+y)次内完成。因为NOT Caesar的倒排记录表需要提取其他所有词项对应的倒排记录表。所以需要遍历几乎全体倒排记录表，于是时间复杂度即为所有倒排记录表的长度的和N，即O(N) 或者说O(x+N-y)。
```

![](https://ws3.sinaimg.cn/large/006tNbRwly1fx0s0txff9j313a068mz4.jpg)

```
时间复杂度为O(qN)，其中q为表达式中词项的个数，N为所有倒排记录表长度之和。也就是说可以在词项个数q及所有倒排记录表长度N的线性时间内完成合并。由于任意布尔表达式处理算法复杂度的上界为O(N)，所以上述复杂度无法进一步改进。
```

![](https://ws2.sinaimg.cn/large/006tNbRwly1fx4gk3q8oej30tu062di0.jpg)

```
a. 析取范式为：(Brutus And Not Anthony And Not Cleopatra) OR (Caesar AND NOT Anthony AND NOT Cleopatra)
b. 这里的析取范式处理比前面的合取范式更有效。这是因为这里先进行AND操作(括号内)，得到的倒排记录表都不大，再进行OR操作效率就不会很低。而前面需要先进行OR操作，得到的中间倒排记录表会更大一些。
c. 上述结果不一定对，比如两个罕见词A和B构成的查询 (A OR B) AND NOT(HONG OR KONG)，假设HONG KONG一起出现很频繁。此时合取方式可能处理起来更高效。如果在析取范式中仅有词项的非操作时，b中结果不对。
```

![](https://ws3.sinaimg.cn/large/006tNbRwly1fx51emlwojj31gw02aq3e.jpg)

![](https://ws3.sinaimg.cn/large/006tNbRwly1fx51f2b54ij31g40hitc4.jpg)

```
由于：
(tangerine OR trees) ➔ 46653+316812 = 363465
(marmalade OR skies)➔ 107913+271658 = 379571
(kaleidoscope OR eyes）➔ 87009+213312 = 30321    
所以推荐处理次序为：
(kaleidoscope OR eyes）AND (tangerine OR trees) AND (marmalade OR skies)


根据使用并集的列表长度的保守估计，建议的顺序是:(kaleidoscope OR eyes)（300,321）and (tangerine OR trees)（363,465）and (marmalade OR skies) （379,571）. 但是，取决于实际分布  (tangerine OR trees)可能比 (marmalade OR skies)更长，因为前者的两个组成部分更不对称。 例如，预计11和9990的并集比5000和5000的并集更长，尽管保守估计不然。
S. Singh’s solution:
执行时间 : 
(i) (tangerine OR trees) = O(46653+316812) = O(363465) 
(ii) (marmalade OR skies) = O(107913+271658) = O(379571) 
(iii) (kaleidoscope OR eyes) = O(46653+87009) = O(300321)
执行顺序:
a. 任意顺序执行(i), (ii), (iii)  (任何情况总的复杂度： O(363465+379571+300321) )
b. 执行 (i) AND (iii) = (iv): 在AND运算符的情况下，合并记录表的复杂性取决于较短记录表的长度。 因此，记录表越小越短，花费的时间就越少。选择（i）而不是（ii）的原因是如果选择（i），则输出列表（iv）更可能更短。
c. 执行（iv）and（ii）：这是唯一剩下的合并的操作。
```

![image-20181112095809168](/Users/idejie/Library/Application%20Support/typora-user-images/image-20181112095809168.png)

```
令friends、romans和countrymen的文档频率分别为x、y、z。如果z极高，则将N-z作为NOT countrymen的长度估计值，然后按照x、y、N-z从小到大合并。如果z极低，则按照x、y、z从小到大合并。
```

![](https://ws4.sinaimg.cn/large/006tNbRwly1fxceywovgbj30oi020jrv.jpg)

```
排序不保证是最佳的。 考虑三个词项，倒排记录表中s1 = 100，s2 = 105和s3 = 110.假设s1和s2的交集长度为100，s1和s3的交集长度为0.排序s1，s2，s3需要100 + 105 + 100 + 110 = 315步。更合理的顺序是s1,s3,s2此时需要100 + 110 + 0 + 0 = 210步。

不一定。比如三个长度分别为x,y,z的倒排记录表进行合并，其中x>y>z，如果x和y的交集为空集，那么有可能先合并x、y效率更高
```

![](https://ws2.sinaimg.cn/large/006tNbRwly1fxcf8r228aj31gi020aar.jpg)

```python
answer<- ( )
while p1!=NIL and p2!=NIL
do if docID(p1)=docID(p2)
then 	ADD(answer,docID(p1))
	p1 <- next(p1)
    p2 <- next(p2)
else if docID(p1)<docID(p2)
then 	ADD(answer,docID(p1))
    p1 <- next(p1)
else 	ADD(answer,docID(p2))
	p2 <-next(p2)
if p1!=NIL    // x还有剩余 
then while p1!=NIL do ADD (answer, docID(p1))
else while p2!=NIL do ADD(answer,docID(p2))
return(answer) 
```

![](https://ws3.sinaimg.cn/large/006tNbRwly1fxdnrqhu5dj31me04cgn4.jpg)

```python
由于NOT y几乎要遍历所有倒排表，因此如果采用列举倒排表的方式非常耗时。可以采用两个有序集合求减的方式处理 x AND NOT y。算法如下：

Meger(p1,p2)

answer      ()
while p1!=NIL and p2!=NIL
do if docID(p1) =docID(p2)
then	p1next(p1)
	p2next(p2)
else if docID(p1)<docID(p2)
then	ADD(answer, docID(p1))
	p1next(p1)
else	ADD(answer, docID(p2))
	p2next(p2)
	if p1!=NIL    // x还有剩余 
	then while p1!=NIL do ADD (answer, docID(p1))
	return(answer)
```

![](https://ws3.sinaimg.cn/large/006tNbRwly1fxdo2q8sxwj31nm04ctav.jpg)

```
professor teacher lecturer /s explain!
```

![](https://ws1.sinaimg.cn/large/006tNbRwly1fxdoq1804cj31oy0g0dls.jpg)

```
a.google
(i)找到约 37,800,000 条结果
(ii)找到约 36,600,000 条结果
(iii)找到约 66,100,000 条结果
b.
(i)找到约 492,000,000 条结果
(ii)找到约 75,500,000 条结果 
(iii)找到约 572,000,000 条结果
```

## 第二章

![](https://ws2.sinaimg.cn/large/006tNbRwly1fxj5fc17bij310m0a2ad2.jpg)

```
a F 
b T 
c F 
d F
```

![](https://ws2.sinaimg.cn/large/006tNbRwly1fxj5jiufxwj314y0b4gn3.jpg)

```
a cos
b shiite
c contd
d hawaii
e orourke
```

![](https://ws1.sinaimg.cn/large/006tNbRwly1fxj5l33kkdj31go0cutbh.jpg)

```
c 不应该同样结果 营销和市场是两个概念
d 大学和宇宙也是两个不同的概念
```

![](https://ws4.sinaimg.cn/large/006tNbRwly1fxj5ovmct8j312q0agwhf.jpg)

![image-20181124145430651](/Users/idejie/Library/Application%20Support/typora-user-images/image-20181124145430651.png)



```
a.为了防止使用规则's'->''等错误干扰。
b.circus->circu, canaries->canar, boss->boss
c. y->i
d.不会，因为查询也会进行词干还原，此时可以认为poni就是pony(ponies)
```

![](https://ws3.sinaimg.cn/large/006tNbRwly1fxj5w26klcj30ts01ywf0.jpg)



```
这种情况需要对倒排索引的表都进行查询
```

![](https://ws3.sinaimg.cn/large/006tNbRwly1fxj5xj26kkj31go0gc795.jpg)

```
a. 11 
	1. 4 & 47
	2. 6 & 47
	...
	10. 32 & 47
	11. 47 & 47
b.6
	1. 4 & 47 
	2. 14 & 47 
	3. 22 & 47 
	4. 120 & 47 
	5. 81 & 47 
	6. 47 & 47
```

![](https://ws3.sinaimg.cn/large/006tNbRwly1fxj61m2t02j31di0gcagi.jpg)

```
a. 一次  24 ->75
b.  19次
(3,3)
(5,5)
(9,89)
(15,89)
(24,89)
(75,89)
(75,89)
(92,89)
(81,89)
(84,89)
(89,89)
(92,95)
(115,95)
(96,95)
(96,97)
(97,97)
(100,99)
(100，100)
(101，115)
c. 19
(3,3)
(5,5)
(9,89)
(15,89)
(24,89)
(39,89)
(60,89)
(68,89)
(75,89)
(81,89)
(84,89)
(89,89)
(92,95)
(96,95)
(96,97)
(97,97)
(99,100)
(100,100)
(101,115)
```

![](https://ws3.sinaimg.cn/large/006tNbRwly1fxj6cwtfm7j31gw03kta0.jpg)

```
Some alumni had arrived from New York. University faculty said that Stanford is the best place to study....
```

![](https://ws4.sinaimg.cn/large/006tNbRwly1fxj6dj05ewj318m0ocn3k.jpg)

```
a 2 4 7
b 4
```

![](https://ws3.sinaimg.cn/large/006tNbRwly1fxj6pzrgrqj30s405kwfa.jpg)

![](https://ws2.sinaimg.cn/large/006tNbRwly1fxj6qmjgm5j31hw0fg79k.jpg)

```
a.1,3
b.k=1 doc3
k=2,3,4 doc1,3
k>=5 1,2,3
```



![](https://ws4.sinaimg.cn/large/006tNbRwly1fxj6r4eo7mj31h40a6n2c.jpg)

```
O((m+n)L) 
m为词项1的倒排索引表中文档记录长度，相应的n为词项2的
```

![](https://ws1.sinaimg.cn/large/006tNbRwly1fxj6rem2gdj31gg0cedlc.jpg)

```

```

![](https://ws2.sinaimg.cn/large/006tNbRwly1fxj6rrgqrtj31gq0egwki.jpg)

```

```

![image-20181124153155600](/Users/idejie/Library/Application%20Support/typora-user-images/image-20181124153155600.png)

```

```

