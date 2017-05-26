---
title: 面向对象考试题（2015-2016）
tag: 面向对象
category: 课程复习
date: 2016-6-22 21:18
---

## 2015-2016年第一学期山东大学软件学院面向对象试卷

### 一、简答（30分）

#### **1.试用面向对象语言简述改写和重定义的异同，以及方法绑定时的差别** 

(1)如果子类的方法具有与父类的方法相同的名称和类型签名，称子类的方法**改写**了父类的方法

(2)重定义是一种重载，当子类定义了一个与父类具有相同名称但签名类型不同的方法是，发生重定义。

相同点：它们发生时都与父类方法的名称相同，如都是draw方法。

不同点：改写是具有相同的签名（参数类型，数量，顺序）一样；重载时具有与父类不同的签名

方法绑定：重定义是在编译时就执行，属于静态绑定；改写是在运行时执行，属于动态绑定。

#### **2.试用面向对象语言简述this的多态性** 

（１）表示对当前对象的引用！

（２）表示引用类的成员变量，而非函数参数，注意在函数参数和成员变量同名是进行区分！其实这是第一种用法的特例，比较常用，所以那出来强调一下。

（３）用于在构造方法中引用满足指定参数类型的构造器（其实也就是构造方法）。但是这里必须非常注意：只能引用一个构造方法且必须位于开始

举例：

```java
package test;
public class ThisTest {
  private int i=0;
  public static void main(String[] args){
       ThisTest tt0=new ThisTest(10);
       ThisTest tt1=new ThisTest("ok");
       ThisTest tt2=new ThisTest(20,"ok again!");
      
       System.out.println(tt0.increment().increment().increment().i);
       //tt0.increment()返回一个在tt0基础上ｉ++的ThisTest对象，
       //接着又返回在上面返回的对象基础上i++的ThisTest对象！
    }
    //第一个构造器：有一个int型形参
    ThisTest(int i){
       this.i=i+1;//此时this表示引用成员变量ｉ，而非函数参数ｉ
       System.out.println("Int constructor i——this.i:  "+i+"——"+this.i);
       //System.out.println("i-1:"+(i-1)+"this.i+1:"+(this.i+1));
       //从两个输出结果充分证明了i和this.i是不一样的！
    }
    //  第二个构造器：有一个String型形参
    ThisTest(String s){
       System.out.println("String constructor:  "+s);
    }
    //  第三个构造器：有一个int型形参和一个String型形参
    ThisTest(int i,String s){
       this(s);//this调用第二个构造器
       //this(i);
      
       this.i=i++;//this以引用该类的成员变量
       System.out.println("Int constructor:  "+i+"/n"+"String constructor:  "+s);
    }
    public ThisTest increment(){
       this.i++;
       return this;//返回的是当前的对象，该对象属于（ThisTest）
    }
    
}
 
运行结果：
 
Int constructor i——this.i:  10——11
String constructor:  ok
String constructor:  ok again!
Int constructor:  21
String constructor:  ok again!
14
```





#### **3.试用面向对象语言简述替换原则** 

子类实例可以代替超类的实例，出现在超类的实例可以合法的出现在任何地方。C++采用最小静态空间分配，即只分配超类所需的内存空间；Java采用的是动态内存分配，即分配用于保存一个指针的内存空间，运行时通过堆来分配所需的内存空间，同时将指针设为相应的合适值。

#### 4.为什么要尽量使用组合复用而不要用继承复用 

- 组合复用提供一种利用已存在的软件组件来创建新的应用程序的方法。委托，非替换。
- 继承复用通过继承，新的类可以声明为已经存在类的子类。通过这种方法，与初始的类的相关的所有的数据字段和函数都自动地与心得数据抽象简历联系。
- 组合复用简单，可以显示在特定的数据结构中需要执行的哪些操作。
- 继承复用：新的数据结构的操作是原有的数据结构的操作的超集，为了解哪些操作对新数据结构合法，必须检查原有数据结构的声明
- 继承复用代码简洁，但规则不简练，需要同时了解超类和子类
- 组合复用代码长，但可以不用参照原有数据结构的声明
- 继承复用无法阻止用户不正确的使用超类的方法操纵数据结构
- 组合复用中List类作为集合的存储机制使用
- 继承复用可以吧心得抽象作为已存在的多态函数的一个参数来使用，组合复用不支持替换，不能把新的抽象作为已存在多态函数的一个参数来使用
- 继承复用执行时具有优势决定使用哪种复用方式：考虑替换原则，是否需要保留类型签名。

#### 5.重载方法绑定（书P91页例子），简述重载方法绑定的步骤 

（Object Animal Plant。给出不同签名问执行哪一个方法并给出理由，参考课本91页dessert甜点的例子。）

**p91页例子：**

Pie和Cake继承Dessert，ApplePie继承Pie，ChocolateCake继承Cake

