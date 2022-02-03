<<<<<<< HEAD
# Local Inference deployment

## 1. Description

This document describes deploying segmentation models on the server side using the Python interface for Paddle Inference. With a certain configuration and a small amount of code, you can integrate the model into your own service to complete the task of image segmentation.

Paddle Inference's [official website document](https://paddleinference.paddlepaddle.org.cn/product_introduction/summary.html) introduces the steps to deploy the model, various API interfaces, examples, etc. You can use it according to your actual needs .

## 2. Preliminary preparation

Please use the [Model Export Tool](../../model_export.md) to export your model, or click to download our [Sample Model](https://paddleseg.bj.bcebos.com/dygraph/demo/bisenet_demo_model.tar.gz) for testing.

Then prepare a test image for the test effect, we provide a [image](https://paddleseg.bj.bcebos.com/dygraph/demo/cityscapes_demo.png) in the validation set of cityscapes for demonstration effect, if Your model is trained using another dataset, please prepare test images by yourself.

## 3. Prediction

Enter the following command in the terminal to make predictions:
```shell
python deploy/python/infer.py --config /path/to/deploy.yaml --image_path
````

The parameter descriptions are as follows:
|Parameter name|Purpose|Required option|Default value|
|-|-|-|-|
|config|**The configuration file generated when exporting the model**, not the configuration file in the configs directory|Yes|-|
|image_path|The path or directory of the predicted image|is|-|
|use_cpu|Whether to use X86 CPU prediction, the default is to use GPU prediction|No|No|
|use_trt|Whether to enable TensorRT to speed up prediction|No|No|
|use_int8|Whether to run in int8 mode when starting TensorRT prediction|no|no|
|use_mkldnn|Whether to enable MKLDNN for accelerated prediction|No|No|
|batch_size|single card batch size|no|specified value in configuration file|
|save_dir|Directory where prediction results are saved|no |output|
|with_argmax| Perform argmax operation on the prediction result|No|No|

*Test examples and predicted results are as follows*
![cityscape_predict_demo.png](../../images/cityscapes_predict_demo.png)

**Notice**

1. When using quantitative model prediction, both TensorRT prediction and int8 prediction need to be turned on to have the acceleration effect

2. To use TensorRT, you need to use the Paddle library that supports the TRT function. Please refer to [Appendix](https://www.paddlepaddle.org.cn/documentation/docs/zh/install/Tables.html#whl-release) to download the corresponding PaddlePaddle installation package, or refer to [source code compilation](https://www.paddlepaddle.org.cn/documentation/docs/zh/install/compile/fromsource.html) to compile it yourself.
=======
# 本地Inference部署

## 1. 说明

本文档介绍使用飞桨推理的Python接口在服务器端部署分割模型。大家通过一定的配置，加上少量的代码，即可把模型集成到自己的服务中，完成图像分割的任务。

飞桨推理的[官网文档](https://paddleinference.paddlepaddle.org.cn/product_introduction/summary.html)介绍了部署模型的步骤、多种API接口、示例等等，大家可以根据实际需求进行使用。

## 2. 前置准备

请使用[模型导出工具](../../model_export.md)导出您的模型, 或点击下载我们的[样例模型](https://paddleseg.bj.bcebos.com/dygraph/demo/bisenet_demo_model.tar.gz)用于测试。

接着准备一张测试图片用于试验效果，我们提供了cityscapes验证集中的一张[图片](https://paddleseg.bj.bcebos.com/dygraph/demo/cityscapes_demo.png)用于演示效果，如果您的模型是使用其他数据集训练的，请自行准备测试图片。

## 3. 预测

在终端输入以下命令进行预测:
```shell
python deploy/python/infer.py --config /path/to/deploy.yaml --image_path
```

参数说明如下:
|参数名|用途|是否必选项|默认值|
|-|-|-|-|
|config|**导出模型时生成的配置文件**, 而非configs目录下的配置文件|是|-|
|image_path|预测图片的路径或者目录|是|-|
|use_cpu|是否使用X86 CPU预测，默认是使用GPU预测|否|否|
|use_trt|是否开启TensorRT来加速预测|否|否|
|use_int8|启动TensorRT预测时，是否以int8模式运行|否|否|
|use_mkldnn|是否开启MKLDNN进行加速预测|否|否|
|batch_size|单卡batch size|否|配置文件中指定值|
|save_dir|保存预测结果的目录|否|output|
|with_argmax|对预测结果进行argmax操作|否|否|

*测试样例和预测结果如下*
![cityscape_predict_demo.png](../../images/cityscapes_predict_demo.png)

**注意**

1. 当使用量化模型预测时，需要同时开启TensorRT预测和int8预测才会有加速效果

2. 使用TensorRT需要使用支持TRT功能的Paddle库，请参考[附录](https://www.paddlepaddle.org.cn/documentation/docs/zh/install/Tables.html#whl-release)下载对应的PaddlePaddle安装包，或者参考[源码编译](https://www.paddlepaddle.org.cn/documentation/docs/zh/install/compile/fromsource.html)自行编译。
>>>>>>> 9c8570af (add new models)
