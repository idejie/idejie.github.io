---
title: 利用 Google 资源进行机器学习
date: 2018-01-23 23:02:41
tags: Google,Colab
category: 教程
---

在这篇文章中，我将演示如何通过google colab 使用机器学习。(需科学上网)

Google colab是Google数据科学的一个内部研究工具。他们早些时候向公众发布了这个工具，传播机器学习教育和研究的崇高目标。这已经有相当长的一段时间了，不过最近有一个新特点会引起很多人的兴趣。

> You can use GPU as a backend for free for 12 hours at a time.
>
> 您可以一次将GPU作为后端免费使用12小时

*“GPU compute for free? Are you kidding me?”*

这是我立即想到的那种问题。事实上，它工作得很好，非常有用。请通过这个[Kaggle讨论](https://www.kaggle.com/getting-started/47096)了解更多关于这个公告的细节。讨论的几个要点:

1.当前在后端使用的GPU是K80。
2.12小时限制是为了连续分配虚拟机。这意味着我们甚至可以在12小时后通过连接到不同的虚拟机来使用GPU计算。

Google Colab有很多不错的功能，协作是其中的一个主要功能。我不打算在这里介绍这些功能，（见我上一篇文章 [Google-Colab 简介](http://blog.idejie.com/2018/01/23/colab/)），但是特别是如果你和一群人一起工作，这是一件好事。

所以让我们开始通过这个服务一起使用fastai 吧。

## Get Started

### 1.使用 google 账户登录

### 2.库的安装和使用

Colab 自带了 Tensorflow、Matplotlib、Numpy、Pandas 等深度学习基础库。如果还需要其他依赖，如 Keras，可以新建代码块，输入

```shell
#其他库的安装也类如此
#如：
# 安装最新版本Keras  https://keras.io/
# !pip install keras
# 指定版本安装  !pip install keras==2.0.9
```

### 3 Google Drive 文件操作

#### 授权登录

对于同一个 notebook，登录操作只需要进行一次，然后才可以进度读写操作。

```shell
# 安装 PyDrive 操作库，该操作每个 notebook 只需要执行一次
!pip install -U -q PyDrive
```

正式鉴权

```python
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# 授权登录，仅第一次的时候会鉴权
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)
```

执行这段代码后，会打印以下内容，点击连接进行授权登录，获取到 token 值填写到输入框，按 Enter 继续即可完成登录。![img](http://upload-images.jianshu.io/upload_images/854231-6c9034087199c6ac.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 遍历目录

```python
# 列出根目录的所有文件
# "q" 查询条件教程详见：https://developers.google.com/drive/v2/web/search-parameters
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s, mimeType: %s' % (file1['title'], file1['id'], file1["mimeType"]))
```

可以看到控制台打印结果
```python
 title: Colab 测试, id: 1cB5CHKSdL26AMXQ5xrqk2kaBv5LSkIsJ8HuEDyZpeqQ, mimeType: application/vnd.google-apps.document

title: Colab Notebooks, id: 1U9363A12345TP2nSeh2K8FzDKSsKj5Jj, mimeType: application/vnd.google-apps.folder
```
其中 id 是接下来的教程获取文件的唯一标识。根据 mimeType 可以知道 `Colab 测试` 文件为 doc 文档，而 Colab Notebooks 为文件夹（也就是 Colab 的 Notebook 储存的根目录），如果想查询 Colab Notebooks 文件夹下的文件，查询条件可以这么写：

```python
# '目录 id' in parents
file_list = drive.ListFile({'q': "'1cB5CHKSdL26AMXQ5xrqk2kaBv5LBkIsJ8HuEDyZpeqQ' in parents and trashed=false"}).GetList()
```

#### 读取文件内容

目前测试过可以直接读取内容的格式为 `.txt`（mimeType: text/plain），读取代码：

```
file = drive.CreateFile({'id': "替换成你的 .txt 文件 id"}) 
file.GetContentString()
```

而 `.csv` 如果用`GetContentString()`只能打印第一行的数据，要用``

```python
file = drive.CreateFile({'id': "替换成你的 .csv 文件 id"}) 
#这里的下载操作只是缓存，不会在你的Google Drive 目录下多下载一个文件
file.GetContentFile('iris.csv', "text/csv") 

# 直接打印文件内容
with open('iris.csv') as f:
  print f.readlines()
# 用 pandas 读取
import pandas
pd.read_csv('iris.csv', index_col=[0,1], skipinitialspace=True)
```

Colab 会直接以表格的形式输出结果（下图为截取 iris 数据集的前几行）， iris 数据集地址为 http://aima.cs.berkeley.edu/data/iris.csv ，学习的同学可以执行上传到自己的 Google Drive。![img](http://upload-images.jianshu.io/upload_images/854231-8dd03edab3209a35.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 写文件操作

```python
# 创建一个文本文件
uploaded = drive.CreateFile({'title': '示例.txt'})
uploaded.SetContentString('测试内容')
uploaded.Upload()
print('创建后文件 id 为 {}'.format(uploaded.get('id')))
```

更多操作可查看 http://pythonhosted.org/PyDrive/filemanagement.html

### 4 Google Sheet 电子表格操作

#### 授权登录

对于同一个 notebook，登录操作只需要进行一次，然后才可以进度读写操作。

```shell
# 安装相应的库
!pip install --upgrade -q gspread
```

鉴权

```python
from google.colab import auth
auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials

gc = gspread.authorize(GoogleCredentials.get_application_default())
```

#### 读取

把 iris.csv 的数据导入创建一个 Google Sheet 文件来做演示，可以放在 Google Drive 的任意目录

```python
worksheet = gc.open('iris').sheet1

# 获取一个列表[
# [第1行第1列, 第1行第2列, ... , 第1行第n列], ... ,[第n行第1列, 第n行第2列, ... , 第n行第n列]]
rows = worksheet.get_all_values()
print(rows)

#  用 pandas 读取
import pandas as pd
pd.DataFrame.from_records(rows)
```

打印结果分别为

> [['5.1', '3.5', '1.4', '0.2', 'setosa'], ['4.9', '3', '1.4', '0.2', 'setosa'], ...![img](http://upload-images.jianshu.io/upload_images/854231-16ef6d58748e80d5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 写入

```python
sh = gc.create('谷歌表') # 尽量英文

# 打开工作簿和工作表
worksheet = gc.open('谷歌表').sheet1
cell_list = worksheet.range('A1:C2')

import random
for cell in cell_list:
  cell.value = random.randint(1, 10)
worksheet.update_cells(cell_list)
```

### 5 下载文件到本地

```python
with open('example.txt', 'w') as f:
  f.write('测试内容')
files.download('example.txt')
```

### 6.附加说明

通过前面，你已经知道了如何对 Google Drive 和 Sheet 做操作了。你可以将所需文件上传至 相应位置。

也可以直接在 colab上传。`File->Upload Notebook`。

### 7.不使用 GPU

这里以我在 Github 的开源LSTM 文本分类项目为例子https://github.com/Jinkeycode/keras_lstm_chinese_document_classification把 `master/data` 目录下的三个文件存放到 Google Drive 上。该示例演示的是对健康、科技、设计三个类别的标题进行分类。

#### 新建

在 Colab 上新建 Python2 的笔记本![img](http://upload-images.jianshu.io/upload_images/854231-10c33b01a51c7a14.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### 安装依赖

```python
!pip install keras
!pip install jieba
!pip install h5py

import h5py
import jieba as jb
import numpy as np
import keras as krs
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
```

#### 加载数据

授权登录

```python
# 安装 PyDrive 操作库，该操作每个 notebook 只需要执行一次
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

def login_google_drive():
  # 授权登录，仅第一次的时候会鉴权
  auth.authenticate_user()
  gauth = GoogleAuth()
  gauth.credentials = GoogleCredentials.get_application_default()
  drive = GoogleDrive(gauth)
  return drive
```

列出 GD 下的所有文件

```python
def list_file(drive):
  file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
  for file1 in file_list:
    print('title: %s, id: %s, mimeType: %s' % (file1['title'], file1['id'], file1["mimeType"]))
    

drive = login_google_drive()
list_file(drive)
```

缓存数据到工作环境

```python
def cache_data():
  # id 替换成上一步读取到的对应文件 id
  health_txt = drive.CreateFile({'id': "117GkBtuuBP3wVjES0X0L4wVF5rp5Cewi"}) 
  tech_txt = drive.CreateFile({'id': "14sDl4520Tpo1MLPydjNBoq-QjqOKk9t6"})
  design_txt = drive.CreateFile({'id': "1J4lndcsjUb8_VfqPcfsDeOoB21bOLea3"})
  #这里的下载操作只是缓存，不会在你的Google Drive 目录下多下载一个文件
  
  health_txt.GetContentFile('health.txt', "text/plain")
  tech_txt.GetContentFile('tech.txt', "text/plain")
  design_txt.GetContentFile('design.txt', "text/plain")
  
  print("缓存成功")
  
cache_data()
```

读取工作环境的数据

```python
def load_data():
    titles = []
    print("正在加载健康类别的数据...")
    with open("health.txt", "r") as f:
        for line in f.readlines():
            titles.append(line.strip())

    print("正在加载科技类别的数据...")
    with open("tech.txt", "r") as f:
        for line in f.readlines():
            titles.append(line.strip())


    print("正在加载设计类别的数据...")
    with open("design.txt", "r") as f:
        for line in f.readlines():
            titles.append(line.strip())

    print("一共加载了 %s 个标题" % len(titles))

    return titles
  
titles = load_data()
```

加载标签

```python
def load_label():
    arr0 = np.zeros(shape=[12000, ])
    arr1 = np.ones(shape=[12000, ])
    arr2 = np.array([2]).repeat(7318)
    target = np.hstack([arr0, arr1, arr2])
    print("一共加载了 %s 个标签" % target.shape)

    encoder = LabelEncoder()
    encoder.fit(target)
    encoded_target = encoder.transform(target)
    dummy_target = krs.utils.np_utils.to_categorical(encoded_target)

    return dummy_target
  
target = load_label()
```

#### 文本预处理

```python
max_sequence_length = 30
embedding_size = 50

# 标题分词
titles = [".".join(jb.cut(t, cut_all=True)) for t in titles]

# word2vec 词袋化
vocab_processor = tf.contrib.learn.preprocessing.VocabularyProcessor(max_sequence_length, min_frequency=1)
text_processed = np.array(list(vocab_processor.fit_transform(titles)))

# 读取词标签
dict = vocab_processor.vocabulary_._mapping
sorted_vocab = sorted(dict.items(), key = lambda x : x[1])
```

#### 构建神经网络

这里使用 Embedding 和 lstm 作为前两层，通过 softmax 激活输出结果

```python
# 配置网络结构
def build_netword(num_vocabs):
    # 配置网络结构
    model = krs.Sequential()
    model.add(krs.layers.Embedding(num_vocabs, embedding_size, input_length=max_sequence_length))
    model.add(krs.layers.LSTM(32, dropout=0.2, recurrent_dropout=0.2))
    model.add(krs.layers.Dense(3))
    model.add(krs.layers.Activation("softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    return model
  
num_vocabs = len(dict.items())
model = build_netword(num_vocabs=num_vocabs)

import time
start = time.time()
# 训练模型
model.fit(text_processed, target, batch_size=512, epochs=10, )
finish = time.time()
print("训练耗时：%f 秒" %(finish-start))
```

#### 预测样本

sen 可以换成你自己的句子，预测结果为`[健康类文章概率, 科技类文章概率, 设计类文章概率]`, 概率最高的为那一类的文章，但最大概率低于 0.8 时判定为无法分类的文章。

```python
sen = "做好商业设计需要学习的小技巧"
sen_prosessed = " ".join(jb.cut(sen, cut_all=True))
sen_prosessed = vocab_processor.transform([sen_prosessed])
sen_prosessed = np.array(list(sen_prosessed))
result = model.predict(sen_prosessed)

catalogue = list(result[0]).index(max(result[0]))
threshold=0.8
if max(result[0]) > threshold:
    if catalogue == 0:
        print("这是一篇关于健康的文章")
    elif catalogue == 1:
        print("这是一篇关于科技的文章")
    elif catalogue == 2:
        print("这是一篇关于设计的文章")
    else:
        print("这篇文章没有可信分类")
```

### 8.使用 GPU

a.为您的笔记本启用GPU后端`Runtime->Change runtime type->Hardware Accelerator->GPU`

b.检查GPU是否启用，可以运行我共享笔记本中的第一个单元。（我已经上传了fastai Lesson 1的notebook。请访问这个[笔记本](https://drive.google.com/file/d/1Yhmmws6eelhXs2WQHJ7BUMQO9Wu5MoQj/view?usp=sharing)以供参考）

![](https://ws2.sinaimg.cn/large/006tKfTcgy1fnqyyv64gbj30vy09ogn3.jpg)

c. 安装 fast.ai & pytorch

```shell
!pip install http://download.pytorch.org/whl/cu75/torch-0.3.0.post4-cp36-cp36m-linux_x86_64.whl  && pip install torchvision
!pip install fastai
```

d.下载数据，你也可以提前上传至 drive

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fnqz1hbfk9j315k02agm0.jpg)

### 9.效果说明

执行并不是很顺畅，但是也在意料之中

a.在尝试连接GPU运行时，它有时会抛出一个错误，指出它无法连接。这是由于尝试使用该服务的人数众多与GPU机器的数量相关。根据之前分享的kaggle讨论，他们计划添加更多的GPU机器。
 b.有时，运行时间会间歇性地死掉。这可能有许多潜在的原因。
c.可用的RAM数量是13GB，因为它是免费的，所以太好了。但是像第一课那样的大型网络，大多数时候都有内存警告。

### 10.总结

谷歌真的帮助减少进入深度学习的门槛。而像这样的工具将帮助许多无法承受GPU资源的人。我真的希望这将是一个完全缩小的服务很快，并将保持自由。

我会继续更新这篇文章，因为我会弄清楚如何处理这些小问题，并使流程顺利进行。如果有人能够解决这些小问题，请在评论中告诉我。

### 参考文章：

> 1.[Fast.ai Lesson 1 on Google Colab (Free GPU)](https://towardsdatascience.com/fast-ai-lesson-1-on-google-colab-free-gpu-d2af89f53604)
>
> 2.[想免费用谷歌资源训练神经网络？Colab 详细使用教程](https://jinkey.ai/post/tech/xiang-mian-fei-yong-gu-ge-zi-yuan-xun-lian-shen-jing-wang-luo-colab-xiang-xi-shi-yong-jiao-cheng)

