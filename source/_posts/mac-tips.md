---
title: 关于Mac使用的Tips
date: 2016-08-23 22:19:45
tags: Mac
category: 教程
---

### 0.App Store 应用太贵？

​	xclient.info网站基本满足大多数人【想不花钱下载】的需求

​	链接：[xclient](http://xclient.info/)（壕们请购买正版）

### 1.百度云下载大文件

​	请移步另一篇博客[百度云破解](http://blog.idejie.com/2016/08/24/baiduyun-crack/)

### 2.查看当前隐藏文件目录：


 在终端输入：
```shell
 	defaults write com.apple.finder _FXShowPosixPathInTitle -bool TRUE
```

### 3.shell下装两个下载软件

```shell
	brew install wget axe
```
### 4.Safari配合`popclip`使用

### 5.终极 Shell——Zsh

​	Zsh相关介绍:[知乎](https://www.zhihu.com/search?type=content&q=zsh)

​	目前最好用的Zsh:[oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)

​	Mac安装很简单，下面两句命令里面的一句命令就可以

​	**via curl**

```shell
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

​	**via wget**

```shell
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```



### 6.Mac快捷键汇总

#### 常用的一些：

> command+Z=撤銷（如果可以的話）
> command+Y=重做（如果可以的話）
> command+C=復制?command+V=粘貼（將文件拷貝到某處）
> command+option+V=將文件移動到某處?command+A=全選
> command+shift+C：打開字體設置窗口（如果可以的話）
> command+T：打開字體設置窗口（如果可以的話）
> command+P：打印（如果可以的話）
> command+保存（如果可以的話）
> command+shift+S：另存為（如果可以的話）
> command+space：切換輸入法
> command+option+T：特殊符號（如果可以的話）（註：特殊符號窗口左上角齒輪按鈕可進行設置，增加更多符號表）
> command+option+D=啟用/禁用Dock自動隱藏功能
> ?command+option+esc：顯示強制推出窗口
> command+option+shift+esc：強制推出當前程序
> command+option+Q：註銷當前用戶
> command+,：偏好設置（如果可以的話）
> command+Q：退出當前應用程序
> command+W：關閉當前窗口（有寫程序會直接退出）
> command+E：推出所選/當前磁盤（如果可以的話）
> command+F：全屏顯示（如果可以的話）
> command+M：最小化窗口（如果可以的話）
> command+H：隱藏當前程序窗口
> command+option+H：隱藏其他程序窗口
> command+delete：移到廢紙簍
> ?command+shift+delete：清空廢紙簍（有詢問）
> command+option+shift+delete：清空廢紙簍（無提示）
> command+shift+T：添加到Dock
> command+T：添加到Finder邊欄
> option+space：菜單欄左側搜索
> option+shift+space：高級搜索
> command+option+eject：睡眠（相當於盒蓋）
> command+option+control+eject：關機
> option+power=關機（無詢問）
> shift（+fn）+F11=減小音量（無聲音提示）
> shift（+fn）+F12=增大音量（無聲音提示）

#### 一些窗口操作的：

> 按住shift單擊窗口左上角⊕符號可最大化窗口
> 按住command點擊Dock程序、文件夾或替身可到達該文件位置
> 按住control單擊（左鍵或觸控板）與鼠標右鍵單擊效果相同
> 在Launchpad裏按command+B：可以切換背景樣式，共有四種（10.7.3中改為command+option+control+B）
> 在Dashboard中選中一個widget，按command+R有旋轉特效。
> 在系統自帶拼音輸入法中，按Shift＋6：打開表情符號選擇。
> command+～：同一應用多窗口間切換

#### Finder下:

>
> command+shift+U：打開【實用工具】文件夾
> command+shift+F：打開【所有文件】側邊欄文件夾
> command+shift+O：打開【文稿】側邊欄文件夾
> command+shift+D：打開【桌面】側邊欄文件夾
> command+option+L：打開【下載】側邊欄文件夾
> command+shift+H：打開【個人】側邊欄文件夾
> command+shift+C：打開【電腦】側邊欄文件夾
> command+shift+R：打開【AirDrop】側邊欄文件夾
> command+shift+K：打開【網絡】側邊欄文件夾
> command+shift+A：打開【應用程序】側邊欄文件夾
> command+shift+N：新建文件夾
> command+option+N：用所選項目新建文件夾

#### 在Dock栏上：

>
> 按住command和option後單擊一個圖標：打開程序並隱藏當前桌面的所有程序
> 按住option後單擊iPhotos：更改iPhotos使用的圖庫
> 在抓圖工具中：
> command+shift+A：截取圈取的部分
> command+shift+W：截取選定的某個窗口
> command+Z：截取整個屏幕
> command+shift+Z：定時截圖整個屏幕，默認10秒

#### 关于截圖：

>
> 1.command+shift+3:全屏截圖，保存截圖到桌面文件
> 2.command+shift+4:鼠標選定區域截圖，保存截圖到桌面文件
> 3.command+shift+control+3：全屏截圖，保存到剪貼板
> 4.command+shift+control+4：鼠標選定區域截圖，保存到剪貼板
> 5.command+shift(+control)+4然後按下空格鍵，鼠標變成小相機，選擇某一窗口後點擊鼠標左鍵對單個窗口截圖。不必擔心其它窗口的遮擋。
> 6.按command+shift(+control)+4然後畫一個抓取的區域，不要松開鼠標，接著
> (1)按住空格可以移動這個區域
> (2)按住Shift將鎖定X或者Y軸進行拖動
> (3)按住option後將按照區域圓心進行放大
> 7.打開終端， 輸入： /System/Library/CoreServices/loginwindow.app/Contents/MacOS/loginwindow
> 登錄界面講直接顯示在桌面上。關閉終端時該界面會一同消失。
> 8.按esc鍵可取消截屏
> 關於開機：
> 開機時按住C鍵：光盤開機
> 開機時按住N鍵：網絡開機
> 開機時按住T鍵：硬盤開機
> 開始時按option鍵：選擇開機磁盤
> 開機時按command+option+shift+delete組合鍵：以外接儲存裝置內的系統開機
> 開機時按shift鍵：安全模式開機
> 開機時按V鍵：進入Verbose模式
> 開機時按S鍵：進入Single-User單人模式
> 開機時按住鼠標（左）鍵：將光盤強制退出
> 開機時按command+option+O+F組合鍵：進入Open Firmware模式
> 開機時按住command+option+P+R直到第二聲開機聲完後放開：清除PRAM
> 開機時按住command+option+N+V組合鍵：清除NV RAM
> 開機時按住Mute靜音鍵：靜音開機

#### 文檔定位：

>
> control+↑或↓：上一頁 / 下一頁
> control+←或→ ：光標定位在該行開頭 / 結尾
> option+←或→ ：光標向左 / 右移動一個詞
> option+↑或↓：光標定位在該段開頭 / 結尾
> command+↑或↓：到達該頁頁首 / 頁尾
> option+delete：刪除前面的一個詞
> command+delete：刪除該行處於光標前的所有字符
> fn+←或→ ：頁首 / 頁尾
> fn+↑或↓：上一頁 / 下一頁
> fn+delete：Del

### 8.移动硬盘使用

​	选择磁盘工具先将其分为a,b两个区。

​	a区为timemachine使用盘（大小是电脑存储大小的两倍），格式选为OS X扩展 日志式。

​	b区选为fat格式。fat格式在win下也能使用。（最好使用ntfs格式）

### 9.MacBook 清灰

[	清洁您的 Apple 产品](https://support.apple.com/zh-cn/HT3226)


[	如何对 Apple 内置或外置键盘、触控板和鼠标进行消毒](https://support.apple.com/zh-cn/HT201294)

[	知乎专栏：MacBook 一定要注意清灰——记录15" MacBook Pro (mc723) 拆机清理风扇、拆光驱换硬盘、重涂CPU 硅脂](http://zhuanlan.zhihu.com/thinkandtalk/19704849)



### 10.[Mac OS X Terminal 101：终端使用初级教程](https://www.renfei.org/blog/mac-os-x-terminal-101.html)