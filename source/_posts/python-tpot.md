---
title: 在Python中自动化你的机器学习-TPOT和基因算法
date: 2017-07-25 00:02:01
tags: TPOT
category: Python
---

​	自动化机器学习（AML）是一种流水线（也称管线），它能够让你自动执行机器学习（ML）问题中的重复步骤，从而节省时间，让你专注于使你的专业知识发挥更高价值。 最重要的是，它不仅是一些模糊的想法，而且还有一些基于标准python ML包建立的应用包，如scikit-learn。

​	在这种情况下，任何熟悉机器学习的人都可能会回想起网格搜索（grid search）这个概念。 他们这样想是完全正确的。 实际上，AML是在scikit-learn中应用的网格搜索的扩展，而不是迭代这些值预先定义的集合和其组合，它通过搜索方法，特征，变换和参数值来获得最佳解决方案。 因此，AML“网格搜索”不需要在可能的配置空间上进行详尽的搜索 - AML有一个很赞的应用叫做TPOT包，其提供了像 遗传算法这样的应用，可用来在某个配置中混合各个参数并达到最佳设置。

​	在这篇文章中，我将简要介绍一些AML的基础知识，然后在应用中使用TPOT软件包，并且包括遗传算法解决方案的优化问题。

#基础概念
​	基本概念非常简单，一旦我们收到原始数据，我们就开始使用标准的ML流水线。
![](https://alookanalytics.files.wordpress.com/2017/05/tpot-ml-pipeline.png?w=600&h=286)
​	在这条流水线中，我们有一些针对于给定数据集/问题的步骤，很明显数据清理的自动化是一个问题。 然而，在这个过程中，我们得到以下任务：
- 特征预处理
- 特征选择
- 模型选择
- ...



​	这些任务的共同之处在于，在每个方案中我们先使用一组方法，然后我们评估其性能（特征重要性，模型性能...）。 由于我们对各个步骤有明确的指标，所以我们可以自动化流程。 在这里，我们在方法，特征，变换和参数值中获得AML搜索的最佳解决方案。

Python中的自动机器学习存在以下包：

- TPOT
- Auto-Sklearn
- Auto-Weka
- Machine-JS
  -DataRobot

#优势
​	除了明显的节省时间的特点外，还有其他优点。这个应用的其中一个优点曾发表在 Airbnb的这篇[博客](https://medium.com/airbnb-engineering/automated-machine-learning-a-paradigm-shift-that-accelerates-data-scientist-productivity-airbnb-f1f8a10d61f8)中，就是**能够轻松创建基准**（他们也提到了其他的优点）。 这使我们能够判断现有ML模型的性能，并将他与其他模型的相关值进行关联。

​	另一个优势是**规范作用于任何ML任务的基本方法**。它不是一个经典的文档或指南，而是我们可以准备一个设置，它可以直接让解决这个问题的人使用。

​	此外，它使我们能够**执行快速原型设计的任务**，例如，为用户更好地估计基本模型可以实现的性能，而无需实施它们。 这个结果只是一个配置而且无需执行。

#TPOT包中的AML
我们将看一下在TPOT包中的一个非常基本的样例。最基本的是在TPOT包中分配和拟合一个简单的分类器或者回归器。
```python
from tpot import TPOTClassifier, TPOTRegressor
 
# create instance 
tpot = TPOTClassifier()
# fit instance
tpot.fit(X_train, y_train)
 
# create instance
tpot = TPOTRegressor()
# fit instance
tpot.fit(X_train, y_train)
 
# evaluate performance on test data
tpot.score(X_test, y_test)
 
# export the script used to create the best model
tpot.export('tpot_exported_pipeline.py')
```

脚本的最后一行用于将脚本导出为标准scikit-learn的代码，这使我们能够就当前最佳解决方案对脚本进一步修改/优化。

##基因算法和它的参数
针对TPOT分类器和回归器，我们有一组已提供的参数，样例如下：
```python
class TPOTBase(BaseEstimator):
 
    def __init__(self, generations=100, population_size=100, offspring_size=None,
                 mutation_rate=0.9, crossover_rate=0.1,
                 scoring=None, cv=5, n_jobs=1,
                 max_time_mins=None, max_eval_time_mins=5,
                 random_state=None, config_dict=None, warm_start=False,
                 verbosity=0, disable_update_check=False):

```
许多参数在逻辑上与scikit-learn的参数相符，因此我们不会进一步探索。 相反，我们将看看与TPOT中使用的遗传算法相关的参数（详细列表和使用参数参考[文档](http://rhiever.github.io/tpot/using/)）。

**遗传算法**基于创建初始种群迭代地组合群体成员，从而根据父母的“特征/参数”创建子代的思想。 在每次迭代结束时，我们进行拟合测试，并将把最适合的个体从原始的种群取出+新的种群被创建。 因此，在每次迭代中，我们将创建新的后代，如果后代表现更好，就可以用它们取代现有的个体。 这使得总体性能增加或者至少在每次迭代保持相同。
遗传算法的参数：

- generations – 确定创建子代（新个体）的迭代次数
- population_size – 创建个体的初始数量（这些用于创建后代）
- offspring_size – 每一代所需创造的新个体数
- mutation_rate – 出现属性值随机更改的概率（包括新参数的方法，在初始群体中可能不可用）
- crossover_rate –用于创造后代的个体所占的百分比

使用这个迭代过程，我们选出最佳配置。 准备遗传算法的结果一般取决于初始状态。 因此，它随机产生的初始种群影响输出，重新运行相同的设置可能会输出不同的结果。
##自定义设置词典

不是用潜在的scikit-learn功能的标准值，您可以定义自己的字典，这使您能够合并有关该领域的知识或你所需参数（例如你经历过的并不是对于给定的应用程序的ML算法 ）。 字典的例子如下所示：
```python
classifier_config_dict = {
 
    # Classifiers
    'sklearn.naive_bayes.GaussianNB': {
    },
 
    'sklearn.naive_bayes.BernoulliNB': {
        'alpha': [1e-3, 1e-2, 1e-1, 1., 10., 100.],
        'fit_prior': [True, False]
    },
 
    'sklearn.naive_bayes.MultinomialNB': {
        'alpha': [1e-3, 1e-2, 1e-1, 1., 10., 100.],
        'fit_prior': [True, False]
    },
 
    'sklearn.tree.DecisionTreeClassifier': {
        'criterion': ["gini", "entropy"],
        'max_depth': range(1, 11),
        'min_samples_split': range(2, 21),
        'min_samples_leaf': range(1, 21)
    }
}
```
##Iris样例
这里我们有一个使用scikit-learn所提供的数据集的样例，和TPOT的输出
```python
from tpot import TPOTClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
 
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data.astype(np.float64),
    iris.target.astype(np.float64), train_size=0.8, test_size=0.2)
 
tpot = TPOTClassifier(generations=5, population_size=50, verbosity=2, n_jobs=-1)
tpot.fit(X_train, y_train)
print(tpot.score(X_test, y_test))
 
############ OUTPUT #########################
Optimization Progress:  33%|███▎      | 100/300 [00:25<02:36,  1.28pipeline/s]
Generation 1 - Current best internal CV score: 0.9833333333333334
Optimization Progress:  50%|█████     | 150/300 [00:39<00:58,  2.57pipeline/s]
Generation 2 - Current best internal CV score: 0.9833333333333334
Optimization Progress:  67%|██████▋   | 200/300 [00:52<00:28,  3.48pipeline/s]
Generation 3 - Current best internal CV score: 0.9833333333333334
Optimization Progress:  83%|████████▎ | 250/300 [01:05<00:10,  4.66pipeline/s]
Generation 4 - Current best internal CV score: 0.9833333333333334
                                                                               
Generation 5 - Current best internal CV score: 0.9916666666666668
 
Best pipeline: KNeighborsClassifier(Nystroem(input_matrix, Nystroem__gamma=0.4, Nystroem__kernel=linear, Nystroem__n_components=DEFAULT), KNeighborsClassifier__n_neighbors=12, KNeighborsClassifier__p=1, KNeighborsClassifier__weights=DEFAULT)
0.933333333333
```
更复杂的样例参照TPOT的[样例](https://github.com/rhiever/tpot/tree/master/tutorials)
#总结
自动机器学习使我们能够节省时间并优化你必须具有创造力的代码部分。 它减少了重复的任务，对于这个领域的人来说，不如探索解决问题的新方法那么有趣。 尝试将这些自动化方法融入到你自己的工作流程中，只需确保考虑到计算时间，因为运行在许多集合上会导致计算密集型任务。