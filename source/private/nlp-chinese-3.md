---
title: 语义分析（图片语义）
date: 2017-05-18 19:58:08
tags: 语义分析
category: NLP
---

### 3 图片语义分析

#### 3.1 图片分类

图片分类是一个最基本的图片语义分析方法。

##### 基于深度学习的图片分类

传统的图片分类如下图所示，首先需要先手工提取图片特征，譬如SIFT, GIST，再经由VQ coding和Spatial pooling，最后送入传统的分类模型(例如SVM等)。

![tranditional-imageclassify](http://dataunion.org/wp-content/uploads/2015/02/tranditional-imageclassify.png)

图23. 传统图片分类流程图

传统方法里，人工特征提取是一个巨大的消耗性工作。而随着[深度学习](http://lib.csdn.net/base/deeplearning)的进展，不再需要人工特征，通过深度学习自动提取特征成为一种可能。接下来主要讲述卷积神经网络在图片分类上的使用。

下图是一个经典的卷积神经网络模型图，由Hinton和他的学生Alex Krizhevsky在ILSVRC(Imagenet Large Scale Visual Recognition Competition) 2012中提出。 整个网络结构包括五层卷积层和三层全连接层，网络的最前端是输入图片的原始像素点，最后端是图片的分类结果。一个完整的卷积层可能包括一层convolution，一层Rectified Linear Units，一层max-pooling，一层normalization。

![convolution7](http://dataunion.org/wp-content/uploads/2015/02/convolution7.png)

图24. 卷积神经网络结构图

对于每一层网络，具体的网络参数配置如下图所示。InputLayer就是输入图片层，每个输入图片都将被缩放成227*227大小，分rgb三个颜色维度输入。Layer1~ Layer5是卷积层，以Layer1为例，卷积滤波器的大小是11*11，卷积步幅为4，本层共有96个卷积滤波器，本层的输出则是96个55*55大小的图片。在Layer1，卷积滤波后，还接有ReLUs操作和max-pooling操作。Layer6~ Layer8是全连接层，相当于在五层卷积层的基础上再加上一个三层的全连接神经网络分类器。以Layer6为例，本层的神经元个数为4096个。Layer8的神经元个数为1000个，相当于训练目标的1000个图片类别。

![convolution_config](http://dataunion.org/wp-content/uploads/2015/02/convolution_config.png)

图25. CNN网络参数配置图

基于Alex Krizhevsky提出的cnn模型，在13年末的时候，我们实现了用于广点通的图片分类和图片检索(可用于广告图片作弊判别)，下面是一些示例图。

图片分类示例：

![image_classify](http://dataunion.org/wp-content/uploads/2015/02/image_classify.png)

图26. 图片分类示例图

图片检索示例：

![image_search2](http://dataunion.org/wp-content/uploads/2015/02/image_search2.png)

![image_search1](http://dataunion.org/wp-content/uploads/2015/02/image_search1.png)

图27. 图片检索示例图

##### 图片分类上的最新进展

在ILSVRC 2012中，Alex Krizhevsky基于GPU实现了上述介绍的，这个有60million参数的模型(简称为AlexNet)，赢得了第一名。这个工作是开创性的，它引领了接下来ILSVRC的风潮。2013年，Clarifai通过cnn模型可视化技术调整网络[架构](http://lib.csdn.net/base/architecture)，赢得了ILSVRC。2014年，google也加入进来，它通过增加模型的层数（总共22层），让深度更深[48]，并且利用multi-scale data training，取得第一名。baidu最近通过更加“粗暴”的模型[44]，在GooLeNet的基础上，又提升了10%，top–5错误率降低至6%以下。具体结果如下图所示。

![imagenet_result](http://dataunion.org/wp-content/uploads/2015/02/imagenet_result.png)

图28. ImageNet Classification Result

先简单分析一下“GoogLeNet”[48,51]所采用的方法：

- 大大增加的网络的深度，并且去掉了最顶层的全连接层：因为全连接层（Fully Connected）几乎占据了CNN大概90%的参数，但是同时又可能带来过拟合（overfitting）的效果。
- 模型比以前AlexNet的模型大大缩小，并且减轻了过拟合带来的副作用。Alex模型参数是60M，GoogLeNet只有7M。
- 对于google的模型，目前已有开源的实现，有兴趣请点击[Caffe+GoogLeNet](https://github.com/BVLC/caffe/tree/master/models/bvlc_googlenet)。

再分析一下“Deep Image by baidu[44]”所采用的方法：

- Hardware/Software Co-design。baidu基于GPU，利用36个服务节点开发了一个专为深度学习运算的supercompter(名叫Minwa，敏娲)。这台supercomputer具备TB级的host memory，超强的数据交换能力，使能训练一个巨大的深层神经网络成为可能。而要训练如此巨大的神经网络，除了硬件强大外，还需要高效的并行计算框架。通常而言，都要从data-parallelism和model-data parallelism两方面考虑。
  - data-parallelism：训练数据被分成N份。每轮迭代里，各个GPU基于各自的训练数据计算梯度，最后累加所有梯度数据并广播到所有GPU。
  - model-data parallelism：考虑到卷积层参数较少但消耗计算量，而全连接层参数相对比较多。所以卷积层参数以local copy的形式被每个GPU所持有，而全连接层的参数则被划分到各个CPU。每轮迭代里，卷积层计算可以由各个GPU独立完成，全连接层计算需要由所有GPU配合完成，具体方法请参考[46]。
- Data augmentation。训练一个如此巨大的神经网络(100billion个参数)，如果没有充分的训练数据，模型将很大可能陷入过拟合，所以需要采用众多data augmentation方法增加训练数据，例如：剪裁，不同大小，调亮度，饱和度，对比度，偏色等(color casting, vignetting, lens distortion, rotation, flipping, cropping)。举个例子，一个彩色图片，增减某个颜色通道的intensity值，就可以生成多张图片，但这些图片和原图的类目是一致的，相当于增加了训练数据。
- Multi-scale training：训练不同输入图片尺度下(例如512*512，256*256)的多个模型，最后ensemble多个模型的输出结果。

#### 3.2 Image2text，Image2sentence

上面讲述的图片分类对图片语义的理解比较粗粒度，那么我们会想，是否可以将图片直接转化为一堆词语或者一段文本来描述。转化到文本后，我们积累相对深的文本处理技术就都可以被利用起来。

##### Image2text

首先介绍一种朴素的基于卷积神经网络的image to text方法。

- 首先它利用深度卷积神经网络和深度自动编码器提取图片的多层特征，并据此提取图片的visual word，建立倒排索引，产生一种有效而准确的图片搜索方法。
- 再充分利用大量的互联网资源，预先对大量种子图片做语义分析，然后利用相似图片搜索，根据相似种子图片的语义推导出新图片的语义。

其中种子图片，就是可以覆盖所有待研究图片的行业，但较容易分析语义的图片集。这种方法产生了更加丰富而细粒度的语义表征结果。虽说简单，但效果仍然不错，方法的关键在于种子图片。利用比较好的种子图片(例如paipai数据)，简单的方法也可以work得不错。下图是该方法的效果图。

[![image_semantic2](http://dataunion.org/wp-content/uploads/2015/02/image_semantic2.png)](http://dataunion.org/wp-content/uploads/2015/02/image_semantic2.png)[![image_semantic](http://dataunion.org/wp-content/uploads/2015/02/image_semantic.png)](http://dataunion.org/wp-content/uploads/2015/02/image_semantic.png)

图29. 图片语义tag标注示例图

上面的baseline方法，在训练数据优质且充分的情况下，可以取得很不错的图片tag提取效果，而且应用也非常广泛。但上面的方法非常依赖于训练数据，且不善于发现训练数据之外的世界。

另一个直观的想法，是否可以通过word embedding建立image与text的联系[26]。例如，可以先利用CNN训练一个图片分类器。每个类目label可以通过word2vec映射到一个embedding表示。对于一个新图片，先进行分类，然后对top-n类目label所对应的embedding按照权重(这里指这个类目所属的概率)相加，得到这个图片的embedding描述，然后再在word embedding空间里寻找与图片embedding最相关的words。

##### Image detection

接下来再介绍下image detection。下图是一个image detection的示例，相比于图片分类，提取到信息将更加丰富。

![image_detection](http://dataunion.org/wp-content/uploads/2015/02/image_detection.png)

图30. 图片detection示例

目前最先进的detection方法应该是Region-based CNN(简称R-CNN)[75]，是由Jeff Donahue和Ross Girshick提出的。R-CNN的具体想法是，将detection分为寻找object和识别object两个过程。在第一步寻找object，可以利用很多region detection[算法](http://lib.csdn.net/base/datastructure)，譬如selective search[76]，CPMC，objectness等，利用很多底层特征，譬如图像中的色块，图像中的边界信息。第二步识别object，就可以利用“CNN+SVM”来做分类识别。

![r-cnn](http://dataunion.org/wp-content/uploads/2015/02/r-cnn.png)

图31. Image detection系统框图

- 给定一张图片，利用selective search方法[76]来产生2000个候选窗口。
- 然后利用CNN进行对每一个候选窗口提取特征(取全连接层的倒数第一层)，特征长度为4096。
- 最后用SVM分类器对这些特征进行分类（每一个目标类别一个SVM分类器），SVM的分类器的参数个数为：4096*N，其中N为目标的类别个数，所以比较容易扩展目标类别数。

这里有R-CNN的实现，请点击[rcnn code](https://github.com/rbgirshick/rcnn)

##### Image2sentence

那能否通过深度学习方法，直接根据image产生sentence呢？我们先看一组实际效果，如下图所示(copy from 文献[43])。

![image2sentence_example](http://dataunion.org/wp-content/uploads/2015/02/image2sentence_example.png)

图32. image2sentence示例图

关于这个方向，最近一年取得了比较大的突破，工业界(Baidu[77]，Google[43]，Microsoft[80,81]等)和学术界(Stanford[35]，Borkeley[79]，UML[19]，Toronto[78]等)都发表了一系列论文。

简单归纳一下，对这个问题，主要有两种解决思路：

- Pipeline方法。这个思路相对直观一点，先学习到image中visual object对应的word(如上一节image detection所述)，再加上language model，就可以生成sentence。这种方法各个模块可以独立调试，相对来说，更灵活一点。如下图所示，这是microsoft的一个工作[81]，它分为三步：(1)利用上一节提到的思路detect words；(2)基于language model(RNN or LSTM)产生句子；(3)利用相关性模型对句子打分排序。
  [![AIC](http://dataunion.org/wp-content/uploads/2015/02/AIC.png)](http://dataunion.org/wp-content/uploads/2015/02/AIC.png)图33. “pipeline” image captioning
- End-to-end方法，即通过一个模型直接将image转换到sentence。google基于CNN+RNN开发了一个Image Caption Generator[43]。这个工作主要受到了基于RNN的机器翻译[27][42]的启发。在机器翻译中，“encoder” RNN读取源语言的句子，将其变换到一个固定长度的向量表示，然后“decoder” RNN将向量表示作为隐层初始值，产生目标语言的句子。那么一个直观的想法是，能否复用上面的框架，考虑到CNN在图片特征提取方面的成功应用，将encoder RNN替换成CNN，先利用CNN将图片转换到一个向量表示，再利用RNN将其转换到sentence。可以通过图片分类提前训练好CNN模型，将CNN最后一个隐藏层作为encoder RNN的输入，从而产生句子描述。如下图所示。
  [![cnn_rnn](http://dataunion.org/wp-content/uploads/2015/02/cnn_rnn.png)](http://dataunion.org/wp-content/uploads/2015/02/cnn_rnn.png)[![cnn_lstm](http://dataunion.org/wp-content/uploads/2015/02/cnn_lstm.png)](http://dataunion.org/wp-content/uploads/2015/02/cnn_lstm.png)图34. “CNN+LSTM” Image Caption GeneratorLi-Feifei团队在文献[35]也提到一种image2sentence方法，如下图所示。与google的做法类似，图片的CNN特征作为RNN的输入。[![cnn-rnn](http://dataunion.org/wp-content/uploads/2015/02/cnn-rnn.png)](http://dataunion.org/wp-content/uploads/2015/02/cnn-rnn.png)图35. “CNN+RNN”生成图片描述此方法有开源实现，有兴趣请参考：[neuraltalk](https://github.com/karpathy/neuraltalk)

#### 3.3 训练深度神经网络的tricks

考虑到图片语义分析的方法大部分都是基于深度学习的，Hinton的学生Ilya Sutskever写了一篇深度学习的综述文章[47]，其中提到了一些训练深度神经网络的tricks，整理如下：

- 保证训练数据的质量
- 使训练数据各维度数值的均值为0，方差为一个比较小的值
- 训练时使用minbatch，但不要设得过大，在合理有效的情况下，越小越好。
- 梯度归一化，将梯度值除于minbatch size。
- 设置一个正常的learning rate，validation无提升后，则将原learning rate除于5继续
- 模型参数随机初始化。如果是深层神经网络，不要设置过小的random weights。
- 如果是在训练RNN or LSTM，对梯度设置一个限值，不能超过15 or 5。
- 注意检查梯度计算的正确性
- 如果是训练LSTM，initialize the biases of the forget gates of the LSTMs to large values
- Data augmentation很实用。
- Dropout在训练时很有效，不过记得测试时关掉Dropout。
- Ensembling。训练多个神经网络，最后计算它们的预测值的平均值。

### 4 总结

#### 4.1 语义分析方法在实际业务中的使用

前面讲述了很多语义分析方法，接下来我们看看如何利用这些方法帮忙我们的实际业务，这里举一个例子，用户广告的语义匹配。

在广点通系统中，用户与广告的关联是通过定向条件来匹配的，譬如某些广告定向到“北京+男性”，那么当“北京+男性”的用户来到时，所有符合定向的广告就将被检索出，再按照“ecpm*quality”排序，将得分最高的展示给用户。但是凭借一些人口属性，用户与广告之间的匹配并不精确，做不到“广告就是想用户所想”，所以用户和广告的语义分析就将派上用场了，可以从这样两方面来说明：

- 特征提取。基于上面介绍的方法，提取用户和广告的语义特征。
  - 用户语义特征。可以从用户的搜索，购物，点击，阅读记录中发现用户兴趣。考虑到最终的用户描述都是文本，那么文本topic分析，文本分类，文本keyword提取，文本核心term提取都可以运用起来，分析出用户的语义属性，还可以利用矩阵分解和文本分类找到相似用户群。
  - 广告语义特征。在广点通里，广告可以从两个维度来描述，一方面是文本，包括广告title和landing page，另一方面是广告展示图片。利用文本和图片的语义分析方法，我们可以提取出广告的topic，类目，keyword，tag描述。
- 语义匹配。提取到相应的语义特征之后，怎么用于改善匹配呢？
  - 用户-广告的语义检索。基于keyword、类目以及topic，对广告建立相应的倒排索引，直接用于广告检索。
  - 用户-广告的语义特征。分别提取用户和广告的语义特征，用于计算用户-广告的relevance，pctr，pcvr，达到精确排序。

#### 4.2 Future

对于文本和图片的语义分析，可以看到：最近几年，在某些任务上，基于深度学习的方法逐渐超过了传统方法的效果。但目前为止，对于深度学习的发掘才刚刚开始，比较惊艳的神经网络方法，也只有有限几种，譬如CNN，RNN，RBM等。

上文只是介绍了我们在工作中实践过的几个小点，还有更多方法需要我们去挖掘：

- Video。Learn about 3D structure from motion。如文献[19]所示，研究将视频也转换到自然语言。
- Deep Learning + Structured Prediction，用于syntactic representation。

#### 4.3 总结

上文主要从文本、图片这两方面讲述了语义分析的一些方法，并结合个人经验做了一点总结。

原本想写得更全面一些，但写的时候才发现上面所述的只是沧海一粟，后面还有更多语义分析的内容之后再更新。另外为避免看到大篇理论就头痛，文中尽可能不出现复杂的公式和理论推导。如果有兴趣，可以进一步阅读参考文献，获得更深的理解。谢谢。