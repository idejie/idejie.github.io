##输入输出

# name = input()
# print ('hello',name)

##转义字符

# print('\\r:','\r')

##打印多行

# print('''j
# k
# l''')

##布尔值

# print(True and False)
# print(True or False)
# print (not True)

##字符串和编码

# print('%2d-%02d' % (3, 3)) 
# #第一个2表示这个字段长度为2，不足补空格；02表示这个字段长度为2，不足补0
# print('%5.3d-%05.3d' %(3,3))
# #第一个5.3表示表示这个字段长度为5，不足的补空格，整数部分最短为3位，不足补0；
# #05.3表示表示这个字段长度为5，不足的补0，整数部分最短为3位，不足补0；
# print('%2d-%2d' %(0300,300))
# #0300是八进制 如果是什么 X就是16进制，但是输出还是10进制整数
# #python3会报错
# print('%.2f' % 3.1415926)
# print('%5.2f' % 3.1415926)
# print('%5.2f' % 3.1)
# print('%05.2f' % 3.1)
# print('Age: %s. Gender: %s' % (25, True))
# print('growth rate: %d %%' % 7)
# print('growth rate: %d %s' %(7,'%'))

##list

# classmate = ['张三','李四']
# print(classmate)
# classmate.append('王五')
# print(classmate)
# classmate.insert(1,'钱六')
# print(classmate)
# classmate.pop()
# print(classmate)
# classmate.pop(1)
# print(classmate)
# print(classmate[-1])
# print(len(classmate))

# ##list和数组的不同
# L = ['Apple', 123, True]
# print(L)
# s = ['python', 'java', ['asp', 'php'], 'scheme']
# print(s)
# print(s[2][0])

##tuple
# classmates = ('Michael', 'Bob', 'Tracy')
# print(classmates)
# print(classmates[2])

# t = (1,)
# print(t)
# print(len(t))

# # classmates[2]="xx"##报错
# t = ('a', 'b', ['A', 'B'])
# t[2][0] = 'X'
# t[2][1] = 'Y'
# print(t)

##dict

# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'])

##set
# s=(1)
# print(type(s))
# s=(1,)
# print(type(s))
# s=([1,2,3,2,3])
# print(type(s))
# s = set([1,2,3, 2, 3])
# print(type(s))
# print (s)
# s.add(4)
# print(s)
# s.remove(3)
# print(s)
# s2=set([2,3,4])
# print(s&s2)
# print(s|s2)

##切片
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[0:3])
# print(L[:3])
# print(L[1:3])
# print(L[-2:])
# print(L[-2:-1] )
#tuple 同理

# L = list(range(100))
# print(L[:10:2])
# print(L[::5])
# print(L[:])

##迭代

#1.list tuple
#2.dict
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)
# for value in d.values():
#     print(value)
# for k,v in d.items():
#     print(k,v)

##列表生成式
# L = [x * x for x in range(1, 11) if x % 2 == 0]
# print(L)
# S = [m + n for m in 'ABC' for n in 'XYZ']
# print(S)

##生成器
# g = (x * x for x in range(10))
# print(g)
# print(next(g))

##yield
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)
# o =odd()
# print(next(o))
# print(next(o))
# print(next(o))
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# f = fib(6)
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
#
# for n in fib(6):
#     print(n)

##迭代器

#一类是集合数据类型，如list、tuple、dict、set、str等；

#一类是generator，包括生成器和带yield的generator function。


##条件判断
# x =input()
# if(x=="a"):
# 	print("a")
# else:
# 	print("not a")

##循环

##for...in
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)
# print(list(range(5)))

##while
# n = 9
# while n > 0:
#     print(n)
#     n = n-1

##break
# n = 9
# while n > 0:
#     if(n==3):
#         break
#     print(n)
#     n=n-1

##continue
# n = 9
# while n > 0:
#     n = n - 1
#     if n==3:
#         continue
#     print(n)

##函数

