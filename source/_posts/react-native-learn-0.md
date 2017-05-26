---
title: React-Native学习（一）：了解React-Native
date: 2016-12-05 14:53:19
tags: React-Native
category: 教程
---

> LEARN ONCE, WRITE ANYWHERE: BUILD MOBILE APPS WITH REACT

*以下为转载*：[Jag的技术博客](https://jaggerwang.net/react-native-cross-platform-mobile-app-develop-intro/)

# 0.开篇

[React Native](//link.zhihu.com/?target=https%3A//facebook.github.io/react-native/) (简称RN)是Facebook于2015年4月开源的跨平台移动应用开发框架，是Facebook早先开源的UI框架 [React](//link.zhihu.com/?target=https%3A//facebook.github.io/react/) 在原生移动应用平台的衍生产物，目前支持iOS和安卓两大平台。RN使用Javascript语言，类似于HTML的JSX，以及CSS来开发移动应用，因此熟悉Web前端开发的技术人员只需很少的学习就可以进入移动应用开发领域。

RN运行时包含一个原生主线程和一个JS线程，JS线程执行JS代码，负责界面布局和业务逻辑处理，原生线程负责界面渲染和原生功能执行。RN尽量使用原生组件（现有原生组件经过封装后可在JS里调用），以避免重复造轮子。这样有很多好处，一是可以利用现有的大量的原生组件；二是可以达到跟原生组件一样的性能；三是通过JS封装过后的组件可以支持跨平台。

JS在RN里面的作用类似于Python这样的支持调用原生C库的脚本语言，都是起着“胶水”的作用。复杂计算和系统功能通过调用原生接口来完成，流程控制和业务逻辑则在“胶水”语言里完成。这样既提高了开发效率，又兼顾了性能。

# 1.起源

本文章系列是 [Go + Docker API服务开发和部署](//link.zhihu.com/?target=https%3A//jaggerwang.net/develop-and-deploy-api-service-with-go-and-docker-intro/) 的姊妹篇，都是笔者在开发 [在球场](//link.zhihu.com/?target=https%3A//www.zaiqiuchang.com/) 这款体育社交类应用过程中的技术总结。该应用已经发布到AppStore、GooglePlay和腾讯应用宝，覆盖iOS和安卓两大平台。平台之间的代码复用率超过90%，流畅度接近原生应用。相比而言iOS的体验更为流畅一些，毕竟RN最先支持的就是iOS平台，优化做得更好。

经过这次的实际开发体验，笔者相信RN以后将成为绝大多数移动应用开发的首选技术。除开那些对性能要求非常苛刻的应用，比如游戏类。RN目前的短板在于代码的稳定性不够，经JS封装的原生组件还比较少。不过这些随着时间的发展将会很快解决，毕竟RN从开源到现在也才一年多时间就达到了目前的水平，发展速度非常之快。

# 2.内容目录

简化版的代码已在GitHub开源，[在球场开源版](//link.zhihu.com/?target=https%3A//github.com/jaggerwang/zqc-app-demo) 。网易云课堂上有讲解更详细的付费视频课程，[React Native跨平台移动应用开发之基础篇](//link.zhihu.com/?target=http%3A//study.163.com/course/courseMain.htm%3FcourseId%3D1003433016) 。

1. 开篇
2. [搭建开发和调试环境](//link.zhihu.com/?target=https%3A//jaggerwang.net/react-native-cross-platform-mobile-app-develop-environment/)
3. [技术栈](//link.zhihu.com/?target=https%3A//jaggerwang.net/react-native-cross-platform-mobile-app-develop-techs)
4. [布局和导航](//link.zhihu.com/?target=https%3A//jaggerwang.net/react-native-cross-platform-mobile-app-develop-layout)
5. [启动](//link.zhihu.com/?target=https%3A//jaggerwang.net/react-native-cross-platform-mobile-app-develop-bootstrap)
6. [数据同步](//link.zhihu.com/?target=https%3A//jaggerwang.net/react-native-cross-platform-mobile-app-develop-data-sync/)
7. [登录注册](//link.zhihu.com/?target=https%3A//jaggerwang.net/react-native-cross-platform-mobile-app-develop-register-login/)
8. [首页](//link.zhihu.com/?target=https%3A//jaggerwang.net/react-native-cross-platform-mobile-app-develop-nearby/)
9. [打包发布](//link.zhihu.com/?target=https%3A//jaggerwang.net/react-native-cross-platform-mobile-app-develop-package-publish/)

# 3.其他资料

1. [视频课程 - React Native跨平台移动应用开发之基础篇](//link.zhihu.com/?target=http%3A//study.163.com/course/courseMain.htm%3FcourseId%3D1003433016)
2. [在球场开源版](//link.zhihu.com/?target=https%3A//github.com/jaggerwang/zqc-app-demo)
3. [技术文章 - Go + Docker API服务开发和部署](//link.zhihu.com/?target=https%3A//jaggerwang.net/develop-and-deploy-api-service-with-go-and-docker-intro/)
4. [在球场官网](//link.zhihu.com/?target=https%3A//www.zaiqiuchang.com/)

