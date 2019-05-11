---
title: 关于支付宝AR红包的破解
date: 2016-12-24 16:18:29
category: 教程
---

昨天支付宝憋了一个大招： **AR红包**

这是一个基于图像识别和LBS的case，而且这次针对上次有人通过`抓包`的方式破解微信朋友圈图片（去年春节微信朋友圈推出的）的问题，alipay对数据流进行了处理，现在抓包是抓不到了。

但是~其实目前破解还是很简单的。

**方法一：**PS

```
点击查看线索，并快速截屏
打开PhotoShop等图片处理工具
把深度图条扣掉
把剩余的图拼在一起 #建议大家建立一个【动作】，很快的
支付宝扫图片
```

**方法二：**BitMap

```
同样得先获取到图片
算出每条横杠的相对坐标
用BitMap把图片存起来
去横杠
拼接
支付宝扫图片
```

大致上的代码：

```java
public class ARView extends View {
    private static final int dividerHeight = 7;// 这个值是慢慢试出来的
    private static final int pictureHeight = 8;// 这个不是整图的高，而是每一条没有被挡住的高
    private Paint mPaint; //用于在canvas上绘制
    private Bitmap mBitmap; // 最终要画的图
    public ARView(Context context, AttributeSet attrs) {
        super(context, attrs);
        mPaint = new Paint();
    }
    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    @Override
    protected void onDraw(Canvas canvas) {
    if (mBitmap == null) {
        final int widthh = getWidth();//  获取屏幕宽，为了最后把图片放大到填满屏幕宽度
        InputStream is = null;
        try {
            is = getContext().getAssets().open("a.png");//我截的图就直接丢assets里了，命名为a.png
            BitmapRegionDecoder decoder = BitmapRegionDecoder.newInstance(is, true);//我们只要加载线索图那一部分即可，不用加载全图
            Rect rect = new Rect(330, 963, 750, 1383);//上面定位到的坐标
            Bitmap bitmap = decoder.decodeRegion(rect, null);// 好了，拿到图了
            //不要吐槽我这里的bitmap全部没有调用recycle，只要不报错，先实现看效果再说
            bitmap = bitmap.copy(Bitmap.Config.ARGB_8888, true);//上面拿到的图是不能通过setPixel修改的，所以cp一个新的可以修改的对象。
            restoreBitmap(bitmap);//这是我自定义的方法，这是关键
            final Matrix matrix = new Matrix();
            fianl float scale = (float) width / bitmap.getWidth();// 计算屏幕宽与图片宽之比
            matrix.setScale(scale);
            mBitmap = Bitmap.createBitmap(bitmap, 0, 0, bitmap.getWidth(), bitmap.getHeight()，matrix, true);//放大图片
        } catch (Exception e) {
        } finally {
            if (is != null) {
                try {
                    is.close();
                } catch (Exception e) {
                }
           }
       }
       canvas.drawBitmap(mBitmap, 0, 0, mPaint);
    }
    private void restoreBitmap(Bitmap bitmap) {
    // ...
    }
}
```

**方法三：**

来自**虎嗅网**

```
①用深度卷积网络CNN在ImageNet上训练一个Autoencoder，训练的模型可以用AlexNet的改装版：
　　a，需要一个 Tensorflow环境或者 Caffe环境；
　　b，用一个3层卷积(Conv)、3层解卷积(Deconv)的网络进行端对端训练 ，用sigmoid交叉熵作loss；
　　c，当loss收敛时，就可以拿来破解了。
②按上面的方法先截个图，并把横条图颜色部分都置为0，然后将此图片作为卷积网络的输入部分；
③对卷积网络进行Forward，我们就可以拿到不带横条的原图。
```





以上，`仅供娱乐`。

转载请告知我。