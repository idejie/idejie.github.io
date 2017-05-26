---
title: 理解 Python 中的 yield
date: 2017-04-19 21:39:08
tags: yield
category: Python
---

## 如何生成斐波那契數列

斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，任意一个数都可由前两个数相加得到。用计算机程序输出斐波那契數列的前 N 个数是一个非常简单的问题，许多初学者都可以轻易写出如下函数：

- 第一种：最简单的方法

  ```python
  def fab(max):
       n ,a ,b = 0 , 0 , 1
       while n < max :
           print b
           a ,b = b , a+b
           n = n + 1
  ```

  ​

  执行 fab(5)，我们可以得到如下输出：

  ```
  1
  1
  2
  3
  5
  ```

  结果没有问题，但有经验的开发者会指出，直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，因为 fab 函数返回 None，其他函数无法获得该函数生成的数列。

- 第二种：有返回值的

  ```python
  def fab(max): 
      n, a, b = 0, 0, 1 
      L = [] 
      while n < max: 
          L.append(b) 
          a, b = b, a + b 
          n = n + 1 
      return L
  ```

  改写后的 fab 函数通过返回 List 能满足复用性的要求，但是更有经验的开发者会指出，该函数在运行中占用的内存会随着参数 max 的增大而增大，如果要控制内存占用，最好不要用 List

  来保存中间结果，而是通过 iterable 对象来迭代。例如，在 Python2.x 中，代码：

- 第三种：使用 iterable 对象来迭代

