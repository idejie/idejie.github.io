---
title: 算法（五）：最大流
date: 2019-01-10 14:15:44
tags: 最大流
category: 课程复习
---

# 网络流算法

## 1.基本概念

![](https://blog.idejie.com/pics/max-flow0.jpg)

老板让你从1往3运东西，蓝色箭头的代表桥，蓝色数字代表桥的载重，超过载重车是走不成的。

那么怎么用才能实现一次从1到3输送最多的货物呢？

这就是**网络流**问题

一般化地，

网络流$G=(V, E)$是一个有向图，其中每条边$(u, v)$均有一个非负的容量值，记为$c(u, v) ≧ 0$。如果$(u, v) ∉ E$(即没有边)则可以规定$c(u, v) = 0$。网络流中有两个特殊的顶点，即源点$s$和汇点$t$。

与网络流相关的一个概念是流。设$G$是一个流网络，其容量为$c$。设$s$为网络的源点，$t$为汇点，那么$G$的流是一个函数$f：V×V →R$，满足一下性质：

**容量限制**：对所有顶点对$u，v∈V$，满足$f(u, v) ≦ c(u, v)$；（怕桥塌了）

**反对称性**：对所有顶点对$u，v∈V$，满足$f(u, v) = - f(v, u)$; （多了运不出去，少了不够运）

**流守恒性**：对所有顶点对$u∈V-\{s, t\}$，满足$Σv∈Vf(u,v)=0$。（反对称性的求和）

$f(u, v)$称为从顶点$u$到顶点$v$的流，流的值定义为：$|f| =Σv∈Vf(s,v)$，即从源点$s$出发的总的流。

在最大流问题中，我们需要求解源点$s$到汇点$t$之间的最大流$f(s, t)$，同时我们还希望了解达到该值的流。对于一个指定的源点$s$和指定汇点$t$的网，我们称之为**$st$-网**。

## 2.求解

### 2.1两个策略一般化

- 反平行边（加入一个节点，将其中一个边拆成两个）
- 超级源点和超级汇点

### 2.2 Ford-Fulkson算法解决

基本思路很简单,每次用dfs从源到汇找一条可行路径， 然后把这条路塞满。这条路径上容量最小的那条边的容量，就是这次dfs所找到的流量。然后对于路径上的每条边，其容量要减去刚才找到的流量。

这样，每次dfs都可能增大流量，直到某次dfs找不到可行路径为止，最大流就求出来了。

**但是这样未必正确**

![](https://blog.idejie.com/pics/max-flow1.jpg)

按照上述算法最大流为100，但答案是200。

问题出在过早地认为边a → b上流量不为0，因而“封锁”了流量继续增大的可能。

所以算法要**改进**

**一个改进的思路**：应能够修改已建立的流网络，使得“不合理”的流量被删掉。

**一种实现**：对上次dfs时找到的流量路径上的边，添加一条“反向”边，反向边上的容量等于上次dfs时
找到的该边上的流量，然后再利用“反向”的容量和其他边上剩余的容量寻找路径。

- 第一次DFS后

  ![](https://blog.idejie.com/pics/max-flow2.jpg)

- 施加反向边

  ![](https://blog.idejie.com/pics/max-flow3.jpg)

- 第二次dfs

  ![](https://blog.idejie.com/pics/max-flow4.jpg)

  第二次dfs搜索又找到了一个流量为100的流，加上第一次搜索得到的流量为100的流，总流量上升到200

- 施加反向边

  ![](https://blog.idejie.com/pics/max-flow5.jpg)

这样施加反向边的网络叫做 **残差网络**

**定义**：在一个网络流图上，找到一条源到汇的路径（即找到了一个流量）后，对路径上所有的边，其容量都减去此次找到的流量，对路径上所有的边，都添加一条反向边，其容量也等于此次找到的流量，这样得到的新图，就称为原图的“残余网络”

**为什么施加反向边就是正确的了呢？**

假设在第一次寻找流的时候，发现在b->a上可以有流量n来自源，到达b，再流出a后抵达汇点。

![](https://blog.idejie.com/pics/max-flow6.jpg)

构建残余网络时添加反向边a->b，容量是n,增广的时候发现了流量n-k，即新增了n-k的流量。这n-k的流量，从a进，b出，最终流到汇点

![](https://blog.idejie.com/pics/max-flow7.jpg)



现要证明这2n-k的从流量，在原图上确实是可以从源流到汇的。

把流入b的边合并，看做一条，把流出a的边也合并，同理把流入a和流出b的边也都合并

![](https://blog.idejie.com/pics/max-flow8.jpg)

在原图上可以如下分配流量，则能有2n-k从源流到汇点：

![](https://blog.idejie.com/pics/max-flow9.jpg)

**总结**

```
求最大流的过程，就是不断找到一条源到汇的路径，然后构建残余网络，再在残余网络上寻找新的路径，使总流量增加，然后形成新的残余网络，再寻找新路径…..直到某个残余网络上找不到从源到汇的路径为止，最大流就算出来了。
每次寻找新流量并构造新残余网络的过程，就叫做寻找流量的“增广路径”，也叫“增广”

现在假设每条边的容量都是整数(有理数都可以变化成整数)
这个算法每次都能将流至少增加1 
由于整个网络的流量最多不超过 图中所有的边的容量和C，从而算法会结束
现在来看复杂度找增广路径的算法可以用dfs， 复杂度为边数m+顶点数n
Dfs 最多运行C次
所以时间复杂度为C*(m+n) =C* n^2
```

这个算法实现很简单但是注意到在图中C可能很大很大比如说下面这张图

![](https://blog.idejie.com/pics/max-flow10.jpg)

如果运气不好 这种图会让你的程序执行200次dfs虽然实际上最少只要2次我们就能得到最大流

所以，还需要**改进**每次选择的路径最大流

在每次增广的时候，选择从源到汇的**具有最少边数**的增广路径,即不是通过dfs寻找增广路径，而是通过bfs寻找增广路径。

这就是Edmonds-Karp 算法了。

### 2.3 Edmonds-Karp 算法解决

例：Poj 1273 Drainage Ditches [【链接】](http://poj.org/problem?id=1273)

```
Drainage Ditches
Time Limit: 1000MS		Memory Limit: 10000K
Total Submissions: 87253		Accepted: 33930
Description

Every time it rains on Farmer John's fields, a pond forms over Bessie's favorite clover patch. This means that the clover is covered by water for awhile and takes quite a long time to regrow. Thus, Farmer John has built a set of drainage ditches so that Bessie's clover patch is never covered in water. Instead, the water is drained to a nearby stream. Being an ace engineer, Farmer John has also installed regulators at the beginning of each ditch, so he can control at what rate water flows into that ditch. 
Farmer John knows not only how many gallons of water each ditch can transport per minute but also the exact layout of the ditches, which feed out of the pond and into each other and stream in a potentially complex network. 
Given all this information, determine the maximum rate at which water can be transported out of the pond and into the stream. For any given ditch, water flows in only one direction, but there might be a way that water can flow in a circle. 
Input

The input includes several cases. For each case, the first line contains two space-separated integers, N (0 <= N <= 200) and M (2 <= M <= 200). N is the number of ditches that Farmer John has dug. M is the number of intersections points for those ditches. Intersection 1 is the pond. Intersection point M is the stream. Each of the following N lines contains three integers, Si, Ei, and Ci. Si and Ei (1 <= Si, Ei <= M) designate the intersections between which this ditch flows. Water will flow through this ditch from Si to Ei. Ci (0 <= Ci <= 10,000,000) is the maximum rate at which water will flow through the ditch.
Output

For each case, output a single integer, the maximum rate at which water may emptied from the pond.
Sample Input

5 4
1 2 40
1 4 20
2 4 20
2 3 30
3 4 10
Sample Output

50
```



**题意:**

​       现在有m个池塘(从1到m开始编号,1为源点,m为汇点),及n条有向水渠,给出这n条水渠所连接的点和所能流过的最大流量，求从源点到汇点能流过的最大流量。



**赤裸裸的最大流算法** 用EK求解

```c++
#include <iostream>
#include <queue>
#include <deque> 
using namespace std;
int G[300][300]; // 存邻接矩阵，G_{i,j}就是i到j的承载量
int Prev[300]; //路径上每个节点的前驱节点
bool Visited[300]; //前驱节点是否被访问
int n,m; //m是顶点数目，顶点编号从1开始 1是源，m是汇, n是边数

unsigned Augment() //寻找增广边
{
	int v;
	int i;
	deque<int> q; //存储访问过的边
	memset(Prev,0,sizeof(Prev));
	memset(Visited,0,sizeof(Visited));
	Prev[1] = 0;
	Visited[1] = 1;
	q.push_back(1);
	bool bFindPath = false;
	//用bfs寻找一条源到汇的可行路径，注意用BFS了
    while(! q.empty()) {
		v = q.front();
		q.pop_front();
		for( i = 1;i <= m;i ++) {
            //必须是依然有容量的边，才可以走
			if( G[v][i] > 0 && Visited[i] == 0) {
				Prev[i] = v;
				Visited[i] = 1;
				if( i == m ) {
					bFindPath = true;
					q.clear();
					break;
				}
				else
					q.push_back(i);
			}
		}
	}
    if(!bFindPath)
		return 0;
    int nMinFlow = 999999999;
	v = m;
	//寻找源到汇路径上容量最小的边，其容量就是此次增加的总流量
	while( Prev[v] ) {
		nMinFlow = min( nMinFlow,G[Prev[v]][v]);
		v = Prev[v];
	}
    //沿此路径添加反向边，同时修改路径上每条边的容量
	v = m;
	while( Prev[v] ) {
		G[Prev[v]][v] -= nMinFlow;
		G[v][Prev[v]] += nMinFlow;
		v = Prev[v];
	}
	return nMinFlow;
}

int main()
{
	while (cin >> n >> m ) 
	{
		//m是顶点数目，顶点编号从1开始
		int i,j,k;
        int s,e,c;
        memset( G,0,sizeof(G));
        for( i = 0;i < n;i ++ ) {
            cin >> s >> e >> c;
            G[s][e] += c; //两点之间可能有多条边
        }
        unsigned int MaxFlow = 0;
        unsigned int aug;
        while( aug = Augment() )//寻找增广路径，每有一条就增加最大流
            MaxFlow += aug;
        cout << MaxFlow << endl;
	}
	return 0;
}
```

前面的网络流算法，每进行一次增广，都要做一遍BFS，十分浪费。能否少做几次BFS?

这里Dinic算法改进了这个问题

### 2.4 Dinic算法

Edmonds-Karp的提高余地：需要多次从s到t调用BFS，可以设法减少调用次数。

亦即：使用一种代价较小的高效增广方法。

考虑：在一次增广的过程中，寻找多条增广路径。

**DFS**

详细分析

![](https://blog.idejie.com/pics/max-flow11.jpg)

1.先利用 BFS对残余网络分层

一个节点的“层”数，就是源点到它最少要经过的边数。于是得到

![](https://blog.idejie.com/pics/max-flow12.jpg)

2.分完层后，利用DFS从前一层向后一层反复寻找增广路。

因此，前面在分层时，只要进行到汇点的层次数被算出即可停止，因为按照该DFS的规则，和汇点同层或更下一层的节点，是不可能走到汇点的。

DFS过程中，要是碰到了汇点，则说明找到了一条增广路径。此时要增加总流量的值，消减路径上各边的容量，并添加反向边，即所谓的进行增广。

DFS找到一条增广路径后，并不立即结束，而是**回溯后继续DFS寻找下一个增广路径**。

**回溯到哪个节点呢？**

回溯到的节点u满足以下条件：
1) DFS搜索树的树边(u,v)上的容量已经变成0。即刚刚找到的增广路径上所增加的流量，等于(u,v)本次增广前的容量。(DFS的过程中，是从u走到更下层的v的)
2)u是满足条件 1)的最上层的节点

如果回溯到源点而且无法继续往下走了，DFS结束。

因此，一次DFS过程中，可以找到多条增广路径。

DFS结束后，对残余网络再次进行分层，然后再进行DFS

当残余网络的分层操作无法算出汇点的层次（即BFS到达不了汇点）时，算法结束，最大流求出。

一般用栈实现DFS,这样就能从栈中提取出增广路径。

Dinic 复杂度是 $n\times n \times m$ (n是点数，m是边数）

**如果要求出最大流中每条边的流量，怎么办？**

将原图备份，原图上的边的容量减去做完最大流的残余网络上的边的剩余容量，就是边的流量。

CPP实现

```cpp
#include <iostream> 
#include <queue> 
#include <vector> 
#include <algorithm> 
#include <deque> 
using namespace std;
#define INFINITE 999999999 //Poj 1273 Drainage Ditches 的 Dinic算法
int G[300][300];
bool Visited[300];
int Layer[300]; int n,m; //1是源点，m是汇点
bool CountLayer() {
	int layer = 0; deque<int>q;
	memset(Layer,0xff,sizeof(Layer)); //都初始化成-1
	Layer[1] = 0; q.push_back(1);
	while( ! q.empty()) {
		int v = q.front();
		q.pop_front();
		for( int j = 1; j <= m; j ++ ) {
			if( G[v][j] > 0 && Layer[j] == -1 ) {
			//Layer[j] == -1 说明j还没有访问过
			Layer[j] = Layer[v] + 1;
			if( j == m ) //分层到汇点即可
				return true;
			else
				q.push_back(j);
    		}
		}
	}
	return false;
}
int Dinic(){
	int i; 
    int s;
	int nMaxFlow = 0;
    deque<int> q; //DFS用的栈
	while( CountLayer() ) { //只要能分层
		q.push_back(1); //源点入栈
		memset(Visited,0,sizeof(Visited)); 
        Visited[1] = 1;
		while( !q.empty()) {
			int nd = q.back();
			if( nd == m ) { // nd是汇点
				//在栈中找容量最小边
				int nMinC = INFINITE;
                int nMinC_vs; //容量最小边的起点
				for( i = 1;i < q.size(); i ++ ) {
					int vs = q[i-1];
					int ve = q[i];
					if( G[vs][ve] > 0 ) {
						if( nMinC > G[vs][ve] ) {
							nMinC = G[vs][ve];
							nMinC_vs = vs;
						}
					}
                }
				//增广，改图
				nMaxFlow += nMinC;
				for( i = 1;i < q.size(); i ++ ) {
					int vs = q[i-1];
					int ve = q[i];
					G[vs][ve] -= nMinC; //修改边容量
					G[ve][vs] += nMinC; //添加反向边
				}
				//退栈到 nMinC_vs成为栈顶，以便继续dfs
				while( !q.empty() && q.back() != nMinC_vs ) {
					Visited[q.back()] = 0; //没有这个应该也对
                    q.pop_back();
				}
			}
			else { //nd不是汇点
				for( i = 1;i <= m; i ++ ) {
                	if( G[nd][i] > 0 && Layer[i] == Layer[nd] + 1 &&! Visited[i]) {
                    	//只往下一层的没有走过的节点走
                    	Visited[i] = 1;
                    	q.push_back(i);
                    	break;
					}
				}
				if( i > m) //找不到下一个点
					q.pop_back(); //回溯
			}
		}
	}
	return nMaxFlow;
}
int main(){
	while (cin >> n >> m ) {
		int i,j,k;
		int s,e,c;
		memset( G,0,sizeof(G));
        for( i = 0;i < n;i ++ ) {
			cin >> s >> e >> c;
			G[s][e] += c; //两点之间可能有多条边
        }
		cout << Dinic() << endl;
	}
	return 0;
}
```

### 2.5 有流量下界的网络最大流

如果流网络中每条边e对应两个数字B(e)和C(e),分别表示该边上的流量至少要是B(e)，最多
C(e),那么，在这样的流网络上求最大流，就是有下界的最大流问题。
 这种网络不一定存在可行流，如

![](https://blog.idejie.com/pics/max-flow13.jpg)

![](https://blog.idejie.com/pics/max-flow14.jpg)

如果我们沿着s-a-b-t路线走 仅能得到一个100的流

![](https://blog.idejie.com/pics/max-flow15.jpg)



思路：将下界“分离”出去，使问题转换为下界为０的普通网络流问题。

![](https://blog.idejie.com/pics/max-flow16.jpg)

![](https://blog.idejie.com/pics/max-flow17.jpg)

![](https://blog.idejie.com/pics/max-flow18.jpg)

![](https://blog.idejie.com/pics/max-flow19.jpg)

![](https://blog.idejie.com/pics/max-flow20.jpg)

![](https://blog.idejie.com/pics/max-flow21.jpg)

在做过一遍最大流的新图的残余网络中，去掉t->s以及s->t的边，然后以s为源，t为汇再做一次最大流，
此时得到的流量 sum2，则 sum1+sum2就是在原图上满足下界的最大流。
和x,y相连的边不用处理，因为x,y实际上是只能流入或只能流出的点，在图中不起作用。
**要想求出每条边上的流量，怎么办？**

在做第二次最大流之前，将图备份到G2
经过两次求最大流后，最后变成的残余网络是G
此时G2\[i]\[j] – G\[i]\[j] + LC\[i\][j] 就是 i->j上的流量LC\[i\][j] 是i->j边上的流量下界(下界是被满足的）

**处理网络流题目要注意，如果有重边，则要将重边上的容量和下界累加，合并成一条边**

### 2.6最小费用最大流

![](https://blog.idejie.com/pics/max-flow22.jpg)

![](https://blog.idejie.com/pics/max-flow23.jpg)

反复用spfa算法做源到汇的最短路进行增广，边权值为边上单位费用。反向边上的单位费用是负的。
直到无法增广，即为找到最小费用最大流。
成立原因：每次增广时，每增加1个流量，所增加的费用都是最小的。
因为有负权边（取消流的时候产生的），所以不能用迪杰斯特拉算法求最短路。



```
POJ 2135
 题目描述：
 有n个景点，一个人要从1号景点走到n号景点，再从n号景点走到1号（回来的路不能重复，不一定走完所有景点，只要求从1到n即可），给你一些景点之间的路的长度（双向），问你最短需要走多少路才能回来？
 解题报告：
 最小费用就是路径长度的总和，最大流就是来回的两条路。
 由于去和回来可以看成：2条从1到n的不同的路。所以转化成求从1到n的两条不同的路。
假设a b之间有长度为c的路。按照最小费用流建
图：
 ab之间费用为c，容量是1。
 ba之间费用为c，容量是1.
 建立一个源点，连接1号景点，无费用，容量为2（表示可以有两条路）
 同理，建立一个汇点，连接n号景点，无费用，容量为2.
 这样，如果求的的最大流是2，就表示了有两条从1到n的不同的路。（因为中间的点边容量只是1，只能用一次）
 这样求的最小费用最大流的最小费用就是最短路径长度。
```



## 3.练习

### 3.1 ACM Computer Factory（POJ 3436 ）

```
Description

As you know, all the computers used for ACM contests must be identical, so the participants compete on equal terms. That is why all these computers are historically produced at the same factory.

Every ACM computer consists of P parts. When all these parts are present, the computer is ready and can be shipped to one of the numerous ACM contests.

Computer manufacturing is fully automated by using N various machines. Each machine removes some parts from a half-finished computer and adds some new parts (removing of parts is sometimes necessary as the parts cannot be added to a computer in arbitrary order). Each machine is described by its performance (measured in computers per hour), input and output specification.

Input specification describes which parts must be present in a half-finished computer for the machine to be able to operate on it. The specification is a set of P numbers 0, 1 or 2 (one number for each part), where 0 means that corresponding part must not be present, 1 — the part is required, 2 — presence of the part doesn't matter.

Output specification describes the result of the operation, and is a set of P numbers 0 or 1, where 0 means that the part is absent, 1 — the part is present.

The machines are connected by very fast production lines so that delivery time is negligibly small compared to production time.

After many years of operation the overall performance of the ACM Computer Factory became insufficient for satisfying the growing contest needs. That is why ACM directorate decided to upgrade the factory.

As different machines were installed in different time periods, they were often not optimally connected to the existing factory machines. It was noted that the easiest way to upgrade the factory is to rearrange production lines. ACM directorate decided to entrust you with solving this problem.

Input

Input file contains integers P N, then N descriptions of the machines. The description of ith machine is represented as by 2 P + 1 integers Qi Si,1 Si,2...Si,P Di,1 Di,2...Di,P, where Qi specifies performance, Si,j — input specification for part j, Di,k — output specification for part k.

Constraints

1 ≤ P ≤ 10, 1 ≤ N ≤ 50, 1 ≤ Qi ≤ 10000

Output

Output the maximum possible overall performance, then M — number of connections that must be made, then M descriptions of the connections. Each connection between machines A and B must be described by three positive numbers A B W, where W is the number of computers delivered from A to B per hour.

If several solutions exist, output any of them.

Sample Input

Sample input 1
3 4
15  0 0 0  0 1 0
10  0 0 0  0 1 1
30  0 1 2  1 1 1
3   0 2 1  1 1 1
Sample input 2
3 5
5   0 0 0  0 1 0
100 0 1 0  1 0 1
3   0 1 0  1 1 0
1   1 0 1  1 1 0
300 1 1 2  1 1 1
Sample input 3
2 2
100  0 0  1 0
200  0 1  1 1
Sample Output

Sample output 1
25 2
1 3 15
2 3 10
Sample output 2
4 5
1 3 3
3 5 3
1 2 1
2 4 1
4 5 1
Sample output 3
0 0
Hint

Bold texts appearing in the sample sections are informative and do not form part of the actual data.
```

**题目解析**：

输入：

电脑由3个部件组成，共有4台机器，

1号机器产量15, 能给空电脑加上2号部件 能产出具有2的电脑

2号 机器产量10，能给空电脑加上2号部件和3号部件 ，生产出同时有2和3的电脑

3号机器产量30，能有必须有2号部件和3号部件有无均可的电脑变成成品

4号机器产量3，能把必须有3号部件和2号部件可有可无的电脑编程成品
输出：单位时间最大产量25,有两台机器有协作关系，
1号机器单位时间内要将15个电脑给3号机器加工
2号机器单位时间内要将10个电脑给3号机器加工

**建模**：

建模分析：
每个工厂有三个动作：
1)接收原材料
2)生产
3)将其产出的半成品给其他机器，或产出成品。
这三个过程都对应不同的流量。

**网络流模型**：
1) 添加一个原点S,S提供最初的原料 00000...
2) 添加一个汇点T, T接受最终的产品 11111....
3) 将每个机器拆成两个点: 编号为i的接收节点，和编号为i+n的产出节点（n是机器数目），前者用于接收原料，后者用于提供加工后的半成品或成品。这两个点之间要连一条边，容量为单位时间产量Qi
4) S 连边到所有接收 "0000..." 或 "若干个0及若干个2"的机器，容量为无穷大
5) 产出节点连边到能接受其产品的接收节点，容量无穷大
6) 能产出成品的节点，连边到T，容量无穷大。
7) 求S到T的最大流



![](https://blog.idejie.com/pics/max-flow24.jpg)

```
15 0 0 0 0 1 0
10 0 0 0 0 1 1
30 0 1 2 1 1 1
31 0 2 1 1 1 1
```

### 3.2 Optimal Milking（poj 2112）

```
Description

FJ has moved his K (1 <= K <= 30) milking machines out into the cow pastures among the C (1 <= C <= 200) cows. A set of paths of various lengths runs among the cows and the milking machines. The milking machine locations are named by ID numbers 1..K; the cow locations are named by ID numbers K+1..K+C. 

Each milking point can "process" at most M (1 <= M <= 15) cows each day. 

Write a program to find an assignment for each cow to some milking machine so that the distance the furthest-walking cow travels is minimized (and, of course, the milking machines are not overutilized). At least one legal assignment is possible for all input data sets. Cows can traverse several paths on the way to their milking machine. 
Input

* Line 1: A single line with three space-separated integers: K, C, and M. 

* Lines 2.. ...: Each of these K+C lines of K+C space-separated integers describes the distances between pairs of various entities. The input forms a symmetric matrix. Line 2 tells the distances from milking machine 1 to each of the other entities; line 3 tells the distances from machine 2 to each of the other entities, and so on. Distances of entities directly connected by a path are positive integers no larger than 200. Entities not directly connected by a path have a distance of 0. The distance from an entity to itself (i.e., all numbers on the diagonal) is also given as 0. To keep the input lines of reasonable length, when K+C > 15, a row is broken into successive lines of 15 numbers and a potentially shorter line to finish up a row. Each new row begins on its own line. 
Output

A single line with a single integer that is the minimum possible total distance for the furthest walking cow. 
Sample Input

2 3 2
0 3 2 1 1
3 0 3 2 0
2 3 0 1 0
1 2 1 0 2
1 0 0 2 0
Sample Output

2
```

有K台挤奶机器和C头牛(统称为物体），每台挤奶机器只能容纳M头牛进行挤奶。现在给出dis\[K + C]\[K + C]的矩阵，dis\[i\][j]若不为0则表示第i个物体到第j个物体之间有路，dis\[i]\[j]就是该路的长度。（1 <= K <= 30,1 <=C <= 200）

现在问你怎么安排这C头牛到K台机器挤奶，使得需要走最长路程到挤奶机器的奶牛所走的路程最少，求出这个最小值。

利用Floyd算法求出每个奶牛到每个挤奶机的最短距离。
则题目变为：
已知C头奶牛到K个挤奶机的距离，每个挤奶机只能有M个奶牛，每个奶牛只能去一台挤奶机，求这些奶牛到其要去的挤奶机距离的最大值的最小值。

**网络流模型**：
每个奶牛最终都只能到达一个挤奶器，每个挤奶器只能有M个奶牛，可把奶牛看做网络流中的流。
每个奶牛和挤奶器都是一个节点，添加一个源，连边到所有奶牛节点，这些边容量都是1。
添加一个汇点，每个挤奶器都连边到它。这些边的容量都是M。

先假定一个最大距离的的最小值 maxdist, 在上述图中，如果奶牛节点i和挤奶器节点j之间的距离<=maxdist,则从i节点连一条边到j节点，表示奶牛i可以到挤奶器j去挤奶。该边容量为1。该图上的最大流如果是C(奶牛数），那么就说明假设的 maxdist成立，则减小 maxdist再试总之，要二分 maxdist, 对每个maxdist值，都重新构图，看其最大流是否是C，然后再决定减少或增加maxdist

### 3.3 pigs(POJ 1149)

```
Description

Mirko works on a pig farm that consists of M locked pig-houses and Mirko can't unlock any pighouse because he doesn't have the keys. Customers come to the farm one after another. Each of them has keys to some pig-houses and wants to buy a certain number of pigs. 
All data concerning customers planning to visit the farm on that particular day are available to Mirko early in the morning so that he can make a sales-plan in order to maximize the number of pigs sold. 
More precisely, the procedure is as following: the customer arrives, opens all pig-houses to which he has the key, Mirko sells a certain number of pigs from all the unlocked pig-houses to him, and, if Mirko wants, he can redistribute the remaining pigs across the unlocked pig-houses. 
An unlimited number of pigs can be placed in every pig-house. 
Write a program that will find the maximum number of pigs that he can sell on that day.
Input

The first line of input contains two integers M and N, 1 <= M <= 1000, 1 <= N <= 100, number of pighouses and number of customers. Pig houses are numbered from 1 to M and customers are numbered from 1 to N. 
The next line contains M integeres, for each pig-house initial number of pigs. The number of pigs in each pig-house is greater or equal to 0 and less or equal to 1000. 
The next N lines contains records about the customers in the following form ( record about the i-th customer is written in the (i+2)-th line): 
A K1 K2 ... KA B It means that this customer has key to the pig-houses marked with the numbers K1, K2, ..., KA (sorted nondecreasingly ) and that he wants to buy B pigs. Numbers A and B can be equal to 0.
Output

The first and only line of the output should contain the number of sold pigs.
Sample Input

3 3
3 1 10
2 1 2 2
2 1 3 3
1 2 6
Sample Output

7
```

**题目大意**

1.Mirko养着一些猪 猪关在一些猪圈里面 猪圈是锁着的他自己没有钥匙（汗）

2.只有要来买猪的顾客才有钥匙

3.顾客依次来 每个顾客会用他的钥匙打开一些猪圈 买走一些猪 然后锁上

4.在锁上之前 Mirko有机会重新分配这几个已打开猪圈的猪

5.现在给出一开始每个猪圈的猪数 每个顾客所有的钥匙和要买走的猪数 问Mirko最多能卖掉几头猪

```
3 3
3 1 10
2 1 2 2
2 1 3 3
1 2 6

3个猪圈分别有3，1，10头猪
第一个顾客有1，2猪圈的钥匙要买2头
第二个顾客有1，3猪圈的钥匙要买3头
第三个顾客有2猪圈的钥匙要买6头
```

![](https://blog.idejie.com/pics/max-flow25.jpg)

1） 三个顾客，就有三轮交易，每一轮分别都有 3个猪圈和 1 个顾客的节点。
2） 从源点到第一轮的各个猪圈各有一条边，容量就是各个猪圈里的猪的初始数量。
3） 从各个顾客到汇点各有一条边，容量就是各个顾客能买的数量上限。
4）在某一轮中，从该顾客打开的所有猪圈都有一条边连向该顾客，容量都是 +∞。
5） 最后一轮除外，从每一轮的 i 号猪圈都有一条边连向下一轮的 i 号猪圈，容量都是 +∞，表示这一轮剩下的猪可以留到下一轮。
6） 最后一轮除外，从每一轮被打开的所有猪圈，到下一轮的同样这些猪圈，两两之间都要连一条边，容量+∞表示它们之间可以任意流通。

这个网络模型的最大流量就是最多能卖出的数量。图中最多有 2 + N + M × N ≈ 100,000 个节点。
这个模型虽然很直观，但是节点数太多了，计算速度肯定会很慢。其实不用再想别的算法，就让我们继续上面的例子，用合并的方法来简化这个网络模型。
首先，最后一轮中没有打开的猪圈就可以从图中删掉了，也就是下面图中红色的部分，显然它们对整个网络的流量没有任何影响。

![](https://blog.idejie.com/pics/max-flow26.jpg)

用以下3条规律合并节点：
规律 1. 如果几个节点的流量的来源完全相同，则可以把它们合并成一个。
规律 2. 如果几个节点的流量的去向完全相同，则可以把它们合并成一个。
规律 3. 如果从点 u 到点 v 有一条容量为 +∞的边，并且 u 是 v 的唯一流量来源，或者 v 是 u的唯一流量去向，则可以把 u 和 v 合并成一个节点。

根据规律1，可以把蓝色部分右边的 1、 2 号节点合并成一个；

根据规律2，可以把蓝色部分左边的 1、 2 号节点合并成一个；

最后，根据规律3，可以把蓝色部分的左边和右边（已经分别合并成了一个
节点）合并成一个节点。

于是，会得到下页的图。也就是说，最后一轮除外，每一轮被打开的猪圈和下一轮的同样这些猪圈都可以被合并成一个点。

![](https://blog.idejie.com/pics/max-flow27.jpg)

接着，根据规律3，此中的蓝色节点、2 号猪圈和 1 号顾客这三点可以合并成一个；两个 3 号猪圈和 2 号顾客也可以合并成一个点。当然，如果两点之间有多条同向的边，则这些边可以合并成一条，容量相加。最终，上例中的网络模型被简化成了下页图 的样子。

![](https://blog.idejie.com/pics/max-flow28.jpg)

从上图 重新总结一下构造这个网络流模型的规则：
1)每个顾客分别用一个节点来表示。
2)对于每个猪圈的第一个顾客，从源点向他连一条边，容量就是该猪圈里的猪的初始数量。如果从源点到一名顾客有多条边，则可以把它们合并成一条，容量相加。

3)对于每个猪圈，假设有 n 个顾客打开过它，则对所有整数 i ∈ [1, n)，从该猪圈的第 i 个顾客向第 i + 1 个顾客连一条边，容量为 +∞。
4)从各个顾客到汇点各有一条边，容量是各个顾客能买的数量上限。

新的网络模型中最多只有 2 + N = 102 个节点，计算速度就可以相当快了。可以这样理解这个新的网络模型：对于
某一个顾客，如果他打开了猪圈 h，则在他走后，他打开的所有猪圈里剩下的猪都有可能被换到 h 中，因而这些猪都有可能被 h 的下一个顾客买走。所以对于一个顾客打开的所有猪圈，从该顾客到各猪圈的下一个顾客，都要连一条容量为 +∞ 的边。
在面对网络流问题时，如果一时想不出很好的构图方法，不如先构造一个最直观的模型，然后再用合并节点和边的
方法来简直化这个模型。经过简化以后，好的构图思路自然就会涌现出来了。这是解决网络流问题的一个好方法。

### 3.4Budget(POj 2396 )

```
Description

We are supposed to make a budget proposal for this multi-site competition. The budget proposal is a matrix where the rows represent different kinds of expenses and the columns represent different sites. We had a meeting about this, some time ago where we discussed the sums over different kinds of expenses and sums over different sites. There was also some talk about special constraints: someone mentioned that Computer Center would need at least 2000K Rials for food and someone from Sharif Authorities argued they wouldn't use more than 30000K Rials for T-shirts. Anyway, we are sure there was more; we will go and try to find some notes from that meeting. 

And, by the way, no one really reads budget proposals anyway, so we'll just have to make sure that it sums up properly and meets all constraints.
Input

The first line of the input contains an integer N, giving the number of test cases. The next line is empty, then, test cases follow: The first line of each test case contains two integers, m and n, giving the number of rows and columns (m <= 200, n <= 20). The second line contains m integers, giving the row sums of the matrix. The third line contains n integers, giving the column sums of the matrix. The fourth line contains an integer c (c < 1000) giving the number of constraints. The next c lines contain the constraints. There is an empty line after each test case. 

Each constraint consists of two integers r and q, specifying some entry (or entries) in the matrix (the upper left corner is 1 1 and 0 is interpreted as "ALL", i.e. 4 0 means all entries on the fourth row and 0 0 means the entire matrix), one element from the set {<, =, >} and one integer v, with the obvious interpretation. For instance, the constraint 1 2 > 5 means that the cell in the 1st row and 2nd column must have an entry strictly greater than 5, and the constraint 4 0 = 3 means that all elements in the fourth row should be equal to 3.
Output

For each case output a matrix of non-negative integers meeting the above constraints or the string "IMPOSSIBLE" if no legal solution exists. Put one empty line between matrices.
Sample Input

2

2 3 
8 10 
5 6 7 
4 
0 2 > 2 
2 1 = 3 
2 3 > 2 
2 3 < 5 

2 2 
4 5 
6 7 
1 
1 1 > 10
Sample Output

2 3 3 
3 3 4 

IMPOSSIBLE 

```

现在有一个n*m的方阵,方阵里面的数字未知,但是我们知道如下约束条件:
1> 每一行的数字的和
2> 每一列的数字的和
3> 某些格子里的数，大小有限制。比如规定第2行第3列的数字必须大于5(或必须小于3,或必须等于10等）
求解是否存在在满足所有的约束的条件下用正数来填充该方阵的方案,若有,输出填充后的方阵,否则输出IMPOSSIBLE.

这道题可以转化成容量有上下界的最大流问题,将方阵的行从1……n编号,列n+1……n+m编号,添加源点s=0和汇点
t=n+m+1.
1>将源点和每一个行节点相连,相连所形成的边的容量和下界置为该行所有数字的和
2>将每一个列节点和汇点相连,相连所形成的边的容量和下界都置为该列所有数字的和
3>从每个行节点到每个列节点连边，容量为无穷大
4> 如果u行v列的数字必须大于w,则边流量的下界是w+1
5> 如果u行v列的数字必须小于w,则边容量改为w-1
6> 如果u行v列的数字必须等于w,则边流量的下界和容量都是w
找到的可行流（也是最大流），就是问题的解

本题trick:
1) W可能为负数，产生流量下界为负数的情况。应处理成0
2) 数据本身可能矛盾。比如前面说了 (2,1) =1,后面又说(2,1) = 10