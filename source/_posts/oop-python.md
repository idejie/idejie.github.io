---
title: 从 Python 谈OOP
date: 2017-04-28 14:33:46
tags: OOP
category: Python
---

> OOP（Object Oriented Programming），面向对象编程。

## 概述

面向对象编程是一种程序设计的思想，或者叫做一种程序设计模式。

核心就是**一切皆对象**。

好处：可以联系现实中的事务，利用人的日常思维；模块化，可复用;灵活，可扩展。

## 创建类和对象

- **什么是对象？**

前面说了，一切皆对象。所有能称得上”东西“的实体，都可以称作对象。在 Python 中每一种数据类型，都是对象。对象是程序的基本单元，换句话说，程序其实是对象的集合。对象，能接收消息，也能够处理这些消息，当然也能发出消息。

- **类和实例**

Python 中除了 int、float、str，bool等基本数据类型，还可以自定义创建数据类型。这就需要引入”类“这个概念。

**什么是类？**类，通俗一点讲就是模板，比如 student 类，就是学生的模板。Java 和 Python 定义类都是”class“这个关键字。

```python
class Student(object): ##这就定义了一个类(模板)
    pass
```

用模板创建出来的对象叫做**实例**。`xiaoming = Student()`就创建一个 Student 类型的数据 xiaoming。xiaoming 是一个对象，也是 Student 类的一个实例。

类中定义了一组变量和方法，用该类实例化的对象，都会获得这些属性和方法。但是每一个实例都是独立的，也就是说，当一个实例的属性和方法发生变化时，不影响其他的实例。

```python
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
```

这是一个定义了 Student的完整的类，\_\_init\_\_方法是一个特殊的方法，从对象的角度，他为 Student 能创建的实例都绑定了两个属性。所以说 Student 有 name 和 score 这两个属性，以及一个 pritnt方法。从对象的生命周期上来讲，_\_init\_\_方法对象实例化的入口，也就是说在执行`bart = Student('Bart Simpson', 59)`时，程序执行到__\_init\_\_方法便创建了一个对象，并被分派给某些变量赋值。

## OOP 的三大特性：封装、继承、多态

