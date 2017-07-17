---
title: 使用 OpenWRT 来 DIY 路由器
date: 2017-07-17 22:15:43
tags: OpenWRT
category: 教程
---

# OpenWRT

**OpenWrt**是适合于[嵌入式](https://zh.wikipedia.org/wiki/%E5%B5%8C%E5%85%A5%E5%BC%8F)设备的一个[Linux](https://zh.wikipedia.org/wiki/Linux)发行版。

相对原厂固件而言，OpenWrt不是一个单一、静态的[固件](https://zh.wikipedia.org/wiki/%E5%9B%BA%E4%BB%B6)，而是提供了一个可添加软件包的可写的[文件系统](https://zh.wikipedia.org/wiki/%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F)。这使用户可以自由的选择应用程序和配置，而不必受设备提供商的限制，并且可以使用一些适合某方面应用的软件包来定制你的设备。对于开发者来说，OpenWrt是一个框架，开发者不必麻烦的构建整个固件就能得到想要的[应用程序](https://zh.wikipedia.org/wiki/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F)；对于用户来说，这意味着完全定制的能力，与以往不同的方式使用设备，OPKG包含超过3500个软件。 默认使用LuCI作为web交互界面。

# Supported Device

详见官方提供的[列表](https://wiki.openwrt.org/toh/start)

# Just do it

本人使用的路由器为小米路由器 Mini(R1CM)

## 1.将路由器的原系统更新至开发版

- 请先准备一个U盘，并确保这个U盘的格式为FAT或FAT32.


- 在miwifi.com官网下载路由器对应的ROM包，并将其放在U盘的根目录下，命名为miwifi.bin
- 断开小米路由器mini的电源，将U盘插入路由器的USB接口
- 按下reset按钮后重新接入电源，待指示灯变为黄色闪烁状态后松开reset键
- 等待5~8分钟，刷机完成之后系统会自动重启并进入正常的启动状态（指示灯由黄灯常亮变为蓝灯常亮），此时，说明刷机成功完成！

## 2.开启 SSH 权限

- 使用小米提供的官方 APP 绑定路由器
- 查看官网提供的 SSH 密码[网站](http://d.miwifi.com/rom/ssh)
- 下载对应的工具包
- 请将下载的工具包bin文件复制到U盘（FAT/FAT32格式）的根目录下，保证文件名为miwifi_ssh.bin；
- 断开小米路由器的电源，将U盘插入USB接口；
- 按住reset按钮之后重新接入电源，指示灯变为黄色闪烁状态即可松开reset键；
- 等待3-5秒后安装完成之后，小米路由器会自动重启，之后您就可以尽情折腾啦 ：）

## 3.安装 OpenWRT

- 使用命令行工具SSH 连接

```shell
ssh root@192.168.31.1
```

![](https://ws2.sinaimg.cn/large/006tKfTcly1fhn9732jg9j30eg085q45.jpg)

- [下载](http://downloads.openwrt.org/chaos_calmer/15.05.1/ramips/mt7620/openwrt-15.05.1-ramips-mt7620-xiaomi-miwifi-mini-squashfs-sysupgrade.bin)OpenWRT官方提供的小米路由器定制包
- 使用 `scp`将 OpenWRT工具包拷贝至路由器

```shell
scp ./openwrt-15.05.1-ramips-mt7620-xiaomi-miwifi-mini-squashfs-sysupgrade.bin root@192.168.31.1:/tmp #注意使用/tmp 目录，其他目录只可读
```

- 写入 OpenWRT

```shell
mtd -r write /tmp/openwrt-15.05.1-ramips-mt7620-xiaomi-miwifi-mini-squashfs-sysupgrade.bin OS1
```

- 等待设备重启，大约3min

## 4.开始 OpenWRT

- 浏览器打开192.168.1.1


- 初始密码为 admin，上方会提示你修改密码,点击进入

![](https://ws3.sinaimg.cn/large/006tKfTcly1fhn9c0927aj30du06574j.jpg)

- 同时开启远程访问权限（可选）

![](https://ws1.sinaimg.cn/large/006tKfTcly1fhn9dm3ag5j30iv018t8q.jpg)

- save & apply

- 设置网络

  ![](https://ws4.sinaimg.cn/large/006tKfTcly1fhn9fhwbg7j30ds021aa7.jpg)

  - 点击 **Interfaces**
  - ![](https://ws1.sinaimg.cn/large/006tKfTcly1fhn9g6yjxxj30ql06w75i.jpg)
  - 根据提示和个人情况进行配置网络

  ![](https://ws4.sinaimg.cn/large/006tKfTcly1fhn9h76i2bj30b207zwf6.jpg)


- ssh 连接 OpenWRT

![](https://ws4.sinaimg.cn/large/006tKfTcly1fhn99bmdsdj30b708bab2.jpg)

# 更进一步

## 开启中文界面

```shell
opkg update
opkg install luci-i18n-base-zh-cn
```

![](https://ws2.sinaimg.cn/large/006tKfTcly1fhn9klmhe7j30ep029aa6.jpg)

![](https://ws1.sinaimg.cn/large/006tKfTcly1fhn9ktqgvjj30dk05xdg2.jpg)

## 挂载 U 盘

你会发现装上几个软件包，overplay就快满了,所以挂载 U 盘吧

以 NTFS 盘为例

- 安装必要安装包

```
opkg update
opkg install fdisk
opkg install kmod-usb-storage kmod-fs-ntfs ntfs-3g kmod-nls-utf8 kmod-fs-nfs-common kmod-fs-nfs 
```

- 查看 U 盘盘符

```shell
fdisk -l
```

![](https://ws1.sinaimg.cn/large/006tKfTcly1fhn9p1gda9j30bm00w0ss.jpg)

- 挂载 /dev/sda1(可能是其他名字)到overplay
  ![](https://ws1.sinaimg.cn/large/006tKfTcly1fhn9p1gda9j30bm00w0ss.jpg)

- 查看挂载是否成功

  ![](https://ws1.sinaimg.cn/large/006tKfTcly1fhn9rgqurvj30c403tjrz.jpg)

- 接下来就可以任性装包了

## Python

```shell
opkg install python
```

- pip

```
python get-pip.py
```

下载[get-pip.py](https://bootstrap.pypa.io/get-pip.py)

## More

**wait ...**