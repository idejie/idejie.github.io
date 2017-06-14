---
title: 学习ThreeJS一哈
date: 2017-06-14 19:46:30
tags: ThreeJS
category: JavaScript
---

# 〇、概述

**什么是 ThreeJS**

首先你要知道 OpenGL 和 WebGL。

> OpenGL（全写Open Graphics Library）是指定义了一个跨编程语言、跨平台的[编程接口](http://baike.baidu.com/item/%E7%BC%96%E7%A8%8B%E6%8E%A5%E5%8F%A3)规格的专业的图形[程序接口](http://baike.baidu.com/item/%E7%A8%8B%E5%BA%8F%E6%8E%A5%E5%8F%A3)。它用于[三维图像](http://baike.baidu.com/item/%E4%B8%89%E7%BB%B4%E5%9B%BE%E5%83%8F)（二维的亦可），是一个功能强大，调用方便的底层图形库。
>
> WebGL（全写Web Graphics Library）是一种3D绘图标准，这种绘图技术标准允许把JavaScript和OpenGL ES 2.0结合在一起，通过增加OpenGL ES 2.0的一个JavaScript绑定，WebGL可以为HTML5 Canvas提供硬件3D加速渲染，这样Web开发人员就可以借助系统显卡来在浏览器里更流畅地展示3D场景和模型了，还能创建复杂的导航和数据视觉化。显然，WebGL技术标准免去了开发网页专用渲染插件的麻烦，可被用于创建具有复杂3D结构的网站页面，甚至可以用来设计3D网页游戏等等。
>
> from baidu

然后什么是 ThreeJS

>ThreeJS就是用 WebGL 实现的一个3D 的 JS 库

**ThreeJS 有什么用**

封装了底层的图形接口，可以在 HTML 上利用 Canvas 和 SVG 进行渲染3D 模块。

**为什么学习 ThreeJS**

效果酷炫，想利用这个库重新设计我的 blog

# 一、开始

## 1.开发环境

个人比较习惯 SublimeText3+Chrome

安装 ThreeJS 的话：下载[源码](https://threejs.org/build/three.js);使用 npm

## 2.Hello ThreeJS

先引入

```html
<script type="text/javascript" src='js/three.js'></script>
```



然后创建一个 Canvas

```html
<canvas id='demo' width="100%" height="100%"></canvas>
```

ThreeJS 由渲染器(Render)、场景(Scene)、摄像机（Camera）,以及我们创建的三维模型

![](https://ws2.sinaimg.cn/large/006tKfTcly1fgl0fffauvj30gz0ed75h.jpg)

**渲染器**：渲染器利用 id 属性和Canvas元素进行绑定

```javascript
var renderer = new THREE.WebGLRenderer({      
  canvas: document.getElementById('your-canvas-id') 
});
```



也可以让他自动生成一个 Canvas

```javascript
var renderer = new THREE.WebGLRenderer(); 
renderer.setSize(400, 300);  
document.getElementsByTagName('body')[0].appendChild(renderer.domElement); 
```

**场景**：在 ThreeJS 都是将物体加载到场景中

```javascript
var scene = new THREE.Scene(); 
```

**摄像机**：相当于一个三维坐标系的建立，采用相机透视成影

```javascript
var camera = new THREE.PerspectiveCamera(45, 4 / 3, 1, 1000); 
camera.position.set(0, 0, 5); 
scene.add(camera);  
<!-- cammera 也要加载到场景中 -->
```

试着渲染一个长方形

```javascript
<!DOCTYPE html>
<html>

<head>
    <meta charset=utf-8>
    <title>Hello ThreeJS</title>
    <link rel="stylesheet" type="text/css" href="css/style.css"> </style>
    <!--  引入 ThreeJS -->
    <script type="text/javascript" src='js/three.js'></script>
</head>

<body onload="init()">
    <p>Hello ThreeJS</p>
    <script type="text/javascript">
    function init() {
        
        //renderer
        var renderer = new THREE.WebGLRenderer();
        renderer.setSize(400, 300);
        renderer.setClearColor(0xffff00);
        document.getElementsByTagName('body')[0].appendChild(renderer.domElement);

        //scene
        var scene = new THREE.Scene();

        //camera
        var camera = new THREE.PerspectiveCamera(45,4/3,1,1000);
        camera.position.set(0,0,5);
        scene.add(camera);

        //初始化一个 Cube
        var cube = new THREE.Mesh(
        	new THREE.CubeGeometry(1,2,3),new THREE.MeshBasicMaterial({
        		color: 0xff0000
        	}));

        scene.add(cube);
        renderer.render(scene,camera);
    }
    </script>
</body>

</html>
```

# 二、Camera

## **什么是 Camera**

由于图像或者视频都是二维的，把三维的图像转换成二维的，就需要类似于平时的摄像机

![](https://ws4.sinaimg.cn/large/006tKfTcly1fgl0queix3j30e90be0tj.jpg)

而且根据投影方式的不同，又分为正交投影和透视投影

## **Orthographic Camera**

**正交投影**一个长方体为例，正交投影就相当数学老师在黑板上画的。

![](https://ws2.sinaimg.cn/large/006tKfTcly1fgl0yh0krqj30d007pdg2.jpg)

构造函数

```javascript
THREE.OrthographicCamera(left,right,top,botton,near,far)
```

![](https://ws3.sinaimg.cn/large/006tKfTcly1fgl11t882kj31kw1ff799.jpg)

这6个参数分别代表着正交投影摄像机到空间的6个位置，这样围成的一个长方体称之为 **视景体**

在视景体中只有上图灰色位置才能显示在屏幕上

为了保持照相机的横竖比例,需要保证 (right - left) 与 (top - bottom) 的比例与 Canvas宽度与高度的比例一致。

near 与 far 都是指到照相机位置在深度平面的位置,而照相机不应该拍摄到其后方的物体,因此这两个值应该均为正值。为了保证场景中的物体不会因为太近或太远而被照相机忽略,一般 near 的值设置得较小, far 的值设置得较大,具体值视场景中物体的位置等决定。

​				

## Perspective Camera		

透视投影摄像机获得结果和人眼在真实世界看到的“近大远小”的效果相似

他的构造函数

```javascript
THREE.PerspectiveCamera(fov, aspect, near, far)
```

![](https://ws4.sinaimg.cn/large/006tKfTcly1fgl34j239zj30s90ca0tw.jpg)

透视图中,灰色的部分是视景体,是可能被渲染的物体所在的区域。 fov 是视景体竖直方向上的张角(是角度制而非弧度制),如侧视图所示。

aspect 等于 width / height ,是照相机水平方向和竖直方向长度的比值,通常设为Canvas 的横纵比例。

near 和 far 分别是照相机到视景体最近、最远的距离,均为正值,且 far 应大于near 。

## 示例

正交摄像机的位置：

**基础配置**	

```javascript
var camera = new THREE.OrthographicCamera(-2, 2, 1.5, -1.5, 1, 10); 
camera.position.set(0, 0, 5);
scene.add(camera);
```

在原点处创建一个边长为 1正方体,为了和透视效果做对比,这里我们使用wireframe

而不是实心的材质,以便看到正方体后方的边:

```javascript
var cube = new THREE.Mesh(
  new THREE.CubeGeometry(1, 1, 1), 
  new THREE.MeshBasicMaterial({
    color: 0xff0000,
    wireframe: true })
  );
```

**改变长宽比例**

```javascript
var camera = new THREE.OrthographicCamera(-1, 1, 1.5, -1.5, 1, 10);
```

**改变相机位置**

```javascript
var camera = new THREE.OrthographicCamera(-2, 2, 1.5, -1.5, 1, 10); 
camera.position.set(1, 0, 5);
```

**改变相机角度**

```javascript
camera.position.set(4, -3, 5);//此时看不到物体
```

让相机指向原点

```javascript
camera.lookAt(new THREE.Vector3(0, 0, 0));
```

透视相机再来试一遍：

**基础配置**

```javascript
        var camera = new THREE.PerspectiveCamera(45,400/300,1,10); 
        camera.position.set(0, 0, 5);
        scene.add(camera);
        //初始化一个 Cube
        var cube = new THREE.Mesh(
        	new THREE.CubeGeometry(1,1,1),
        	new THREE.MeshBasicMaterial({
        		color: 0xff0000,
        		wireframe: true
        	})
        );
```

**改变竖直张角**

把 fov 的45改成60

为什么正方体显得更小了呢?我们从下面的侧视图来看,虽然正方体的实际大小并未改变,但是将照相机的竖直张角设置得更大时,视景体变大了,因而正方体相对于整个视景体的大小就变小了,看起来正方形就显得变小了。

![](https://ws3.sinaimg.cn/large/006tKfTcly1fgl3nqwdxaj30io0go0tf.jpg)

# 三、基本几何形状

## 立方体

## 平面

## 球体

## 圆形

## 圆柱

## 圆台

## 正 N 面体

## 圆环面

## 圆环结

# 四、基本的文字形状

# 五、材质

# 六、网格

# 七、动画

# 八、导入外部模型

# 九、光

# 十、着色				

​			
​		
​	