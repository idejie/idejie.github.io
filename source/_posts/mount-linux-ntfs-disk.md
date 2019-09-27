---
title: Linux挂载NTFS盘爬坑
date: 2019-09-24 17:03:07
tags: NTFS
category: Linux
---

> 最近下载的数据有点多，Ubuntu系统盘空间不够了，寻思着挂载一个移动硬盘上去，可以随时拷贝数据了

## 问题

使用`mount`命令挂载成功，但是挂载目录**权限**迅速变成`777`，新建目录、新建文件也是`777`

```bash
$ sudo mount /dev/sda2 /data
$ ls -al /|grep data
drwxrwxrwx   2 root root       4096 Sep 24 08:38 data
$ ls -al /data
total 8
drwxrwxrwx  1 root root 4096 Sep 25 01:44 .
drwxr-xr-x 25 root root 4096 Sep 24 08:38 ..
drwxrwxrwx  1 root root    0 Sep 24 08:09 .fseventsd
drwxrwxrwx  1 root root    0 Sep 24 02:44 my_data
$ ls -al /data/my_data
total 23263020
drwxrwxrwx 1 root root       4096 Sep 24 05:25 .
drwxrwxrwx 1 root root          0 Sep 24 02:44 ..
-rwxrwxrwx 1 root root 1460568449 Aug 15 10:22 DCMH-FLICKR-25K.mat
-rwxrwxrwx 1 root root 3320572656 Aug 19 07:19 FLICKR-25K.mat
drwxrwxrwx 1 root root       4096 Dec 18  2008 iaprtc12
-rwxrwxrwx 1 root root  212159349 Aug 15 10:27 imagenet-vgg-f.mat
drwxrwxrwx 1 root root          0 Aug 16 07:40 mirflickr
-rwxrwxrwx 1 root root 4942078436 Sep  1 07:39 mobike.zip
drwxrwxrwx 1 root root       4096 Aug 13 10:03 NUS-WIDE
-rwxrwxrwx 1 root root 6934610146 Sep 23 12:50 task2.zip
drwxrwxrwx 1 root root          0 Aug 20 09:20 task3
-rwxrwxrwx 1 root root 6951316869 Sep 23 12:50 task3.zip
```

如上，所有的文件权限都变成了`777`

```shell
$ sudo chomd -x task3.zip
$ ls -al task3.zip
-rwxrwxrwx 1 root root 6951316869 Sep 23 12:50 task3.zip
$ sudo chown dejie:dejie task3.zip
-rwxrwxrwx 1 root root 6951316869 Sep 23 12:50 task3.zip
```

`chmod`和`chown`,以及`chgrp`都失效了

## 解决

首先挂载`mount`只有root用户可以执行

然后目前看文件的权限，文件时`-rwxrwxrwx`，目录是`drwxrwxrwx`

分析原因可能是挂载的时候出现了问题，极有可能是NTFS盘的原因，毕竟是windows下的格式

后发现mount在挂载时，自动启用了ntfs或者ntfs-3g文件系统格式

而使用这种格式时，NTFS硬盘一旦挂载，所有的权限都和初始指定的权限有关，就算创建新的文件、目录也是按照初始权限，无法修改

**这权限可不可以改呢？**

这权限和系统的`umask`有关，这个编码正好和linux下的权限编码相反。

具体地讲，[维基百科-umask](https://gg0.chn.moe/extdomains/en.wikipedia.org/wiki/Umask)

**umask命令**用来设置限制新建文件权限的掩码。当新文件被创建时，其最初的权限由文件创建掩码决定。用户每次注册进入系统时，umask命令都被执行， 并自动设置掩码mode来限制新文件的权限。用户可以通过再次执行umask命令来改变默认值，新的权限将会把旧的覆盖掉。

举一个简单的例子，[在Linux中设置UMASK值](https://www.cnblogs.com/wish123/p/7073114.html)

对于root用户，系统默认的umask值是0022；对于普通用户，系统默认的umask值是0002。执行umask命令可以查看当前用户的umask值。

umask值一共有4组数字，其中第1组数字用于定义特殊权限，我们一般不予考虑，与一般权限有关的是后3组数字。

默认情况下，对于目录，用户所能拥有的最大权限是777；对于文件，用户所能拥有的最大权限是目录的最大权限去掉执行权限，即666。因为x执行权限对于目录是必须的，没有执行权限就无法进入目录，而对于文件则不必默认赋予x执行权限。

对于root用户，他的umask值是022。当root用户创建目录时，默认的权限就是用最大权限777去掉相应位置的umask值权限，即对于所有者不必去掉任何权限，对于所属组要去掉w权限，对于其他用户也要去掉w权限，所以目录的默认权限就是755；当root用户创建文件时，默认的权限则是用最大权限666去掉相应位置的umask值，即文件的默认权限是644。

可以通过下面的测试操作来了解umask值。

```bash
$ mkdir directory1 #创建测试目录
$ ll -d directory1 #目录的默认权限是755
drwxr-xr-x. 2 root root 4096 12月 2 13:08 directory1
$ touch file1 #创建测试文件
$ ll file1 #文件的默认权限是644
-rw-r--r--. 1 root root 0 12月 2 13:09 file1
```

通过umask命令可以修改umask值，比如将umask值设为0077。

```bash
$ umask 0077
$ umask
0077
```

此时创建的目录默认权限为700，文件默认权限是600：

```bash
$ mkdir directory2
$ ll -d directory2
drwx------. 2 root root 4096 12月 2 13:14 directory2
$ touch file2
$ ll file2
-rw-------. 1 root root 0 12月 2 13:14 file2
```

考虑一下，如果将umask值设为0003，那么此时创建的目录或文件的默认权限是多少？

正确的结果应该是：目录的默认权限是774，文件的默认权限是664。在计算默认权限时，不应用最大权限直接减去umask值，而是将umask值所对应的相应位置的权限去掉，这样才能得到正确的结果。

`mode_code + mask_code = 777 `

**所以，我们在挂载的时候要指定umask**

```bash
$ sudo mount -t ntfs /dev/sda2 /data -o iocharset=utf8,umask=001
```

同样，你还可以使用`fmask`和`dmask`分别指定文件权限、目录权限

```bash
sudo mount -t ntfs /dev/sda2 /data -o iocharset=utf8,fmask=111,dmask=002
```

你也可以可以配置在`/etc/fstab`下面，在后面`追加一行`

```
/dev/sda2 /data ntfs  iocharset=utf8,fmask=111,dmask=002 0 0
```

**怎么在挂载后修改权限呢？**

针对NTFS盘，目前还没有找到方法

只能格式化为ext或者xfs格式了。。。c

