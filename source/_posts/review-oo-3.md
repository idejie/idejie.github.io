---
title: 面向对象复习（三）
tag: 面向对象
category: 课程复习
date: 2016-6-5 21:18
---

## 十三、多态变量

- 多态变量是指可以引用多种对象类型的变量。


- 这种变量在程序执行过程可以包含不同类型的数值。


- 对于动态类型语言，所有的变量都可能是多态的。


- 对于静态类型语言，多态变量则是替换原则的具体表现。

    Parent variable=new Child();

### 1.实际用法

很少使用赋值，通常是伴随着函数或方法调用，通过数值和参数之间的绑定来实现的。

### 2.多台变量的形式

- 简单变量
- 接收器变量

  多态变量最常用的场合是作为一个数值，用来表示正在执行的方法内部的接收器。

  隐藏

  伪变量smalltalk:self，C++,Java,C#:this

  **作用**：

  ​	（1）多态接收器功能的强大之处表现在消息传递与改写相结合时。这种结合是软件框架开发的	

  ​			关键

  ​	（2）一般框架系统中的方法分为两大类：

  ​			在父类中定义基础方法，被多个子类所继承，但不被改写；

  ​			父类定义了关于多种活动的方法，但要延迟到子类才实现。

- 反多态

  向下造型是处理多态变量的过程，并且在某种意义上这个过程的取消操作就是替换。

  能够将其赋值给一个声明为子类的变量吗？

  该取消多态赋值的过程，也称为反多态。

- 纯多态(多态方法)

## 十四、泛型

- 泛型通过类型的使用提供了一种将类或者函数参数化的方法。


- 与通常的函数参数一样，泛型提供了一种无需识别特定数值的定义算法的方法。


- 泛型将名称定义为类型参数。


- 在编译器读取类描述时，无法知道类型的属性，但是该类型参数可以像类型一样用于类定义内部。


- 在将来的某一时刻，会通过具体的类型来匹配这一类型参数，这样就形成了类的完整声明。


- C++支持

```
Apple类:使用printOn方法将自身输出。

Orange类:使用writeTo方法将自身输出。

二进制提供

希望将Apple对象和Orange对象保存在同一个列表中，并且使用一个多态函数将它们输出。
```

(1)定义一个公共的父类，具有共同行为

``` C++
class Fruit {

  public:

  virtual void print (ostream&)=0;//纯虚方法

};

```

(2)n使用模版，创建一个fruitadapter类，将以Apple或者Orange为参数，同时符合水果的定义
``` C++

template<class T>

class FruitAdapter : public Fruit {

public:

   FruitAdapter(T & f):theFruit(f){ }

   T &value ( ){ return theFruit;}

   virtual void print ( ostream& out ){print(theFruit,out);}

public:

  T & theFruit;

};  
```
(3)使用模版函数简化适配器的创建过程
``` C++
template<class T>

Fruit* new Fruit( T & f )

{

  return new FruitAdapter<T>(f);

};  
```
（4）

```C++
Apple anApple(“Rome”);
Orange anOrange;

List<Fruit *> fruitList;

fruitList.insert(newFruit(anApple));
fruitList.insert(newFruit(anOrange));

List<Fruit *> ::iterator start = fruitList.begin();
List<Fruit *> ::iterator stop = fruitList.end();

For ( ;start!=stop; ++start) {
	Fruit & aFruit = *start;
   aFruit.print(cout);
}

```

## 十五、框架

对于一类相似问题的骨架解决方案。

通过类的集合形成，类之间紧密结合，共同实现对问题的可复用解决方案

继承和改写的强大能力体现

最常见的框架

Java中的GUI框架

Web开发中的Struts框架

框架开发的一个重要基础

使用继承的两种方式：

代码复用：基本方法，对问题的现存的解决方案。

概念复用：特化方法，用于特定应用的解决方案。

## 十六、对象互联

一种考虑对象互连的方式就是研究可视性和依赖性这两个概念。

可视性描述了关于名称的特性，通过该名称句柄可以存取对象，如果对象的名称是合法的且代表该对象，那么在这个特定环境下该对象就是可见的。

描述可视性的相关术语还包括标识符的范畴

依赖性将两个对象或者类联系起来，在不存在另外一个对象的条件下，如果一个对象的存在无任何意义，就说该对象依赖于另外那个对象。

例如:子类几乎总是依赖于它的父类



耦合(coupling)和内聚(cohesion)的思想提供了一个框架，用于评价对象和类的应用是否有效。

耦合描述类之间的关系，内聚描述类内部的关系。