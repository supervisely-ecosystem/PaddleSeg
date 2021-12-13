<<<<<<< HEAD
English|[简体中文](python_inference_cn.md)
# Paddle Inference Deployment（Python）

## 1. Description

This document introduces how to deploy the segmentation model on the server side (Nvidia GPU or X86 CPU) by Python api of Paddle Inference.

Paddle provides multiple prediction engine deployment models for different scenarios (as shown in the figure below), for more details, please refer to [document](https://paddleinference.paddlepaddle.org.cn/product_introduction/summary.html).

![inference_ecosystem](https://user-images.githubusercontent.com/52520497/130720374-26947102-93ec-41e2-8207-38081dcc27aa.png)

## 2. Prepare the model and data

Download [sample model](https://paddleseg.bj.bcebos.com/dygraph/demo/bisenet_demo_model.tar.gz) for testing.

If you want to use other models, please refer to [document](../../model_export.md) to export the model, and then test it.
=======
# Paddle Inference部署（Python）

## 1. 说明

本文档介绍使用Paddle Inference的Python接口在服务器端(Nvidia GPU或者X86 CPU)部署分割模型。

飞桨针对不同场景，提供了多个预测引擎部署模型（如下图），更多详细信息请参考[文档](https://paddleinference.paddlepaddle.org.cn/product_introduction/summary.html)。

![inference_ecosystem](https://user-images.githubusercontent.com/52520497/130720374-26947102-93ec-41e2-8207-38081dcc27aa.png)

## 2. 准备模型和数据

下载[样例模型](https://paddleseg.bj.bcebos.com/dygraph/demo/bisenet_demo_model.tar.gz)用于测试。

如果要使用其他模型，大家可以参考[文档](../../model_export.md)导出预测模型，再进行测试。
>>>>>>> 9c8570af (add new models)

```shell
wget https://paddleseg.bj.bcebos.com/dygraph/demo/bisenet_demo_model.tar.gz
tar zxvf bisenet_demo_model.tar.gz
```

<<<<<<< HEAD
Download a [picture](https://paddleseg.bj.bcebos.com/dygraph/demo/cityscapes_demo.png) of cityscapes to test.

If the model is trained using other dataset, please prepare test images by yourself.
=======
下载cityscapes验证集中的一张[图片](https://paddleseg.bj.bcebos.com/dygraph/demo/cityscapes_demo.png)用于演示效果。

如果模型是使用其他数据集训练的，请自行准备测试图片。
>>>>>>> 9c8570af (add new models)

```
wget https://paddleseg.bj.bcebos.com/dygraph/demo/cityscapes_demo.png
```

<<<<<<< HEAD
## 3. Prepare the deployment environment


Paddle Inference is the native inference library of Paddle, which provides server-side deployment model. Using the Python interface to deploy Paddle Inference model, you need to install PaddlePaddle according to the deployment situation. That is, the Python interface of Paddle Inference is integrated in PaddlePaddle.

On the server side, Paddle Inference models can be deployed on Nvidia GPU or X86 CPU. The model deployed on Nvidia GPU has fast calculation speed, and on X86 CPU has a wide range of applications.



1) Prepare the X86 CPU deployment environment

If you deploy the model on X86 CPU, please refer to the [document](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/linux-pip.html) to prepare the environment and install the CPU version of PaddlePaddle (recommended version>=2.1)，Read the installation document in detail, and choose to install the correct version of PaddlePaddle according to whether the X86 CPU machine supports avx instructions.

2) Prepare Nvidia GPU deployment environment

Paddle Inference deploys the model on the Nvidia GPU side and supports two calculation methods: Naive method and TensorRT method. The TensorRT method has a variety of calculation accuracy, which is usually faster than the Naive method.

If you use the Naive method to deploy the model on the Nvidia GPU, you can refer to the [document](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/linux-pip.html) to prepare the CUDA environment and install the corresponding GPU version of PaddlePaddle（recoment paddlepaddle-gpu>=2.1. For example:

```
# CUDA10.1 PaddlePaddle
python -m pip install paddlepaddle-gpu==2.1.2.post101 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
```

If you use TensorRT to deploy the model on the Nvidia GPU, please refer to the [document](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/linux-pip.html) to prepare the CUDA environment and install the corresponding GPU version of PaddlePaddle（recoment paddlepaddle-gpu>=2.1. For example:

```
python -m pip install paddlepaddle-gpu==[version] -f https://www.paddlepaddle.org.cn/whl/stable/tensorrt.html
```

To deploy the model using TensorRT on Nvidia GPU, you need to download the TensorRT library. 
The CUDA10.1+cudnn7 environment requires TensorRT 6.0, and the CUDA10.2+cudnn8.1 environment requires TensorRT 7.1. You can download it on the [TensorRT official website](https://developer.nvidia.com/tensorrt). We only provide the link of TensorRT under Ubuntu system here.
=======
## 3. 准备部署环境

Paddle Inference是飞桨的原生推理库，提供服务端部署模型的功能。使用Paddle Inference的Python接口部署模型，只需要根据部署情况，安装PaddlePaddle。即是，Paddle Inference的Python接口集成在PaddlePaddle中。

在服务器端，Paddle Inference可以在Nvidia GPU或者X86 CPU上部署模型。Nvidia GPU部署模型计算速度快，X86 CPU部署模型应用范围广。

1) 准备X86 CPU部署环境

如果在X86 CPU上部署模型，请参考[文档](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/linux-pip.html)准备环境、安装CPU版本的PaddlePaddle（推荐版本>=2.1）。详细阅读安装文档底部描述，根据X86 CPU机器是否支持avx指令，选择安装正确版本的PaddlePaddle。

2) 准备Nvidia GPU部署环境

Paddle Inference在Nvidia GPU端部署模型，支持两种计算方式：Naive方式和TensorRT方式。TensorRT方式有多种计算精度，通常比Naive方式的计算速度更快。

如果在Nvidia GPU使用Naive方式部署模型，同样参考[文档](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/linux-pip.html)准备CUDA环境、安装GPU版本的PaddlePaddle（请详细阅读安装文档底部描述，推荐版本>=2.1）。比如：

```
# CUDA10.1的PaddlePaddle
python -m pip install paddlepaddle-gpu==2.1.2.post101 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
```

如果在Nvidia GPU上使用TensorRT方式部署模型，同样参考[文档](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/linux-pip.html)准备CUDA环境（只支持CUDA10.1+cudnn7或者CUDA10.2+cudnn8.1）、安装对应GPU版本（支持TensorRT）的PaddlePaddle（请详细阅读安装文档底部描述，推荐版本>=2.1）。比如：

```
python -m pip install paddlepaddle-gpu==[版本号] -f https://www.paddlepaddle.org.cn/whl/stable/tensorrt.html
```

在Nvidia GPU上使用TensorRT方式部署模型，大家还需要下载TensorRT库。
CUDA10.1+cudnn7环境要求TensorRT 6.0，CUDA10.2+cudnn8.1环境要求TensorRT 7.1。
大家可以在[TensorRT官网](https://developer.nvidia.com/tensorrt)下载。这里只提供Ubuntu系统下TensorRT的下载链接。
>>>>>>> 9c8570af (add new models)

```
wget https://paddle-inference-dist.bj.bcebos.com/tensorrt_test/cuda10.1-cudnn7.6-trt6.0.tar
wget https://paddle-inference-dist.bj.bcebos.com/tensorrt_test/cuda10.2-cudnn8.0-trt7.1.tgz
```

<<<<<<< HEAD
Download and decompress the TensorRT library, and add the path of the TensorRT library to LD_LIBRARY_PATH, `export LD_LIBRARY_PATH=/path/to/tensorrt/:${LD_LIBRARY_PATH}`


## 4. Inference

In the root directory of PaddleSeg, execute the following command to predict:
=======
下载、解压TensorRT库，将TensorRT库的路径加入到LD_LIBRARY_PATH，`export LD_LIBRARY_PATH=/path/to/tensorrt/:${LD_LIBRARY_PATH}`

## 4. 预测

在PaddleSeg根目录，执行以下命令进行预测:
>>>>>>> 9c8570af (add new models)

```shell
python deploy/python/infer.py \
    --config /path/to/model/deploy.yaml \
    --image_path /path/to/image/path/or/dir
```

<<<<<<< HEAD
**The parameter description is as follows:**
|Parameter name|Function|Is it a required option|Default|
|-|-|-|-|
|config|**The configuration file generated when exporting the model**, ot the configuration file in the configs directory|Yes|-|
|image_path|The path or directory or file list of the input picture|Yes|-|
|batch_size|Batch size for single card |No|1|
|save_dir|Path to save result|No|output|
|device|Inference device, options are'cpu','gpu'|No|'gpu'|
|use_trt|Whether to enable TensorRT to accelerate prediction \(when device=gpu, this parameter takes effect\)|No|False|
|precision|The precision when enable TensorRT, the options are'fp32','fp16','int8' \(when device=gpu, this parameter takes effect\)|No|'fp32'|
|enable_auto_tune|When Auto Tune is turned on, part of the test data will be collected dynamic shapes offline for TRT deployment \(this parameter take effect when device=gpu, use_trt=True, and paddle version>=2.2\)|No| False |
|cpu_threads|The number of cpu threads \(when device=cpu, this parameter takes effect\)|No|10|
|enable_mkldnn|whether to use MKL-DNN to accelerate cpu prediction \(when device=cpu, this parameter takes effect\)|No|False|
|benchmark|Whether to generate logs, including environment, model, configuration, and performance information|No|False|
|with_argmax|Perform argmax operation on the prediction result|No|False|

**Instructions**
* If you deploy the model on an X86 CPU, you must set the device to cpu. In addition, the unique parameters for CPU deployment include cpu_threads and enable_mkldnn.
* If you use Naive mode to deploy the model on the Nvidia GPU, you must set the device to gpu.
* If you use TensorRT to deploy the model on Nvidia GPU, you must set device to gpu and use_trt to True. This method supports three precisions:
    * Load the conventional prediction model, set precision to fp32, and execute fp32 precision at this time
    * Load the conventional prediction model, set the precision to fp16, and execute the fp16 precision. It can speed up the inference time
    * Load the quantitative prediction model, set precision to int8, and execute int8 precision. It can speed up the  inference time
* If you use TensorRT mode to deploy the model on the Nvidia GPU and appears an error message `(InvalidArgument) some trt inputs dynamic shape inof not set`, you can set the enable_auto_tune parameter as True. At this time, use part of the test data to collect dynamic shapes offline, and use the collected dynamic shapes for TRT deployment. (Note that a small number of models do not support deployment using TensorRT on Nvidia GPUs).
* If you want to enable it --benchmark, you need to install auto_log, please refer to [installation method](https://github.com/LDOUBLEV/AutoLog).

The prediction results of the test sample are as follows:

![cityscape_predict_demo.png](../../images/cityscapes_predict_demo.png)

=======
**参数说明如下:**
|参数名|用途|是否必选项|默认值|
|-|-|-|-|
|config|**导出模型时生成的配置文件**, 而非configs目录下的配置文件|是|-|
|image_path|预测图片的路径或者目录或者文件列表|是|-|
|batch_size|单卡batch size|否|1|
|save_dir|保存预测结果的目录|否|output|
|device|预测执行设备，可选项有'cpu','gpu'|否|'gpu'|
|use_trt|是否开启TensorRT来加速预测（当device=gpu，该参数才生效）|否|False|
|precision|启动TensorRT预测时的数值精度，可选项有'fp32','fp16','int8'（当device=gpu，该参数才生效）|否|'fp32'|
|enable_auto_tune|开启Auto Tune，会使用部分测试数据离线收集动态shape，用于TRT部署（当device=gpu、use_trt=True、paddle版本>=2.2，该参数才生效）| 否 | False |
|cpu_threads|使用cpu预测的线程数（当device=cpu，该参数才生效）|否|10|
|enable_mkldnn|是否使用MKL-DNN加速cpu预测（当device=cpu，该参数才生效）|否|False|
|benchmark|是否产出日志，包含环境、模型、配置、性能信息|否|False|
|with_argmax|对预测结果进行argmax操作|否|否|

**使用说明如下：**
* 如果在X86 CPU上部署模型，必须设置device为cpu，此外CPU部署的特有参数还有cpu_threads和enable_mkldnn。
* 如果在Nvidia GPU上使用Naive方式部署模型，必须设置device为gpu。
* 如果在Nvidia GPU上使用TensorRT方式部署模型，必须设置device为gpu、use_trt为True。这种方式支持三种数值精度：
    * 加载常规预测模型，设置precision为fp32，此时执行fp32数值精度
    * 加载常规预测模型，设置precision为fp16，此时执行fp16数值精度，可以加快推理速度
    * 加载量化预测模型，设置precision为int8，此时执行int8数值精度，可以加快推理速度
* 如果在Nvidia GPU上使用TensorRT方式部署模型，出现错误信息`(InvalidArgument) some trt inputs dynamic shape inof not set`，可以设置enable_auto_tune参数为True。此时，使用部分测试数据离线收集动态shape，使用收集到的动态shape用于TRT部署。（注意，少部分模型暂时不支持在Nvidia GPU上使用TensorRT方式部署）。
* 如果要开启`--benchmark`的话需要安装auto_log，请参考[安装方式](https://github.com/LDOUBLEV/AutoLog)。

测试样例的预测结果如下。

![cityscape_predict_demo.png](../../images/cityscapes_predict_demo.png)
>>>>>>> 9c8570af (add new models)
