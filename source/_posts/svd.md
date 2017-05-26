---
title: 基于MovieLens数据集的电影推荐系统（简易版）
date: 2017-03-25 20:06:59
tags: 推荐系统
category: 数据挖掘
---

## MovieLens

数据集给了三个信息：ratings/movies/users，是6000名用户对4000部电影的评分。内容如下：

- ratings.dat

  ```
  #=======================================================================
  #             UserID::MovieID::Rating::Timestamp
  #=======================================================================
  	- UserIDs range between 1 and 6040 
  	- MovieIDs range between 1 and 3952
  	- Ratings are made on a 5-star scale (whole-star ratings only)
  	- Timestamp is represented in seconds since the epoch as returned by time(2)
  	- Each user has at least 20 ratings
  ```

  ​

- users.dat

  ```
  #=======================================================================
  #         UserID::Gender::Age::Occupation::Zip-code
  #=======================================================================
  	- Gender is denoted by a "M" for male and "F" for female
  	- Age is chosen from the following ranges:
  		*  1:  "Under 18"
  		* 18:  "18-24"
  		* 25:  "25-34"
  		* 35:  "35-44"
  		* 45:  "45-49"
  		* 50:  "50-55"
  		* 56:  "56+"
  	- Occupation is chosen from the following choices:
  		*  0:  "other" or not specified
  		*  1:  "academic/educator"
  		*  2:  "artist"
  		*  3:  "clerical/admin"
  		*  4:  "college/grad student"
  		* ...........
  		* 19:  "unemployed"
  		* 20:  "writer"
  ```

  ​

- movies.dat

  ```
  #=======================================================================
  #             MovieID::Title::Genres
  #=======================================================================
  	- Titles are identical to titles provided by the IMDB (includingyear of release)
  	- Genres are pipe-separated and are selected from the following genres:
    		* Action
    		* Adventure
    		* Animation
    		* Children's
    		* Comedy
    		* Crime
    		* Documentary
    		* ......
    		* Western
  	- Some MovieIDs do not correspond to a movie due to accidental duplicate entries and/or test entries
  	- Movies are mostly entered by hand, so errors and inconsistencies may exist

  ```



## 算法

### 0.[常用算法对比](http://blog.jobbole.com/72373/)

### 1.关联规则（啤酒和尿布）

- 关联规则是形如X→Y的蕴涵式。其中，X和Y分别称为关联规则的先导和后继。