##定义一个函数
# def my_abs(x):
#     if x>0:
#         return x
#     else:
#         return -x
# print(my_abs(-1))

##返回多个值
# def swap(a,b):
#     t=a
#     a=b
#     b=t
#     return a,b
# print(swap(1,2))

##定义一个空函数
# def nop():
#     pass

##递归函数
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
##函数参数
##参数检查
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs('a'))

##位置参数
# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#print(power(5,4))

##默认参数
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#print(power(5))
#print(power(5,1))

##可变参数
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc([1,2,3]))
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc(1,2,3))

##关键词参数
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
# person('Michael', 30)

##命名关键字参数
#
# def person(name, age, *, city, job):
#     print(name, age, city, job)
# person('Jack', 24,city='Beijing', job='Engineer')  ##必须 args='value'
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)
# person('Jack', 24, 's','Beijing', 'Engineer')

##参数组合
## 顺序：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

###函数式编程
##高阶函数

##函数也可以指向变量

# def add(x,y,f):
#     print (f(x)+f(y))
# add(-1,1,abs)


##map
# def f(x):
# 	return x*x

# r = map(f,[1,2,3,4,5])
# print(list(r))
# L=[]
# for n in [1,2,3,4]:
# 	L.append(n)
# print(L)
# print(list (map(str,[1,2,3,4,5,6])))

##reduce

# from functools import reduce
# def f(x,y):
# 	return x+y
# print(reduce(f,[1,2,3,4]))

##  map  then  reduce

# from functools import reduce 
# def f(x,y):
# 	return x*10+y
# def char2num(s):
# 	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# r = reduce(f,map(char2num,'13579'))
# print(r,type(r))

##filter
# def is_odd(n):
#     return n % 2 == 1

# r = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# print(r)

## filter 产生素数

##生成奇数
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# ##筛选函数
# def _not_divisible(n):
#     return lambda x: x % n > 0
# ##生成素数
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
# ##打印
# for n in primes():
#     if n < 10:
#         print(n)
#     else:
#         break

##sorted

# r =sorted([36,5,-12,9,-21])
# print(r)

# r = sorted(['bob','about','Zoo','zoo'],key=str.lower,reverse=True)
# print(r)

##返回函数

##可以返回一个函数

# def lazy_sum(*args):
#     def sum():
#         ax=0
#         for n in args:
#             ax+=n
#         return ax
#     return sum
# f=lazy_sum(1,3,5,7,9)
# f2=lazy_sum(1,3,5,7,9)
# print(f())
# print(f==f2)

##闭包

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
# f1, f2, f3 = count()
#
# print(f1(),f2(),f3())

##匿名函数 lambda

# def fn():
#     x,y=1,2
#     return lambda :x+y
#
# print(fn()())

# def fn():
#     x,y=1,2
#     return lambda  x,y:x+y
# print(fn()(3,4))

# def fn():
#     x,y=1,2
#     return lambda x=x,y=y:x+y
# print(fn()())

##装饰器


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print('call %s()'%func.__name__)
#         return func(*args,**kw)
#     return wrapper

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('%s %s'%(text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator
# @log('www')
# def now():
#     print('2017-6-1')
# now()

##偏函数
# print( int('12345', base=8))
# print(int('12345', 16))
#
# import functools
# int8 = functools.partial(int,base=8)
# print(int8('17'))

##错误处理
# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     bar('0')
#
# main()

# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise
#
# bar()

##调试

# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
# def main():
#     foo('0')
# main()

# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

# s = '0'
# n = int(s)
# print(10 / n)

# err.py
# import pdb
#
# s = '0'
# n = int(s)
# pdb.set_trace() # 运行到这里会自动暂停
# print(10 / n)

# import unittest
# class Dict(dict):
#
#     def __init__(self, **kw):
#         super().__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
# class TestDict(unittest.TestCase):
#
#     def test_init(self):
#         d = Dict(a=1, b='test')
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))
#
#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key, 'value')
#
#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
#
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']
#
#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty
# if __name__ == '__main__':
#     unittest.main()
#
# class TestDict(unittest.TestCase):
#
#     def setUp(self):
#         print('setUp...')
#
#     def tearDown(self):
#         print('tearDown...')


