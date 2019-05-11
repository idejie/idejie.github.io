---
title: 震惊！9行代码就能搭建一个神经网络
date: 2017-04-07 20:45:49
tags: AI
category: 教程
---

> 原文：[How to build a simple neural network in 9 lines of Python code](https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1)
>
> 以下为翻译

作为学习AI的一部分，我给自己设定了一个在Python中构建一个简单神经网络的目标。为了确保我能真正理解他，我决定从头构建，而不适用神经网络库。感谢Andrew Trask 的博客，我用9行代码实现了。

```python
from numpy import exp, array, random, dot
training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T
random.seed(1)
synaptic_weights = 2 * random.random((3, 1)) - 1
for iteration in xrange(10000):
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
print 1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights))))
```



在这篇博文中，我会解释一下我是如何做到的，所以你也可以建立自己的。 我还提供一个更长的，但更漂亮的源代码版本。

但首先，什么是**神经网络**？

​	 人脑由1000亿个称为神经元的细胞组成，通过突触连接在一起。 如果对神经元有足够的突触输入，那神经元也会发射。 我们把这个过程叫做“思考”。

![](https://blog.idejie.com/pics/how-to-build-a-simple-neural-network-in-9-lines-of-python-code0.jpg)



我们可以通过在计算机上创建一个神经网络来建模这个过程。 没有必要在分子水平上模拟人类大脑的生物复杂性，只是实现其较高级别的规则。 我们使用一种称为矩阵的数学方法，即**数字网格**。 为了使其变得非常简单，我们将模拟单个神经元，具有三个输入和一个输出。

我们要训练神经元来解决下面的问题。 前四个例子称为训练集。 你能锻炼出模式吗？ '**？**'是0或1吗？

![](https://blog.idejie.com/pics/how-to-build-a-simple-neural-network-in-9-lines-of-python-code1.jpg)

您可能已经注意到，输出总是等于最左侧输入列的值。 所以答案是'？'应该是1。

## **训练过程**

但是我们如何教我们的神经元来正确回答这个问题？ 我们将给每个输入一个权重，这可以是一个正数或负数。 具有大正负重或负重的输入将对神经元的输出具有很强的影响。 在开始之前，我们将每个权重设置为随机数。 然后我们开始训练过程：

1. 从训练集示例中获取输入，通过权重进行调整，并通过特殊公式计算神经元的输出。
2. 计算误差，这是训练集示例中神经元输出与期望输出之间的差异。
3. 根据误差的方向，稍微调整权重
4. 重复此过程10,000次。

![](https://blog.idejie.com/pics/how-to-build-a-simple-neural-network-in-9-lines-of-python-code2.jpg)

最终，神经元的权重将达到训练集的最佳值。 如果我们允许神经元考虑一个新的情况，那么遵循相同的模式，它应该做出很好的预测。

这个过程称为**反向传播**。

## **计算神经元输出的公式**

你可能会想，计算神经元输出的特殊公式是什么？ 首先，我们采用神经元输入的加权和，即：

![](https://blog.idejie.com/pics/how-to-build-a-simple-neural-network-in-9-lines-of-python-code3.jpg)

接下来我们归一化这个，所以结果在0和1之间。为此，我们使用一个数学上方便的函数，称为**Sigmoid**函数：

![](https://blog.idejie.com/pics/how-to-build-a-simple-neural-network-in-9-lines-of-python-code4.jpg)

如果绘制在图形上，Sigmoid函数绘制S形曲线。

![](https://blog.idejie.com/pics/how-to-build-a-simple-neural-network-in-9-lines-of-python-code5.jpg)

所以通过将第一个方程代入第二个方程，输出神经元的最终公式是：

![](https://blog.idejie.com/pics/how-to-build-a-simple-neural-network-in-9-lines-of-python-code6.jpg)

你可能已经注意到，我们没有使用最小的触发阈值，这是为了保持简单。

## **用于调整重量的公式**

在训练周期中，我们调整权重。 但是我们靠什么来调整权重呢？ 我们可以使用“误加权导数”公式：

![](https://blog.idejie.com/pics/how-to-build-a-simple-neural-network-in-9-lines-of-python-code7.jpg)

为什么要用这个公式？ 

​	首先我们要使调整与错误的大小成比例。 其次，我们乘以输入，它是0或1.如果输入为0，则不调整重量。 最后，我们乘以Sigmoid曲线的梯度。 要理解最后一个，请考虑：

1.我们用Sigmoid曲线来计算神经元的输出。

2.如果输出是一个大的正数或负数，它表示神经元是相当自信的一种或另一种方式。

3.在大数字处，S形曲线具有浅梯度。

4.如果神经元有信心现有的权重是正确的，那么它不想要特别调整它。 乘以Sigmoid曲线梯度实现这一点。

Sigmoid曲线的梯度可以通过采用导数求出：

![](https://blog.idejie.com/pics/how-to-build-a-simple-neural-network-in-9-lines-of-python-code7.jpg)

所以通过将第二个方程代入第一个方程，调整权重的最终公式是：

![](https://blog.idejie.com/pics/how-to-build-a-simple-neural-network-in-9-lines-of-python-code9.jpg)

有一些替代公式，这将使神经元能够更快地学习，但是这个方法的优点是相当简单。

## **构建Python代码**

虽然我们不会使用神经网络库，但我们将从名为numpy的Python数学库导入四种方法。 这些是：

- exp —自然指数
- array — 创建一个矩阵
- dot —矩阵乘法
- random — 随机数

例如，我们可以使用array（）方法来表示前面显示的训练集：

```python
training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T
```



`.T`功能将矩阵从水平转换为垂直。 所以计算机正在存储这样的数字。

![](https://blog.idejie.com/pics/how-to-build-a-simple-neural-network-in-9-lines-of-python-code10.jpg)

好。 我想我们已经准备好了更漂亮的源代码版本。 一旦我给了你，我将总结一些最后的想法。

我已经添加了对我的源代码的注释，逐一解释一切。 请注意，在每次迭代中，我们同时处理整个训练集。 因此，我们的变量是矩阵，它们是数字格。 这是一个用Python编写的完整工作示例：

```python
from numpy import exp, array, random, dot


class NeuralNetwork():
    def __init__(self):
        # 生成随机数
        random.seed(1)

        # 建立一个神经元，3输入：1输出
        # 为3*1的矩阵分配权重，值：-1 ~ 1
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

    # Sigmoid函数，描述S型曲线
    # 用这个函数输入加权和
    # 并将它们0-1标准化
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # Sigmoid函数的导数
    # 也就是Sigmoid函数的梯度
    # 它表示我们对已有权重的信心
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # 通过调整权重训练神经网络
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            # 通过我们的神经网络（单个神经元）传递训练集。
            output = self.think(training_set_inputs)

            # 计算误差（期望输出与预测输出之间的差值）。
            error = training_set_outputs - output

            # 将输入的误差乘以Sigmoid曲线的梯度。
            # 这意味着更少的自信的权重被调整得更多。
            # T这意味着输入为零，不会导致权重的更改。
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            # 调整权重.
            self.synaptic_weights += adjustment

    # 神经网络运算
    def think(self, inputs):
        # 通过我们的神经网络（我们的单个神经元）传递输入。
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == "__main__":

    #初始化一个神经网络
    neural_network = NeuralNetwork()

    print "Random starting synaptic weights: "
    print neural_network.synaptic_weights

    # 训练集。 我们有4个例子，每个由3个输入值和1个输出值组成。
    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T

    # 训练神经网络使用训练集。
    # 做一次10000次，每次都是微弱调整。
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print "New synaptic weights after training: "
    print neural_network.synaptic_weights

    # 用测试集测试神经网络。
    print "Considering new situation [1, 0, 0] -> ?: "
    print neural_network.think(array([1, 0, 0]))
```

## 最后的想法

尝试使用此终端命令运行神经网络：
python main.py
你应该得到如下结果：

```shell
Random starting synaptic weights:
[[-0.16595599]
[ 0.44064899]
[-0.99977125]]

New synaptic weights after training:
[[ 9.67299303]
[-0.2078435 ]
[-4.62963669]]

Considering new situation [1, 0, 0] -> ?:
[ 0.99993704]
```
我们做到了！ 我们使用Python构建了一个简单的神经网络！

首先，神经网络分配自身随机权重，然后使用训练集训练自己。 然后考虑一个新的情况[1，0，0]，并预测0.99993704。 正确的答案是1.所以非常接近！

传统的电脑程式通常无法学习。 神经网络令人惊奇的是，他们可以学习，适应和应对新的情况。 就像人的心灵一样。
当然这只是一个执行一个非常简单任务的神经元。 

但是，如果我们将数百万个神经元挂在一起呢？ 

我们有一天可以创造一些有意识的东西吗？