![](https://ww3.sinaimg.cn/large/006tKfTcly1fdzd5ari8bj30jq08iq3h.jpg)

### 2.Slope One

举个例子

![](https://ww4.sinaimg.cn/large/006tKfTcly1fdzdjr4aaqj30df049aab.jpg)

？=4-（（5-3）+（4-3））/2

- 基本的想法来自于简单的一元线性模型![](https://ww2.sinaimg.cn/large/006tKfTcly1fdzd7bb284j303100oq2s.jpg)已知一组训练点![](https://ww1.sinaimg.cn/large/006tKfTcly1fdzd7xwj4kj301q00vdfo.jpg) 利用此线性模型最小化预测误差的平方和，我们可以获得![](https://ww2.sinaimg.cn/large/006tKfTcly1fdzd8vvdjfj304c01bq2t.jpg)

- 当我们要预测新点的时候，带入原来的一元线性模型就好了

- 误差多大？![](https://ww4.sinaimg.cn/large/006tKfTcly1fdzdb17cn7j307501rjrc.jpg)

  ​	其中 Sj,i() 表示同时对item i 和 j 给予了评分的用户集合，而 card()表示集合包含的元素数量。

- 将

![](https://ww4.sinaimg.cn/large/006tKfTcly1fdzddmfcsuj302f00ot8k.jpg)作为新的item的预测值



*注*：这个没有考虑到使用不同用户数量平均值。假设有2000个用户同时评论了item j和k，而只有20个用户评分了item j和item l，那么显然用dev(j,k)比dev(j,l)更有权威

### 3.SVD

[推荐阅读文章](http://blog.sina.com.cn/s/blog_628cc2b70102w4t3.html)

简单的说就是把高维稀疏矩阵进行分解：

![](https://ww3.sinaimg.cn/large/006tNbRwly1fe6g3vhavtj30nz0bxmxp.jpg)

#### 一些补充知识

##### 1.正交矩阵

![](https://ww1.sinaimg.cn/large/006tNbRwly1fe6g5y0n80j30ov0giab6.jpg)

假设二维空间中的一个向量OA，它在标准坐标系也即e1、e2表示的坐标是中表示为(a,b)'（用'表示转置），现在把它用另一组坐标e1'、e2'表示为(a',b')'，存在矩阵U使得(a',b')'=U(a,b)'，则U即为正交矩阵。从图中可以看到，正交变换只是将变换向量用另一组正交基表示，在这个过程中并没有对向量做拉伸，也不改变向量的空间位置，加入对两个向量同时做正交变换，那么变换前后这两个向量的夹角显然不会改变。上面的例子只是正交变换的一个方面，即旋转变换，可以把e1'、e2'坐标系看做是e1、e2坐标系经过旋转某个斯塔角度得到，怎么样得到该旋转矩阵U呢？如下：

![](https://ww4.sinaimg.cn/large/006tNbRwly1fe6g73syd7j30as0793yl.jpg)

a'和b'实际上是x在e1'和e2'轴上的投影大小，所以直接做内积可得，then

![](https://ww1.sinaimg.cn/large/006tNbRwly1fe6g7ssuurj3052022a9z.jpg)

从图中可以看到![](https://ww2.sinaimg.cn/large/006tNbRwly1fe6g8b4hj4j303m01mt8l.jpg)![](https://ww2.sinaimg.cn/large/006tNbRwly1fe6g8gip64j303x01mwed.jpg)

所以

![](https://ww2.sinaimg.cn/large/006tNbRwly1fe6g8src90j306v01umx4.jpg)

正交阵U行（列）向量之间都是单位正交向量。上面求得的是一个旋转矩阵，它对向量做旋转变换！也许你会有疑问：刚才不是说向量空间位置不变吗？怎么现在又说它被旋转了？对的，这两个并没有冲突，说空间位置不变是绝对的，但是坐标是相对的，加入你站在e1上看OA，随着e1旋转到e1'，看OA的位置就会改变。如下图：

![](https://ww1.sinaimg.cn/large/006tNbRwly1fe6g97q4r6j30p90g9jsn.jpg)

如图，如果我选择了e1'、e2'作为新的标准坐标系，那么在新坐标系中OA（原标准坐标系的表示）就变成了OA'，这样看来就好像坐标系不动，把OA往顺时针方向旋转了“斯塔”角度，这个操作实现起来很简单：将变换后的向量坐标仍然表示在当前坐标系中。

旋转变换是正交变换的一个方面，这个挺有用的，比如在开发中需要实现某种旋转效果，直接可以用旋转变换实现。正交变换的另一个方面是反射变换，也即e1'的方向与图中方向相反，这个不再讨论。

总结：正交矩阵的行（列）向量都是两两正交的单位向量，正交矩阵对应的变换为正交变换，它有两种表现：旋转和反射。正交矩阵将标准正交基映射为标准正交基（即图中从e1、e2到e1'、e2'）

##### 2.EVD

  在讨论SVD之前先讨论矩阵的特征值分解（EVD），在这里，选择一种特殊的矩阵——对称阵（酉空间中叫hermite矩阵即厄米阵）。对称阵有一个很优美的性质：它总能相似对角化，对称阵不同特征值对应的特征向量两两正交。一个矩阵能相似对角化即说明其特征子空间即为其列空间，若不能对角化则其特征子空间为列空间的子空间。现在假设存在mxm的满秩对称矩阵A，它有m个不同的特征值，设特征值为![](https://ww2.sinaimg.cn/large/006tNbRwly1fe6gazmlosj301c01g0sk.jpg)

对应的单位特征向量为![img](http://img.blog.csdn.net/20150123145830171)

则有

​                                                                 ![img](http://img.blog.csdn.net/20150123150002344)

进而

​                                                               ![img](http://img.blog.csdn.net/20150123150119033)

​                                                  ![img](http://img.blog.csdn.net/20150123150331493)

​                                                    ![img](http://img.blog.csdn.net/20150123150505140)

所以可得到A的特征值分解（由于对称阵特征向量两两正交，所以U为正交阵，正交阵的逆矩阵等于其转置）

​                                                        ![img](http://img.blog.csdn.net/20150123150757364)

这里假设A有m个不同的特征值，实际上，只要A是对称阵其均有如上分解。

矩阵A分解了，相应的，其对应的映射也分解为三个映射。现在假设有x向量，用Ａ将其变换到Ａ的列空间中，那么首先由U'先对x做变换：

​                                                                              ![img](http://img.blog.csdn.net/20150123151414245)

U是正交阵U'也是正交阵，所以U'对x的变换是正交变换，它将x用新的坐标系来表示，这个坐标系就是A的所有正交的特征向量构成的坐标系。比如将x用A的所有特征向量表示为：

​                                         ![img](http://img.blog.csdn.net/20150123151915529)

则通过第一个变换就可以把x表示为[a1 a2 ... am]'：

​                           ![img](http://img.blog.csdn.net/20150123152046383)

紧接着，在新的坐标系表示下，由中间那个对角矩阵对新的向量坐标换，其结果就是将向量往各个轴方向拉伸或压缩：

​                              ![img](http://img.blog.csdn.net/20150123152331057)

从上图可以看到，如果A不是满秩的话，那么就是说对角阵的对角线上元素存在0，这时候就会导致维度退化，这样就会使映射后的向量落入m维空间的子空间中。

最后一个变换就是U对拉伸或压缩后的向量做变换，由于U和U'是互为逆矩阵，所以U变换是U'变换的逆变换。

因此，从对称阵的分解对应的映射分解来分析一个矩阵的变换特点是非常直观的。假设对称阵特征值全为1那么显然它就是单位阵，如果对称阵的特征值有个别是0其他全是1，那么它就是一个正交投影矩阵，它将m维向量投影到它的列空间中。

根据对称阵A的特征向量，如果A是2*2的，那么就可以在二维平面中找到这样一个矩形，是的这个矩形经过A变换后还是矩形：

​                                      ![img](http://img.blog.csdn.net/20150123155218277)

这个矩形的选择就是让其边都落在A的特征向量方向上，如果选择其他矩形的话变换后的图形就不是矩形了！

#### 奇异值分解——SVD

   上面的特征值分解的A矩阵是对称阵，根据EVD可以找到一个（超）矩形使得变换后还是（超）矩形，也即A可以将一组正交基映射到另一组正交基！那么现在来分析：对任意M*N的矩阵，能否找到一组正交基使得经过它变换后还是正交基？答案是肯定的，它就是SVD分解的精髓所在。

   现在假设存在M*N矩阵A，事实上，A矩阵将n维空间中的向量映射到k（k<=m）维空间中，k=Rank(A)。现在的目标就是：在n维空间中找一组正交基，使得经过A变换后还是正交的。假设已经找到这样一组正交基：

​                                                               ![img](http://img.blog.csdn.net/20150123160515876)

则A矩阵将这组基映射为：

​                                                            ![img](http://img.blog.csdn.net/20150123160626263)

如果要使他们两两正交，即

​                                      ![img](http://img.blog.csdn.net/20150123160744762)

根据假设，存在

​                                      ![img](http://img.blog.csdn.net/20150123160916671)

所以如果正交基v选择为A'A的特征向量的话，由于A'A是对称阵，v之间两两正交，那么

​                                                  ![img](http://img.blog.csdn.net/20150123161147171)

这样就找到了正交基使其映射后还是正交基了，现在，将映射后的正交基单位化：

因为

​                  ![img](http://img.blog.csdn.net/20150123161911890)

所以有

​                                ![img](http://img.blog.csdn.net/20150123162005218)

所以取单位向量

​                                        ![img](http://img.blog.csdn.net/20150123162032674)

由此可得

​                ![img](http://img.blog.csdn.net/20150123162324773)

当k < i <= m时，对u1，u2，...，uk进行扩展u(k+1),...,um，使得u1，u2，...，um为m维空间中的一组正交基，即

![img](http://img.blog.csdn.net/20150123162811221)

同样的，对v1，v2，...，vk进行扩展v(k+1),...,vn（这n-k个向量存在于A的零空间中，即Ax=0的解空间的基），使得v1，v2，...，vn为n维空间中的一组正交基，即

![img](http://img.blog.csdn.net/20150123202328388)

则可得到

![img](http://img.blog.csdn.net/20150123165814334)

继而可以得到A矩阵的奇异值分解：

​                                                 ![img](http://img.blog.csdn.net/20150123170018218)

​                ![img](http://img.blog.csdn.net/20150123170122018)

现在可以来对A矩阵的映射过程进行分析了：如果在n维空间中找到一个（超）矩形，其边都落在A'A的特征向量的方向上，那么经过A变换后的形状仍然为（超）矩形！

vi为A'A的特征向量，称为A的右奇异向量，ui=Avi实际上为AA'的特征向量，称为A的左奇异向量。下面利用SVD证明文章一开始的满秩分解：

![img](http://img.blog.csdn.net/20150123170421531)

利用矩阵分块乘法展开得：

![img](http://img.blog.csdn.net/20150123171001047)

可以看到第二项为0，有

​                               ![img](http://img.blog.csdn.net/20150123171137580)

令

![img](http://img.blog.csdn.net/20150123171202821)

​            ![img](http://img.blog.csdn.net/20150123171215379)

则A=XY即是A的满秩分解。

整个SVD的推导过程就是这样，后面会介绍SVD在推荐系统中的具体应用，也就是复现Koren论文中的[算法](http://lib.csdn.net/base/datastructure)以及其推导过程。

参考文献：[A Singularly Valuable Decomposition The SVD of a Matrix](http://www-users.math.umn.edu/~lerman/math5467/svd.pdf)

## SVD在推荐系统中的应用