```java
void order(Desser d,Cake c);
void order(Pie p,Desser d);
void order(ApplePie a,Cake c);

order(aDessert,aCake);//执行方法一
order(anApplePie,aDessert);//执行方法二
order(aDessert,aDessert);//错误
order(anApplePie,AChocolateCake);//执行方法三
order(aPie,aCake)；//错误
order(aChocolateCake,anApplePie);//错误
order(aChocolateCake,aChocolateCake);//方法一
order(aPie,aChocolateCake);//错误
```



1.找到所有能进行调用的方法，即各个参数可以合法的赋值给各个参数类型的所有方法。（实参是形参的一种即可）如果找到一个参数类型完全匹配的方法（没有别的候选方法），那就执行这个方法。

2.如果有候选方法（即第一步产生的集合中任何方法），并且候选方法的形参都可以赋值给集合中任何方法，则移除。重复操作，直至无法实现进一步的缩减。

3.如果只剩一种方法，那么就调用这个方法。如果剩余方法不止一个，那么就会产生歧义，编译器将报错。



eg:

```java
order (aDessert, aCake);
//由于 Dessert 和 Cake 与第一个方法的类型签名直接匹配,因此第一个函数调用是合法的。
```

类似地,由于只有第二个方法的参数可以合法地接受 第二个函数的实参的赋值,因此第二个函数调用能够与第二个重载方法相 匹配(在第一个和第三个方法中出现的将 Dessert 类型的实参赋值给 Cake 参数是非法的)。

第三个函数调用实例是非法的。通过第一步筛选后,由于 Dessert 类型 的数值不能任意地向下造型为更特殊的类型,因此可能调用的候选方法的 集合就为空了,同时报告编译错误。
第四个函数调用就更加微妙了。经过第一步处理后,存在着三个候选 方法。因此,选择方法的算法进行到第二步。在这一步中,首先,由于 ApplePie 是一个比 Dessert 更特殊的类(ApplePie 可以赋值给 Dessert,反之 则不行),并且第二个参数是一致的,因此第一个重载方法就被排除了。基 于同样的原因(两个参数都不是更特殊的类型,Pie 不如 ApplePie 特殊, Dessert 不如 Cake 特殊),第二个方法也被排除了。由此,只剩下一个方法, 因此,第四个函数调用将执行第三个方法。
92
与第三个方法类似,最后这个函数调用也是无效的。经过第一步处理 之后,只有最后一个方法得以排除,可能调用的方法集合中还剩下两个方 法。由于 Dessert 不能赋值给 Pie,因此无法将第一个方法归人第二个方法。 同时,由于 Dessert 无法转换成 Cake,因此也无法将第二个方法归入第一 个方法。这样,在第二步处理之后,留下两个方法,编译器无法决定使用 它们之中的哪一个方法,于是就产生错误。

最后一个错误是因为第一步可以筛选出方法一和方法二来，但是方法一和方法二从特殊性上讲是一样的，所以错误。

二、重构（30分）

1.totalPrice方法，A产品八折，B产品满100减20，C产品11号七折，12号满200返现5元，试简述满足开闭原则的解决方案（画类图，写代码框架） 

 

（零件总价格totalPrice，算法里一个for循环，Part[] parts都计算在内形成总价，现需要修改三种零件的价格的原价上进行修改，A零件打八折，B零件满200减10，C零件从11号当天1折，以后每天增加1折，到20号为止，问totalPrice的设计是否合理，如何改进。）

2.矩形类里面有resize方法，setWidth,setHeight方法，现在有一个Square类，继承自矩形类并实现这三个方法。问，这样的设计合理吗？不合理的话怎么改（解题思路。设计矩形和正方形的共同父类） 

（矩形内有resize方法，会自动检测，如果宽小于高，则自动+1，直到大于高，题目中代码有问题，要求修改。代码如下：

class Square extends RecTangle(){  

public Square (double s){super(s,s)}   

public void setWidth(double w){  

super.setWidth(w);   

super.setHeight(w);   

}   

public void setHeight(double h){   

super.setWidth(h);   

super.setHeight(h);   

}  

）

3.苹果有writeTo方法，橘子有write方法来实现输出，现在要让苹果和橘子在同一个列表中，且可以使用print方法打印输出，试写出代码框架，要求：使用适配器模式，纯多态，反射和内省，来实现。 

三代码题（40分） 

1.公司批准预算支出，五万元以下可由主任审批，五万元以上（包括五万元）十万元以上由副董事长审批，十万元（包括十万）以上五十万元由董事长审批，超过五十万元由会议决定，试用责任链模式解决这种问题，画出类图，给出代码框架 

2.有七喜、可乐、雪碧、美年达等饮料，分别可以使玻璃瓶装，易拉罐、100ML塑料瓶、200ML塑料瓶等规格，可以通过冷饮店，超市、冰淇淋店等销售渠道销售，问用什么样的设计模式能减少子类的数量，画出设计模式的类图，并给出代码框架，子类实现一个就行。 

 

3.是食堂为了满足不同学生的需求，提供了很多调料供学生自由添加，应使用什么设计模式来实现这种情况，画出清炒白菜加盐、加辣椒、加胡椒的对象图。

 