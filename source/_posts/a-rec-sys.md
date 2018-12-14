---
title: 记又一次推荐系统
date: 2018-12-14 15:09:15
tags: 数据分析
category: 教程
---

罗平老师在讲数据挖掘的时候大致提供了以下几种方式：

![](https://ws3.sinaimg.cn/large/006tNbRwly1fy6b0vq6uyj30bi0jgtal.jpg)

## 0.数据

**数据集描述**

从国内某著名财经新闻网站—财新网随机选取了10000名用户，并抽取了这10000名用户在2014年3月的所有新闻浏览记录，每条记录包括用户编号、新闻编号、浏览时间（精确到秒）以及新闻文本内容，其中用户编号已做匿名化处理，防止暴露用户隐私。

数据格式说明如下：

**训练集数据：**训练集数据每一行为一个浏览记录，该行浏览记录包含6个字段，分别记录一下信息：

**用户编号**	     **新闻编号**  	**浏览时间**	   **新闻标题**	**新闻详细内容**	**新闻发表时间**，

字段之间用table符即”\t”隔开，文本编码为utf8编码格式，如下为截取训练集中的一行：

​	![](https://ws2.sinaimg.cn/large/006tNbRwly1fxp50f1fpjj30bj00nmx7.jpg)



## 1.非个性化推荐

对于没有历史记录的用户，提供了目前热门新闻。

![](https://ws1.sinaimg.cn/large/006tNbRwly1fy68pk87ygj32ko0sswoa.jpg)

## 2.基于内容的推荐

本项目中考虑到了新闻本身所具有的特征，利用CNN和jieba分词，抽取了主题和标签。

### 抽取标签

这里使用的是[fxsjy/jieba](https://github.com/fxsjy/jieba)，对标题的实体词进行了提取。

结果如下：

```
分词前：
   标题： 消失前的马航370
分词后：
[('马航', 3.9849225009666664),('370', 3.9849225009666664), ('消失', 2.074425740486667)]
```

### 抽取主题

这里参考了[gaussic/text-classification-cnn-rnn](https://github.com/gaussic/text-classification-cnn-rnn),使用[THUCTC: 一个高效的中文文本分类工具包](http://thuctc.thunlp.org/)和CNN进行了训练。

具体过程，见[我的Google Colab](https://colab.research.google.com/drive/1wZyWCByPzBnrPYtXFRnQnLk4QTBRzWXc)

训练数据有6500条新闻，共10个主题。类别如下：

```
体育, 财经, 房产, 家居, 教育, 科技, 时尚, 时政, 游戏, 娱乐
```

训练效果

```
Training and evaluating...
Epoch: 1
Iter:      0, Train Loss:    2.3, Train Acc:  10.94%, Val Loss:    2.3, Val Acc:   9.92%, Time: 0:00:03 *
Iter:    100, Train Loss:   0.84, Train Acc:  78.12%, Val Loss:    1.2, Val Acc:  66.86%, Time: 0:00:07 *
Iter:    200, Train Loss:    0.6, Train Acc:  79.69%, Val Loss:    0.6, Val Acc:  79.30%, Time: 0:00:11 *
Iter:    300, Train Loss:   0.32, Train Acc:  90.62%, Val Loss:   0.43, Val Acc:  86.24%, Time: 0:00:15 *
Iter:    400, Train Loss:   0.27, Train Acc:  92.19%, Val Loss:   0.32, Val Acc:  90.82%, Time: 0:00:19 *
Iter:    500, Train Loss:   0.24, Train Acc:  92.19%, Val Loss:   0.28, Val Acc:  92.32%, Time: 0:00:23 *
Iter:    600, Train Loss:   0.25, Train Acc:  95.31%, Val Loss:    0.3, Val Acc:  90.72%, Time: 0:00:26 
Iter:    700, Train Loss:   0.21, Train Acc:  92.19%, Val Loss:   0.29, Val Acc:  91.46%, Time: 0:00:30 
Epoch: 2
Iter:    800, Train Loss:   0.18, Train Acc:  93.75%, Val Loss:   0.27, Val Acc:  92.48%, Time: 0:00:34 *
Iter:    900, Train Loss:  0.094, Train Acc:  96.88%, Val Loss:   0.29, Val Acc:  92.60%, Time: 0:00:38 *
Iter:   1000, Train Loss:  0.046, Train Acc: 100.00%, Val Loss:   0.26, Val Acc:  92.02%, Time: 0:00:41 
Iter:   1100, Train Loss:   0.16, Train Acc:  96.88%, Val Loss:   0.24, Val Acc:  92.98%, Time: 0:00:45 *
Iter:   1200, Train Loss:   0.14, Train Acc:  95.31%, Val Loss:   0.24, Val Acc:  93.08%, Time: 0:00:49 *
Iter:   1300, Train Loss:   0.08, Train Acc:  98.44%, Val Loss:   0.23, Val Acc:  92.82%, Time: 0:00:52 
Iter:   1400, Train Loss:  0.076, Train Acc:  98.44%, Val Loss:   0.23, Val Acc:  93.10%, Time: 0:00:56 *
Iter:   1500, Train Loss:  0.082, Train Acc:  95.31%, Val Loss:   0.22, Val Acc:  93.82%, Time: 0:01:00 *
Epoch: 3
Iter:   1600, Train Loss:  0.058, Train Acc:  98.44%, Val Loss:    0.2, Val Acc:  94.40%, Time: 0:01:03 *
Iter:   1700, Train Loss:  0.092, Train Acc:  96.88%, Val Loss:   0.24, Val Acc:  92.74%, Time: 0:01:07 
Iter:   1800, Train Loss:  0.095, Train Acc:  95.31%, Val Loss:   0.22, Val Acc:  93.32%, Time: 0:01:11 
Iter:   1900, Train Loss:  0.048, Train Acc:  98.44%, Val Loss:   0.24, Val Acc:  93.12%, Time: 0:01:14 
Iter:   2000, Train Loss:  0.012, Train Acc: 100.00%, Val Loss:   0.23, Val Acc:  93.16%, Time: 0:01:18 
Iter:   2100, Train Loss:   0.13, Train Acc:  96.88%, Val Loss:   0.25, Val Acc:  93.24%, Time: 0:01:22 
Iter:   2200, Train Loss:  0.023, Train Acc: 100.00%, Val Loss:   0.22, Val Acc:  93.76%, Time: 0:01:25 
Iter:   2300, Train Loss:   0.14, Train Acc:  96.88%, Val Loss:   0.24, Val Acc:  93.00%, Time: 0:01:29 
Epoch: 4
Iter:   2400, Train Loss:   0.09, Train Acc:  98.44%, Val Loss:   0.25, Val Acc:  92.18%, Time: 0:01:32 
Iter:   2500, Train Loss:  0.077, Train Acc:  98.44%, Val Loss:   0.22, Val Acc:  93.72%, Time: 0:01:36 
Iter:   2600, Train Loss:   0.12, Train Acc:  96.88%, Val Loss:   0.23, Val Acc:  93.68%, Time: 0:01:40 
No optimization for a long time, auto-stopping...
```

测试效果：

```
Testing...
Test Loss:   0.11, Test Acc:  96.85%
Precision, Recall and F1-Score...
              precision    recall  f1-score   support

          体育       0.99      0.99      0.99      1000
          财经       0.95      0.99      0.97      1000
          房产       1.00      1.00      1.00      1000
          家居       0.98      0.91      0.94      1000
          教育       0.95      0.93      0.94      1000
          科技       0.94      0.98      0.96      1000
          时尚       0.98      0.98      0.98      1000
          时政       0.94      0.95      0.94      1000
          游戏       0.98      0.98      0.98      1000
          娱乐       0.98      0.97      0.98      1000

   micro avg       0.97      0.97      0.97     10000
   macro avg       0.97      0.97      0.97     10000
weighted avg       0.97      0.97      0.97     10000

Confusion Matrix...
[[995   0   0   0   2   0   0   2   0   1]
 [  0 989   0   0   2   3   0   6   0   0]
 [  0   1 997   1   1   0   0   0   0   0]
 [  2  25   2 906  11  15   8  25   1   5]
 [  5   6   0   4 929  16   6  27   3   4]
 [  1   0   0   2   5 983   1   3   5   0]
 [  1   0   0   3   4   4 978   0   3   7]
 [  1  12   0   3  14  16   0 952   1   1]
 [  0   1   0   1   4   2   4   2 984   2]
 [  2   3   0   4   5   6   4   0   4 972]]
Time usage: 0:00:08
```

### 推荐

1.基于用户已阅读的新闻，进行分析。能够找到用户目前关心的问题。

![](https://ws4.sinaimg.cn/large/006tNbRwly1fy68om8ixzj31xb0u079c.jpg)

2.根据其余新闻的主题和标签权重，推荐给用户目前关心的新闻

![](https://ws1.sinaimg.cn/large/006tNbRwly1fy68pk87ygj32ko0sswoa.jpg)

3.同理可以推荐给用户推荐关注同一主题和标签相似的用户

4.也可以给新闻推荐相关新闻和潜在阅读的用户

## 3.协同过滤

1.SVD

![](https://ws2.sinaimg.cn/large/006tNbRwly1fy6by05szpj30u00vhahu.jpg)

```python
class SVD(AlgoBase):

    def __init__(self, n_factors=100, n_epochs=20, biased=True, init_mean=0,
                 init_std_dev=.1, lr_all=.005,
                 reg_all=.02, lr_bu=None, lr_bi=None, lr_pu=None, lr_qi=None,
                 reg_bu=None, reg_bi=None, reg_pu=None, reg_qi=None,
                 random_state=None, verbose=False):

        self.n_factors = n_factors
        self.n_epochs = n_epochs
        self.biased = biased
        self.init_mean = init_mean
        self.init_std_dev = init_std_dev
        self.lr_bu = lr_bu if lr_bu is not None else lr_all
        self.lr_bi = lr_bi if lr_bi is not None else lr_all
        self.lr_pu = lr_pu if lr_pu is not None else lr_all
        self.lr_qi = lr_qi if lr_qi is not None else lr_all
        self.reg_bu = reg_bu if reg_bu is not None else reg_all
        self.reg_bi = reg_bi if reg_bi is not None else reg_all
        self.reg_pu = reg_pu if reg_pu is not None else reg_all
        self.reg_qi = reg_qi if reg_qi is not None else reg_all
        self.random_state = random_state
        self.verbose = verbose

        AlgoBase.__init__(self)

    def fit(self, trainset):

        AlgoBase.fit(self, trainset)
        self.sgd(trainset)

        return self

    def sgd(self, trainset):


        # user biases
        cdef np.ndarray[np.double_t] bu
        # item biases
        cdef np.ndarray[np.double_t] bi
        # user factors
        cdef np.ndarray[np.double_t, ndim=2] pu
        # item factors
        cdef np.ndarray[np.double_t, ndim=2] qi

        cdef int u, i, f
        cdef double r, err, dot, puf, qif
        cdef double global_mean = self.trainset.global_mean

        cdef double lr_bu = self.lr_bu
        cdef double lr_bi = self.lr_bi
        cdef double lr_pu = self.lr_pu
        cdef double lr_qi = self.lr_qi

        cdef double reg_bu = self.reg_bu
        cdef double reg_bi = self.reg_bi
        cdef double reg_pu = self.reg_pu
        cdef double reg_qi = self.reg_qi

        rng = get_rng(self.random_state)

        bu = np.zeros(trainset.n_users, np.double)
        bi = np.zeros(trainset.n_items, np.double)
        pu = rng.normal(self.init_mean, self.init_std_dev,
                        (trainset.n_users, self.n_factors))
        qi = rng.normal(self.init_mean, self.init_std_dev,
                        (trainset.n_items, self.n_factors))

        if not self.biased:
            global_mean = 0

        for current_epoch in range(self.n_epochs):
            if self.verbose:
                print("Processing epoch {}".format(current_epoch))
            for u, i, r in trainset.all_ratings():

                # compute current error
                dot = 0  # <q_i, p_u>
                for f in range(self.n_factors):
                    dot += qi[i, f] * pu[u, f]
                err = r - (global_mean + bu[u] + bi[i] + dot)

                # update biases
                if self.biased:
                    bu[u] += lr_bu * (err - reg_bu * bu[u])
                    bi[i] += lr_bi * (err - reg_bi * bi[i])

                # update factors
                for f in range(self.n_factors):
                    puf = pu[u, f]
                    qif = qi[i, f]
                    pu[u, f] += lr_pu * (err * qif - reg_pu * puf)
                    qi[i, f] += lr_qi * (err * puf - reg_qi * qif)

        self.bu = bu
        self.bi = bi
        self.pu = pu
        self.qi = qi

    def estimate(self, u, i):
        # Should we cythonize this as well?

        known_user = self.trainset.knows_user(u)
        known_item = self.trainset.knows_item(i)

        if self.biased:
            est = self.trainset.global_mean

            if known_user:
                est += self.bu[u]

            if known_item:
                est += self.bi[i]

            if known_user and known_item:
                est += np.dot(self.qi[i], self.pu[u])

        else:
            if known_user and known_item:
                est = np.dot(self.qi[i], self.pu[u])
            else:
                raise PredictionImpossible('User and item are unkown.')

        return est
```



在前20天的数据上进行了测试，效果并不佳，分析原因应该rating的评分只有{0,1}

而SVD比较适用的场景是已知用户rating{0,1,2,3,4,5}预测出[0,5]的rating

```
Evaluating RMSE, MAE of algorithm SVD on 5 split(s).

                  Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std     
RMSE (testset)    3.1992  3.1094  2.7596  2.9421  2.2683  2.8557  0.3299  
MAE (testset)     1.9766  0.2567  0.2586  1.9881  1.9611  1.2882  0.8415  
Fit time          2.99    3.12    3.09    3.00    3.10    3.06    0.05    
Test time         0.12    0.09    0.12    0.11    0.15    0.12    0.02    
user: 5218791    item: 100642618  r_ui = None   est = 3.00   {'was_impossible': False}
```

接着用SVD++和NMF进行了测试，结果如下

2.SVD++

![](https://ws2.sinaimg.cn/large/006tNbRwly1fy6byus9euj31260t2n30.jpg)

```python
class SVDpp(AlgoBase):

    def __init__(self, n_factors=20, n_epochs=20, init_mean=0, init_std_dev=.1,
                 lr_all=.007, reg_all=.02, lr_bu=None, lr_bi=None, lr_pu=None,
                 lr_qi=None, lr_yj=None, reg_bu=None, reg_bi=None, reg_pu=None,
                 reg_qi=None, reg_yj=None, random_state=None, verbose=False):

        self.n_factors = n_factors
        self.n_epochs = n_epochs
        self.init_mean = init_mean
        self.init_std_dev = init_std_dev
        self.lr_bu = lr_bu if lr_bu is not None else lr_all
        self.lr_bi = lr_bi if lr_bi is not None else lr_all
        self.lr_pu = lr_pu if lr_pu is not None else lr_all
        self.lr_qi = lr_qi if lr_qi is not None else lr_all
        self.lr_yj = lr_yj if lr_yj is not None else lr_all
        self.reg_bu = reg_bu if reg_bu is not None else reg_all
        self.reg_bi = reg_bi if reg_bi is not None else reg_all
        self.reg_pu = reg_pu if reg_pu is not None else reg_all
        self.reg_qi = reg_qi if reg_qi is not None else reg_all
        self.reg_yj = reg_yj if reg_yj is not None else reg_all
        self.random_state = random_state
        self.verbose = verbose

        AlgoBase.__init__(self)

    def fit(self, trainset):

        AlgoBase.fit(self, trainset)
        self.sgd(trainset)

        return self

    def sgd(self, trainset):

        # user biases
        cdef np.ndarray[np.double_t] bu
        # item biases
        cdef np.ndarray[np.double_t] bi
        # user factors
        cdef np.ndarray[np.double_t, ndim=2] pu
        # item factors
        cdef np.ndarray[np.double_t, ndim=2] qi
        # item implicit factors
        cdef np.ndarray[np.double_t, ndim=2] yj

        cdef int u, i, j, f
        cdef double r, err, dot, puf, qif, sqrt_Iu, _
        cdef double global_mean = self.trainset.global_mean
        cdef np.ndarray[np.double_t] u_impl_fdb

        cdef double lr_bu = self.lr_bu
        cdef double lr_bi = self.lr_bi
        cdef double lr_pu = self.lr_pu
        cdef double lr_qi = self.lr_qi
        cdef double lr_yj = self.lr_yj

        cdef double reg_bu = self.reg_bu
        cdef double reg_bi = self.reg_bi
        cdef double reg_pu = self.reg_pu
        cdef double reg_qi = self.reg_qi
        cdef double reg_yj = self.reg_yj

        bu = np.zeros(trainset.n_users, np.double)
        bi = np.zeros(trainset.n_items, np.double)

        rng = get_rng(self.random_state)

        pu = rng.normal(self.init_mean, self.init_std_dev,
                        (trainset.n_users, self.n_factors))
        qi = rng.normal(self.init_mean, self.init_std_dev,
                        (trainset.n_items, self.n_factors))
        yj = rng.normal(self.init_mean, self.init_std_dev,
                        (trainset.n_items, self.n_factors))
        u_impl_fdb = np.zeros(self.n_factors, np.double)

        for current_epoch in range(self.n_epochs):
            if self.verbose:
                print(" processing epoch {}".format(current_epoch))
            for u, i, r in trainset.all_ratings():

                # items rated by u. This is COSTLY
                Iu = [j for (j, _) in trainset.ur[u]]
                sqrt_Iu = np.sqrt(len(Iu))

                # compute user implicit feedback
                u_impl_fdb = np.zeros(self.n_factors, np.double)
                for j in Iu:
                    for f in range(self.n_factors):
                        u_impl_fdb[f] += yj[j, f] / sqrt_Iu

                # compute current error
                dot = 0  # <q_i, (p_u + sum_{j in Iu} y_j / sqrt{Iu}>
                for f in range(self.n_factors):
                    dot += qi[i, f] * (pu[u, f] + u_impl_fdb[f])

                err = r - (global_mean + bu[u] + bi[i] + dot)

                # update biases
                bu[u] += lr_bu * (err - reg_bu * bu[u])
                bi[i] += lr_bi * (err - reg_bi * bi[i])

                # update factors
                for f in range(self.n_factors):
                    puf = pu[u, f]
                    qif = qi[i, f]
                    pu[u, f] += lr_pu * (err * qif - reg_pu * puf)
                    qi[i, f] += lr_qi * (err * (puf + u_impl_fdb[f]) -
                                         reg_qi * qif)
                    for j in Iu:
                        yj[j, f] += lr_yj * (err * qif / sqrt_Iu -
                                             reg_yj * yj[j, f])

        self.bu = bu
        self.bi = bi
        self.pu = pu
        self.qi = qi
        self.yj = yj

    def estimate(self, u, i):

        est = self.trainset.global_mean

        if self.trainset.knows_user(u):
            est += self.bu[u]

        if self.trainset.knows_item(i):
            est += self.bi[i]

        if self.trainset.knows_user(u) and self.trainset.knows_item(i):
            Iu = len(self.trainset.ur[u])  # nb of items rated by u
            u_impl_feedback = (sum(self.yj[j] for (j, _)
                               in self.trainset.ur[u]) / np.sqrt(Iu))
            est += np.dot(self.qi[i], self.pu[u] + u_impl_feedback)

        return est
```

测试结果

```
Evaluating RMSE, MAE of algorithm SVDpp on 5 split(s).

                  Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std     
RMSE (testset)    3.5485  2.1529  3.7026  3.5110  2.2989  3.0428  0.6717  
MAE (testset)     1.9857  1.9543  1.9847  1.9908  1.9644  1.9760  0.0141  
Fit time          21.72   21.36   22.19   22.13   22.26   21.93   0.34    
Test time         0.39    0.43    0.40    0.44    0.39    0.41    0.02    
user: 5218791    item: 100642618  r_ui = None   est = 3.00   {'was_impossible': False}
```



3.NMF

![](https://ws4.sinaimg.cn/large/006tNbRwly1fy6bygl93zj30u00x1ai5.jpg)

```python
class NMF(AlgoBase):

    def __init__(self, n_factors=15, n_epochs=50, biased=False, reg_pu=.06,
                 reg_qi=.06, reg_bu=.02, reg_bi=.02, lr_bu=.005, lr_bi=.005,
                 init_low=0, init_high=1, random_state=None, verbose=False):

        self.n_factors = n_factors
        self.n_epochs = n_epochs
        self.biased = biased
        self.reg_pu = reg_pu
        self.reg_qi = reg_qi
        self.lr_bu = lr_bu
        self.lr_bi = lr_bi
        self.reg_bu = reg_bu
        self.reg_bi = reg_bi
        self.init_low = init_low
        self.init_high = init_high
        self.random_state = random_state
        self.verbose = verbose

        if self.init_low < 0:
            raise ValueError('init_low should be greater than zero')

        AlgoBase.__init__(self)

    def fit(self, trainset):

        AlgoBase.fit(self, trainset)
        self.sgd(trainset)

        return self

    def sgd(self, trainset):

        # user and item factors
        cdef np.ndarray[np.double_t, ndim=2] pu
        cdef np.ndarray[np.double_t, ndim=2] qi

        # user and item biases
        cdef np.ndarray[np.double_t] bu
        cdef np.ndarray[np.double_t] bi

        # auxiliary matrices used in optimization process
        cdef np.ndarray[np.double_t, ndim=2] user_num
        cdef np.ndarray[np.double_t, ndim=2] user_denom
        cdef np.ndarray[np.double_t, ndim=2] item_num
        cdef np.ndarray[np.double_t, ndim=2] item_denom

        cdef int u, i, f
        cdef double r, est, l, dot, err
        cdef double reg_pu = self.reg_pu
        cdef double reg_qi = self.reg_qi
        cdef double reg_bu = self.reg_bu
        cdef double reg_bi = self.reg_bi
        cdef double lr_bu = self.lr_bu
        cdef double lr_bi = self.lr_bi
        cdef double global_mean = self.trainset.global_mean

        # Randomly initialize user and item factors
        rng = get_rng(self.random_state)
        pu = rng.uniform(self.init_low, self.init_high,
                         size=(trainset.n_users, self.n_factors))
        qi = rng.uniform(self.init_low, self.init_high,
                         size=(trainset.n_items, self.n_factors))

        bu = np.zeros(trainset.n_users, np.double)
        bi = np.zeros(trainset.n_items, np.double)

        if not self.biased:
            global_mean = 0

        for current_epoch in range(self.n_epochs):

            if self.verbose:
                print("Processing epoch {}".format(current_epoch))

            # (re)initialize nums and denoms to zero
            user_num = np.zeros((trainset.n_users, self.n_factors))
            user_denom = np.zeros((trainset.n_users, self.n_factors))
            item_num = np.zeros((trainset.n_items, self.n_factors))
            item_denom = np.zeros((trainset.n_items, self.n_factors))

            # Compute numerators and denominators for users and items factors
            for u, i, r in trainset.all_ratings():

                # compute current estimation and error
                dot = 0  # <q_i, p_u>
                for f in range(self.n_factors):
                    dot += qi[i, f] * pu[u, f]
                est = global_mean + bu[u] + bi[i] + dot
                err = r - est

                # update biases
                if self.biased:
                    bu[u] += lr_bu * (err - reg_bu * bu[u])
                    bi[i] += lr_bi * (err - reg_bi * bi[i])

                # compute numerators and denominators
                for f in range(self.n_factors):
                    user_num[u, f] += qi[i, f] * r
                    user_denom[u, f] += qi[i, f] * est
                    item_num[i, f] += pu[u, f] * r
                    item_denom[i, f] += pu[u, f] * est

            # Update user factors
            for u in trainset.all_users():
                n_ratings = len(trainset.ur[u])
                for f in range(self.n_factors):
                    user_denom[u, f] += n_ratings * reg_pu * pu[u, f]
                    pu[u, f] *= user_num[u, f] / user_denom[u, f]

            # Update item factors
            for i in trainset.all_items():
                n_ratings = len(trainset.ir[i])
                for f in range(self.n_factors):
                    item_denom[i, f] += n_ratings * reg_qi * qi[i, f]
                    qi[i, f] *= item_num[i, f] / item_denom[i, f]

        self.bu = bu
        self.bi = bi
        self.pu = pu
        self.qi = qi

    def estimate(self, u, i):
        # Should we cythonize this as well?

        known_user = self.trainset.knows_user(u)
        known_item = self.trainset.knows_item(i)

        if self.biased:
            est = self.trainset.global_mean

            if known_user:
                est += self.bu[u]

            if known_item:
                est += self.bi[i]

            if known_user and known_item:
                est += np.dot(self.qi[i], self.pu[u])

        else:
            if known_user and known_item:
                est = np.dot(self.qi[i], self.pu[u])
            else:
                raise PredictionImpossible('User and item are unkown.')

        return est
```

测试结果：

```
Evaluating RMSE, MAE of algorithm NMF on 5 split(s).

                  Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std     
RMSE (testset)    1.4553  3.1385  2.6589  3.1678  1.3156  2.3472  0.8070  
MAE (testset)     0.2974  0.3051  0.3071  0.3158  0.2926  0.3036  0.0080  
Fit time          3.63    3.93    3.79    3.78    3.84    3.80    0.10    
Test time         0.10    0.11    0.10    0.07    0.10    0.10    0.02    
user: 5218791    item: 100642618  r_ui = None   est = 0.77   {'was_impossible': False}
```

4.KNN

测试结果

`KNN-withMeans`

```
Evaluating RMSE, MAE of algorithm KNNWithMeans on 5 split(s).

                  Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std     
RMSE (testset)    2.0990  1.2991  2.6015  2.8567  3.1200  2.3953  0.6434  
MAE (testset)     0.2634  0.2485  0.2582  0.2585  0.2702  0.2597  0.0071  
Fit time          6.13    6.01    5.97    5.98    6.02    6.02    0.06    
Test time         3.22    3.10    3.12    3.06    3.10    3.12    0.05    
Computing the pearson_baseline similarity matrix...
Done computing similarity matrix.
user: 5218791    item: 100642618  r_ui = None   est = 1.00   {'actual_k': 0, 'was_impossible': False}
```
`KNNwithZScore`

```
Evaluating RMSE, MAE of algorithm KNNWithZScore on 5 split(s).

                  Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std     
RMSE (testset)    3.8673  1.3135  2.9476  1.1390  2.1894  2.2914  1.0207  
MAE (testset)     0.3336  0.3354  0.3437  0.3326  0.3481  0.3387  0.0061  
Fit time          6.15    6.18    6.16    6.85    6.63    6.39    0.29    
Test time         3.18    3.13    3.74    3.55    3.51    3.42    0.23    
Computing the pearson_baseline similarity matrix...
Done computing similarity matrix.
user: 5218791    item: 100642618  r_ui = None   est = 1.00   {'actual_k': 0, 'was_impossible': False}
```

5.SlopeOne

![](https://ws1.sinaimg.cn/large/006tNbRwly1fy6c3xrt5kj311i0lc41r.jpg)

```python
class SlopeOne(AlgoBase):

    def __init__(self):

        AlgoBase.__init__(self)

    def fit(self, trainset):

        n_items = trainset.n_items

        # Number of users having rated items i and j: |U_ij|
        cdef np.ndarray[np.int_t, ndim=2] freq
        # Deviation from item i to item j: mean(r_ui - r_uj for u in U_ij)
        cdef np.ndarray[np.double_t, ndim=2] dev

        cdef int u, i, j, r_ui, r_uj

        AlgoBase.fit(self, trainset)

        freq = np.zeros((trainset.n_items, trainset.n_items), np.int)
        dev = np.zeros((trainset.n_items, trainset.n_items), np.double)

        # Computation of freq and dev arrays.
        for u, u_ratings in iteritems(trainset.ur):
            for i, r_ui in u_ratings:
                for j, r_uj in u_ratings:
                    freq[i, j] += 1
                    dev[i, j] += r_ui - r_uj

        for i in range(n_items):
            dev[i, i] = 0
            for j in range(i + 1, n_items):
                dev[i, j] /= freq[i, j]
                dev[j, i] = -dev[i, j]

        self.freq = freq
        self.dev = dev

        # mean ratings of all users: mu_u
        self.user_mean = [np.mean([r for (_, r) in trainset.ur[u]])
                          for u in trainset.all_users()]

        return self

    def estimate(self, u, i):

        if not (self.trainset.knows_user(u) and self.trainset.knows_item(i)):
            raise PredictionImpossible('User and/or item is unkown.')

        # Ri: relevant items for i. This is the set of items j rated by u that
        # also have common users with i (i.e. at least one user has rated both
        # i and j).
        Ri = [j for (j, _) in self.trainset.ur[u] if self.freq[i, j] > 0]
        est = self.user_mean[u]
        if Ri:
            est += sum(self.dev[i, j] for j in Ri) / len(Ri)

        return est
```



测试结果

```
Evaluating RMSE, MAE of algorithm SlopeOne on 5 split(s).

                  Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std     
RMSE (testset)    1.3812  3.9225  2.1889  3.0699  1.3975  2.3920  0.9853  
MAE (testset)     0.6560  0.6645  0.6779  0.6300  0.6701  0.6597  0.0165  
Fit time          0.66    0.59    0.62    0.62    0.59    0.62    0.03    
Test time         0.39    0.38    0.32    0.37    0.38    0.37    0.02    
user: 5218791    item: 100642618  r_ui = None   est = 0.00   {'was_impossible': False}
```

此时误差较小，但是试了几组数据预测的都不准

6.Co-Clustering

![](https://ws4.sinaimg.cn/large/006tNbRwly1fy6c5j5y0zj311y0hyq6j.jpg)

```python
class CoClustering(AlgoBase):

    def __init__(self, n_cltr_u=3, n_cltr_i=3, n_epochs=20, random_state=None,
                 verbose=False):

        AlgoBase.__init__(self)

        self.n_cltr_u = n_cltr_u
        self.n_cltr_i = n_cltr_i
        self.n_epochs = n_epochs
        self.verbose=verbose
        self.random_state = random_state

    def fit(self, trainset):

        # All this implementation was hugely inspired from MyMediaLite:
        # https://github.com/zenogantner/MyMediaLite/blob/master/src/MyMediaLite/RatingPrediction/CoClustering.cs

        AlgoBase.fit(self, trainset)

        # User and item means
        cdef np.ndarray[np.double_t] user_mean
        cdef np.ndarray[np.double_t] item_mean

        # User and items clusters
        cdef np.ndarray[np.int_t] cltr_u
        cdef np.ndarray[np.int_t] cltr_i

        # Average rating of user clusters, item clusters and co-clusters
        cdef np.ndarray[np.double_t] avg_cltr_u
        cdef np.ndarray[np.double_t] avg_cltr_i
        cdef np.ndarray[np.double_t, ndim=2] avg_cocltr

        cdef np.ndarray[np.double_t] errors
        cdef int u, i, r, uc, ic
        cdef double est

        # Randomly assign users and items to intial clusters
        rng = get_rng(self.random_state)
        cltr_u = rng.randint(self.n_cltr_u, size=trainset.n_users)
        cltr_i = rng.randint(self.n_cltr_i, size=trainset.n_items)

        # Compute user and item means
        user_mean = np.zeros(self.trainset.n_users, np.double)
        item_mean = np.zeros(self.trainset.n_items, np.double)
        for u in trainset.all_users():
            user_mean[u] = np.mean([r for (_, r) in trainset.ur[u]])
        for i in trainset.all_items():
            item_mean[i] = np.mean([r for (_, r) in trainset.ir[i]])

        # Optimization loop. This could be optimized a bit by checking if
        # clusters where effectively updated and early stop if they did not.
        for epoch in range(self.n_epochs):

            if self.verbose:
                print("Processing epoch {}".format(epoch))

            # Update averages of clusters
            avg_cltr_u, avg_cltr_i, avg_cocltr = self.compute_averages(cltr_u,
                                                                       cltr_i)
            # set user cluster to the one that minimizes squarred error of all
            # the user's ratings.
            for u in self.trainset.all_users():
                errors = np.zeros(self.n_cltr_u, np.double)
                for uc in range(self.n_cltr_u):
                    for i, r in self.trainset.ur[u]:
                        ic = cltr_i[i]
                        est = (avg_cocltr[uc, ic] +
                               user_mean[u] - avg_cltr_u[uc] +
                               item_mean[i] - avg_cltr_i[ic])
                        errors[uc] += (r - est)**2
                cltr_u[u] = np.argmin(errors)

            # set item cluster to the one that minimizes squarred error over
            # all the item's ratings.
            for i in self.trainset.all_items():
                errors = np.zeros(self.n_cltr_i, np.double)
                for ic in range(self.n_cltr_i):
                    for u, r in self.trainset.ir[i]:
                        uc = cltr_u[u]
                        est = (avg_cocltr[uc, ic] +
                               user_mean[u] - avg_cltr_u[uc] +
                               item_mean[i] - avg_cltr_i[ic])
                        errors[ic] += (r - est)**2
                cltr_i[i] = np.argmin(errors)

        # Compute averages one last time as clusters may have change
        avg_cltr_u, avg_cltr_i, avg_cocltr = self.compute_averages(cltr_u,
                                                                   cltr_i)
        # Set cdefed arrays as attributes as they are needed for prediction
        self.cltr_u = cltr_u
        self.cltr_i = cltr_i

        self.user_mean = user_mean
        self.item_mean = item_mean

        self.avg_cltr_u = avg_cltr_u
        self.avg_cltr_i = avg_cltr_i
        self.avg_cocltr = avg_cocltr

        return self

    def compute_averages(self, np.ndarray[np.int_t] cltr_u,
                         np.ndarray[np.int_t] cltr_i):

        # Number of entities in user clusters, item clusters and co-clusters.
        cdef np.ndarray[np.int_t] count_cltr_u
        cdef np.ndarray[np.int_t] count_cltr_i
        cdef np.ndarray[np.int_t, ndim=2] count_cocltr

        # Sum of ratings for entities in each cluster
        cdef np.ndarray[np.int_t] sum_cltr_u
        cdef np.ndarray[np.int_t] sum_cltr_i
        cdef np.ndarray[np.int_t, ndim=2] sum_cocltr

        # The averages of each cluster (what will be returned)
        cdef np.ndarray[np.double_t] avg_cltr_u
        cdef np.ndarray[np.double_t] avg_cltr_i
        cdef np.ndarray[np.double_t, ndim=2] avg_cocltr

        cdef int u, i, r, uc, ic
        cdef double global_mean = self.trainset.global_mean

        # Initialize everything to zero
        count_cltr_u = np.zeros(self.n_cltr_u, np.int)
        count_cltr_i = np.zeros(self.n_cltr_i, np.int)
        count_cocltr = np.zeros((self.n_cltr_u, self.n_cltr_i), np.int)

        sum_cltr_u = np.zeros(self.n_cltr_u, np.int)
        sum_cltr_i = np.zeros(self.n_cltr_i, np.int)
        sum_cocltr = np.zeros((self.n_cltr_u, self.n_cltr_i), np.int)

        avg_cltr_u = np.zeros(self.n_cltr_u, np.double)
        avg_cltr_i = np.zeros(self.n_cltr_i, np.double)
        avg_cocltr = np.zeros((self.n_cltr_u, self.n_cltr_i), np.double)

        # Compute counts and sums for every cluster.
        for u, i, r in self.trainset.all_ratings():
            uc = cltr_u[u]
            ic = cltr_i[i]

            count_cltr_u[uc] += 1
            count_cltr_i[ic] += 1
            count_cocltr[uc, ic] += 1

            sum_cltr_u[uc] += r
            sum_cltr_i[ic] += r
            sum_cocltr[uc, ic] += r

        # Then set the averages for users...
        for uc in range(self.n_cltr_u):
            if count_cltr_u[uc]:
                avg_cltr_u[uc] = sum_cltr_u[uc] / count_cltr_u[uc]
            else:
                avg_cltr_u[uc] = global_mean

        # ... for items
        for ic in range(self.n_cltr_i):
            if count_cltr_i[ic]:
                avg_cltr_i[ic] = sum_cltr_i[ic] / count_cltr_i[ic]
            else:
                avg_cltr_i[ic] = global_mean

        # ... and for co-clusters
        for uc in range(self.n_cltr_u):
            for ic in range(self.n_cltr_i):
                if count_cocltr[uc, ic]:
                    avg_cocltr[uc, ic] = (sum_cocltr[uc, ic] /
                                          count_cocltr[uc, ic])
                else:
                    avg_cocltr[uc, ic] = global_mean

        return avg_cltr_u, avg_cltr_i, avg_cocltr

    def estimate(self, u, i):

        if not (self.trainset.knows_user(u) and self.trainset.knows_item(i)):
            return self.trainset.global_mean

        if not self.trainset.knows_user(u):
            return self.cltr_i[i]

        if not self.trainset.knows_item(i):
            return self.cltr_u[u]

        # I doubt cdefing makes any difference here as cython has no clue about
        # arrays self.stuff... But maybe?
        cdef int _u = u
        cdef int _i = i
        cdef int uc = self.cltr_u[_u]
        cdef int ic = self.cltr_i[_i]
        cdef double est

        est = (self.avg_cocltr[uc, ic] +
               self.user_mean[_u] - self.avg_cltr_u[uc] +
               self.item_mean[_i] - self.avg_cltr_i[ic])

        return est
```

```
Evaluating RMSE, MAE of algorithm CoClustering on 5 split(s).

                  Fold 1  Fold 2  Fold 3  Fold 4  Fold 5  Mean    Std     
RMSE (testset)    4.6504  1.0863  1.3100  2.0196  1.3350  2.0803  1.3226  
MAE (testset)     0.2811  0.2160  0.2247  0.2337  0.2250  0.2361  0.0232  
Fit time          1.79    1.82    1.81    1.81    1.80    1.81    0.01    
Test time         0.11    0.07    0.10    0.10    0.10    0.10    0.02    
user: 5218791    item: 100642618  r_ui = None   est = 0.97   {'was_impossible': False}
```

此方法的误差和准确度都可以了。

## 4.混合推荐

本项目感觉已经考了了混合推荐了，个性化和非个性化。

其实还有一个框架，算是本项目的一个`TODO`:

![https://github.com/lyst/lightfm/raw/master/lightfm.png](https://github.com/lyst/lightfm/raw/master/lightfm.png)

LightFM是针对隐式和显式反馈的许多流行推荐算法的Python实现，包括BPR和WARP排名损失的有效实现。它易于使用，快速（通过多线程模型估计），并产生高质量的结果。

它还可以将项目和用户元数据合并到传统的矩阵分解算法中。它将每个用户和项目表示为其功能的潜在表示的总和，从而允许推荐推广到新项目（通过项目功能）和新用户（通过用户功能）。

## 5.项目构建

选定算法后，使用flask+html实现了一个系统，大致结构如下。

![](https://ws2.sinaimg.cn/large/006tNbRwly1fy6caq2v6jj31fi0u0tdg.jpg)

项目地址：[推荐系统](https://github.com/idejie/recsys_web)

