<<<<<<< HEAD
English|[简体中文](serving_cn.md)
# Paddle Serving deployment

## Overview

The model trained by PaddleSeg can be deployed as a service using [Paddle Serving](https://github.com/PaddlePaddle/Serving).

This turtorial introduces the deployment method using Paddle Serving. For more details, please refer to the [document](https://github.com/PaddlePaddle/Serving/blob/v0.6.0/README_CN.md).


## Environmental preparation

Environment preparations are required on the server side and the client side. Please refer to [document](https://github.com/PaddlePaddle/Serving/blob/v0.6.0/README_CN.md#%E5%AE%89%E8%A3%85) for more details.

On the server side:
* Install PaddlePaddle (version>=2.0)
* Install paddle-serving-app (version>=0.6.0)
* Install paddle-serving-server or paddle-serving-server-gpu (version>=0.6.0)

    ```shell
    pip3 install paddle-serving-app==0.6.0

    # CPU
    pip3 install paddle-serving-server==0.6.0

    # Choose paddle-serving-server-gpu according to your GPU environment
    pip3 install paddle-serving-server-gpu==0.6.0.post102 #GPU with CUDA10.2 + TensorRT7
    pip3 install paddle-serving-server-gpu==0.6.0.post101 # GPU with CUDA10.1 + TensorRT6
    pip3 install paddle-serving-server-gpu==0.6.0.post11 # GPU with CUDA10.1 + TensorRT7
    ```

On the client side:
* Install paddle-serving-app (version>=0.6.0)
* Install paddle-serving-client (version>=0.6.0)

    ```shell
    pip3 install paddle-serving-app==0.6.0
    pip3 install paddle-serving-client==0.6.0
    ```
 
## Prepare model and data

Download the [sample model](https://paddleseg.bj.bcebos.com/dygraph/demo/bisenet_demo_model.tar.gz) for testing. If you want to use other models, please refer to [model export tool](../../model_export.md).

```shell
$ wget https://paddleseg.bj.bcebos.com/dygraph/demo/bisenet_demo_model.tar.gz
tar zxvf bisenet_demo_model.tar.gz
```

Download a [picture](https://paddleseg.bj.bcebos.com/dygraph/demo/cityscapes_demo.png) from cityscape to test.  If your model is trained on other datasets, please prepare test images by yourself.

```shell
$ wget https://paddleseg.bj.bcebos.com/dygraph/demo/cityscapes_demo.png
```

## Convert model

Before Paddle Serving is deployed, we need to convert the prediction model. For details, please refer to the [document](https://github.com/PaddlePaddle/Serving/blob/v0.6.0/doc/SAVE_CN.md).

On the client side, execute the following script to convert the sample model.
=======
# Paddle Serving部署

## 概述

PaddleSeg训练出来的模型，大家可以使用[Paddle Serving](https://github.com/PaddlePaddle/Serving)进行服务化部署。

本文以一个示例介绍使用Paddle Serving部署的方法，更多使用教程请参考[文档](https://github.com/PaddlePaddle/Serving/blob/v0.6.0/README_CN.md)。


## 环境准备

使用Paddle Serving部署模型，要求在服务器端和客户端进行如下环境准备。大家具体可以参考[文档](https://github.com/PaddlePaddle/Serving/blob/v0.6.0/README_CN.md#%E5%AE%89%E8%A3%85)进行安装。

在服务器端：
* 安装PaddlePaddle (版本>=2.0)
* 安装paddle-serving-app（版本>=0.6.0）
* 安装paddle-serving-server或者paddle-serving-server-gpu （版本>=0.6.0）

```
pip3 install paddle-serving-app==0.6.0

# CPU
pip3 install paddle-serving-server==0.6.0

# GPU环境需要确认环境再选择
pip3 install paddle-serving-server-gpu==0.6.0.post102 #GPU with CUDA10.2 + TensorRT7
pip3 install paddle-serving-server-gpu==0.6.0.post101 # GPU with CUDA10.1 + TensorRT6
pip3 install paddle-serving-server-gpu==0.6.0.post11 # GPU with CUDA10.1 + TensorRT7
```

在客户端：
* 安装paddle-serving-app（版本>=0.6.0）
* 安装paddle-serving-client（版本>=0.6.0）

```
pip3 install paddle-serving-app==0.6.0
pip3 install paddle-serving-client==0.6.0
```

## 准备模型和数据

下载[样例模型](https://paddleseg.bj.bcebos.com/dygraph/demo/bisenet_demo_model.tar.gz)用于测试。如果要使用其他模型，大家可以使用[模型导出工具](../../model_export.md)。

```shell
wget https://paddleseg.bj.bcebos.com/dygraph/demo/bisenet_demo_model.tar.gz
tar zxvf bisenet_demo_model.tar.gz
```

下载cityscapes验证集中的一张[图片](https://paddleseg.bj.bcebos.com/dygraph/demo/cityscapes_demo.png)用于演示效果。如果大家的模型是使用其他数据集训练的，请自行准备测试图片。

```
wget https://paddleseg.bj.bcebos.com/dygraph/demo/cityscapes_demo.png
```

## 转换模型

Paddle Serving部署之前，我们需要对预测模型进行转换，详细信息请参考[文档](https://github.com/PaddlePaddle/Serving/blob/v0.6.0/doc/SAVE_CN.md)。

在准备好环境的客户端机器上，执行如下脚本对样例模型进行转换。
>>>>>>> 9c8570af (add new models)

```shell
python -m paddle_serving_client.convert \
    --dirname ./bisenetv2_demo_model \
    --model_filename model.pdmodel \
    --params_filename model.pdiparams
```

<<<<<<< HEAD
After excuting the script, the "serving_server" folder in the current directory saves the server model and configuration, and the "serving_client" folder saves the client model and configuration.

## Server Deployment

You can use `paddle_serving_server.serve` to start the RPC service, please refer to the [document](https://github.com/PaddlePaddle/Serving/blob/v0.6.0/README_CN.md#rpc%E6%9C%8D%E5%8A%A1).

If you finish to prepare environment on server side, export the  server model and  serving_server file, execute the following command to start the service. We use port 9292 on the server side. The server ip can be inquired by `hostname -i`.
=======
执行完成后，当前目录下的serving_server文件夹保存服务端模型和配置，serving_client文件夹保存客户端模型和配置。

## 服务器端开启服务

大家可以使用paddle_serving_server.serve启动RPC服务，详细信息请参考[文档](https://github.com/PaddlePaddle/Serving/blob/v0.6.0/README_CN.md#rpc%E6%9C%8D%E5%8A%A1)。

在服务器端配置好环境、准备保存服务端模型和配置的serving_server文件后，执行如下命令，启动服务。我们在服务器端使用9292端口，服务器ip使用`hostname -i`查看。
>>>>>>> 9c8570af (add new models)

```shell
python -m paddle_serving_server.serve \
    --model serving_server \
    --thread 10 \
    --port 9292 \
    --ir_optim
```

<<<<<<< HEAD
## Client request service
=======
## 客户端请求服务
>>>>>>> 9c8570af (add new models)

```
cd PaddleSeg/deploy/serving
```

<<<<<<< HEAD
Set the path of the serving_client file, the server-side ip and port, and the path of the test picture, and execute the following commands.
=======
设置serving_client文件的路径、服务器端ip和端口、测试图片的路径，执行如下命令。
>>>>>>> 9c8570af (add new models)

```shell
python test_serving.py \
    --serving_client_path path/to/serving_client \
    --serving_ip_port ip:port \
    --image_path path/to/image\
```

<<<<<<< HEAD
After the execution is complete, the divided image is saved in "result.png" in the current directory.
=======
执行完成后，分割的图片保存在当前目录的"result.png"。
>>>>>>> 9c8570af (add new models)

![cityscape_predict_demo.png](../../images/cityscapes_predict_demo.png)
