<<<<<<< HEAD
=======
<<<<<<< HEAD
English|[简体中文](model_export_onnx_cn.md)
# Export model with ONNX format

After training the model by PaddleSeg, we also support exporting model with ONNX format. This tutorial provides an example to introduce it.

For the complete method of exporting ONNX format models, please refer to [Paddle2ONNX](https://github.com/PaddlePaddle/Paddle2ONNX)。

## 1.Export the inference model

Refer to [document](./model_export.md) to export model, and save the exported inference model to the output folder, as follows.


```shell
./output
  ├── deploy.yaml            # deployment-related profile
  ├── model.pdmodel          # topology file of inference model
  ├── model.pdiparams        # weight file of inference model
  └── model.pdiparams.info   # additional information, generally do not need attention to this file
```

## 2. Export ONNX format model

Install Paddle2ONNX (version 0.6 or higher).
=======
>>>>>>> PaddlePaddle-release/2.4
# 导出ONNX格式模型

PaddleSeg训练好模型后，也支持导出ONNX格式模型，本教程提供一个示例介绍使用方法。

导出ONNX格式模型的完整方法，请参考[Paddle2ONNX](https://github.com/PaddlePaddle/Paddle2ONNX)。

## 1. 导出预测模型

参考[文档](./model_export.md)导出预测模型。

复用[文档](./model_export.md)中的示例，成功将导出的预测模型文件保存在output文件夹中，如下。

```shell
./output
  ├── deploy.yaml            # 部署相关的配置文件，主要说明数据预处理的方式
  ├── model.pdmodel          # 预测模型的拓扑结构文件
  ├── model.pdiparams        # 预测模型的权重文件
  └── model.pdiparams.info   # 参数额外信息，一般无需关注
```

## 2. 导出ONNX格式模型

安装Paddle2ONNX（高于或等于0.6版本)。
<<<<<<< HEAD
=======
>>>>>>> 9c8570af (add new models)
>>>>>>> PaddlePaddle-release/2.4

```
pip install paddle2onnx
```

<<<<<<< HEAD
执行如下命令，使用Paddle2ONNX将output文件夹中的预测模型导出为ONNX格式模型。

=======
<<<<<<< HEAD
Execute the following command to export the prediction model in the output folder to an ONNX format model by Paddle2ONNX.
=======
执行如下命令，使用Paddle2ONNX将output文件夹中的预测模型导出为ONNX格式模型。

>>>>>>> 9c8570af (add new models)
>>>>>>> PaddlePaddle-release/2.4
```
paddle2onnx --model_dir output \
            --model_filename model.pdmodel \
            --params_filename model.pdiparams \
            --opset_version 11 \
            --save_file output.onnx
```

<<<<<<< HEAD
=======
<<<<<<< HEAD
The exported ONNX format model is saved as output.onnx file.

Reference documents:
* [Paddle2ONNX](https://github.com/PaddlePaddle/Paddle2ONNX)
* [ONNX](https://onnx.ai/)


=======
>>>>>>> PaddlePaddle-release/2.4
导出的ONNX格式模型保存为output.onnx文件。

参考文档：
* [Paddle2ONNX](https://github.com/PaddlePaddle/Paddle2ONNX)
* [ONNX](https://onnx.ai/)
<<<<<<< HEAD
=======
>>>>>>> 9c8570af (add new models)
>>>>>>> PaddlePaddle-release/2.4
