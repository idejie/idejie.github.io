---
title: Sublime Text 3 总结
date: 2016-12-05 16:21:33
tags: Sublime Text 3
category: 工具
---

# 1.下载

[官网](http://www.sublimetext.com/3)

Sublime Text：一款具有代码高亮、语法提示、自动完成且反应快速的编辑器软件，不仅具有华丽的界面，还支持插件扩展机制，用她来写代码，绝对是一种享受。相比于难于上手的Vim，浮肿沉重的Eclipse，VS，即便体积轻巧迅速启动的Editplus、Notepad++，在SublimeText面前大略显失色，无疑这款性感无比的编辑器是Coding和Writing最佳的选择，没有之一。

# 2.配置

### 1.**Package Control组件安装**

按Ctrl+`调出console（注：安装有QQ输入法的这个快捷键会有冲突的，输入法属性设置-输入法管理-取消热键切换至QQ拼音）粘贴以下代码到底部命令行并回车：

```cpp
import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
```

重启Sublime Text 3。如果在Perferences->package settings中看到package control这一项，则安装成功。按下Ctrl+Shift+P调出命令面板输入install 调出 Install Package 选项并回车，然后在列表中选中要安装的插件。

## 2.插件安装

按下Command+shift+P

输入Install

然后分别搜索

- **Material Theme**
- **HTML-CSS-JS Prettify**
- **SideBarEnhancements**
- **Color Highlighter**
- **Sublime Linter**
- **Alignment**
- **JSFormat**
- **Emment**
- **Bracket Highlighter**
- **Color Picker**
- **Auto FileName**
- **Nodejs**
- ​