##文档测试
# class Dict(dict):
#     '''
#     Simple dict but also support access as x.y style.
#
#     >>> d1 = Dict()
#     >>> d1['x'] = 100
#     >>> d1.x
#     100
#     >>> d1.y = 200
#     >>> d1['y']
#     200
#     >>> d2 = Dict(a=1, b=2, c='3')
#     >>> d2.c
#     '3'
#     >>> d2['empty']
#     Traceback (most recent call last):
#         ...
#     KeyError: 'empty'
#     >>> d2.empty
#     Traceback (most recent call last):
#         ...
#     AttributeError: 'Dict' object has no attribute 'empty'
#     '''
#     def __init__(self, **kw):
#         super(Dict, self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
# if __name__=='__main__':
#     import doctest
#     doctest.testmod()
#     print("0000")


##IO编程

##读
# f =  open('./hello.txt','r')
# r = f.read()
# print(r)
# f.close()

# try:
#     f = open('./hello.t', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#
# with open('./hello.py', 'r',encoding='utf-8', errors='ignore') as f:
#     # print(f.read())
#     for line in f.readlines():
#         print(line.strip())  # 把末尾的'\n'删掉

##写
# f = open('./test.txt', 'w')
# f.write('hello')
# f.close()
# f = open('./test.txt','r')
# r = f.read()
# print(r)

##StringIO

# from io import StringIO
# f =StringIO()
# f.write('hello')
# f.write(' ')
# f.write('python')
# print(f.getvalue())

# from io import StringIO
#
# f = StringIO('Hello\nHi\nGoodBye')
# while True:
#     s= f.readline()
#     if s=='':
#         break
#     print(s.strip())

##ByteIO

# from io import BytesIO
#
# f=BytesIO()
# f.write(" 照片你玩个".encode('utf-8'))
# print(f.getvalue())

# from io import BytesIO
#
# f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())

##操作文件和目录
# import os
# print(os.name)
# print(os.uname())
# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.environ.get('x','default'))
# print(os.path.abspath('.'))
# print(os.path.join(os.path.abspath('.'), 'testdir'))
# os.mkdir(os.path.abspath('.')+'/testdir')
# os.rmdir(os.path.abspath('.')+'/testdir')
# print(os.path.split('/Users/michael/testdir/file.txt'))
# print(os.path.splitext('/path/to/file.t'))
# os.rename('test.txt', 'test.py')
# os.remove('test.py')
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

##序列化

##pickle

# import pickle
#
# d= dict(name="BOB",age=20,score=88)
# print(pickle.dumps(d))

# f= open('dump.txt','w')
# f.write("hello")

# f= open('dump.txt','wb')
# pickle.dump(d,f)
# f.close()
# f=open('dump.txt','rb')
# d=pickle.load(f)
# f.close()
# print(d)

##JSON
# import json
# d=dict(name='Bob',age=20,score=88)
# d2=dict(name="ss",other=d)
# print(json.dumps(d2))
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str))

##JSON进阶

# import json
# class Student(object):
#     def __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
# s = Student('Bob',20,88)
# print(json.dumps(s,default=student2dict))
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print(json.loads(json_str, object_hook=dict2student))

##多进程
# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

##mutilprocessing 库平台
# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print("I am the child process %s(%s)..."%(name,os.getpid()))
# if __name__=='__main__':
#     print("I am Parent process %s..."%os.getpid())
#     p=Process(target=run_proc,args=('test',))
#     print("start")
#     p.start()
#     print("join")
#     p.join()
#     print("end")

##Pool 批量子进程

# from multiprocessing import Pool
# import os,time,random
# def long_time_task(name):
#     print('Run task %s(%s)'%(name,os.getpid()))
#     start=time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.'%(name,(end-start)))
# if __name__=='__main__':
#     print('Parent process %s.'%os.getpid())
#     p=Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print("Wait")
#     p.close()
#     p.join()
#     print("End")

##子进程
# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

##子进程输入

# import subprocess

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

##进程间的通信
# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

##多线程

# import time, threading
#
# # 新线程执行的代码:
# def loop():
#     print('2thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('1thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

##lock
#
# import time, threading
#
# # 假定这是你的银行存款:
# balance = 0
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)
#
# balance = 0
# lock = threading.Lock()
#
# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()

##多 CPU
# import threading, multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

##ThreadLocal
# import threading
#
# # 创建全局ThreadLocal对象:
# local_school = threading.local()
#
# def process_student():
#     # 获取当前线程关联的student:
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))
#
# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()
#
# t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

##分布式进程

    ##master
# import random, time, queue
# from multiprocessing.managers import BaseManager
#
# # 发送任务的队列:
# task_queue = queue.Queue()
# # 接收结果的队列:
# result_queue = queue.Queue()
#
# # 从BaseManager继承的QueueManager:
# class QueueManager(BaseManager):
#     pass
#
# # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)
# # 绑定端口5000, 设置验证码'abc':
# manager = QueueManager(address=('', 5000), authkey=b'abc')
# # 启动Queue:
# manager.start()
# # 获得通过网络访问的Queue对象:
# task = manager.get_task_queue()
# result = manager.get_result_queue()
# # 放几个任务进去:
# for i in range(10):
#     n = random.randint(0, 10000)
#     print('Put task %d...' % n)
#     task.put(n)
# # 从result队列读取结果:
# print('Try get results...')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result: %s' % r)
# # 关闭:
# manager.shutdown()
# print('master exit.')

##worker
# import time, sys, queue
# from multiprocessing.managers import BaseManager
#
# # 创建类似的QueueManager:
# class QueueManager(BaseManager):
#     pass
#
# # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
# QueueManager.register('get_task_queue')
# QueueManager.register('get_result_queue')
#
# # 连接到服务器，也就是运行task_master.py的机器:
# server_addr = 'localhost'
# print('Connect to server %s...' % server_addr)
# # 端口和验证码注意保持与task_master.py设置的完全一致:
# m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# # 从网络连接:
# m.connect()
# # 获取Queue的对象:
# task = m.get_task_queue()
# result = m.get_result_queue()
# # 从task队列取任务,并把结果写入result队列:
# for i in range(10):
#     try:
#         n = task.get(timeout=1)
#         print('run task %d * %d...' % (n, n))
#         r = '%d * %d = %d' % (n, n, n*n)
#         time.sleep(1)
#         result.put(r)
#     except queue.Queue.Empty:
#         print('task queue is empty.')
# # 处理结束:
# print('worker exit.')

##正则表达式

# \d \w  . \d{n} \d{n,m} \s \s+
# 转义字符
#[0-9a-zA-Z\_]
#[0-9a-zA-Z\_]+
#[a-zA-Z\_][0-9a-zA-Z\_]*
#[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}
#A|B (P|p)yhton
#^\d
#\d$


##re 模块

# import re
# print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
# print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

##切分字符串
# print('ab c'.split(' '))
# print('ab  c'.split(' '))
# print('ab   c'.split(' '))
# print('a b   c'.split(' '))

# import re
# print(re.split(r'\s+','ab  c'))
# print(re.split(r'[\s\,]+','a,b,,c  d'))
# print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

##分组
# import re
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))

##变态版
# import re
# t = '19:05:30'
#
# m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)

##贪婪匹配
# import re
# r=re.match(r'^(\d+)(0*)$', '102300').groups()
# print(r)
# r=re.match(r'^(\d+?)(0*)$', '102300').groups()
# print(r)

##编译

# import re
# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# r=re_telephone.match("010-12345").groups()
# print(r)
# r=re_telephone.match("010-8086").groups()
# print(r)